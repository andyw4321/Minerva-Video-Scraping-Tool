from selenium import webdriver
import time
import urllib.request


driver = webdriver.Chrome("C:/webdriver/chromedriver.exe")
driver.implicitly_wait(10)

def minerva_login(email,password):
	driver.get('https://seminar.minerva.kgi.edu/?password=1')
	driver.find_element_by_id("js-email").send_keys(email)
	driver.find_element_by_id("js-password").send_keys(password)
	driver.find_element_by_id("sign-in").click()


def navigate_to_recent_courses(coursexapth_dash):
	driver.find_element_by_xpath(coursexapth_dash).click()
	time.sleep(5)
	driver.find_element_by_class_name('show-more-or-less').click()
	time.sleep(1)
	pastclassbox = driver.find_element_by_class_name("past-classes-region")
	classtitles = pastclassbox.find_elements_by_class_name("title")
	classcount = len(classtitles)
	global titlelist
	global linklist
	titlelist = []
	linklist = []
	for i in range(classcount):
		titlelist.append(classtitles[i].text)
		linklist.append(classtitles[i].get_attribute('href'))
	for k in range(2):
		driver.find_element_by_class_name('next-page').click()
		time.sleep(2)
		pastclassbox = driver.find_element_by_class_name("past-classes-region")
		classtitles = pastclassbox.find_elements_by_class_name("title")
		classcount = len(classtitles)
		for i in range(classcount):
			titlelist.append(classtitles[i].text)
			linklist.append(classtitles[i].get_attribute('href'))
	#reverse sequence of the course titles and the associated links
	titlelist.reverse()
	linklist.reverse()
	#clean up the class titles to remove invalid characters for file names
	for i in range(len(titlelist)):
		titlelist[i] = titlelist[i].replace(':','')
	for i in range(len(titlelist)):
		titlelist[i] = titlelist[i].replace('?','')

def navigate_to_past_courses(coursexpath_list):
	time.sleep(3)
	driver.find_element_by_xpath('//*[@id="minerva-dashboard"]/div[1]/div/div/div/div[2]/aside/nav/ul/li[7]/section/div/ul/li[5]/a').click()
	time.sleep(3)
	driver.find_element_by_xpath(coursexapth_list).click()
	time.sleep(5)
	driver.find_element_by_class_name('show-more-or-less').click()
	time.sleep(1)
	pastclassbox = driver.find_element_by_class_name("past-classes-region")
	classtitles = pastclassbox.find_elements_by_class_name("title")
	classcount = len(classtitles)
	global titlelist
	global linklist
	titlelist = []
	linklist = []
	for i in range(classcount):
		titlelist.append(classtitles[i].text)
		linklist.append(classtitles[i].get_attribute('href'))
	for k in range(2):
		time.sleep(3)
		driver.find_element_by_class_name('next-page').click()
		time.sleep(2)
		pastclassbox = driver.find_element_by_class_name("past-classes-region")
		classtitles = pastclassbox.find_elements_by_class_name("title")
		classcount = len(classtitles)
		for i in range(classcount):
			titlelist.append(classtitles[i].text)
			linklist.append(classtitles[i].get_attribute('href'))
	#reverse sequence of the course titles and the associated links
	titlelist.reverse()
	linklist.reverse()
	#clean up the class titles to remove invalid characters for file names
	for i in range(len(titlelist)):
		titlelist[i] = titlelist[i].replace(':','')
	for i in range(len(titlelist)):
		titlelist[i] = titlelist[i].replace('?','')



def download(address):
	totalclasscount = len(titlelist)
	vlinklist = []
	for i in range(totalclasscount):
		driver.get(linklist[i])
		time.sleep(10)
		driver.find_element_by_class_name('action-button').click()
		time.sleep(10)
		vlink = driver.find_element_by_xpath('//*[@id="vjs_video_3_html5_api"]/source')
		vlinklist.append(vlink.get_attribute('src'))
		saveaddress = address + "{}.mp4".format(titlelist[i])
		urllib.request.urlretrieve(vlink.get_attribute('src'), saveaddress)
