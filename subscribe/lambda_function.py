import os
import json
import boto3
import re

def lambda_handler(event, context):
    userNum = event['number']
    topic = event['topic']
    
    #Require +1 (US country code) and 10 digits
    checkNum = re.search("\+1\d{10}", userNum)
    
    topicList = {'main_topic', 'crob_topic', 'bad_topic', 'hydrate_topic'}
    
    if topic not in topicList:
        #API Gateway configured to return 400
        raise Exception('badrequest')
        return False
    
    if not checkNum:
        #API Gateway configured to return 400
        raise Exception('badrequest')
        return False
    else:
        client = boto3.client('sns')
        response = client.subscribe(
            # use Lambda environment variable to get ARN
            TopicArn=os.environ[topic],
            Protocol='sms',
            Endpoint=userNum)
            
    print(topic)
    if topic == 'main_topic':
        response = client.publish(
        PhoneNumber=userNum,
        Message= 'Registration Confirmed! Welcome to FeelGood!'
        )
    elif topic == 'bad_topic':
        response = client.publish(
        PhoneNumber=userNum,
        Message= 'Registration Confirmed! Welcome to FeelBad!'
        )
    elif topic == 'crob_topic':
        response = client.publish(
        PhoneNumber=userNum,
        Message= 'Registration Confirmed! Welcome to FeelCaw!'
        )
    elif topic == 'hydrate_topic':
        response = client.publish(
        PhoneNumber=userNum,
        Message= 'Registration Confirmed! Welcome to FeelHydrated!'
        )
        
    return True
