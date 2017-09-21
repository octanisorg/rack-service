import RPi.GPIO as GPIO

def rack_compartment5Function(state):
    if(state == "open"):
        GPIO.output(16, GPIO.HIGH)
    else:
        GPIO.output(16, GPIO.LOW)
