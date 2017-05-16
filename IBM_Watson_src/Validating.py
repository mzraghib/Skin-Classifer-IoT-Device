#validate with a set of 50 images not used for training
import json
from os.path import join, dirname
import os
from watson_developer_cloud import VisualRecognitionV3
from os import listdir

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='bdf6bdf975fee1450156508498b95d16adc5e0a')

path  = "/home/zuhayr/BU/EC500J1/Project/Dataset/Testing/Validating/M_pos_SK_neg(V)"

count = 0
	
for file in os.listdir(path):
    if file.endswith(".jpg"):
    	image = os.path.join(path, file)
    	print(image)
    	count += 1
    	print(count)
    	with open(image, 'rb') as image_file:
    		skin_results = visual_recognition.classify(images_file=image_file,
    	                                      threshold=0.1,
                                              classifier_ids=['SkinLesionClassifier_892871557'])

    		print(json.dumps(skin_results, indent=2))

''' #for single picture from Validating folder           
skin_path = '/home/zuhayr/BU/EC500J1/Project/Dataset/Testing/Validating/M_pos_SK_neg(V)/ISIC_0000145.jpg'
'''

''' #for single picture from training folder  
#skin_path = '/home/zuhayr/BU/EC500J1/Project/Dataset/Training/M_pos_SK_negFINAL/ISIC_0011136.jpg'





'''
