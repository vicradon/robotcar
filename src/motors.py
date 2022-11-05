import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep 
import rospy
from std_msgs.msg import Int32
from sensor_msgs.msg import Joy

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

motor1pin1 = 5
motor1pin2 = 6
motor2pin1 = 13
motor2pin2 = 19

def init():
    GPIO.setup(motor1pin1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(motor1pin2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(motor2pin1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(motor2pin2, GPIO.OUT, initial=GPIO.LOW)

init()


def forward():
    GPIO.output(motor1pin1, GPIO.HIGH)
    GPIO.output(motor1pin2, GPIO.LOW)
    GPIO.output(motor2pin1, GPIO.HIGH)
    GPIO.output(motor2pin2, GPIO.LOW)
    sleep(0.3)
    init()

def backward():
    GPIO.output(motor1pin1, GPIO.LOW)
    GPIO.output(motor1pin2, GPIO.HIGH)
    GPIO.output(motor2pin1, GPIO.LOW)
    GPIO.output(motor2pin2, GPIO.HIGH)
    sleep(0.3)
    init()

def left():
    GPIO.output(motor1pin1, GPIO.LOW)
    GPIO.output(motor1pin2, GPIO.LOW)
    GPIO.output(motor2pin1, GPIO.HIGH)
    GPIO.output(motor2pin2, GPIO.LOW)
    sleep(0.3)
    init()

def right():
    GPIO.output(motor1pin1, GPIO.HIGH)
    GPIO.output(motor1pin2, GPIO.LOW)
    GPIO.output(motor2pin1, GPIO.LOW)
    GPIO.output(motor2pin2, GPIO.LOW)
    sleep(0.3)
    init()

def motor_callback(msg):
    buttons = msg.buttons
    if buttons[-4]:
        forward()
    elif buttons[-3]:
        backward()
    elif buttons[-2]:
        left()
    elif buttons[-1]:
        right()

def main():
    try:
        rospy.init_node('motors', anonymous=True)
        rospy.Subscriber("joy", Joy, callback=motor_callback, callback_args=None, queue_size=100)
        rospy.spin()

    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == '__main__':
    try:
        main()
        # GPIO.cleanup()
    except rospy.ROSInterruptException:
        GPIO.cleanup()

