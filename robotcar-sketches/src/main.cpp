#include <AFMotor.h>
#include <ros.h>
#include <std_msgs/String.h>
#include <geometry_msgs/Twist.h>
#include <robotcar/DPad.h>
#include <std_msgs/Int32.h>

AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

ros::NodeHandle nh;

int motor_speed = 100;
int motor_delay = 100;

void dPadMessageCb(const robotcar::DPad &dpad_msg)
{
  motor1.setSpeed(motor_speed);
  motor2.setSpeed(motor_speed);
  motor3.setSpeed(motor_speed);
  motor4.setSpeed(motor_speed);

  // forward
  if (dpad_msg.data[0])
  {
    motor1.run(FORWARD);
    motor2.run(FORWARD);
    motor3.run(FORWARD);
    motor4.run(FORWARD);
  }

  // right
  if (dpad_msg.data[1])
  {
    motor1.run(FORWARD);
    motor2.run(FORWARD);
    motor3.run(FORWARD);
    motor4.run(RELEASE);
  }

  // backward
  if (dpad_msg.data[2])
  {
    motor1.run(BACKWARD);
    motor2.run(BACKWARD);
    motor3.run(BACKWARD);
    motor4.run(BACKWARD);
  }

  // left
  if (dpad_msg.data[3])
  {
    motor1.run(RELEASE);
    motor2.run(FORWARD);
    motor3.run(FORWARD);
    motor4.run(FORWARD);
  }

  // accelerate
  if (dpad_msg.data[4] && motor_speed <= 250)
  {
    motor_speed += 5;
  }

  // decelerate
  if (dpad_msg.data[5] && motor_speed >= 5)
  {
    motor_speed -= 5;
  }

  // brake
  if (dpad_msg.data[6])
  {
    motor1.run(RELEASE);
    motor2.run(RELEASE);
    motor3.run(RELEASE);
    motor4.run(RELEASE);
  }
}

ros::Subscriber<robotcar::DPad> dPadSubscriber("dpad", &dPadMessageCb);

std_msgs::Int32 left_tick;
std_msgs::Int32 right_tick;

ros::Publisher leftTickPublisher("left_tick", &left_tick);
ros::Publisher rightTickPublisher("right_tick", &right_tick);

int led_delay = 2000;

void setup()
{
  nh.initNode();
  nh.advertise(leftTickPublisher);
  nh.advertise(rightTickPublisher);
  nh.subscribe(dPadSubscriber);
  pinMode(A0, INPUT);
  pinMode(A5, INPUT);
}

void loop()
{
  left_tick.data = digitalRead(A6);
  right_tick.data = digitalRead(A0);

  leftTickPublisher.publish(&left_tick);
  rightTickPublisher.publish(&right_tick);

  nh.spinOnce();
  delay(1);
}
