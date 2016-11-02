import mraa

def lamp_on(pin):
  lamp = mraa.Gpio(pin)
  lamp.dir(mraa.DIR_OUT)
  lamp.write(1)

def lamp_off(pin):
  lamp = mraa.Gpio(pin)
  lamp.dir(mraa.DIR_OUT)
  lamp.write(0)