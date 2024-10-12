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


from spatialmath import SE3
from spatialmath.base import *
from math import pi
import math
robot = rtb.DHRobot(
    [
        rtb.RevoluteMDH(a = 0, alpha = 0, d = utils.d_1, offset = pi),
        rtb.RevoluteMDH(a = 0, alpha = pi, d = 0, offset = 0),
        rtb.RevoluteMDH(a = 0, alpha = utils.a_2, d = 0, offset = 0)
    ], name="HW3rob")
#create joint3 to end-effect
translate_to_end = SE3(utils.a_3 + (-utils.d_6),-utils.d_5,utils.d_4)
#add end-effect to robot
robot.tool = translate_to_end
print(robot)
#===========================================<ตรวจคำตอบข้อ 1>====================================================#
#code here


def Proof1(q:list[float])->list[float]:
    # find jacobian from frame 0
    J = robot.jacob0(q) 
#==============================================================================================================#
#===========================================<ตรวจคำตอบข้อ 2>====================================================#
#code here

#==============================================================================================================#
#===========================================<ตรวจคำตอบข้อ 3>====================================================#
#code here

#==============================================================================================================#