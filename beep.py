import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set beep duration in seconds
beep_duration = 0.2;
# Set the delay between the two beeps
beep_delay = 0.15;

# Set GPIO pins
horn_input = 4;
relay_output = 23;

# Setup input and output
GPIO.setup(horn_input, GPIO.IN)
GPIO.setup(relay_output, GPIO.OUT)

# Handle horn press event
def hornEventHandler_rising (pin):
    # First beep
    print("beep")
    GPIO.output(relay_output,True)
    time.sleep(float(beep_duration))	
    # Delay between beeps
    GPIO.output(relay_output,False)
    time.sleep(float(beep_delay))
    # Second beep
    print("beep")
    GPIO.output(relay_output,True)
    time.sleep(float(beep_duration))
    GPIO.output(relay_output,False)
	
GPIO.add_event_detect(horn_input, GPIO.RISING, callback=hornEventHandler_rising) 
 
try:  
    while True : pass  
except:
    GPIO.cleanup()    
