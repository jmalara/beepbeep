import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

GPIO.output(23, 1)
time.sleep(float(sys.argv[1]))
GPIO.output(23, 0)

time.sleep(float(sys.argv[2]))
GPIO.output(23, 1)

time.sleep(float(sys.argv[1]))
GPIO.output(23, 0)

GPIO.cleanup()
