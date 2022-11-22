import numpy as np

def normalized_vec(v):      # returns a unit vector (normalized vector)
    return v / np.linalg.norm(v)


def qr_decomposition(A):    # qr_decomposition using gram-schimidt process
    order = len(A)
    A = np.transpose(A)   # get transpose of column vectors

    # setup Ui dan Q
    U = np.zeros((order,order))
    Q = np.zeros((order,order))
    R = np.zeros((order,order))

    U[0] = A[0]
    Q[0] = normalized_vec(U[0])

    
    for i in range(1,order):
        U[i] = A[i]
        for j in range(i,0,-1):
            U[i] -= (np.dot(A[i], Q[j-1])*Q[j-1])
        Q[i] = normalized_vec(U[i])

    for i in range(0,order):
        for j in range(i,order):
            R[i][j] = np.dot(A[j], Q[i])

    Q = np.transpose(Q)
    return Q,R


def QR_eig(A, iteration=60):
    # uses QR algorithm
    # returns eigenvalues [k1, k2, ..., kn] and eigenvectors [v1 | v2 | ... | vn]
    # if A is symmetric, returned eigenvectors should be a good approximation to the exact eigenvectors of A

    Ac = np.copy(A)
    n = np.shape(A)[0]
    eigvecs = np.eye(n)

    for i in range(iteration):
        Q,R = qr_decomposition(Ac)
        Ac = np.matmul(R,Q)
        eigvecs = np.matmul(eigvecs, Q)

    eigvals = np.diag(Ac)

    return eigvals, eigvecs

