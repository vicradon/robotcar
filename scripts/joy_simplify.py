#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Joy
from robotcar.msg import DPad

def motor_callback(msg):
    '''
    We go clockwise
    '''
    buttons = msg.buttons
    dPad = DPad()
    # forward, right, downward, left, accelerate, decelerate, brake
    dPad.data = [buttons[-4], buttons[-1], buttons[-3], buttons[-2], buttons[5], buttons[4], buttons[6]]
    pub.publish(dPad)

def main():
    try:
        global pub
        rospy.init_node('motors', anonymous=True)
        pub = rospy.Publisher('dpad', DPad, queue_size=10)
        rospy.Subscriber("joy", Joy, callback=motor_callback, callback_args=None, queue_size=100)
        rospy.spin()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
