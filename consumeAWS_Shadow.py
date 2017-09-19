from tkinter import *

import time
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
import json

import RackActions


# Custom MQTT message callback
def customCallback_01(client, userdata, message):
    # print("Received a new message: ")
    # print(message.payload)
    # print("from topic: ")
    # print(message.topic)
    print("--------END customCallback_01------\n\n")



def customCallback_02(client, userdata, message):
    # print("Received a new message: ")
    # print(message.payload)
    # print("from topic: ")
    # print(message.topic)
    RackActions.GetUpdatedRackState(message)


# --------------------------------------------------------------
# -----------SHADOW CLIENT ACTIONS -----------------------------
# --------------------------------------------------------------

# Create an AWS IoT MQTT Shadow Client using Websocket SigV4
# myShadowClient = AWSIoTPyMQTT.AWSIoTMQTTShadowClient("raul",  useWebsocket=True)
#
# myShadowClient.clearLastWill()
#
# myShadowClient.configureEndpoint("aj34tk2y4o3ym.iot.eu-central-1.amazonaws.com", 443)
#
# # For Websocket, we only need to configure the root CA
# myShadowClient.configureCredentials("certif")
#
# #                                       baseReconnectQuietTimeSecond, maxReconnectQuietTimeSecond, stableConnectionTimeSecond
# #myShadowClient.configureAutoReconnectBackoffTime(3, 10, 12)
#
# #                                       timeoutSecond
# myShadowClient.configureConnectDisconnectTimeout(10)
# myShadowClient.configureMQTTOperationTimeout(5)
#
# # Connect to AWS IoT with default keepalive set to 30 seconds
# myShadowClient.connect(30)
#
# # Create a device shadow handler for shadow named "green_rack_raspi", using non-persistent subscription
# OctanisRackShadow = myShadowClient.createShadowHandlerWithName("green_rack_raspi", False)
#
# # # Retrieve the shadow JSON document from AWS IoT, with a timeout set to 5 seconds
# OctanisRackShadow.shadowGet(customCallback_01, 5)


# --------------------------------------------------------------
# -----------MESSAGE BROKER CLIENT ACTIONS----------------------
# --------------------------------------------------------------
# Create an AWS IoT MQTT Client using Websocket SigV4
myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient("raul", useWebsocket=True)

myAWSIoTMQTTClient.configureEndpoint("aj34tk2y4o3ym.iot.eu-central-1.amazonaws.com", 443)

myAWSIoTMQTTClient.configureCredentials("certif")

myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)

myAWSIoTMQTTClient.configureMQTTOperationTimeout(15)

myAWSIoTMQTTClient.connect()
# https://github.com/aws/aws-iot-device-sdk-python
# DOC: https://s3.amazonaws.com/aws-iot-device-sdk-python-docs/sphinx/html/generated/AWSIoTPythonSDK.MQTTLib.html?highlight=subscribe#AWSIoTPythonSDK.MQTTLib.AWSIoTMQTTClient.subscribe
myAWSIoTMQTTClient.subscribe("$aws/things/green_rack_raspi/shadow/update/accepted", 1, customCallback_02)

time.sleep(2)

while True:
    time.sleep(1)

print("End process")






#
# # Retrieve the AWS IoT MQTT Client used in the AWS IoT MQTT Shadow Client
# thisAWSIoTMQTTClient = myShadowClient.getMQTTConnection()
#
# # Perform plain MQTT operations using the same connection
# #thisAWSIoTMQTTClient.publish("Topic", "Payload", 1)
#

# See: https://github.com/aws/aws-iot-device-sdk-python/blob/master/samples/ThingShadowEcho/ThingShadowEcho.py
# newPayload = '{"m":"hello"}'
# OctanisRackShadow.shadowUpdate(newPayload, None, 5)
# print("Sent.")



# OctanisRackShadow.unsubscribe("Rack")
