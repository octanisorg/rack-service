import RPi.GPIO as GPIO

def rack_compartment3Function():
    if(state == "open"):
        GPIO.output(6, GPIO.HIGH)
    else:
        GPIO.output(6, GPIO.LOW)
