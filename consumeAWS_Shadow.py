import time
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
import json
import RackActions

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

#setup gpio
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)



# Custom MQTT message callback

def customCallback_02(client, userdata, message):
    # print("Received a new message: ")
    # print(message.payload)
    # print("from topic: ")
    # print(message.topic)
    RackActions.GetUpdatedRackState(message)



# --------------------------------------------------------------
# -----------MESSAGE BROKER CLIENT ACTIONS----------------------
# --------------------------------------------------------------
# Create an AWS IoT MQTT Client using Websocket SigV4
myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient("raul", useWebsocket=True)

myAWSIoTMQTTClient.configureEndpoint("aj34tk2y4o3ym.iot.eu-central-1.amazonaws.com", 443)

myAWSIoTMQTTClient.configureCredentials("C:\Raul\Desarrollos\Python\Octanis\Rack\certif")

myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)

myAWSIoTMQTTClient.configureMQTTOperationTimeout(15)

myAWSIoTMQTTClient.connect()
# https://github.com/aws/aws-iot-device-sdk-python
# DOC: https://s3.amazonaws.com/aws-iot-device-sdk-python-docs/sphinx/html/generated/AWSIoTPythonSDK.MQTTLib.html?highlight=subscribe#AWSIoTPythonSDK.MQTTLib.AWSIoTMQTTClient.subscribe
myAWSIoTMQTTClient.subscribe("$aws/things/green_rack_raspi/shadow/update/accepted", 1, customCallback_02)

time.sleep(2)

while True:
    time.sleep(1)

