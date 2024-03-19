#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray
from pynput import keyboard

def on_key_press(key, publisher):
    movement = Float64MultiArray()
    try:
        command = ''# change the axis according to unity as its differnt as compare to ros 
        if key.char == 'w':  # Forward
            movement.data =  [0.0, 1.0, 0.0] # x, y, z
            command = 'forward'
        elif key.char == 's':  # Backward
            movement.data = [0.0, -1.0, 0.0]
            command = 'backward'
        elif key.char == 'a':  # Left
            movement.data = [-1.0, 0.0, 0.0] 
            command = 'left'
        elif key.char == 'd':  # Right (x is left and right in unit so i chnage the whole code accrdingly)
            movement.data = [1.0, 0.0, 0.0]
            command = 'right'
        else:
            return
        publisher.publish(movement)
        rospy.loginfo('Publishing command: %s', command) # to check if its working prints the command
    except AttributeError:
        pass

def listener():
    rospy.init_node('keyboard_publisher', anonymous=True) # node name 

    # init the pub with topic name , lib and frequency
    publisher = rospy.Publisher('car_movement', Float64MultiArray, queue_size=10)
    rospy.loginfo('Keyboard Publisher Node has started.')
    
    # Start listening to the keyboard

    with keyboard.Listener(
            on_press=lambda event: on_key_press(event, publisher)) as listener:
        rospy.spin()

if __name__ == '__main__':
    listener()
