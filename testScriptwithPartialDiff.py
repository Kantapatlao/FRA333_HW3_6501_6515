##### NOTE: This isn't working. Try to rewrite test script using partial differential method but failed.

import math
import numpy as np
import sympy as sp

def makeDH(a, alpha, d, zeta, joint):
    zeta = zeta + joint

    return sp.Matrix([[sp.cos(zeta), -sp.sin(zeta)*sp.cos(alpha), sp.sin(zeta)*sp.sin(alpha), a*sp.cos(zeta)],
                      [sp.sin(zeta), sp.cos(zeta)*sp.cos(alpha), -sp.cos(zeta)*sp.sin(alpha), a*sp.sin(zeta)],
                      [0, sp.sin(alpha), sp.cos(alpha), d],
                      [0, 0, 0, 1]])

def makeTranslation(x,y,z):

    return sp.Matrix([[1, 0, 0, x],
                      [0, 1, 0, y],
                      [0, 0, 1, z],
                      [0, 0, 0, 1]])


def proof_jacobian(q: list[float]):

    # Define time
    t = sp.symbols("t")
    Zd_1 = sp.symbols("Zd_1")
    Zd_2 = sp.symbols("Zd_2")
    Zd_3 = sp.symbols("Zd_3")
    
    # Define zeta variable
    Z_1 = sp.Function("Z_1")(t)
    Z_2 = sp.Function("Z_2")(t)
    Z_3 = sp.Function("Z_3")(t)
    
    Full_T_Mat = makeDH(0, 0, 0.0892, math.pi, Z_1) @ makeDH(0, math.pi/2, 0, 0, Z_2) @ makeDH(-0.425, 0, 0, 0, Z_3) @ makeTranslation(-0.39243-0.082, -0.093, 0.109)
    Full_T_Mat = Full_T_Mat @ sp.Matrix([[0, 0 ,1, 0],
                                         [0, 1, 0, 0],
                                         [-1, 0, 0, 0],
                                         [0, 0, 0, 1]])
    
    D_Full_T_dt = sp.diff(Full_T_Mat, t)
    D_Full_T_dt = sp.simplify(D_Full_T_dt)

    D_Full_T_dt = D_Full_T_dt.subs(sp.Derivative(Z_1, t), Zd_1)
    D_Full_T_dt = D_Full_T_dt.subs(sp.Derivative(Z_2, t), Zd_2)
    D_Full_T_dt = D_Full_T_dt.subs(sp.Derivative(Z_3, t), Zd_3)

    D_Full_T_dt = D_Full_T_dt.subs(Z_1, q[0])
    D_Full_T_dt = D_Full_T_dt.subs(Z_2, q[1])
    D_Full_T_dt = D_Full_T_dt.subs(Z_3, q[2]) 


    print(D_Full_T_dt)
    pass

proof_jacobian([0,-3.14/2,-0.2])