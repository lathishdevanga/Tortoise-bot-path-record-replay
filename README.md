K Laxmi Pai
	
1:52 PM (13 minutes ago)
	
	
to me
# Tortoisebot in ROS2 Jazzy which records a path and replays it

# Overview
This project provides a complete simulation environment for the TortoiseBot mobile robot. It includes:

URDF/Xacro robot description
Gazebo simulation world
Teleop keyboard control
Launch files for easy startup

# Prerequisites
System Requirements

OS: Ubuntu 24.04 (Noble Numbat)
ROS2 Distribution: Jazzy Jalisco
Gazebo: Gazebo Harmonic (gz-harmonic)



# Required ROS2 Packages
bashsudo apt update
```bash
sudo apt install ros-jazzy-desktop
sudo apt install ros-jazzy-gazebo-ros-pkgs
sudo apt install ros-jazzy-teleop-twist-keyboard
sudo apt install ros-jazzy-robot-state-publisher
sudo apt install ros-jazzy-joint-state-publisher
sudo apt install ros-jazzy-xacro
```
After building the workspace and sourcing it,

# Usage
Terminal 1: Launch Gazebo Simulation
```
ros2 launch tortoise_gazebo gazebo.launch.py
```
Terminal 2: Launch the robot
```
ros2 launch tortoise_gazebo spawn_tortoisebot.launch.py
```
Terminal 3: Launch Teleop Keyboard
```
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
Terminal 4: Launch Rviz2
```
ros2 launch tortoisebot_description view_model.launch.py
```


Terminal 4: Start recording
```
ros2 run teleop_memory record_cmdvel
```
Then mover the robot using the already active teleop keys

Terminal 5: To replay the path
```
ros2 run teleop_memory replay_cmdvel
```
# Acknowledgments

ROS2 Jazzy Documentation
Gazebo Simulation Documentation
TortoiseBot Community
