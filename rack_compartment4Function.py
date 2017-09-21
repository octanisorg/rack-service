import RPi.GPIO as GPIO

def rack_compartment4Function():
    if(state == "open"):
        GPIO.output(12, GPIO.HIGH)
    else:
        GPIO.output(12, GPIO.LOW)
