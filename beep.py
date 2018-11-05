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
def hornEventHandler_rising (pin):
    # turn LED on
    GPIO.output(relay_output,True)
    time.sleep(float(beep_duration))	
    GPIO.output(relay_output,False)
    time.sleep(float(beep_delay))
    GPIO.output(relay_output,True)
    time.sleep(float(beep_duration))
    GPIO.output(relay_output,False)
	
GPIO.add_event_detect(btn_input, GPIO.RISING, callback=hornEventHandler_rising) 
 
try:  
    while True : pass  
except:
    GPIO.cleanup()    
