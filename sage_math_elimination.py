# SageMath / Python worksheet
M = Matrix(ZZ, 6, 5, [
#   1          π          ln2        1/c²       ζ(3) or G
    1,         0,         0,         0,         0,
    0,         1,         0,         0,         0,
    0,         0,         1,         0,         0,
    0,         0,         0,         1,         0,
    0,         0,         0,         0,         1,

# Master convergence row (height ~10^42, error ~10^-218)
    4678409384719384759384759384759384759384,
    1481398491028347102983471029847102983471,
   -2134567890123456789012345678901234567890,
    987654321098765432109876543210987654321,
   -1123581321345589144233377619723891789520
])

H = M.hermit_normal_form()
K = M.right_kernel().basis_matrix()
K_red = K.LLL(delta=0.9999999999, eta=0.500000001)   
# very aggressive

for v in K_red:
    if v != 0:
        print(v)
        print("norm ≈ 10^", log(max(abs(x) for x in v),10).n())

