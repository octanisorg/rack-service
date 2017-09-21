import RPi.GPIO as GPIO

def rack_compartment2Function():
    if(state == "open"):
        GPIO.output(20, GPIO.HIGH)
    else:
        GPIO.output(20, GPIO.LOW)
