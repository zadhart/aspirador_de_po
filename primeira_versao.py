from GUI import GUI
from HAL import HAL
import rospy
import random


while True:
    if (HAL.getBumperData().state == 1):
        HAL.setV(0)
        HAL.setW(random.randint(-6, 6))
        rospy.sleep(1)
        HAL.setW(0)
        HAL.setV(1)
        rospy.sleep(1)
    else:
        HAL.setV(1)
        rospy.sleep(1)    
        