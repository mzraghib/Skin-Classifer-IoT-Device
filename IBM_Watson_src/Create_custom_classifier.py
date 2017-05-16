import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='b966b6c9df75fee1450156508498b9ads5d16adc5e0a')

   
with open('/home/zuhayr/BU/EC500J1/Project/Dataset/Training/M_neg_SK_neg.zip', 'rb') as safe, \
    open('/home/zuhayr/BU/EC500J1/Project/Dataset/Training/M_pos_SK_negFINAL.zip', 'rb') as melanoma:
   print(json.dumps(visual_recognition.create_classifier('SkinLesionClassifier', melanoma_positive_examples=melanoma, negative_examples=safe), indent=2))

    
