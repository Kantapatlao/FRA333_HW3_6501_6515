# file สำหรับตรวจคำตอบ
# ในกรณีที่มีการสร้าง function อื่น ๆ ให้ระบุว่า input-output คืออะไรด้วย
'''
ชื่อ_รหัส(ธนวัฒน์_6461)
1. กันตพัฒน์_6501
2. ชวิศ_6515
'''
import HW3_utils as utils
import roboticstoolbox as rtb
import numpy as np
import FRA333_HW3_6501_6515 as Rob
d_1 = 0.0892
a_2 = -0.425
a_3 = -0.39243
d_4 = 0.109
d_5 = 0.093
d_6 = 0.082

from spatialmath import SE3
from spatialmath.base import *
from math import pi
import math
robot = rtb.DHRobot(
    [
        rtb.RevoluteMDH(a = 0, alpha = 0, d = d_1, offset = pi),
        rtb.RevoluteMDH(a = 0, alpha = pi, d = 0, offset = 0),
        rtb.RevoluteMDH(a = 0, alpha = a_2, d = 0, offset = 0)
    ], name="HW3rob")

#create joint3 to end-effect
translate_to_end = SE3(a_3 + (-d_6),-d_5,d_4)
#add end-effect to robot
robot.tool = translate_to_end
#===========================================<ตรวจคำตอบข้อ 1>====================================================#
#code here


def Proof1(q:list[float])->list[float]:
    # find jacobian from frame 0

    J = robot.jacob0(q) 
    ref_J = Rob.endEffectorJacobianHW3(q)
    print("------------------Jacobian FRA333------------------------")
    print(ref_J)
    print("------------------Jacobian RTB------------------------")
    J_linear = J[:3]
    J_angular = J[3:]
    print(J_linear)
    print(J_angular)
#==============================================================================================================#
#===========================================<ตรวจคำตอบข้อ 2>====================================================#
#code here
def Proof2(q:list[float]):
    # find jacobian from frame 0
    J = robot.jacob0(q) 
    J_reduce = J[:3,:] #:3 เอาเเถวบนถึงเเถวที่ 3 , : เท่าหลักทุกตัว
    J_det = np.linalg.det(J_reduce)  #เช็คค่าsingular ต่อไปคือถ้าค่าใกล้ 0 จะถือว่า det เป็น 0 ก็คือการเป็น singularity
    if abs(J_det) < 0.001: #เนื่องจาก det ได้ค่าออกเเค่ตัวเดียว norm คือการรวมค่ามาเป้น vector เดียว เลยต้องใช้เป้น abs เเทน
        kebka_sing = True
    else:
        kebka_sing = False

    ref_sing = Rob.checkSingularityHW3(q)
    print("-----------Singularity From FRA333-------------------")
    print(ref_sing)
    print("-----------Singularity RTB-------------------")
    print(kebka_sing)
    print(J_det)

def Proof3(q:list[float],w:list[float]): #w = wench
    J = robot.jacob0(q) 
    w = np.array(w) #change to nx1 matrix
    #find taq
    taq = robot.pay(w,q,J,0)
    ref_taq = Rob.computeEffortHW3(q,w)

    print("-----------Taque From FRA333-------------------")
    print(ref_taq)
    print("-----------Taque RTB-------------------")
    print(taq)





#==============================================================================================================#
#===========================================<ตรวจคำตอบข้อ 3>====================================================#
#code here

#==============================================================================================================#

#=======================================Test Zone=======================================================#
#param
# q = Rob.q  รอดึง q จากไฟล์จู
q = [pi,pi,0]
w = [1.0,1.0,1.0,1.0,1.0,1.0] #[Moment,Force]
Proof1(q)
Proof2(q)
Proof3(q,w)