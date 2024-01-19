from GUI import GUI
from HAL import HAL
import rospy
import random

w = 1
r = 0.5

while True:
    if (HAL.getBumperData().state == 1):
        w = 1
        HAL.setV(0)
        HAL.setW(random.randint(-6, 6))
        rospy.sleep(1)
        HAL.setW(0)
        HAL.setV(1)
        rospy.sleep(1)
    else:
        HAL.setW(1)
        HAL.setV(1 * w * r)
        rospy.sleep(1)
        w = w + 0.11
