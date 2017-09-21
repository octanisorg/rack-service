# Actions over the Racks

import json
import rack_compartment0Function
import rack_compartment1Function
import rack_compartment2Function
import rack_compartment3Function
import rack_compartment4Function
import rack_compartment5Function
import rack_compartment6Function
import rack_compartment7Function
import rack_compartment8Function
import rack_compartment9Function
import rack_compartment10Function

def GetUpdatedRackState(message):

    # In Py3.x, message.payload comes in as a bytes(string)
    # json.loads needs a string input
    payloadUTF8String = message.payload.decode('utf-8')

    decoded_data = json.loads(payloadUTF8String)


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

    validCompartmentsList = dict(validCompartments)

    for rack_compartment in decoded_data['state']['desired']:
        if rack_compartment in validCompartmentsList:
            print("desired value for {0}: ".format(rack_compartment), decoded_data['state']['desired'][rack_compartment])

            if rack_compartment == "rack_compartment0":
                functionCalled = validCompartmentsList["rack_compartment0"]
                getattr(rack_compartment0Function, functionCalled)(decoded_data['state']['desired'][rack_compartment])
            elif rack_compartment == "rack_compartment1":
                functionCalled = validCompartmentsList["rack_compartment1"]
                getattr(rack_compartment1Function, functionCalled)(decoded_data['state']['desired'][rack_compartment])
            elif rack_compartment == "rack_compartment2":
                functionCalled = validCompartmentsList["rack_compartment2"]
                getattr(rack_compartment2Function, functionCalled)(decoded_data['state']['desired'][rack_compartment])
            elif rack_compartment == "rack_compartment3":
                functionCalled = validCompartmentsList["rack_compartment3"]
                getattr(rack_compartment3Function, functionCalled)(decoded_data['state']['desired'][rack_compartment])
            elif rack_compartment == "rack_compartment4":
                functionCalled = validCompartmentsList["rack_compartment4"]
                getattr(rack_compartment4Function, functionCalled)(decoded_data['state']['desired'][rack_compartment])
            elif rack_compartment == "rack_compartment5":
                functionCalled = validCompartmentsList["rack_compartment5"]
                getattr(rack_compartment5Function, functionCalled)(decoded_data['state']['desired'][rack_compartment])
            elif rack_compartment == "rack_compartment6":
                functionCalled = validCompartmentsList["rack_compartment6"]
                getattr(rack_compartment6Function, functionCalled)(decoded_data['state']['desired'][rack_compartment])
            elif rack_compartment == "rack_compartment7":
                functionCalled = validCompartmentsList["rack_compartment7"]
                getattr(rack_compartment7Function, functionCalled)(decoded_data['state']['desired'][rack_compartment])
            elif rack_compartment == "rack_compartment8":
                functionCalled = validCompartmentsList["rack_compartment8"]
                getattr(rack_compartment8Function, functionCalled)(decoded_data['state']['desired'][rack_compartment])
            elif rack_compartment == "rack_compartment9":
                functionCalled = validCompartmentsList["rack_compartment9"]
                getattr(rack_compartment9Function, functionCalled)(decoded_data['state']['desired'][rack_compartment])
            elif rack_compartment == "rack_compartment10":
                functionCalled = validCompartmentsList["rack_compartment10"]
                getattr(rack_compartment10Function, functionCalled)(decoded_data['state']['desired'][rack_compartment])
            else:
                functionCalled = validCompartmentsList["rack_compartment0"]
                getattr(rack_compartment0Function, functionCalled)(decoded_data['state']['desired'][rack_compartment]) 

            print(functionCalled)


            # if rack_compartment == "rack_compartment0":
            #     functionCalled = validCompartmentsList["rack_compartment0"]
            #     print(functionCalled)
            #     getattr(rack_compartment0Function, functionCalled)()



    # class MQTTMessage:
    #     """ This is a class that describes an incoming message. It is passed to the
    #     on_message callback as the message parameter.
    #     Members:
    #     topic : String. topic that the message was published on.
    #     payload : String/bytes the message payload.
    #     qos : Integer. The message Quality of Service 0, 1 or 2.
    #     retain : Boolean. If true, the message is a retained message and not fresh.
    #     mid : Integer. The message id

