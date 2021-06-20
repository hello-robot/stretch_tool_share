#!python

import reactorx_wrist_V1.python.reactor_wrist as reactor_wrist
from stretch_body.hello_utils import *
import sys


r=reactor_wrist.ReactorWrist()
r.startup()

v_des=[r.motors['reactor_pitch'].params['motion']['default']['vel'], r.motors['reactor_roll'].params['motion']['default']['vel'],r.motors['reactor_gripper'].params['motion']['default']['vel']]
a_des=[r.motors['reactor_pitch'].params['motion']['default']['accel'], r.motors['reactor_roll'].params['motion']['default']['accel'],r.motors['reactor_gripper'].params['motion']['default']['accel']]


def menu_top():
    print('------ MENU -------')
    print('m: menu')
    print('a: increment pitch 10 deg')
    print('b: decrement pitch 10 deg')
    print('c: increment roll 10 deg')
    print('d: decrement roll 10 deg')
    print('e: increment gripper 10 deg')
    print('f: decrement gripper 10 deg')
    print('-----')
    print('p: pitch go to pos ticks')
    print('r: roll go to pos ticks')
    print('g: gripper go to pos ticks')
    print('-----')
    print('0: stow')
    print('1: tool up 0')
    print('2: tool up 90')
    print('3: tool up -90')
    print('4: tool down 0')
    print('5: tool down 90')
    print('6: tool down -90')
    print('7: gripper close')
    print('8: gripper open')
    print('-----')
    print('x: speed slow')
    print('y: speed default')
    print('z: speed fast')
    print('-------------------')

def step_interaction():
    global v_des, a_des
    menu_top()
    x=sys.stdin.readline()
    r.pull_status()
    if len(x)>1:
        if x[0]=='m':
            menu_top()
        if x[0]=='p':
            p = float(x[1:])
            p = r.motors['reactor_pitch'].ticks_to_world_rad(p)
            r.move_to('reactor_pitch',p,v_des[0], a_des[0])
        if x[0]=='r':
            t = float(x[1:])
            t = r.motors['reactor_roll'].ticks_to_world_rad(t)
            r.move_to('reactor_roll', t, v_des[1], a_des[1])
        if x[0] == 'g':
            g = float(x[1:])
            g = r.motors['reactor_gripper'].ticks_to_world_rad(g)
            r.move_to('reactor_gripper', g, v_des[2], a_des[2])
        if x[0] == 'a':
            r.move_by('reactor_pitch', deg_to_rad(10), v_des[0], a_des[0])
        if x[0] == 'b':
            r.move_by('reactor_pitch', deg_to_rad(-10), v_des[0], a_des[0])
        if x[0] == 'c':
            r.move_by('reactor_roll', deg_to_rad(10), v_des[1], a_des[1])
        if x[0] == 'd':
            r.move_by('reactor_roll', deg_to_rad(-10), v_des[1], a_des[1])
        if x[0] == 'e':
            r.move_by('reactor_gripper', deg_to_rad(10), v_des[2], a_des[2])
        if x[0] == 'f':
            r.move_by('reactor_gripper', deg_to_rad(-10), v_des[2], a_des[2])

        if x[0] == 'x':
            v_des = [r.motors['reactor_pitch'].params['motion']['slow']['vel'],
                     r.motors['reactor_roll'].params['motion']['slow']['vel'],
                     r.motors['reactor_gripper'].params['motion']['slow']['vel']]
            a_des = [r.motors['reactor_pitch'].params['motion']['slow']['accel'],
                     r.motors['reactor_roll'].params['motion']['slow']['accel'],
                     r.motors['reactor_gripper'].params['motion']['slow']['accel']]

        if x[0] == 'y':
            v_des = [r.motors['reactor_pitch'].params['motion']['default']['vel'],
                     r.motors['reactor_roll'].params['motion']['default']['vel'],
                     r.motors['reactor_gripper'].params['motion']['default']['vel']]
            a_des = [r.motors['reactor_pitch'].params['motion']['default']['accel'],
                     r.motors['reactor_roll'].params['motion']['default']['accel'],
                     r.motors['reactor_gripper'].params['motion']['default']['accel']]

        if x[0] == 'z':
            v_des = [r.motors['reactor_pitch'].params['motion']['fast']['vel'],
                     r.motors['reactor_roll'].params['motion']['fast']['vel'],
                     r.motors['reactor_gripper'].params['motion']['fast']['vel']]
            a_des = [r.motors['reactor_pitch'].params['motion']['fast']['accel'],
                     r.motors['reactor_roll'].params['motion']['fast']['accel'],
                     r.motors['reactor_gripper'].params['motion']['fast']['accel']]

        if x[0] == '0':
            r.pose('stow')
        if x[0] == '1':
            r.pose('tool_up_0')
        if x[0] == '2':
            r.pose('tool_up_90')
        if x[0] == '3':
            r.pose('tool_up_-90')
        if x[0] == '4':
            r.pose('tool_down_0')
        if x[0] == '5':
            r.pose('tool_down_90')
        if x[0] == '6':
            r.pose('tool_down_-90')
        if x[0] == '7':
            r.pose('tool_down_-90')
        r.push_command()
    else:
        r.pretty_print()

try:
    while True:
        try:
            step_interaction()
        except (ValueError):
            print('Bad input...')
except (ThreadServiceExit, KeyboardInterrupt):
    r.stop()


