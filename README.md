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
sudo apt install gcc vim ...
```

## Repository Description
รายงานนี้เป็นส่วนหนึ่งของวิชา Kinematic ...


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

## Python package requirement 
1. Numpy version 1.26
2. Sympy version 1.13.3
3. roboticstoolbox-python 1.1.1 

***Note*** : This roboticstoolbox-python version doesn't support numpy 2.0 and above yet. If you've numpy version is newer than 1.26, consider installing numpy version 1.26 on seperated python virtual environment. [Guide](https://docs.python.org/3/library/venv.html)

### Install package using pip
```
python -m pip install numpy==1.26 sympy roboticstoolbox-python
```



## How to use?



## Reference

