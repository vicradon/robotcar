#!/usr/bin/env bash

export ROS_MASTER_URI=http://robotpc:11311

source /home/pi/catkin_ws/devel/setup.bash
exec "$@"