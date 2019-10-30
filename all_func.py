#!/usr/bin/python3
# -*- coding: utf-8 -*-
#List of every function usefultesterie

import sys
import os
import time

def restart():
        import sys
        print("argv was",sys.argv)
        print("sys.executable was", sys.executable)
        print("restart now")

        import os
        os.execv(sys.executable, ['python'] + sys.argv)

def restart1():
	#not tested
	os.execv('/AbsolutePathtoScript/a.py', lst_args)  

def restart_program():
	#not tested
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def initiate_browser(streamer_name):
	options = Options()
	options.headless = True
	streamer_link = "https://www.twitch.tv/" + streamer_name
	#global driver
	driver = webdriver.Firefox(options=options)
	driver.get(streamer_link)
	driver.implicitly_wait(15)
	return driver, streamer_link

def initializer_params():
	breakpoint = 1
	coef = 1.1
	streamer_name = 'gotaga'
	delai_time = 1801
	return breakpoint, coef, streamer_name, delai_time

def writecsv_headers():
	with open("test.csv", "a", newline='\n') as fp:
		a = csv.writer(fp)
		row = ["Time clip"] + ["Nb pages au clip"] + ["breakpoint"] + ["breakpoint coef"] + ["time"] + ["streamer"] + ["viewers"] + ["name_file"] + ["calcul"]
		a.writerow(row)
		print("Successfully written headers in csv file")

#Try to clip on the first popup
def click_popupbtn():
	try:
		mature_btn = driver.find_element_by_id('mature-link')
		mature_btn.click()
	except:
		print("mature audiance btn not found")

def twitch_login(streamer_link):
	for cookie in cookies:
		driver.add_cookie(cookie)
	print("cookies sucessfully added")
	driver.refresh()
	time.sleep(115)
	try:
		id = driver.find_element_by_id('username')
		mdp = driver.find_element_by_name('password')
		login = driver.find_element_by_class_name('js-login-text')
		id.send_keys("thimothe")
		mdp.send_keys("tiganala18")
		login.click()
		print("successfully logged")
	except:
		print("login not working")
	time.sleep(7)
	driver.get(streamer_link)
	time.sleep(3)

def breakpointaverage_calculator(delai_time, driver):
	if time.time() - delai_time > 1800:
		counter_moyenne = 0
		addition_msg = 0
		delai_time = time.time()
		while counter_moyenne < 10:
			titre = driver.find_elements_by_class_name('chat-line__message')
			num_page_items = len(titre)
			counter_moyenne += 1
			addition_msg += num_page_items
			breakpoint = addition_msg/counter_moyenne
			print("| Nombre de msg : " + str(num_page_items) + " | Compteur : " + str(counter_moyenne) + " | Message additionné : " + str(addition_msg) + " | Resultat de la divi: " + str(breakpoint) + " |")
			try:
				driver.refresh()
			except:
				print("refresh not working")
			time.sleep(30.0 - ((time.time() - delai_time) % 30.0))	
		print("Calcul du breakpoint terminé")
		print("--------------------------" + "---------------------------------")
		print("Breakpoint: " + str(breakpoint) + " and breakpoint x coef : " + str(breakpoint*coef))
		print("--------------------------" + "---------------------------------")
		return breakpoint, delai_time
	else : 
		print("ca fais moins d'une heure donc pas de calcul de breakpoint")

def current_nb_pages():
	starttime = time.time()
	titre = driver.find_elements_by_class_name('chat-line__message')
	num_page_items = len(titre)
	print("Numbers of messages 30s : " + str(num_page_items))
	try:
		driver.refresh()
	except:
		print("refresh not working")
	time.sleep(30.0 - ((time.time() - starttime) % 30.0))
	return num_page_items

def time_counter():
	clip_time = time.time()
	timestampp = clip_time*1000
	timestamp = round(timestampp)
	realtimestamp = str(timestamp)
	return clip_time
# realtimestap, clip_time 

def breakpoint_adaptater(too_late, too_early):
#If the lastclip was made less than x seconds ago since the current clip
	try: 
		elapsed = clip_time - cliplast_time
		print("temps elapsed : ")
		print(elapsed)
		# 350 represente 30s * 12 donc 12 clips non selectionne --> si il y a 12 clips ou plus non selectionne entre chaque clip selectionne alors diminue le breakpoint
		if elapsed > too_late:
			breakpoint = breakpoint - 1
			# 70 represente 30s * 2 donc si il y a que 2 clips ou moins  non slectionne entre chaque clip selectionne alors augmente le breakpoint
		if elapsed < too_early:
			breakpoint = breakpoint + 1
			# Pour que ca augmente en fonction du temps sans clip et que ca soit plus precis que juste au desssus de x ou en dessous de y
			# if(grade >= 90):
				# print(“You’re doing great!”)
			# elif(grade <= 89 and >= 78):
				# print(“You’re doing good!”)
			# elif(grade >65 and <= 77)
				# print("You need some work")
			# else:
				# print("Contact your teacher")
	except:
		print("Calcul du délai entre le clip précédent et celui-ci échoué")

def parametersclip_add(num_pages_items):
	current_date = strftime("%A %d %B", gmtime())
	current_time = strftime("%I:%M%p", gmtime())
	nb_viewers = driver.find_element_by_class_name('tw-stat__value')
	viewers_string = nb_viewers.text
	tri = repr(nb_viewers.text)
	brut_text = re.split(r"\s", tri)
	streamer_Titre = driver.find_element_by_css_selector('h2')
	streamer_Title = streamer_Titre.get_attribute('innerHTML')
	streamer_jeu = driver.find_element_by_css_selector('p.tw-ellipsis:nth-child(2) > a:nth-child(1)')
	streamer_game = streamer_jeu.get_attribute('innerHTML')
	truestreamer_game = streamer_game.lower()
	realstreamergame = truestreamer_game.replace(" ", "_")
	print("Lien de la video : ")
	print("texte brut : ")
	print(brut_text)
	final_string = viewers_string.replace('\u202f', '')
	print("Nombre brut converti : ")
	print(final_string)
	print("Nombre de messages en 30 secondes qui a engendre la creation du clip :")
	print("nombre de messages enregistrer : ")
	print(num_pages_items)
	vrainumpage = float(num_pages_items)
	vrainbviewers = float(final_string)
	calcul = vrainumpage/vrainbviewers
	clip_time = time.time()
	return final_string, calcul, realstreamergame, vrainbviewers, current_time, streamer_Title, streamer_game, current_date, clip_time

def randomString(stringLength=10):
	"""Generate a random string of fixed length """
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(stringLength))

def createName():
	str_end = randomString(5)
	name1 = "test" + str_end + '.mp4'
	return name1

def csvwriter_clip(clip_time, num_page_items, breakpoint, coef, name1, streamer_name, final_string, current_time):
	with open("lestream.csv", "a", newline='\n') as fp:
		a = csv.writer(fp)
		row = [clip_time] + [num_page_items] + [breakpoint] + [breakpoint*coef] + [current_time] + [streamer_name] + [final_string] + [name1] + [calcul] 
		a.writerow(row)
		print("Enregistrement réussi des params du clip dans test.csv")

def stream_downloader(name1):
	stream_url = streamlink.streams(streamer_link)['best'].url
	print(stream_url)
	ffmpeg_process = Popen(["ffmpeg", "-i", stream_url, "-c", "copy", name1])
	time.sleep(30)
	ffmpeg_process.kill()

def stream_downloader_clip(name1):
	time.sleep(20)
	window_before = driver.window_handles[0]
	try:
		element_to_hover_over = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div[2]")
		hover = ActionChains(driver)
		hover.move_to_element(element_to_hover_over)
		clipbutton = driver.find_element_by_css_selector('.player-controls__right-control-group > div:nth-child(2) > button:nth-child(1)')
		hover.click(clipbutton)
		hover.perform()
		print("Successfully clicked on clip button")
	except:
		print("clip button not found")
	time.sleep(15)
	window_after = driver.window_handles[1]
	driver.switch_to_window(window_after)
	try:
		css = driver.find_element_by_css_selector('.highwind-video-player__container > video:nth-child(1)')
		poney = css.get_attribute('innerHTML')
		outer = css.get_attribute('outerHTML')
		oui = css.get_attribute('src')
	except:
		print('src video clip not found')
	try:
		print("Downloading starts...\n")
		urllib.request.urlretrieve(oui, name1)
		print("Download completed..!!")
	except Exception as e:
		print(e)
	driver.close()
	driver.switch_to_window(window_before)
	driver.refresh()
				
def uploadmongobands3(name1, streamer_Title, streamer_game, current_date, realtimestamp):
	s3 = boto3.client('s3')
	source = "source"
	date = "date"
	filename = name
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
	source: "https://s3.eu-west-3.amazonaws.com/compartiment-thimothe/" + name1 + ".mp4",
	date: datetime.datetime.utcnow(),
	nom: streamer_name,
	"title": streamer_Title,
	"game": streamer_game,
	"trimmed-game": realstreamergame,
	"date": current_date,
	"time": current_time,
	"timestamp": realtimestamp,
	"message": calcul,
	"deleted_date": datetime.datetime.utcnow()
	} 
	collection.insert_one(object)
	print("Successfully sent to MongoDB and AWS")
	os.remove(name1 + ".mp4")

def timestamp_register():
	try:
		cliplast_time = clip_time
	except:
		print("No clip was made yet")
	clip_time = time.time()
	timestampp = clip_time*1000
	timestamp = round(timestampp)
	realtimestamp = str(timestamp)
  
def csvwriter_noclip(clip_time, num_page_items, breakpoint, coef):
	current_time = strftime("%I:%M%p", gmtime())   
	with open("lestream" + ".csv", "a", newline='\n') as fp:
		a = csv.writer(fp)
		row = [clip_time] + [num_page_items] + [breakpoint] + [breakpoint*coef] + [current_time]
		a.writerow(row)
		print("Successfully written no clip stats in csv file")
	print("nombres de pages enregistrer a la fin du script : " + str(num_page_items))

def refresh_try():
	try:
		driver.refresh()
		time.sleep(5)
	except:
		print("refresh bug")

def endscript():
	driver.quit()
	print("script executed successfully")
