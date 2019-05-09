from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import pw
import urllib.request


driver = webdriver.Chrome("C:/webdriver/chromedriver.exe")
driver.implicitly_wait(10)

def minerva_login():
	driver.get('https://seminar.minerva.kgi.edu/?password=1')
	driver.find_element_by_id("js-email").send_keys("hawang@connect.ust.hk")
	driver.find_element_by_id("js-password").send_keys(pw.password)
	driver.find_element_by_id("sign-in").click()

def navigate_to_assessment_page():
	driver.implicitly_wait(20)
	driver.find_element_by_xpath('//*[@id="minerva-dashboard"]/div[1]/div/div/div/div[2]/aside/nav/ul/li[3]/a/span[2]').click()
	time.sleep(2)
	boxes = driver.find_elements_by_class_name('assessment-item-view')
	boxesnumber = len(boxes)
	titles = []
	links = []
	for i in range(boxesnumber):
		titles.append(boxes[i].find_elements_by_class_name('section-link'))
		links.append(boxes[i].find_elements_by_class_name('action-link'))
	titlesnumber = len(titles)
	linksnumber = len(links)
	print('Titles Correspond to Links?',titlesnumber == linksnumber)
	for i in range(titlesnumber):
		print(titles[i][0].text)
	for i in range(linksnumber):
		if links[i] == []:
			print('Not Available')
		else:
			print(links[i][0].get_attribute('href'))

		

	'''classtitle = driver.find_elements_by_class_name('section-link')
	assessmentlink = driver.find_elements_by_link_text(('Review Grades','Assess Recordings'))
	print(type(assessmentlink))
	titlenumbers = len(classtitle)
	linknumbers = len(assessmentlink)
	if titlenumbers == linknumbers:
		print('Mathching Title and Link Number')
	else:
		print('Mismatch Error')
	for i in range(titlenumbers):
		print(classtitle[i].text)
	for i in range(linknumbers):
		print(assessmentlink[i].get_attribute('href'))'''

#only works for recent courses
def navigate_to_course_page():
	driver.find_element_by_xpath('//*[@id="minerva-dashboard"]/div[1]/div/div/div/div[2]/aside/nav/ul/li[7]/section/div/ul/li[4]/a').click()
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
	titlelist.reverse()
	linklist.reverse()
	for i in range(len(titlelist)):
		titlelist[i] = titlelist[i].replace(':','')
	for i in range(len(titlelist)):
		titlelist[i] = titlelist[i].replace('?','')

def navigate_to_past_courses():
	time.sleep(3)
	driver.find_element_by_xpath('//*[@id="minerva-dashboard"]/div[1]/div/div/div/div[2]/aside/nav/ul/li[7]/section/div/ul/li[5]/a').click()
	time.sleep(3)
	driver.find_element_by_xpath('//*[@id="main-semantic-content"]/div/div/section/div/div/table/tbody/tr[3]/td[3]/a').click()
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
	titlelist.reverse()
	linklist.reverse()
	for i in range(len(titlelist)):
		titlelist[i] = titlelist[i].replace(':','')
	for i in range(len(titlelist)):
		titlelist[i] = titlelist[i].replace('?','')



def get_assessment_link():
	totalclasscount = len(titlelist)
	vlinklist = []
	for i in range(totalclasscount):
		driver.get(linklist[i])
		time.sleep(10)
		driver.find_element_by_class_name('action-button').click()
		time.sleep(10)
		vlink = driver.find_element_by_xpath('//*[@id="vjs_video_3_html5_api"]/source')
		vlinklist.append(vlink.get_attribute('src'))
		saveaddress = "/Users/User/Class Videos/{}.mp4".format(titlelist[i])
		urllib.request.urlretrieve(vlink.get_attribute('src'), saveaddress)  
	

def get_assessment_link_cont():
	totalclasscount = len(titlelist)
	vlinklist = []
	for i in range(22,totalclasscount):
		driver.get(linklist[i])
		time.sleep(10)
		driver.find_element_by_class_name('action-button').click()
		time.sleep(10)
		vlink = driver.find_element_by_xpath('//*[@id="vjs_video_3_html5_api"]/source')
		vlinklist.append(vlink.get_attribute('src'))
		saveaddress = "/Users/User/Class Videos/{}.mp4".format(titlelist[i])
		urllib.request.urlretrieve(vlink.get_attribute('src'), saveaddress)  



minerva_login()
navigate_to_past_courses()
get_assessment_link_cont()




