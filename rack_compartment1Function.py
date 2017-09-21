import RPi.GPIO as GPIO

def rack_compartment1Function(state):
    if(state == "open"):
        GPIO.output(21, GPIO.HIGH)
    else:
        GPIO.output(21, GPIO.LOW)
