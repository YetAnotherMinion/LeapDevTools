# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 15:39:48 2014

@author: Isaiah Bell
Copyright (c) 2014
Released under MIT License
"""

from InteractionObjects import LargerPositionVelocityCombination,BlockingThreeDimensionPosition
from Coroutines import coroutine


class KeyBinding(object):
    '''
    Store a list of every interaction object and binds output to some other function call
    
    To add an interaction instance:
        name = [InteractionObject(), callback_for_interaction_instance()] 
    '''
    def __init__(self): # got rid of robot intance
        '''Define the virtual control panel in Leap interaction space and link to CALLBACKS

            Define the callback:
            =======================
                Create a class attribute that can be used as a target. 
                Note that the actual call back definitions are intended private attributes.
                Other coroutine will use callback_target to send data in.

                    self.callback_target = self._actual_callback()

            Package instance and callback:
            ===================================

        '''
        self.frame_control = self._update_position()
        self.containing_sphere = LargerPositionVelocityCombination(CENTER = (0,250,0),WIDTH = 400,HEIGHT = 400,DEPTH = 400,NORMAL_DIRECTION = (0,1,0),
                                                                    callback = self.frame_control,shape = 'ellipsoid')

        self.emergency_stop_callback = self._emergency_stop

        self.centering_gate = BlockingThreeDimensionPosition(CENTER = (0,250,0),WIDTH = 175,HEIGHT = 175,DEPTH = 175,NORMAL_DIRECTION = (0,1,0),
                                                            callback = self.emergency_stop_callback, embedded_parent = self.containing_sphere, shape = 'rectangle')

        '''Make the list of all UI elements '''

        self.UE_list = [self.centering_gate]
                               
    '''BUTTON CALLBACKS ************************************************'''

    @coroutine 
    def _update_position(self):
        count = 0
        while True:
            args,kwargs = (yield)
            print '*'*30
            x = self.containing_sphere.smoothed_x
            y = self.containing_sphere.smoothed_y
            z = self.containing_sphere.smoothed_z
            gain = self.containing_sphere.gain_object.gain
            print gain
            #print 'ARGS:  ',args
            #print '#'*25
            #print 'KWARGS:  ',kwargs
            if count == 0:
                #callback_ep([0,0,.45,0,0,0],'frame_end_effector')
                count += 1
            elif count > 10:
                #callback_ep([0,0,.45,0,0,0],'frame_end_effector')
                count = 0


    
    def _emergency_stop(self):
        print 'emergency_stop'
        print 'Flag:',self.containing_sphere.hand_command_valid
        pass

    def joint_control(self):
        pass
        


