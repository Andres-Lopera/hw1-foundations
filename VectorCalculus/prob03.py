import numpy as np

def dinvA(x):
    
    ### <--- START OF YOUR CODE

    # Define A(x)
    A = np.array([
        [1, x**3 + 3],
        [x**4 + x**2 + 3, x**2 + 1]
    ], dtype=float)

    # Derivative A'(x)
    A_prime = np.array([
        [0, 3*x**2],
        [4*x**3 + 2*x, 2*x]
    ], dtype=float)

    # Compute inverse of A
    A_inv = np.linalg.inv(A)

    # Apply formula: -A^{-1} A' A^{-1}
    dinvA = -A_inv @ A_prime @ A_inv

    ### END OF YOUR CODE --->

    return dinvA

def main():
    x = 1

    print(dinvA(x))

if __name__ == "__main__":
    main()