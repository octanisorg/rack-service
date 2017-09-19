# Actions over the Racks

import json
import rack_compartment0Function
import rack_compartment6Function

def GetUpdatedRackState(message):

    # In Py3.x, message.payload comes in as a bytes(string)
    # json.loads needs a string input
    payloadUTF8String = message.payload.decode('utf-8')
    #print(payloadUTF8String)

    decoded_data = json.loads(payloadUTF8String)
    #print(json.dumps(decoded_data, sort_keys=True, indent=4))


    validCompartments = {           "rack_compartment0": "rack_compartment0Function",
                                    "rack_compartment1": "rack_compartment1Function",
                                    "rack_compartment2": "rack_compartment2Function",
                                    "rack_compartment3": "rack_compartment3Function",
                                    "rack_compartment4": "rack_compartment4Function",
                                    "rack_compartment5": "rack_compartment5Function",
                                    "rack_compartment6": "rack_compartment6Function",
                                    "rack_compartment7": "rack_compartment7Function",
                                    "rack_compartment8": "rack_compartment8Function",
                                    "rack_compartment9": "rack_compartment9Function",
                                    "rack_compartment10": "rack_compartment10Function"
                                }

    #validCompartmentsList = json.dumps(validCompartments)

    validCompartmentsList = dict(validCompartments)

    #validCompartmentsList = json.load(validCompartments)

    for rack_compartment in decoded_data['state']['desired']:
        if rack_compartment in validCompartmentsList:
            print("desired value for {0}: ".format(rack_compartment), decoded_data['state']['desired'][rack_compartment])

            if rack_compartment == "rack_compartment0":
                functionCalled = validCompartmentsList["rack_compartment0"]
                print(functionCalled)
                getattr(rack_compartment0Function, functionCalled)()


    #numCompart = 0

    # while True:
    #     rack_compartmentX = "rack_compartment" + str(numCompart)
    #
    #     if rack_compartmentX in decoded_data['state']['desired']:
    #         print("desired value for {0}: ".format(rack_compartmentX),decoded_data['state']['desired'][rack_compartmentX])
    #         numCompart = numCompart + 1
    #     else:
    #         print("break")
    #         break

        # try:
        #     print("desired value for {0}: ".format(rack_compartmentX), decoded_data['state']['desired'][rack_compartmentX])
        #     numCompart = numCompart + 1
        #
        # except:
        #     break



    # class MQTTMessage:
    #     """ This is a class that describes an incoming message. It is passed to the
    #     on_message callback as the message parameter.
    #     Members:
    #     topic : String. topic that the message was published on.
    #     payload : String/bytes the message payload.
    #     qos : Integer. The message Quality of Service 0, 1 or 2.
    #     retain : Boolean. If true, the message is a retained message and not fresh.
    #     mid : Integer. The message id

