import RPi.GPIO as GPIO

def rack_compartment4Function(state):
    if(state == "open"):
        GPIO.output(12, GPIO.HIGH)
    else:
        GPIO.output(12, GPIO.LOW)
