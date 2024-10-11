# file สำหรับเขียนคำตอบ
# ในกรณีที่มีการสร้าง function อื่น ๆ ให้ระบุว่า input-output คืออะไรด้วย
'''
ชื่อ_รหัส(ธนวัฒน์_6461)
1. กันตพัฒน์_6501
2. ชวิศ_6515
'''
import HW3_utils as utils
import roboticstoolbox as rtb
import numpy as np

from spatialmath import SE3
from spatialmath.base import *
from math import pi
import math
#=============================================<คำตอบข้อ 1>======================================================#
#code here

robot = rtb.DHRobot(
    [
        rtb.RevoluteMDH(a = 0, alpha = 0, d = utils.d_1, offset = pi),
        rtb.RevoluteMDH(a = 0, alpha = pi, d = 0, offset = 0),
        rtb.RevoluteMDH(a = 0, alpha = utils.a_2, d = 0, offset = 0)
    ], name="HW3rob")
#create joint3 to end-effect
translate_to_end = SE3(utils.a_3 + (-utils.d_6),-utils.d_5,utils.d_4)
#add end-effect
robot.tool = translate_to_end
print(robot)
def endEffectorJacobianHW3(q:list[float])->list[float]:
    R , P , R_e , P_e = utils.FKHW3([0,0,0])

    link = ['0to1' , '0to2' ,'0to3' , '0toE']

    for i,l in enumerate(link): #enumerate จะให้ค่า
        print(i,l)


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