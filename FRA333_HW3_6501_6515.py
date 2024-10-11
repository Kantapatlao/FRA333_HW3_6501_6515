# file สำหรับเขียนคำตอบ
# ในกรณีที่มีการสร้าง function อื่น ๆ ให้ระบุว่า input-output คืออะไรด้วย
'''
ชื่อ_รหัส(ธนวัฒน์_6461)
1.กันตพัฒน์_6501
2.ชวิศ_6515
3.
'''

# Import library
import numpy as np
import sympy as sp
import HW3_utils as utils
#=============================================<คำตอบข้อ 1>======================================================#
#code here
def endEffectorJacobianHW3(q:list[float])->list[float]:
    
    # Fetch value from HW3FK function
    R, P, _, _ = utils.FKHW3(q)
    # เพื่อหา Jacobian ของความเร็วเชิงเส้นและเชิงมุม ใช้วิธี Velocity propergation
    # อ้างอิงสูตรจากใน Readme
    # W is angular velocity, V is linear velocity
    # Zd is Zeta dot (Derivative of zeta against time)
    # W_i_j mean angular velocity of 'j' reference from 'i' frame
    # P_0_1 mean position from frame 0's origin to frame 1's origin

    # Define variable
    Zd_1 = sp.symbols('Zd_1')
    Zd_2 = sp.symbols('Zd_2')
    Zd_3 = sp.symbols('Zd_3')

    # Create lambda function of angular velocity and linear velocity
    angular_velo = lambda l_Rot_Mat, l_angular, l_Zeta_dot: np.dot(l_Rot_Mat, l_angular) + (sp.Matrix([0,0,l_Zeta_dot]))
    linear_velo = lambda l_Rot_Mat, l_linear, l_angular, l_pos: np.dot(l_Rot_Mat, (l_linear + np.cross(l_angular, l_pos))) 
    
    # Frame 0
    w_0_0 = np.zeros([3,1])
    v_0_0 = np.zeros([3,1])

    # Frame 1
    # R_1_0 = Transpose(R_0_1)
    R_1_0 = R[:,:,0].transpose()
    P_0_1 = P[:,0]

    w_1_1 = angular_velo(R_1_0, w_0_0, Zd_1)
    v_1_1 = linear_velo(R_1_0, v_0_0, w_0_0.reshape(3), P_0_1) 

    pass




#==============================================================================================================#
#=============================================<คำตอบข้อ 2>======================================================#
#code here
def checkSingularityHW3(q:list[float])->bool:
    pass
#==============================================================================================================#
#=============================================<คำตอบข้อ 3>======================================================#
#code here
def computeEffortHW3(q:list[float], w:list[float])->list[float]:
    pass
#==============================================================================================================#

# Force run and test function
endEffectorJacobianHW3([0,0,0])