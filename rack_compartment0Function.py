import RPi.GPIO as GPIO

def rack_compartment0Function():
    print('this is the rack_compartment0Function call')
    GPIO.output(26, GPIO.HIGH)

