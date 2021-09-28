#!/usr/bin/env python
import stretch_body.pimu
import numpy as np
import time

p = stretch_body.pimu.Pimu()
if not p.startup():
    exit()

history = []
ts = time.time()
while time.time() - ts < 60.0:
    p.pull_status()
    if len(history) >= 100:
        history.pop(0)
    history.append(p.status['voltage'])
    time.sleep(0.02)
    if p.status['voltage'] > np.mean(history) + 3 * np.std(history):
        print('plugged in!')
        p.trigger_beep()
        p.push_command()
        exit()
    else:
        print('Voltage %f Threshold %f'%(p.status['voltage'], np.mean(history) + 3 * np.std(history)))

print('timed out')
p.stop()

