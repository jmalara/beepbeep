import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

beep_duration = 0.2;
beep_delay = 0.15;
horn_input = 4;
relay_output = 23;

# Setup input and output
GPIO.setup(horn_input, GPIO.IN)
GPIO.setup(relay_output, GPIO.OUT)

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
