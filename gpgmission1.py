# -*- coding: utf-8 -*-
"""GPGMission1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14BAKJvL3QhSkfPo7LCU9m0vzS82n3kP6
"""

!pip install easygopigo3
!pip install gopigo3
!curl -kL dexterindustries.com/update_sensors | bash

from easygopigo3 import EasyGoPiGo3
import easygopigo3 as easy
from gopigo3 import FirmwareVersionError
#from di_sensors import DistanceSensor
import time
import sys


def main():
    robot = easy.EasyGoPiGo3()
    try:
      distance_sensor =  robot.init_distance_sensor()  # DistanceSensor()
    except IOError as msg:
      print("GoPiGo3 robot not detected or DistanceSensor not installed.")
      sys.exit(1)
    servo = robot.init_servo()
    servo.rotate_servo(90)  # Adjust the initial orientation of the distance sensor

    # Define the keys for robot control
    keys = {
        "w": "drive",
        "\n": "stop",
        "q": "quit",
        "t": "test"
    }

    # Max speed of the robot
    speed = 300

    print("Press 'w' to drive, 'enter' to stop, and 'q' to quit.")

    while True:
        user_input = input("Enter command: ").strip().lower()
        action = keys.get(user_input)

        if action == "drive":
            drive_distance(robot, distance_sensor, speed)
        elif action == "stop":
            robot.stop()
        elif action == "quit":
            robot.stop()
            break
        elif action == "test":
              print("Yes")

        time.sleep(1)  # Add a delay between commands for better control

def drive_distance(robot, distance_sensor, speed, target_distance=495):
    robot.reset_encoders()
    distance_per_count = 0.05  # Set the distance per encoder count (in centimeters)
    robot.set_speed(speed)
    robot.drive_cm(target_distance)

    while True:
        left_encoder, right_encoder = robot.read_encoders()
        distance_traveled = min(left_encoder, right_encoder) * distance_per_count

        if distance_traveled >= (target_distance / 100):  # Convert target_distance to meters
            break

        if (distance_sensor.read_range() > 1.5) and (distance_traveled < target_distance / 100):
            adjust_direction(robot)

    # Read the final distance from the sensor after driving

    final_distance = robot.read_encoders()
    print(f"Final distance between the robot and the object: {final_distance} cm")

# def adjust_direction(robot):
#     speed = 100
#     robot.set_speed(speed)
#     servo.rotate_servo(45)
#     time.sleep(0.15)
#     distance_left = ds.read_range()
#     servo.rotate_servo(135)
#     time.sleep(0.15)
#     distance_right = ds.read_range()

#     if distance_left > distance_right:
#         robot.drive_degrees(45)
#     else:
#         robot.drive_degrees(135)

#     robot.drive_cm(0.5)
#     time.sleep(0.15)

#     if distance_left > distance_right:
#         robot.drive_degrees(135)
#     else:
#         robot.drive_degrees(45)

#     robot.drive_cm(0.5)
#     time.sleep(0.15)
#     robot.drive_degrees(90)
#     speed = 300
#     robot.set_speed(speed)

def adjust_direction(robot, distance_sensor):
    speed = 100
    robot.set_speed(speed)
    servo.rotate_servo(45)
    time.sleep(0.15)
    distance_left = distance_sensor.read_range()
    servo.rotate_servo(135)
    time.sleep(0.15)
    distance_right = distance_sensor.read_range()

    if distance_left > distance_right:
        robot.drive_degrees(45)
    else:
        robot.drive_degrees(135)

    robot.drive_cm(0.5)
    time.sleep(0.15)

    if distance_left > distance_right:
        robot.drive_degrees(135)
    else:
        robot.drive_degrees(45)

    robot.drive_cm(0.5)
    time.sleep(0.15)
    robot.drive_degrees(90)
    speed = 300
    robot.set_speed(speed)


if __name__ == "__main__":
    main()