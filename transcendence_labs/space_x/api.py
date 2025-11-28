from flask import Flask, jsonify, request
import requests
import numpy as np
from datetime import datetime

app = Flask(__name__)

def fetch_spacex_data(endpoint, params=None):
    url = f"https://api.spacexdata.com/v4/{endpoint}"
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch SpaceX data: {str(e)}"}

def generate_flight_data(flight_name, time=np.linspace(0, 900, 9000), stage='initial'):
    # Fetch Starship flight data (using 2022 data, as 2025 isn’t available)
    launches = fetch_spacex_data("launches", {"name": flight_name})
    if "error" in launches or not launches:
        return {"error": f"Flight {flight_name} not found or API error"}

    # Simulate realistic ascent for SN20 (2022)
    max_altitude = 150000  # m (approximate max altitude for SN20)
    max_velocity = 2500    # m/s (approximate max velocity for SN20)
    
    # Altitude: Parabolic rise to max_altitude, peaking at ~450 s, then stabilizing
    altitude = max_altitude * (time / 450) ** 2 * np.where(time <= 450, 1, 2 - (time / 450))
    altitude = np.clip(altitude, 0, max_altitude)  # Ensure no negative or excessive values
    
    # Velocity: Linear increase to max_velocity over 900 s
    velocity = max_velocity * (time / 900)

    # Basic flight parameters (simulated, adjusted for 2022 Starship tests)
    freq = 20             # Hz (harmonic frequency, 10–50 Hz range, consistent with model)
    damping = 0.1         # Default damping (adjust for isolators/TMDs)

    # Adjust vibration amplitude based on altitude and velocity (simplified model)
    # Lower altitude → higher aerodynamic damping; higher velocity → increased vibration
    aero_damping_factor = 0.1 * np.exp(-altitude / 100000)  # Exponential decay with altitude
    velocity_factor = 1 + 0.01 * velocity / 1000  # Slight increase in vibration with velocity
    
    # Generate vibration data (amplitude in g, based on 2022 test observations)
    omega_f = 2 * np.pi * freq
    if stage == 'initial':
        base_amp = 30  # Adjusted to 30 g for 2022 tests (less powerful than 2025)
        vibration = np.where(time < 420, 
                             base_amp * velocity_factor * np.sin(omega_f * time), 
                             base_amp * 0.1 * velocity_factor * np.sin(omega_f * time))
        thrust_kn = np.where(time < 420, 62000, 5600)  # 62,000 kN pre-hot, 5,600 kN post-hot
    else:  # hot staging
        base_amp = 3    # Adjusted to 3 g for 2022 tests (less coupling)
        vibration = base_amp * velocity_factor * np.sin(omega_f * time)  # Sustained 3 g
        thrust_kn = np.full_like(time, 5600)  # Constant 5,600 kN post-hot staging

    # Add damping effect (including aerodynamic damping)
    effective_damping = damping * 0.9 + aero_damping_factor  # Combine structural and aerodynamic damping
    vibration = vibration * (1 - effective_damping)

    return {
        "flight_name": flight_name,
        "timestamp": datetime.now().isoformat(),
        "time_seconds": time.tolist(),
        "vibration_amplitude_g": vibration.tolist(),
        "thrust_kn": thrust_kn.tolist(),
        "altitude_m": altitude.tolist(),  # Now time-dependent
        "velocity_ms": velocity.tolist(),  # Now time-dependent
        "frequency_hz": freq,
        "damping_factor": damping
    }

@app.route('/flight/<flight_name>', methods=['GET'])
def get_flight_data(flight_name):
    stage = request.args.get('stage', 'initial')  # Get 'stage' from URL query, default to 'initial'
    try:
        data = generate_flight_data(flight_name, stage=stage)
        if "error" in data:
            return jsonify(data), 404
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

@app.route('/flights', methods=['GET'])
def list_flights():
    launches = fetch_spacexdata("launches", {"name__contains": "starship"})
    if "error" in launches:
        return jsonify({"error": launches["error"]}), 500
    return jsonify([{"name": l["name"], "date": l["date_utc"]} for l in launches])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # Keep debug=True for now