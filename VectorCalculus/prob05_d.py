import numpy as np
from prob05_a import Df
from prob05_b import Dg
from prob05_c import Dh

def f(z_1,z_2):
    return z_1*z_2 + 1

def g(y_1,y_2):
    return np.array([[y_1+2*y_2],[4*y_1-y_2]])

def h(x_1,x_2,x_3):
    return np.array([[np.exp(x_1)*np.cos(x_2)+x_3],[np.exp(x_1)*np.sin(x_2)+x_3]])

def dfogoh(x_1,x_2,x_3):
    
    ### <--- START OF YOUR CODE
        # 1) y = h(x)  (shape 2x1)  (memory location {0,0}=y1 row 0 colm 0)
    y = h(x_1, x_2, x_3)
    y1 = y[0, 0]
    y2 = y[1, 0]

    # 2) z = g(y)  (shape 2x1)
    z = g(y1, y2)
    z1 = z[0, 0]
    z2 = z[1, 0]

    # 3) Df at z: shape (2,)
    grad_f = Df(z1, z2)

    # 4) Dg at y: shape (2,2)
    J_g = Dg(y1, y2)

    # 5) Dh at x: shape (2,3)
    J_h = Dh(x_1, x_2, x_3)

    # 6) Chain rule: (1x2)@(2x2)@(2x3) -> (1x3) -> return as (3,)
    dfogoh = grad_f @ J_g @ J_h

    ### END OF YOUR CODE --->

    return dfogoh

def main():

    x_1,x_2,x_3=0,0,0

    print(dfogoh(x_1,x_2,x_3))

if __name__ == "__main__":
    main()
