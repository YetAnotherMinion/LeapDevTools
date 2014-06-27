# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 15:47:17 2014

@author: Isaiah Bell
Copyright 2014
"""

from Keybindings import *
from InteractionObjects import *
from Robot import *

        

                
'''VISUALIZE #################################################################'''
length = 80
height = 19
board = []
for i in range(height):
    if i == 0 or i == height-1:
        board.append(["#"] * length)
    else:
        temp = ["#","#"]
        for i in range(length-2):
            temp.insert(1,"0")
        board.append(temp)
def print_board():
    for row in board:
        print "".join(row)



def player_position(x,y):
    pass


''' TESTS ####################################################################'''

def buffer_test():
    buff = Buffer()
    buff.enqueue('foo')
    buff.enqueue((1,2,3))
    buff.enqueue(Buffer())
    buff.enqueue(4)
    print buff.queue
    print buff.dequeue()
    print "Try illegal access to index -1000:",buff.dequeue(-1000)
    print buff.queue
    for i in range(buff.buffer_size+10):
        buff.enqueue(i)
        print buff.queue

def runtime_test():
    robot = RobotController()
    for i in range(1200):
        main(robot)
        time.sleep(0.01)

def end_effector_test():
    pass

def button_test():
    button = CubicButton(HEIGHT = 200)
    print button.center
    print button.width
    print button.height
    print button.depth
    print button.press_direction
    
def handler_test():
    button = CubicButton()
    interaction_list = [button,button]
    print button
    print interaction_list
    print button.is_valid(1)
    
def key_bind_test():
    keybind = KeyBinding()
    print keybind.nuke_the_universe[0].center
    
def slider_run_test():
    keybind = KeyBinding()
    Inter = InteractionHandler()
    keybind.bar[0].gain = 2
    keybind.gain_slider[0].enforce_slider_normal = False
    
    #loop
    for i in range(6000):
        frame = get_data()
        list_of_elements = Inter.poll_interface_elements(keybind.UE_list,frame)
        Inter.run_interaction_detection(list_of_elements,frame)
        print '**********************************'

        time.sleep(.01)

    
    
    
''' RUN TESTS HERE ############################################################'''

slider_run_test()