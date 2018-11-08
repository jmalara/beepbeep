import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Set beep duration in seconds
beep_duration = 0.2;
# Set the delay between the two beeps
beep_delay = 0.15;

# Set GPIO pins
horn_input = 3;
relay_output = 16;

# Setup input and output
GPIO.setup(horn_input, GPIO.IN)
GPIO.setup(relay_output, GPIO.OUT)

if GPIO.input(horn_input):           # if port 25 == 1  
    print "Port 3 is 1/GPIO.HIGH/True"  
else:  
    print "Port 3 is 0/GPIO.LOW/False"  
 
try:  
    while True : time.sleep(0.05)  
except:
    GPIO.cleanup()    
