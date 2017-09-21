import RPi.GPIO as GPIO

def rack_compartment0Function():
    if(state == "open"):
        GPIO.output(26, GPIO.HIGH)
    else:
        GPIO.output(26, GPIO.LOW)
