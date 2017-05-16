import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3


visual_recognition = VisualRecognitionV3('2016-05-20', api_key='b966b6sd975fef1450156508498b95d16adc5e0a')


'''delete classidier'''
#print(json.dumps(visual_recognition.delete_classifier(classifier_id='SkinLesionClassifier_1787595594'), indent=2))


'''list custom classifiers'''
#print(json.dumps(visual_recognition.list_classifiers(), indent=2))


'''get custom classifier details'''

print(json.dumps(visual_recognition.get_classifier('SkinLesionClassifier_892871557'), indent=2))
