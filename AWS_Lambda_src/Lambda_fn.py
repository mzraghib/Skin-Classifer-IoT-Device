from __future__ import print_function

import json
import urllib
import boto3

from watson_developer_cloud import VisualRecognitionV3


##################################################
print('Loading function')

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))

    s3.download_file("ec500bucket2", "picture.jpg", "/tmp/pic.jpg")
    image = "/tmp/pic.jpg"
    visual_recognition = VisualRecognitionV3('2016-05-20', api_key='b966b6c9975fee1450156508498b95d16adc5e0a')
    
    with open(image, 'rb') as image_file:
        skin_results = visual_recognition.classify(images_file=image_file,
                                      threshold=0,
                                      classifier_ids=['SkinLesionClassifier_892871557'])
    score = str(skin_results['images'][0]['classifiers'][0]['classes'][0]['score'])
    print("score = ", score)
    client = boto3.client('iot-data', region_name='us-east-1')
    response = client.publish(
            topic='sdkTest/sub',
            qos=0,
            payload=json.dumps({score: "lambda response"}))