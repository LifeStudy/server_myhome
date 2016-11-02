import mraa
import time

step_time = 0.0035
steps = 500

x0 = mraa.Gpio(0)
x1 = mraa.Gpio(1)
x2 = mraa.Gpio(2)
x3 = mraa.Gpio(3)

x0.dir(mraa.DIR_OUT)
x1.dir(mraa.DIR_OUT)
x2.dir(mraa.DIR_OUT)
x3.dir(mraa.DIR_OUT)

def stepping(GPIO_0, GPIO_1, GPIO_2, GPIO_3):
  x0.write(GPIO_0)
  x1.write(GPIO_1)
  x2.write(GPIO_2)
  x3.write(GPIO_3)

def time_step(x_time):
  time.sleep(x_time)