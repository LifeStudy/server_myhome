from modules import *

gpio_setup(17,22,23,24)

for i in range(0, steps):
  stepping(1, 0, 0, 0)
  time_step(step_time)
  stepping(0, 1, 0, 0)
  time_step(step_time)
  stepping(0, 0, 1, 0)
  time_step(step_time)
  stepping(0, 0, 0, 1)
  time_step(step_time)
