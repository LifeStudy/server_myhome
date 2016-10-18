import RPi.GPIO as GPIO

def gpio_config(gpio):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(gpio,GPIO.OUT)
	
def lamp_on(gpio_io):
	GPIO.output(gpio_io,GPIO.HIGH)

def lamp_off(gpio_io):
	GPIO.output(gpio_io,GPIO.LOW)
