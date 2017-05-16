#!/usr/bin/python
import os
import pygame, sys
from pygame.locals import *
import pygame.camera

import boto3
#Although opencv gives a clearer image, pygame is used to avoid installing opencv
#which requires 1 to 2gb of free space which was not available

#take picture
#initialise pygame   
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0", (640, 480))  # width =640, height = 480
cam.start()
#take a picture
image = cam.get_image()
cam.stop()

#save picture
pygame.image.save(image,'picture1.jpg')


#######################################
'''send to AWS S3 bucket'''

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Get a bucket by name
bucket = s3.Bucket('ec500bucket2')
#Upload a new file
with open('picture1.jpg','rb') as data:
    bucket.Object('picture.jpg').put(Body=data) #dont change object key here


