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
    ], name="65016515")

print(robot)