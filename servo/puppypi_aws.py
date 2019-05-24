import sys
import getopt
import os.path
import picamera
import time
import boto3
import json
import os

import puppypi_config
import puppypi_util


def generateAndPlayAudio(namebase, audiotext):
	file_mp3 = namebase + '.mp3'
	if (not os.path.exists(file_mp3)):
		puppypi_util.printmsg( 'MP3 file not there - let us create it')
		client = boto3.client('polly')
		response = client.synthesize_speech(OutputFormat='mp3', Text=audiotext, VoiceId='Joey')	
		thebytes = response['AudioStream'].read()
		thefile = open(file_mp3, 'wb')
		thefile.write(thebytes)
		thefile.close()
		
	os.system('mpg123 -q ' + file_mp3 + ' &')


def mainAWS(namebase):
	finalstring = takePhotoAndProcess(namebase)
	puppypi_util.printmsg( '"{}"'.format(finalstring))
	generateAndPlayAudio(namebase, finalstring)


def takePhotoAndProcess(namebase):
	file_jpg=namebase + '.jpg'
	file_json=namebase + '.json'
	puppypi_util.printmsg( 'Name Base:"{}", JPG:"{}"'.format(namebase, file_jpg))
	if (not os.path.exists(file_jpg) or not os.path.exists(file_json)):
		puppypi_util.printmsg( 'File not there - let us create it')
		with picamera.PiCamera() as camera:
		    puppypi_util.printmsg( 'Taking a photo to {}'.format(file_jpg))
		    camera.capture(file_jpg)


		with open(file_jpg, 'rb') as f_file_jpg:
			b_a_jpg = bytearray(f_file_jpg.read())
			rclient = boto3.client('rekognition')
			puppypi_util.printmsg( 'Start image rekognition {}'.format(file_jpg))
			response = rclient.detect_faces(Image={	'Bytes': b_a_jpg}, Attributes=['ALL'])
		puppypi_util.printmsg( 'Wrinting JSON to {}'.format(file_json))
		with open(file_json, 'w') as outfile:
			json.dump(response, outfile)

        try:
   	    finalstring = processJSON(file_json)
        except (IndexError):
            finalstring = 'No face found'
	return finalstring


def processJSON(file_json):
	finalstring = ''
	puppypi_util.printmsg( 'Reading JSON from {}'.format(file_json))
	with open(file_json) as data_file:    
		data = json.load(data_file)

	age_range_low=data["FaceDetails"][0]["AgeRange"]["Low"]
	age_range_high=data["FaceDetails"][0]["AgeRange"]["High"]
	gender=data["FaceDetails"][0]["Gender"]["Value"]

	finalstring = finalstring + 'It is nice to meet a human ' + gender + '. '
	finalstring = finalstring + 'I think you are at least {} but are no older than {} years old. '.format(age_range_low, age_range_high)

	if data["FaceDetails"][0]["Eyeglasses"]["Value"]:
		puppypi_util.printmsg( 'Eyeglasses')
		finalstring = finalstring + 'Nice glasses. '

	if data["FaceDetails"][0]["Sunglasses"]["Value"]:
		puppypi_util.printmsg( 'Sunglasses')
		finalstring = finalstring + 'Possibly sun-glasses. '

	if data["FaceDetails"][0]["Smile"]["Value"]:
		puppypi_util.printmsg( 'Smiling')
		finalstring = finalstring + 'I like your smile. '

	if data["FaceDetails"][0]["Mustache"]["Value"]:
		puppypi_util.printmsg( 'Mustache')
		finalstring = finalstring + 'Cool mustache. '

	if data["FaceDetails"][0]["Beard"]["Value"]:
		puppypi_util.printmsg( 'Beard')
		finalstring = finalstring + 'Neat beard. '

	
	emotion = data["FaceDetails"][0]["Emotions"][0]["Type"]
	finalstring = finalstring + 'Are you feeling ' + emotion + '! '

	return finalstring

