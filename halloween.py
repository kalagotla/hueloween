#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on MON Oct 19 2020

@author: kal @ Dilip Kalagolta (kalagodk@mail.uc.edu)

Add code summary below:
    Code to flicker hue lights controlled with
    phue https://github.com/studioimaginaire/phue
"""

from phue import Bridge
import time
import random
import sys
from multiprocessing import Process

def flicker_white(l_id):

    b = Bridge('192.168.1.35') #Setup bridge instance
    b.connect() #Connect to the bridge

    command_off = {'on': False}
    
    start_time = time.time()
    while True:
        i = 0
        while i<=100:
            command_on =  {'transitiontime': random.randint(1,35), 'on': True,
                           'bri': random.randint(0,150),
                           'xy': [random.random(), random.random()]}
            b.set_light(l_id, command_on)
            b.set_light(l_id, command_off)
            i += 1
        i = 0
        while i<=random.randint(1,50):
            command_on =  {'transitiontime': 1, 'on': True,
                           'bri': 255}
            b.set_light(l_id, command_on)
            b.set_light(l_id, command_off)
            i+=1
    end_time = time.time()
    
    print('Time taken= ', end_time - start_time)

    return


flicker_white(7)
# def run_cpu_tasks_in_parallel(tasks):
#     running_tasks = [Process(target=task) for task in tasks]
#     for running_task in running_tasks:
#         running_task.start()
#     for running_task in running_tasks:
#         running_task.join()

# run_cpu_tasks_in_parallel([flicker(5), flicker(6), flicker(8), flicker(9)])
