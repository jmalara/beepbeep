import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

btn_input = 4;
LED_output = 17;

# GPIO btn_input set up as input.
GPIO.setup(btn_input, GPIO.IN)
GPIO.setup(LED_output, GPIO.OUT)

# handle the button event
def buttonEventHandler_rising (pin):
    # turn LED on
    GPIO.output(LED_output,True)
    
def	def buttonEventHandler_falling (pin):
    # turn LED off
    GPIO.output(LED_output,False)


	
GPIO.add_event_detect(btn_input, GPIO.RISING, callback=buttonEventHandler_rising) 
GPIO.add_event_detect(btn_input, GPIO.FALLING, callback=buttonEventHandler_falling)
 
try:  
    while True : pass  
except:
    GPIO.cleanup()    
