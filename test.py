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

if GPIO.input(horn_input):
    print("volt detected");
 
try:  
    while True : pass  
except:
    GPIO.cleanup()    
