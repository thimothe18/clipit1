#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import sys
from cookies5 import cookies
import time
from time import gmtime, strftime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import clipboard
import boto3
from pymongo import MongoClient
import csv
import urllib.request
import keyboard
import random
import string
import re
import os
import datetime
import subprocess
import streamlink
from subprocess import Popen
from time import sleep

class test:
	def __init__(self, streamer_name, coef, delai_time, breakpoint):
		self.streamer_name = streamer_name
		self.coef = coef
		self.delai_time = delai_time
		self.breakpoint = breakpoint

	def initiate_browser(self):
		self.restart_time = time.time()
		options = Options()
		options.headless = True
		self.driver = webdriver.Firefox(options=options)
		self.streamer_link = "https://www.twitch.tv/" + self.streamer_name
		self.driver.get(self.streamer_link)
		link = self.streamer_link
		print("browser initiated Successfully")
		return link

		#self.driver.implicitly_wait(15)
	def testerie(self):
		print(self.streamer_link)
		print(self.breakpoint)
		print(self.num_page_items)

	def exception(self):
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		print(exc_type, fname, exc_tb.tb_lineno)

	def writecsv_headers(self):
		with open("test.csv", "a", newline='\n') as fp:
			a = csv.writer(fp)
			row = ["Time clip"] + ["Nb pages au clip"] + ["breakpoint"] + ["breakpoint coef"] + ["time"] + ["streamer"] + ["viewers"] + ["name_file"] + ["calcul"]
			a.writerow(row)
			print("Successfully written headers in csv file")

	def click_popupbtn(self):
		try:
			mature_btn = self.driver.find_element_by_id('mature-link')
			mature_btn.click()
			print("mature btn found and clicked on it")
		except:
			print("mature audiance btn not found")

	def twitch_login(self):
		for cookie in cookies:
			self.driver.add_cookie(cookie)
		print("cookies sucessfully added")
		self.driver.refresh()
		time.sleep(115)
		try:
			id = self.driver.find_element_by_id('username')
			mdp = self.driver.find_element_by_name('password')
			login = self.driver.find_element_by_class_name('js-login-text')
			id.send_keys("thimothe")
			mdp.send_keys("tiganala18")
			login.click()
			print("successfully logged")
		except:
			print("login not working")
		time.sleep(7)
		self.driver.get(self.streamer_link)
		time.sleep(3)

	def breakpointaverage_calculator(self):
		if time.time() - self.delai_time > 1800:
			counter_moyenne = 0
			addition_msg = 0
			self.delai_time = time.time()
			while counter_moyenne < 10:
				titre = self.driver.find_elements_by_class_name('chat-line__message')
				self.num_page_items = len(titre)
				counter_moyenne += 1
				addition_msg += self.num_page_items
				self.breakpoint = addition_msg/counter_moyenne
				print("| Nombre de msg : " + str(self.num_page_items) + " | Compteur : " + str(counter_moyenne) + " | Message additionné : " + str(addition_msg) + " | Resultat de la divi: " + str(self.breakpoint) + " |")
				try:
					self.driver.refresh()
				except:
					print("refresh not working")
				time.sleep(30.0 - ((time.time() - self.delai_time) % 30.0))	
			print("Calcul du breakpoint terminé")
			print("--------------------------" + "---------------------------------")
			self.breakpointxcoef = self.breakpoint * self.coef
			print("Breakpoint: " + str(self.breakpoint) + " and breakpoint x coef : " + str(self.breakpointxcoef))
			print("--------------------------" + "---------------------------------")
		else : 
			print("ca fais moins d'une heure donc pas de calcul de breakpoint")

	def current_nb_pages(self):
		starttime = time.time()
		titre = self.driver.find_elements_by_class_name('chat-line__message')
		self.num_page_items = len(titre)
		print("Numbers of messages 30s : " + str(self.num_page_items))
		try:
			self.driver.refresh()
		except:
			print("refresh not working")
		time.sleep(30.0 - ((time.time() - starttime) % 30.0))

	def time_counter(self):
		self.clip_time = time.time()
		timestampp = self.clip_time*1000
		self.timestamp = round(timestampp)
		self.realtimestamp = str(self.timestamp)

	def parametersclip_add(self):
		self.current_date = strftime("%A %d %B", gmtime())
		self.current_time = strftime("%I:%M%p", gmtime())
		nb_viewers = self.driver.find_element_by_class_name('tw-stat__value')
		viewers_string = nb_viewers.text
		tri = repr(nb_viewers.text)
		brut_text = re.split(r"\s", tri)
		streamer_Titre = self.driver.find_element_by_css_selector('h2')
		self.streamer_Title = streamer_Titre.get_attribute('innerHTML')
		streamer_jeu = self.driver.find_element_by_css_selector('p.tw-ellipsis:nth-child(2) > a:nth-child(1)')
		self.streamer_game = streamer_jeu.get_attribute('innerHTML')
		self.truestreamer_game = self.streamer_game.lower()
		self.realstreamergame = self.truestreamer_game.replace(" ", "_")
		print("Lien de la video : ")
		print("texte brut : ")
		print(brut_text)
		self.final_string = viewers_string.replace('\u202f', '')
		print("Nombre brut converti : ")
		print(self.final_string)
		print("Nombre de messages en 30 secondes qui a engendre la creation du clip :")
		print("nombre de messages enregistrer : ")
		print(self.num_page_items)
		vrainumpage = float(self.num_page_items)
		self.vrainbviewers = float(self.final_string)
		self.calcul = vrainumpage/self.vrainbviewers
		print("parameters of clips added successfully")

	def randomString(self, stringLength=10):
		"""Generate a random string of fixed length """
		letters = string.ascii_lowercase
		return ''.join(random.choice(letters) for i in range(stringLength))

	def createName(self):
		self.str_end = p.randomString(5)
		self.name1 = "test" + self.str_end + '.mp4'

	def csvwriter_clip(self):
		with open("lestream.csv", "a", newline='\n') as fp:
			a = csv.writer(fp)
			row = [self.clip_time] + [self.num_page_items] + [self.breakpoint] + [self.breakpointxcoef] + [self.current_time] + [self.streamer_name] + [self.final_string] + [self.name1] + [self.calcul] 
			a.writerow(row)
			print("Enregistrement réussi des params du clip dans test.csv")

	def stream_downloader_clip(self):
		time.sleep(20)
		window_before = self.driver.window_handles[0]
		try:
			#element_to_hover_over = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div[2]")
			#hover = ActionChains(driver)
			#hover.move_to_element(element_to_hover_over)
			#clipbutton = driver.find_element_by_css_selector('.player-controls__right-control-group > div:nth-child(2) > button:nth-child(1)')
			#hover.click(clipbutton)
			#hover.perform()
			ActionChains(self.driver).key_down(Keys.LEFT_ALT).send_keys('x').key_up(Keys.LEFT_ALT).perform()
			print("Successfully clicked on clip button")
		except Exception as e:
			print("clip button not found")
			print(e)
		time.sleep(15)
		window_after = self.driver.window_handles[1]
		self.driver.switch_to_window(window_after)
		try:
			css = self.driver.find_element_by_css_selector('.highwind-video-player__container > video:nth-child(1)')
			poney = css.get_attribute('innerHTML')
			outer = css.get_attribute('outerHTML')
			oui = css.get_attribute('src')
		except:
			print('src video clip not found')
		try:
			print("Downloading starts...\n")
			urllib.request.urlretrieve(oui, self.name1)
			print("Download completed..!!")
		except Exception as e:
			print(e)
		self.driver.close()
		self.driver.switch_to_window(window_before)
		self.driver.refresh()
				
	def uploadmongobands3(self):
		s3 = boto3.client('s3')
		source = "source"
		date = "date"
		filename = self.name1
		bucket_name = 'compartiment-thimothe'
		nom = "name"
				
			# Uploads the given file using a managed uploader, which will split up large
			# files automatically and upload parts in parallel.
		s3.upload_file(filename, bucket_name, filename)
		client = MongoClient('mongodb+srv://cheval:Tiganala18@test-y9xs2.gcp.mongodb.net/test?retryWrites=true')
		db = client.test
		collection = db.items
		collection.create_index("deleted_date", expireAfterSeconds=604800)
		
		object = { 
		source: "https://s3.eu-west-3.amazonaws.com/compartiment-thimothe/" + self.name1,
		date: datetime.datetime.utcnow(),
		nom: self.streamer_name,
		"title": self.streamer_Title,
		"game": self.streamer_game,
		"trimmed-game": self.realstreamergame,
		"date": self.current_date,
		"time": self.current_time,
		"timestamp": self.realtimestamp,
		"message": self.calcul,
		"deleted_date": datetime.datetime.utcnow()
		} 
		collection.insert_one(object)
		print("Successfully sent to MongoDB and AWS")
		os.remove(self.name1)

	def csvwriter_noclip(self):
		current_time = strftime("%I:%M%p", gmtime())   
		with open("lestream" + ".csv", "a", newline='\n') as fp:
			a = csv.writer(fp)
			row = [self.clip_time] + [self.num_page_items] + [self.breakpoint] + [self.breakpointxcoef] + [self.current_time]
			a.writerow(row)
			print("Successfully written no clip stats in csv file")
		print("nombres de pages enregistrer a la fin du script : " + str(self.num_page_items))

	def quitter(self):
		self.driver.quit()
		print("driver discarded successfully")

	def restart(self):
		if time.time() - self.restart_time > 5000:
			self.restart_time = time.time()
			self.driver.quit()
			print("argv was",sys.argv)
			print("sys.executable was", sys.executable)
			print("restart now")
			os.execv(sys.executable, ['python3'] + sys.argv)
			print("Restarting script")
			print("Script successfully restarted")
		else:
			time_passed = time.time() - self.restart_time
			print("Restart time is only " + str(time_passed)  + "/" + "3600")

	def clipcreator(self):
		if self.num_page_items > self.breakpointxcoef:
			p.time_counter()
			p.parametersclip_add()
			p.createName()
			p.csvwriter_clip()
			p.stream_downloader_clip()
			p.uploadmongobands3()
		else:
			print("clip not made this time")

	def restarter(self):
		self.restart_time = time.time()
		self.driver.quit()
		print("argv was",sys.argv)
		print("sys.executable was", sys.executable)
		print("restart now")
		os.execv(sys.executable, ['python3'] + sys.argv)
		print("Restarting script")
		print("Script successfully restarted")

	def watcher(self):
		while self.breakpoint > 0:
			p.breakpointaverage_calculator()
			p.current_nb_pages()
			p.testerie()
			p.clipcreator()
			p.restart()

    # execute only if run as a script
if __name__ == "__main__":
	try:
		p = test('lestream', 1.5, 1801, 1)
		link = p.initiate_browser()
		print(link)
		p.writecsv_headers()
		p.twitch_login()
		p.watcher()
		p.quitter()
	except Exception as e:
		print(e)
		p.exception()
		p.restarter()
