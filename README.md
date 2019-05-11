# Minerva-Video-Scraping-Tool

This is a tool that helps student using Minerva ALF to automate the process of downloading course videos. <br><br><br>

## How to use this tool

#### First, a few prerequisites:

- Python installed, with necessary packages (selenium, time, urllib)
- Chrome webdriver installed (Installation Guide: https://sites.google.com/a/chromium.org/chromedriver/)
- Login credentials to Minerva ALF prepared (by email and password, not Google Account)

#### Understanding the purpose of functions in the code

` login(email,password)`

This is a necessary login step that will be placed at the beginning of the sequence of functions you will run to download the videos. The inputs are strings which are your Minerva ALF login email and password.

`fetch_lectures(coursetitle,sectiontitle,old)`

This is the function that will copy the lecture titles and the associated link to the assessment page (where the video will be found). The input are two strings and one boolean. The first is the course title (e.g. AH51), the second is the section title (e.g. McMinn, MW@10:30), and the boolean indicates whether the course is a current one or a past course (i.e. TRUE = past course, FALSE = current course)

**Caution: Follow the format of the course title and the section title strictly, any mismatch will result in failures in locating the course. (e.g. beware the difference between McMinn, MW@10:30 and McMinn, MW@10:30am)**

` download(address)`

This is the function that will run through all the assessment page and download the videos one by one. The input is a string which states the local folder you want to save the class videos. For example, 'Users/Andy/Class Video'

#### How to initiate download

1. Download the scrape.py file
2. Type the functions at the bottom of the code with necessary inputs so they can be runned.
3. Run the file.

Example of arranging the functions:

~~~~
minerva_login('abcdefg@connect.ust.hk', 'cj5ed4snfdjf63')
navigate_to_recent_courses('AH51 - McMinn, MW@10:30')
download('C:/Users/abcedfg/Class Video')
~~~~

**Remember the quotes for the strings!** <br><br>

## Troubleshoot

The most common errors you may encounter when running this code is **element cannot be found** and/or **element not clickable**. This means the auto broswer cannot find the element that is designated. The exact cause of these errors is not yet clear, but I would attributed it to the variable loading time of the element, especially since ALF is a pretty dynamic website. 

When you encounter this error, just continue to run the code starting from the video that is not yet downloaded in the destination folder. This can be achieved by editing the loop function in the download function. For example, if you already have 10 videos downloaded, change the function to the following:

` for i in range(10, totalclasscount)`<br><br>

## Possible improvement for this code (for developers)

1. Now downloading of the video files is done one by one achieved by *urllib.request.urlretrieve* function, which significantly increase the run time of the code. A more efficient downloading function will be more appropriate.
2. The code can add an alternative login method, by Google Account.

## My Inspiration

It is approaching the end of the semester studying Minerva courses at HKUST through the Active Learning Forum (ALF), I am wondering whether I should download all the course videos to keep them for reference and also for memory :). But one major deterrent was that downloading course videos from the ALF is quite a frustrating and tedious experience, mainly because:

- there are no direct download links for course videos on ALF
- the pages on ALF load very slowly, perhaps it is due to the location of the server (US)
- there are many videos, around 26 per course per semseter, so in total I have accumulated around 156 videos to download

So I find it a real hassle to download all the videos and clicking through them one by one. I want to try to use programming skills to create a tool that would help me automate the process. 
