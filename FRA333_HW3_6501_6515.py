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
    # P_i_jk mean position from frame j's origin to frame k's origin reference from frame 'i'

    # Define variable
    Zd_1 = sp.symbols('Zd_1')
    Zd_2 = sp.symbols('Zd_2')
    Zd_3 = sp.symbols('Zd_3')

    # Create lambda function of angular velocity and linear velocity
    angular_velo = lambda l_Rot_Mat, l_angular, l_Zeta_dot: np.dot(l_Rot_Mat, l_angular) + (sp.Matrix((0, 0, l_Zeta_dot)))
    linear_velo = lambda l_Rot_Mat, l_linear, l_angular, l_pos: np.dot(l_Rot_Mat, (l_linear + np.cross(l_angular, l_pos, axis=0))) 
    
    # Frame 0
    w_0_0 = np.zeros([3,1])
    v_0_0 = np.zeros([3,1])

    # Frame 1
    # R_1_0 = Transpose(R_0_1)
    R_1_0 = R[:,:,0].transpose()
    P_0_01 = P[:,0]

    w_1_1 = angular_velo(R_1_0, w_0_0, Zd_1)
    v_1_1 = linear_velo(R_1_0, v_0_0, w_0_0, P_0_01)


    # Frame 2
    # R_2_1 = R_2_0 * R_0_1 = Transpose(R_0_2) * R_0_1
    R_2_1 = R[:,:,1].transpose() @ R[:,:,0]
    
    # P_1_12 = P_1_02 - P_1_01 =  R_1_0(P_0_02) - R_1_0(P_0_01) = R_1_0(P_0_02 - P_0_01)
    P_1_12 = R_1_0 @ (P[:,1] - P[:,0])

    
    w_2_2 = angular_velo(R_2_1, w_1_1, Zd_2)
    v_2_2 = linear_velo(R_2_1, v_1_1, w_1_1, P_1_12)
 
    # Frame 3
    # R_3_2 = R_3_0 * R_0_2 = Transpose(R_0_3) * R_0_2
    R_3_2 = R[:,:,2].transpose() @ R[:,:,1]

    # P_2_23 = P_2_03 - P_2_02 = R_2_0(P_0_03) - R_2_0(P_0_02) = R_2_0(P_0_03 - P_0_02)
    # R_2_0 = Transpose(R_0_2)
    P_2_23 = R[:,:,1].transpose() @ (P[:,2] - P[:,1])

    w_3_3 = angular_velo(R_3_2, w_2_2, Zd_3)
    v_3_3 = linear_velo(R_3_2, v_2_2, w_2_2, P_2_23)
    
    # Use frame of reference to frame 0 using rotation matrix
    R_0_3 = R[:,:,2]
    w_0_3 = R_0_3.dot(w_3_3)
    v_0_3 = R_0_3.dot(v_3_3)

    # Extract jacobian
    result_w = []
    result_v = []
    dict_order = [Zd_1, Zd_2, Zd_3]

    for row in sp.Matrix(w_0_3):

        coeff_buffer = row.as_coefficients_dict(Zd_1, Zd_2, Zd_3)
        result_in_row = [float(coeff_buffer[key]) for key in dict_order]

        result_in_row = np.array(result_in_row).reshape(3)
        
        result_w.append(result_in_row)

    for row in sp.Matrix(v_0_3):

        coeff_buffer = row.as_coefficients_dict(Zd_1, Zd_2, Zd_3)
        result_in_row = [float(coeff_buffer[key]) for key in dict_order]

        result_in_row = np.array(result_in_row).reshape(3)
        
        result_v.append(result_in_row)

    result_w = np.array(result_w)
    result_v = np.array(result_v)
    
    
    # Since w_0_3 equal to w_0_e, do nothing.
    # v_0_e = v_0_3 + Skew(r_0_3 * p_3_3e) = v_0_3 + Skew(p_0_3e) = v_0_3 + Skew(p_0_0e - p_o_03)
    p_0_3e = P[:,3] - P[:,2]

    # Define skew-symetric lambda function
    Skew = lambda v: np.array([[0, -v[2], v[1]],[v[2], 0, -v[0]],[-v[1], v[0], 0]])
    result_v = result_v + Skew(p_0_3e)

    # Convert from numpy array to normal python list
    result_w = result_w.tolist()
    result_v = result_v.tolist()

    result = [result_w, result_v]
    
    return result




#==============================================================================================================#
#=============================================<คำตอบข้อ 2>======================================================#
#code here
def checkSingularityHW3(q:list[float])->bool:

    Jacobian = endEffectorJacobianHW3(q)

    # Extract jacobian in angular velocity and linear velocity
    j_w = np.array(Jacobian[0])
    j_v = np.array(Jacobian[1])

    # If determinant of jacobian is near zero.
    if abs(np.linalg.det(j_w)) < 0.001:
        print("Singularity in angular movement.")
        return False
    
    if abs(np.linalg.det(j_v)) < 0.001:
        print("Singularity in linear movement.")
        return False
    
    return True

#==============================================================================================================#
#=============================================<คำตอบข้อ 3>======================================================#
#code here
def computeEffortHW3(q:list[float], w:list[float])->list[float]:

    # Sanitize q input
    if (len(q) != 3):
        raise ValueError(f"List is expected to be size of 3, but got size {len(q)}.")

    # Get jacobian and rotation matrix
    Jacobian = endEffectorJacobianHW3(q)
    j_w = np.array(Jacobian[0])
    j_v = np.array(Jacobian[1])
    _, _, R_0_e, _ = utils.FKHW3(q)


    # Check for illegal input and seperate them 
    if (len(w) != 6):
        raise ValueError(f"List is expected to be size of 6, but got size {len(w)}.")
    input_moment_e = np.array(w[:3])
    input_force_e = np.array(w[3:])

    # Since input force is reference on frame e, but jacobian is on frame 0.
    # Transform input using R_0_e

    input_moment_0 = np.dot(R_0_e, input_moment_e)
    input_force_0 = np.dot(R_0_e, input_force_e)

    # Compute joint torque for moment at end effector
    tau_T = np.dot(j_w.transpose(), input_moment_0)

    # Compute joint torque for force at end effector
    tau_F = np.dot(j_v.transpose(), input_force_0)

    # Combine joint torque used for force and moment at end effector
    return tau_F + tau_T


#==============================================================================================================#

# Force run and test function
# print(endEffectorJacobianHW3([0,0,0]))
# checkSingularityHW3([0,0,0])
computeEffortHW3([0,0,0], [1,2,3,4,5,6])