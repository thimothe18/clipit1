#!/usr/bin/python3
# -*- coding: utf-8 -*-
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import clipboard
import boto3

def restart():
	import sys
	print("argv was",sys.argv)
	print("sys.executable was", sys.executable)
	print("restart now")

	import os
	os.execv(sys.executable, ['python'] + sys.argv)
	print("Restarting script")

def initiate_browser():
	options = Options()
	options.headless = True
	streamers = {
		1 : {
			"name": "domingo",
			"instance": "0d4eb30aa2f5142d7"
		},
		2 : {
			"name": "gotaga",
			"instance": "0e9434b17bece5070"
		}
	}
	driver = webdriver.Firefox(options=options)
	streamers_index = 0
	time_counter = 0
	client = boto3.client('ec2', region_name='us-east-1')
	ec2 = boto3.resource('ec2', region_name='us-east-1')

def mature_btn():
	try:
		mature_btn = driver.find_element_by_id('mature-link')
		mature_btn.click()
	except:
		print("mature audiance btn not found")	

def gotostreamer():
	driver.get("https://www.twitch.tv/" + streamers[streamers_index]['name'])
	time.sleep(7)

def streamer_index_checker():
	if streamers_index > 1 :
		streamers_index = 1
	else: 
		streamers_index += 1

def counter():
	time_counter += 1

def livechecker():
	try:
		title1 = driver.find_element_by_css_selector('.live-indicator > div:nth-child(1) > div:nth-child(1) > p:nth-child(1)')
		titre1 = title1.text
		print(titre1)
	except: 
		print("carre rouge direct not found")
		titre1 = "pasdirect"

def vmandscriptstarter():
	if titre1 == "DIRECT":
		print("en direct tmtc")
		filters = [
			{
				'Name': 'instance-state-name', 
				'Values': ['stopped']
			}
		]
		# filter the instances based on filters() above
		instances = ec2.instances.filter(Filters=filters)
		RunningInstances = []	
		for instance in instances:
			# for each instance, append to array and print instance id
			RunningInstances.append(instance.id)
			print ("instance stopped : " + instance.id)
			if instance.id == "i-" + streamers[streamers_index]['instance']:
				client = boto3.client('ec2' ,region_name='us-east-1')
				response = client.start_instances(
				InstanceIds=[
					"i-" + streamers[streamers_index]['instance'],
				],
				DryRun=False
			)
				client = boto3.client('ssm')
				time.sleep(100)
				response = client.send_command(
					InstanceIds=[
						"i-" + streamers[streamers_index]['instance'],
					],
					DocumentName='AWS-RunShellScript',
					DocumentVersion='$DEFAULT',
					# DocumentHash='Sha256 ',
					# DocumentHashType='Sha256',
					TimeoutSeconds=3600,
					Comment='test',
					Parameters={
						"executionTimeout":["9999"],
						'commands': [
							'cd ..',
							'cd ..',
							'cd ..',
							'cd ..',
							'cd home',
							'cd ubuntu', 
							'cd Desktop',
							#'pip3 install selenium',
							#'pip3 install keyboard',
							#'pip3 install pymongo',
							#'pip3 install boto3',
							#'pip3 install clipboard',
							'pip3 install streamlink',
							'export PATH=$PATH:/home/ubuntu/Desktop',
							#'pip3 install pymongo[srv]',
							'python3 stream_client.py'
					]
				},
					OutputS3BucketName='compartiment-thimothe',
					# OutputS3KeyPrefix='string',
					# MaxConcurrency='string',
					# MaxErrors='string',
					# ServiceRoleArn='string',
					# NotificationConfig={
					# 'NotificationArn': 'string',
					# 'NotificationEvents': [
					# 'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
					# ],
					# 'NotificationType': 'Command'|'Invocation'
					# },
					CloudWatchOutputConfig={
						'CloudWatchLogGroupName': 'clipit',
						'CloudWatchOutputEnabled': False
					}
				)
		print("vm and script launched : " + instance.id)
	else:
		print ("wrong vm" + instance.id)

def stoppedvmchecker();
	filters = [
				{
					'Name': 'instance-state-name', 
					'Values': ['running']
				}
			]
			# filter the instances based on filters() above
	instances = ec2.instances.filter(Filters=filters)
	RunningInstances = []	
	for instance in instances:
		# for each instance, append to array and print instance id
		RunningInstances.append(instance.id)
		print ("instance running : " + instance.id)
	print(len(RunningInstances))
	for instance in RunningInstances:
		if instance == "i-" + streamers[streamers_index]['instance']:
			client = boto3.client('ec2' ,region_name='us-east-1')
			response = client.stop_instances(
			InstanceIds=[
				"i-" + streamers[streamers_index]['instance']
			],
			DryRun=False
		)
			print("instance successfully stopped :" + instance)
		else: 
			print("instance already stopped :" + instance)


def rebootchecker():
	if time_counter > 10:
		restart()
	else:
		print("Ca ne fais que " + str(time_counter) + "/100")









while streamers_index < 3: 
	try:
		
		# summit1g ne streame pas actuellement.
		print(streamers[streamers_index]['name'])
		print(titre)

		
		else: 
			

	except Exception as e:
		print(e)
		print("something broked")
		driver.quit()
		continue


