import json
import boto3
import random
import re
import os

def lambda_handler(event, context):
    client = boto3.client('sns')
    
    messageChoices = ['Have a great day!', 'Today is your day!', 
                      'If you can dream it, you can build it.', '🎉', 
                      'It\'s a great day to be awesome!', 
                      'Your computer believes in you!', 
                      'Don\'t give up before you try. Once you\'ve tried, try again.', 
                      'There\'s a sunny day right around the corner!']
    shitpostMessageChoices = ['YEET', 'le CROB', 
                              'CROBBER is the greatest social media platform known to mankind.', 
                              'Lake Titicawcaw is only 42,069 miles away as the CROB flies.', 
                              'Google Docs is the only version control you\'ll ever need', 
                              'Project1_New_New_Final_New_2.pdf.jpg', 'REEEEEEEEEEEEEE',
                              'git push origin master --force', '💩', 
                              '🤬 ', 'Making it Rain 😂', 
                              'Haha, you n00b. No \'Access-Control-Allow-Origin\' header is present on the requested resource.']
    hydrateMessageChoices = ['*Drinks Water*', 'H a v e A S i p p p', 
                             'Drink more water! You\'ll Feel Better!', 
                             'Staying thirsty is old news. Stay hydrated, my friend.', 
                             'https://www.reddit.com/r/hydrohomies', '🧊', '🚰']
    
    index = random.randint(0, len(messageChoices)-1)
    shitpostIndex = random.randint(0, len(shitpostMessageChoices)-1)
    hydrateIndex = random.randint(0, len(hydrateMessageChoices)-1)

    
    response = client.publish(
        # use Lambda environment variables to retrieve ARN
        TopicArn=os.environ['feelGoodTopic'],
        Message= messageChoices[index],
        Subject='Feel Good Message'
    )
    
    response = client.publish(
        # use Lambda environment variables to retrieve ARN
        TopicArn=os.environ['feelBadTopic'],
        Message= shitpostMessageChoices[shitpostIndex],
        Subject='GET WREKT'
    )
    
    
    response = client.publish(
        # use Lambda environment variables to retrieve ARN
        TopicArn=os.environ['feelCawwTopic'],
        Message= translate_message(messageChoices[index]),
        Subject='CAAAAAWWWWW'
    )
    
    response = client.publish(
        # use Lambda environment variables to retrieve ARN
        TopicArn=os.environ['feelHydratedTopic'],
        Message= hydrateMessageChoices[hydrateIndex],
        Subject='Hydration is Life'
    )
    
    return {
        'statusCode': 200
    }

# Borrowed from https://github.com/Chris-Johnston/CROBBER
def translate_message(input: str) -> str:
    """
    Translate a sentence into CRAW speak
    >>> translate_message("Y'all ever just YEET?")
    'CAAWW CAAW CAAW CAAWW'
    """
    return ' '.join([translate_word(x) for x in input.split()])

def translate_word(input: str) -> str:
    """
    Translate a word into CAW speak
    >>> translate_word("tests")
    'CAAWW'
    >>> translate_word("test")
    'CAAW'
    >>> translate_word("")
    ''
    >>> translate_word("a")
    'CA'
    >>> translate_word("ab")
    'CAW'
    >>> translate_word("abc")
    'CAW'
    """
    random.seed("CAAAAAWWWWW")
    if len(input) == 0:
        return ''
    if len(input) == 1:
        return 'CA'
    if len(input) == 2 or len(input) == 3:
        return 'CAW'
    # subtract the starting C and the ending W
    x = len(input) - 2
    # must have at least one A
    num_a = random.randint(1, x)
    return 'C' + ('A'*num_a) + ('W'*(x - (num_a - 1)))
