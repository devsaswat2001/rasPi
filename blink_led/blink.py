import RPi.GPIO as GPIO
import time

pin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.OUT)
GPIO.output(pin,GPIO.HIGH)
time.sleep(4)
GPIO.output(pin,GPIO.LOW)
