# FRA333 Kinematic Homework #3
Author:
1. Kantapat Laohaphan ID: 65340500001
2. Chawit Supcharoen ID: 65340500015

## Too long; Didn't read!
This repository hosts FRA333 Homework#3 answer. Three important files in this repository are:

1. **FRA333_HW3_6501_6515.py** is the answer compute by using velocity propagation method.
2. **testScript.py** is a script used to verify the answer with the help of roboticstoolbox-python package.
3. **HW3_utils.py** is provided by instructor to compute transformation matrix.

### How to run the code?
```
sudo apt install gcc vim
```
## On command prompt
```
pip install roboticstoolbox-python

pip install numpy==1.24.4
```


## Repository Description
รายงานนี้เป็นส่วนหนึ่งของวิชา Kinematic ในการศึกษา วิธีค่าของ Jacobian Matrix , การเช็คว่าเกิดมีการทำให้ระบบ สูญเสียการควบคุมไปมากกว่าหรือเท่ากับ 1 Dof ไหม เเละการหาค่าทอร์ค 


## Math and Theory
Two methods are used to calculate jacobian.
1. Partial differential method
2. Velocity propagation method

Partial differential method integrated in roboticstoolbox-python package was used for code testing. Velocity propergation method will be used for main calculation.

### Velocity propagation method
This method relied on formular that calculate angular and linear velocity of each frame then keep propagate until end-effector's frame has reached.

> <sup>i+1</sup>ω<sub>i+1</sub> = <sup>i+1</sup>R<sub>i</sub> ( <sup>i</sup>ω<sub>i</sub> ) + θ'<sub>i+1</sub>z &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*when θ'z is revolute joint's angular speed*\
> <sup>i+1</sup>v<sub>i+1</sub> = <sup>i+1</sup>R<sub>i</sub> ( <sup>i</sup>v<sub>i</sub> + <sup>i</sup>ω<sub>i</sub> x <sup>i</sup>p<sub>i,i+1</sub>) + d'<sub>i+1</sub>z &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*when d'z is prismatic joint's speed*

pic1\...

### Check for singularity
To check for singularity, split the jacobian into jacobian for linear velocity and jacobian for angular velocity (Each should be 3x3 matrix). Find determinant of both jacobian, if any is near zero (<0.001), function return as true. Otherwise, return false.\
\
Code pic...

### Compute for effort
Effort can be compute from ***"Force-velocity relationship"*** formula.

> τ<sub>f</sub> = J<sub>v</sub><sup>t</sup> x Force\
> τ<sub>m</sub> = J<sub>ω</sub><sup>t</sup> x Moment\
> Στ = τ<sub>f</sub> +  τ<sub>m</sub>

Code pic...

## Testing method
## First create MDH parameters
```
robot = rtb.DHRobot(
    [
        rtb.RevoluteMDH(a = 0, alpha = 0, d = d_1, offset = pi),
        rtb.RevoluteMDH(a = 0, alpha = pi/2, d = 0, offset = 0),
        rtb.RevoluteMDH(a = a_2, alpha = 0, d = 0, offset = 0)
    ], name="HW3rob")

#create joint3 to end-effect
translate_to_end = SE3(a_3 -(d_6),-(d_5),d_4) @ SE3.RPY(0.0,-pi/2,0.0)
#add end-effect to robot
robot.tool = translate_to_end
```
## Proof part
``` 
Use python testScript.py
to Check answer
```

## Proof1 that need to find Jacobian on frame 0
use funtion jacob0(q)

"J = robot.jacob0(q) " to create Jacobian on frame 0



"J_linear = J[:3]
J_angular = J[3:]
print(J_angular)
print(J_linear)" For show jacobian matrix

## Proof2 to show singularity
"
J = robot.jacob0(q) 
J_reduce = J[:3,:] #:3 เอาเเถวบนถึงเเถวที่ 3 , : เท่าหลักทุกตัว
J_det = np.linalg.det(J_reduce)  #เช็คค่าsingular ต่อไปคือถ้าค่าใกล้ 0 จะถือว่า det เป็น 0 ก็คือการเป็น singularity
if abs(J_det) < 0.001: #เนื่องจาก det ได้ค่าออกเเค่ตัวเดียว norm คือการรวมค่ามาเป้น vector เดียว เลยต้องใช้เป้น abs เเทน
    kebka_sing = True
else:
    kebka_sing = False
"
if kebka_sing == True => singularity


## Python package requirement 
1. Numpy version 1.24.4
2. Sympy version 1.13.3
3. roboticstoolbox-python 1.1.1 

***Note*** : This roboticstoolbox-python version doesn't support numpy 2.0 and above yet. If you've numpy version is newer than 1.26, consider installing numpy version 1.26 on seperated python virtual environment. [Guide](https://docs.python.org/3/library/venv.html)

### Install package using pip
```
python -m pip install numpy==1.26 sympy roboticstoolbox-python
```



## How to use?



## Reference

