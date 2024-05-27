#pip install numpy
#pip install pyglet
#pip install python-vlc
#pip install pyaudio
#pip install opencv-python
#pip install pyautogui
#pip install mediapipe
#pip install pyttsx3
#pip install python-pptx
#pip install flask-mysqldb
#pip install wikipedia
#pip install psutil

import cv2
from cv2 import MARKER_TRIANGLE_UP
from pynotifier import Notification
from tkinter import *
import tkinter as Tk
import speech_recognition as sr
import sys
import os
import pyautogui
import pyautogui as spam
import datetime
import pyaudio
import pyttsx3
import webbrowser
import subprocess
from tkinter import *
import time
#import vlc
import numpy as np 
import datetime
import psutil
import wikipedia



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) #[0]-DAVID ,print(voices[1].id)-ZIRA

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Lisning...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Waiting for few Moments")
        query = r.recognize_google(audio,language='en-in')
        print("user said", query)
    except Exception as e:
        print(e)
        speak("Sorry")
        return query 
        print("")
    while True:
        query = takecommand().lower()
        if 'hay siri' in query:
            speak("I am Lisning")
        elif "wikipedia" in query:
            speak("Searching in Wikipedia")
            query-query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to the wikipedia")
            print(results)
            speak(results)
            #Opening website
        elif 'open Youtube' in query:
            webbrowser.open("Youtube.com")
            #play music files
        elif 'play music' in query:
            musicdir="C:\\Users\\MARTIN\\Music\\ADI"
            songs=os.listdir(musicdir)
            print(songs)
            os.startfile(os.path.join(musicdir,songs[16]))
            #opening apps
        elif 'open code' in query:
            codepath="C:\\Users\\MARTIN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'open Chrome' in query:
            codepath1="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codepath1)
        elif 'the time' in query:
            time=datetime.datetime.now().strtime("%H,%M")
            speak(time)
        elif 'quit' in query:
            speak("Quitting sir")
            break
        elif 'exit' in query:
            exit()
        #System command
        #shutdown command
        #use or dolly shutdown in query

        elif 'shutdown' in query:
            speak("okey")
            os.system("shutdown /s /t 06")
            speak('I am going to shutdown the computer sir')
            speak('bye sir, have a good day')
            sys.exit()
        #restart command
        elif 'restart' in query: 
            speak("okey")
            os.system("restart /r /t 06")
            speak('I am going to restart the computer sir')
            speak('bye sir, have a good day')
            sys.exit()
        #log off command
        elif 'log off pc' in query:
            speak("okey")
            os.system("Logoff /l /t 06")
            speak('I am going to logoff the computer sir')
            speak('bye sir, have a good day')
            sys.exit()
        elif 'clear console' in query:
            os.system('cls')
            speak('current console clear sir')
        elif 'battery persantage' in query:
            battery = psutil.sensors_battery()
            percent = battery.percent
            speak('the battery percentage is '+str(percent))
        #mouse command
        elif 'scroll up' in query:
            pyautogui.scroll(200)
            speak('Done')
        elif 'scroll down' in query:
            pyautogui.scroll(-200)
            speak('Done')
        elif 'type' in query:
            newt = query.replace('type ','')
            pyautogui.moveRel(0, -100, duration=0.25)
            speak('Done!')
        elif 'mouse position' in query:
            speak(pyautogui.position())
        elif 'navigative up' in query:
            pyautogui.moverel(0, -100, duration=0.25)
            speak('done!')
        elif 'navigative down' in query:
            pyautogui.moverel(0, 100, during=0.25)
            speak('done!')
        elif 'navigative right' in query:
            pyautogui.moverel(100, 0, during=0.25)
            speak('done!')
        elif 'navigative light' in query:
            pyautogui.moverel(100, 0, during=0.25)
            speak('done!')
        elif 'navigative left' in query:
            pyautogui.moverel(-100, 0, during=0.25)
            speak('done!')
        elif 'left click' in query:
            pyautogui.click(button='left')
            speak('done!')
        elif 'right click' in query:
            pyautogui.click(button='right')
            speak('done!')
        elif 'double click' in query:
            pyautogui.click()
            pyautogui.click()
            speak('done!')
        elif 'open explorer' in query:
            os.startfile('explorer.exe')
            speak('what do wanna see there?')
            
        elif 'open document' in query:
            codepath3 = "C:\\Users\\MARTIN\\Documents"
            os.startfile(codepath3)
        elif 'open downloads' in query:
            codepath4 = "C:\\Users\\MARTIN\\Downloads"
            os.startfile(codepath4)
        elif 'open music' in query:
            codepath5 = "C:\\Users\\MARTIN\\Music"
            os.startfile(codepath5)
        elif 'open Pictures' in query:
            codepath6 = "C:\\Users\\MARTIN\\pictures"
            os.startfile(codepath6)
        elif 'open videos' in query:
            codepath7 = "C:\\Users\\MARTIN\\Videos"
            os.startfile(codepath7)
        elif 'open windows' in query:
            codepath8 = "C:"
            os.startfile(codepath8)
        elif 'open New volume e' in query:
            codepath9 = "E:"
            os.startfile(codepath9)
        elif 'open new volume f' in query:
            codepath10 = "F:"
            os.startfile(codepath10)

        elif 'open youtube' in query or 'youtube' in query or'opening youtube' in query:
            webbrowser.open("Youtube.com")
            print("A.I : Opening Youtube")
            speak("yes sir, Open youtube")
            print("")
            
        elif 'searching youtube' in query or 'youtube search' in query or 'search youtube' in query:
            while True:
                print("")
                speak("Searching command")
                search = input("Youtube : ")
                webbrowser.open("https://www.youtube.com/results?search_query="+search)
                print("A.I : Opening Youtube")
                print("")
                cl=int(input("Click 1 to continue : "))
                if  cl==1:
                    continue
                else:
                    print("Close Youtube") 
                    speak("Closing Youtube")
                    print("")
                    break  

        elif  'open google' in query or 'google'  in query  or'opening google'  in query :
            webbrowser.open("google.com")
            print("A.I : Opening Google")
            speak("yes sir, opeing Google")
            print("")
            User()

        elif 'searching google' in query or'google search'  in query or'search google' in query :
            while True:
                print("")
                speak("Searching command")
                search = input("Google : ")
                webbrowser.open("https://www.google.com/search?q="+search)
                print("A.I : Opening Google")
                print("")
                cl=int(input("Click 1 to continue : "))
                if  cl==1:
                    continue
                else:
                    print("Close Google") 
                    speak("Closing Google")
                    print("")
                    break

        elif 'open instagram'  in query or 'instagram'  in query or'opening instagram'  in query :
            webbrowser.open("instagram.com")
            print("A.I : Opening Instagram")
            speak("yes sir, opeing instagram")
            print("")
            User()
        
        elif'open facebook'  in query or'facebook'  in query or'opeining facebook'  in query :
            webbrowser.open("facebook.com")
            print("A.I : Opening Facebook")
            speak("yes sir, opeing facebook")
            print("")
            User()
        
        elif  'open flipcard' in query or  'flipcard' in query or  'open flipcard online shoping' in query:
            webbrowser.open("flipcart online shoping")
            print("A.I : Opening Flipcard")
            speak("yes sir, opeing flipcard online shoping")
            print("")
            User()

        elif  'searching flipcard' in query or  'flipcard search' in query or  'search flipcard' in query:
            while True:
                print("")
                speak("Searching command")
                search = input("Flipkard : ")
                webbrowser.open("https://www.flipkart.com/search?q="+search)
                print("A.I : Opening Flipcard")
                print("")
                cl=int(input("Click 1 to continue : "))
                if  cl==1:
                    continue
                else:
                    print("Close Flipkart") 
                    speak("Closing Flipkart")
                    print("")
                    break
            

        elif  'open amazon' in query or  'amazon' in query or  'amazon online shoping' in query:
            webbrowser.open("amazon.com")
            print("A.I : Opening Amazon")
            speak("yes sir, opening amazon online shoping ")
            print("")
            User()

        elif  'searching amazon' in query or  'amazon search' in query or  'search amazon' in query:
            while True:
                print("")
                speak("Searching command")
                search = input("Amazon : ")
                webbrowser.open("https://www.amazon.com/s?k="+search)
                print("A.I : Opening Amazon")
                print("")
                cl=int(input("Click 1 to continue : "))
                if  cl==1:
                    continue
                else:
                    print("Close Amazon") 
                    speak("Closing Amazon")
                    print("")
                    break
            

        elif  'open meesho' in query or  'meesho' in query or  'meesho online shoping' in query:
            webbrowser.open("meesho.com")
            print("A.I : Opening Meesho")
            speak("yes sir, opening meesho online shoping sir")
            print("")
            User()

        elif  'searching meesho' in query or  'meesho search' in query or  'search meesho' in query:
            while True:
                print("")
                speak("Searching command")
                search = input("Meesho : ")
                webbrowser.open("https://meesho.com/search?q="+search)
                print("A.I : Opening Meesho")
                print("")
                cl=int(input("Click 1 to continue : "))
                if  cl==1:
                    continue
                else:
                    print("Close Meesho") 
                    speak("Closing Meesho")
                    print("")
                    break
            

        elif  'open wikipedia' in query or  'wikipedia' in query or  'opening wikipedia' in query:
            webbrowser.open("wikipedia.org")
            print("A.I : Opening Wikipedia")
            speak("yes sir, opeing wikipedia")
            print("")
            User()

        elif  'searching wikipedia' in query or  'wikipedia search' in query or  'search wikipedia' in query:
            while True:
                print("")
                speak("Searching command")
                search = input("Wikipedia : ")
                webbrowser.open("https://en.m.wikipedia.org/wiki/"+search)
                print("A.I : Opening Wikipedia")
                print("")
                cl=int(input("Click 1 to continue : "))
                if  cl==1:
                    continue
                else:
                    print("Close Wikipedia") 
                    speak("Closing Wikipedia")
                    print("")
                    break
            

        elif  'download driverpack' in query or  'download driverpack solution' in query or  'driverpack' in query or  'download driverpacksolution' in query:
            webbrowser.open("Download driverpack solution")
            print("A.I : Searching Driverpack File")
            speak("yes sir, searching to google")
            print("")
            User()

        elif  'download windows 10' in query or  'download windows10' in query or  'download windows' in query or  'windows 10' in query or  'windows10' in query:
            webbrowser.open("https://www.microsoft.com/en-in/software-download/windows10")
            print("A.I : Searching Windows10 File")
            speak("yes sir, searching to google")
            print("")
            User()

        elif  'download windows 11' in query or  'download windows11' in query or  'windows 11' in query or  'windows11' in query:
            webbrowser.open("https://www.microsoft.com/software-download/windows11")
            print("A.I : Searching Windows11 File")
            speak("yes sir, searching to google")
            print("")
            User()

        
        elif  'searching annauniversity' in query or  'annauniversity search' in query or  'search annauniversity' in query or  'notes download' in query:
            while True:
                print("")
                search = input("Notes name : ")
                speak("Searching command")
                webbrowser.open("https://annauniversityedu.blogspot.com/search?q="+search)
                print("A.I : Opening Annauniversity official page")
                speak("yes sir, Open Annauniversity official page to search"+ search)
                print("")
                if  cl==1:
                    continue
                else:
                    print("Close Annauniversity website") 
                    speak("Closing Annauniversity website")
                    print("")
                    break
            

            "https://portal.naanmudhalvan.tn.gov.in/students/dashboard"

        elif  'nanmuthalvan' in query or  'Nan Muthalvan' in query or  'NanMuthalvan' in query or  'nm' in query:
            print("")
            webbrowser.open("https://portal.naanmudhalvan.tn.gov.in/students/dashboard")
            print("A.I : Opening nanmuthalvan official page")
            speak("yes sir, Open nanmuthalvan official page ")
            print("")
            User()

        elif  'blackarch' in query or  'BlackArch' in query or  'BlackArch' in query or  'download black arch' in query:
            print("")
            webbrowser.open("https://blackarch.org/downloads.html")
            print("A.I : Opening BlacArch official page")
            speak("yes sir, Open BlacArch official page ")
            print("")
            User()

        elif  'ticket booking' in query or  'booking ticket' in query:
            while True:
                speak("There are three booking options are available")
                print("""
                1.Cinema Tickets
                2.Bus Tickets
                3.Flight, Train & Others""")
                tk=int(input("Enter your choice : "))
                if tk==1:
                    speak("Selected Cinema Tickets Booking")
                    webbrowser.open("https://in.bookmyshow.com/explore/home/chennai")
                    print("")
                elif tk==2:
                    speak("Selected Bus tickets booking")
                    webbrowser.open("https://www.redbus.in/")
                    print("")
                elif tk==3:
                    speak("Flight, Train & Others tickets booking")
                    webbrowser.open("https://www.booking.com/index.en.html?aid=309654;label=hotels-english-en-india-I_3LMGkHqWe_vfh30GlaEQS433577572936:pl:ta:p1:p2:ac:ap:neg:fi:tikwd-101352960:lp9061971:li:dec:dm:ppccp=UmFuZG9tSVYkc2RlIyh9YcsZ-Id2vkzIfTmYhvC5HOg;ws=&gclid=EAIaIQobChMIhuT_yvPq_QIVLZpmAh2rkwwNEAAYASAAEgISw_D_BwE")
                    print("")
                    cl=int(input("Click 1 to continue : "))
                    if  cl==1:
                        continue
                    else:
                        print("Close Youtube") 
                        speak("Closing Youtube")
                        print("")
                        break
                

        
        #////////////////////////////////////
        #\\\\\\opening apps\\\\\\\\\\\\\\\\\
        #////////////////////////////////////

        elif 'open vscode' in query or  'opening vscode' in query or  'vscode' in query or  'vs code' in query:
            codepath="C:\\Users\\MARTIN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            print("A.I : Opening Visual studio code")
            speak("yes sir, opeing Visual studio code")
            print("")
            User()

        elif  'open chrome' in query or  'chrome' in query or  'opening chrome' in query:
            codepath1="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codepath1)
            print("A.I : Opening chrome")
            speak("yes sir, opeing chrome browser")
            print("")
            User()

        #/////////////////////////////////////////////////
        #\\\\\\\\\\\\Sample programming\\\\\\\\\\\\\\\\\\\
        #/////////////////////////////////////////////////
    

        elif 'sample program for gcd of two numbers' in query or 'gcd of two numbers' in query:
            print("""
            Program:
            n1=int(input("Enter the no.1:"))
            n2=int(input("Enter the no.2:"))
            rem=n1%n2
            while rem!=0:
            n1=n2
            n2=rem
            rem=n1%n2
            print("The GCD of given number is: ",n2)
            """)
            print("")
            User()
        elif 'sample program for square root numbers' in query or 'square root numbers' in query:
            print("""
            Program:
            n=float(input("Square root: "))
            x=float(input("Estimate: "))
            final=(0.5*(x+(n/x)))
            print(final)
            for i in range(0,10):
            final=(0.5*(final+(n/final)))
            print(“The square root is: ”,final)
            """)
            print("")
            User()
        elif 'sample program for exponential of numbers' in query or 'exponential of numbers' in query:
            print("""
            Program:
            def power(base,exp):
            if(exp==1):
            return(base)
            if(exp!=1):
            return(base*power(base,exp-1))
            base=int(input("Enter base: "))
            exp=int(input("Enter exponential value: "))
            print("Result:",power(base,exp))""")
            print("")
            User()

        

        #/////////////////////////////////////////////////////
        #\\\\\\\\\\\\\\\\\\\music/////////////////////////////
        #/////////////////////////////////////////////////////
        
        elif  'play music' in query or 'music' in query:
            s=int(input("Enter No : "))
            musicdir="C:\\Users\\MARTIN\\Videos\\Captures"
            songs=os.listdir(musicdir)
            print(songs)
            os.startfile(os.path.join(musicdir,songs[1]))
            print("")
            User()
        elif 'play' in query:
            s=int(input("Enter No : "))
            musicdir="C:\\Users\\MARTIN\\Videos\\Captures"
            songs=os.listdir(musicdir)
            print(songs)
            os.startfile(os.path.join(musicdir,songs[s]))
            print("")
            User()
        
        elif "chatbot" in query:
            User()

        elif 'face detector' in query:
            fd()
            print("")
            User()
        else:
            print("A.I : I can do you understand")
            speak("I can do you understand")
            print("")
            User()          
                
        cl=int(input("Click 1 to continue : "))
        if  cl==1:
            continue
        else:
            print("Close Google") 
            speak("Closing Google")
            print("")
            break
            User()
    
    
        

def fd():
    trainedDataset=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    #Read image
    im=input("")
    img = cv2.imread('BM.jpeg')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = trainedDataset.detectMultiScale(gray)
    print(faces)
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('elon',img)
    cv2.waitKey()


def main():
    print("""
 ___  _____  ___      ____         _____  _____  
|   \ |     |   \    |    | |    | |      |      |\   |
|__ / |____ |    \   |    | |    | |____  |____  | \  |
|  \  |     |    /   |    | |    | |      |      |  \ |
|   \ |____ |___/    |____| |____| |____  |____  |   \|
                          \                            """)
    print("")
    print("Developers : Martin & Bala")
    print("Version - 1.0")
    speak("Hi sir, i am red queen")
    print("")

def rq():
    print("""
 ___  _____  ___      ____         _____  _____  
|   \ |     |   \    |    | |    | |      |      |\   |
|__ / |____ |    \   |    | |    | |____  |____  | \  |
|  \  |     |    /   |    | |    | |      |      |  \ |
|   \ |____ |___/    |____| |____| |____  |____  |   \|
                          \                            """)
    print("")
    print("Developers : Martin & Bala")
    print("Version - 1.0")
    print("")

def timedate():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning Sir")
    elif hour >=12 and hour<18:
        speak("Good afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("how can i help you")

def admin():
    speak("Enter your Admin ID ")
    ad = input("Admin ID : ")
    speak("Enter your admin password")
    ps = int(input("Password : "))
    if ad=='Martin' and ps==4124182111 or ad=='Bala' and ps==7216:
        print("ACCESS GRANTED")
        speak("ACCESS GRANTED")
        print("")
        os.system('cls')
        while True:
                rq()
                timedate()
                print("")
                User()
                
    else:
        print("Invalid user")
        speak("ACCESS DENIED")
        speak("please Try again")
        print("")
        admin()

def User():
    while True:
        user = input("User : ")
        user.lower()
        #/////////////////////////////////
        #\\\\\\\\\normal commands\\\\\\\\\
        #/////////////////////////////////
        if user == 'version':
            speak ("Name  RED QUEEN")
            print("A.I : Name     : RED QUEEN")
            speak("Developers  maarten Bala")
            print("Developers   : MARTIN & Bala")
            speak ("Version 1.0")
            print("Version  : 1.0")
            speak ("FileType  exe")
            print("Type     : exe") 
            speak ("Develope Date  18/03/2023")
            print("Develope Date  : 18/03/2023")
            print("")
            User()

        elif user=='voice assistant' or user=='voice mode':
            takecommand()
            query = takecommand().lower()
            print("")
            User()              
        elif user == 'hi':
            print("A.I : Hi sir")
            speak("hi sir")
            print("")
            User()
        elif user == "hay siri":
            print("A.I : I am lisning")
            speak("I am lisning")
            print("")
            User()
        elif user == 'thanks' or user == 'Thanks' or user == 'thank you' or user == 'Thank You':
            print("User : ",user)
            speak("Its ok Sir")
            print("")
            User()
        elif user == "what is your name":
            print("A.I : RED QUEEN")
            speak("My name is RED QUEEN")
            print("")
            User()
        elif user == "whats my name":
            print("A.I : S.Martin R.Bala")
            speak("S .   Maartin               R       .Bala")
            print("")
            User()
        elif user == "whats the time today" or user == "time today" or user == "time" or user == "today time " or user == "whats time":
            time=datetime.datetime.now()
            print("A.I : ",time)
            speak(time)
            print("")
            User()
        elif user == "love you" or user == "i love you":
            print("A.I :Love you too sir")
            speak(" Love you too sir")
            print("")
            User()
        elif user == 'hey':
            print("Hello sir")
            speak("Hello sir")
            print("")
            User()
        
        elif user=='logout':
            print("Goodbye Sir")
            speak("Goodbye sir")
            quit()

        elif user=='send message':
            limit = input("Enter the no of message : ")
            msg = input("Enter your message : ")
            i=0
            time.sleep(5)
            while i<int(limit):
                spam.typewrite(msg)
                spam.press('Enter')
            i==limit
            quit 
        
        #/////////////////////////////////////////////
        #\\\\\\\\Windows explorer commands\\\\\\\\\\\\
        #/////////////////////////////////////////////
        elif user == "open documents" or user == "documents":
            codepath = "C:\\Users\\MARTIN\\Documents"
            os.startfile(codepath)
            print("A.I : Opening Documents")
            speak("Opening Documents")
            print("")
            User()
        elif user == "open downloads" or user == "downloads" or user == "open videosongs" or user == "open video songs":
            codepath = "C:\\Users\\MARTIN\\Downloads"
            os.startfile(codepath)
            print("A.I : Opening Downloads")
            speak("Opening Downloads")
            print("")
            User()
        elif user == "open music" or user == "music" or user == "songs" or user == "open songs":
            codepath = "C:\\Users\\MARTIN\\Music"
            os.startfile(codepath)
            print("A.I : Opening Music")
            speak("Opening Music")
            print("")
            User()
        elif user == "open pictures" or user == "pictures" or user == "open images":
            codepath = "C:\\Users\\MARTIN\\Pictures"
            os.startfile(codepath)
            print("A.I : Opening pictures")
            speak("Opening pictures")
            print("")
            User()
        elif user == "open windows" or user == "open c" or user == "open c volume" or user == "c" :
            codepath2 = "C:"
            os.startfile(codepath2)
            print("A.I : Opening Windows")
            speak("Opening Windows")
            print("")
            User()
        elif user == "open new volume e" or user == "open e" or user == "open e volume" or user == "e" :
            codepath3 = "E:"
            os.startfile(codepath3)
            print("A.I : Opening volume E")
            speak("Opening volume E")
            print("")
            User()
        elif user == "open new volume e" or user == "open f" or user == "open f volume" or user == "f":
            codepath4 = "F:"
            os.startfile(codepath4)
            print("A.I : Opening volume F")
            speak("Opening volume F")
            print("")
            User()
        
        elif user == 'exit':
            exit()
        #/////////////////////////////////////////////
        #\\\\\\\\\Shotdown, restart, log off\\\\\\\\\\
        #/////////////////////////////////////////////
        elif user == 'shutdown':
            print("A.I : shutdown processing")
            speak("yes sir")
            speak('I am going to shutdown the computer sir')
            speak('bye sir, have a good day')
            os.system("shutdown /s /t 06")
            print("")
            User()
           
        #restart command
        elif user == 'restart':
            print("A.I : Restart processing")
            speak("okey")
            speak('I am going to restart the computer sir')
            speak('bye sir, have a good day')
            os.system("restart /r /t 06")
            print("")
            User() 
        #log off command
        elif user == 'log off pc' or user == 'log off':
            print("A.I : log off processing")
            speak("okey")
            speak('I am going to logoff the computer sir')
            speak('bye sir, have a good day')
            os.system("Logoff /l /t 06")
            print("")
            User() 
        elif user == 'clear console' or user == 'clear' or user == 'cls':
            os.system('cls')
            print("A.I : current console clear sir")
            speak('current console clear sir')
            print("")
            User() 
        elif user == 'battery percantage':
            battery = psutil.sensors_battery()
            percent = battery.percent
            print("A.I : The battery percentage is : "+str(percent))
            speak('the battery percentage is '+str(percent))
            print("")
            User() 
        #mouse command
        elif user == 'scroll up':
            pyautogui.scroll(200)
            print("A.I : Scroll up")
            speak('Done!')
            print("")
            User() 
        elif user == 'scroll down':
            pyautogui.scroll(-200)
            print("A.I : Scroll down")
            speak('Done')
            print("")
            User() 
        elif user == 'type':
            speak("Type your command")
            para=[]
            print("Type your command : ")
            while True:
                line=input()
                if line:
                    para.append(line)
                else:
                    break
                
            print("")
            User()
            
        elif user == 'mouse position':
            speak(pyautogui.position())
            print("A.I : Mouse position")
            print("")
            User()
        elif user == 'navigative up':
            pyautogui.moverel(0, -100, duration=0.25)
            print("A.I : Navigative up")
            speak('done!')
            print("")
            User()
        elif user == 'navigative down':
            pyautogui.moverel(0, 100, during=0.25)
            print("A.I : Navigative down")
            speak('done!')
            print("")
            User()
        elif user =='navigative right':
            pyautogui.moverel(100, 0, during=0.25)
            print("A.I : Navigative right")
            speak('done!')
            print("")
            User()
        elif user == 'navigative light':
            pyautogui.moverel(100, 0, during=0.25)
            print("A.I : Navigative light")
            speak('done!')
            print("")
            User()
        elif user == 'navigative left':
            pyautogui.moverel(-100, 0, during=0.25)
            print("A.I : Navigative left")
            speak('done!')
            print("")
            User()
        elif user == 'left click':
            pyautogui.click(button='left')
            print("A.I : Left click")
            speak('done!')
            print("")
            User()
        elif user == 'right click' or user =='rightclick':
            pyautogui.click(button='right')
            print("A.I : Right click")
            speak('done!')
            print("")
            User()
        elif user =='double click':
            pyautogui.click()
            pyautogui.click()
            print("A.I : Double click")
            speak('done!')
            print("")
            User()

        
        #///////////////////////////////////////////
        #\\\\\\\\\\website\\\\\\\\\\\\\\\\\\\\\\\\
        #//////////////////////////////////////////
        #https://www.youtube.com/results?search_query=   youtube search
        #https://www.youtube.com/watch?v=                play youtube videos
        #https://www.google.com/search?q=                google search
        #https://meesho.com/search?q=                    meesho search
        #https://www.flipkart.com/search?q=              flipcard search
        #https://www.amazon.com/s?k=                     amazon serach
        elif user =='open youtube' or user == 'youtube' or user == 'opening youtube':
            webbrowser.open("Youtube.com")
            print("A.I : Opening Youtube")
            speak("yes sir, Open youtube")
            print("")
            User()

        elif user == 'searching youtube' or user == 'youtube search' or user == 'search youtube':
            while True:
                print("")
                speak("Searching command")
                search = input("Youtube : ")
                webbrowser.open("https://www.youtube.com/results?search_query="+search)
                print("A.I : Opening Youtube")
                print("")
                cl=int(input("Click 1 to continue : "))
                if  cl==1:
                    continue
                else:
                    print("Close Youtube") 
                    speak("Closing Youtube")
                    print("")
                    break
                
                              
            
        elif user == 'open google' or user == 'google' or user == 'opening google':
            webbrowser.open("google.com")
            print("A.I : Opening Google")
            speak("yes sir, opeing Google")
            print("")
            User()

        elif user == 'searching google' or user == 'google search' or user == 'search google':
            while True:
                print("")
                speak("Searching command")
                search = input("Google : ")
                webbrowser.open("https://www.google.com/search?q="+search)
                print("A.I : Opening Google")
                print("")
                cl=int(input("Click 1 to continue : "))
                if  cl==1:
                    continue
                else:
                    print("Close Google") 
                    speak("Closing Google")
                    print("")
                    break

        elif user == 'open instagram' or user == 'instagram' or user == 'opening instagram':
            webbrowser.open("instagram.com")
            print("A.I : Opening Instagram")
            speak("yes sir, opeing instagram")
            print("")
            User()
        
        elif user == 'open facebook' or user == 'facebook' or user == 'opeining facebook':
            webbrowser.open("facebook.com")
            print("A.I : Opening Facebook")
            speak("yes sir, opeing facebook")
            print("")
            User()
        
        elif user == 'open flipcard' or user == 'flipcard' or user == 'open flipcard online shoping':
            webbrowser.open("flipcart online shoping")
            print("A.I : Opening Flipcard")
            speak("yes sir, opeing flipcard online shoping")
            print("")
            User()

        elif user == 'searching flipcard' or user == 'flipcard search' or user == 'search flipcard':
            while True:
                print("")
                speak("Searching command")
                search = input("Flipkard : ")
                webbrowser.open("https://www.flipkart.com/search?q="+search)
                print("A.I : Opening Flipcard")
                print("")
                cl=int(input("Click 1 to continue : "))
                if  cl==1:
                    continue
                else:
                    print("Close Flipkart") 
                    speak("Closing Flipkart")
                    print("")
                    break
            

        elif user == 'open amazon' or user == 'amazon' or user == 'amazon online shoping':
            webbrowser.open("amazon.com")
            print("A.I : Opening Amazon")
            speak("yes sir, opening amazon online shoping ")
            print("")
            User()

        elif user == 'searching amazon' or user == 'amazon search' or user == 'search amazon':
            while True:
                print("")
                speak("Searching command")
                search = input("Amazon : ")
                webbrowser.open("https://www.amazon.com/s?k="+search)
                print("A.I : Opening Amazon")
                print("")
                cl=int(input("Click 1 to continue : "))
                if  cl==1:
                    continue
                else:
                    print("Close Amazon") 
                    speak("Closing Amazon")
                    print("")
                    break
            

        elif user == 'open meesho' or user == 'meesho' or user == 'meesho online shoping':
            webbrowser.open("meesho.com")
            print("A.I : Opening Meesho")
            speak("yes sir, opening meesho online shoping sir")
            print("")
            User()

        elif user == 'searching meesho' or user == 'meesho search' or user == 'search meesho':
            while True:
                print("")
                speak("Searching command")
                search = input("Meesho : ")
                webbrowser.open("https://meesho.com/search?q="+search)
                print("A.I : Opening Meesho")
                print("")
                cl=int(input("Click 1 to continue : "))
                if  cl==1:
                    continue
                else:
                    print("Close Meesho") 
                    speak("Closing Meesho")
                    print("")
                    break
            

        elif user == 'open wikipedia' or user == 'wikipedia' or user == 'opening wikipedia':
            webbrowser.open("wikipedia.org")
            print("A.I : Opening Wikipedia")
            speak("yes sir, opeing wikipedia")
            print("")
            User()

        elif user == 'searching wikipedia' or user == 'wikipedia search' or user == 'search wikipedia':
            while True:
                print("")
                speak("Searching command")
                search = input("Wikipedia : ")
                webbrowser.open("https://en.m.wikipedia.org/wiki/"+search)
                print("A.I : Opening Wikipedia")
                print("")
                cl=int(input("Click 1 to continue : "))
                if  cl==1:
                    continue
                else:
                    print("Close Wikipedia") 
                    speak("Closing Wikipedia")
                    print("")
                    break
            

        elif user == 'download driverpack' or user == 'download driverpack solution' or user == 'driverpack' or user == 'download driverpacksolution':
            webbrowser.open("Download driverpack solution")
            print("A.I : Searching Driverpack File")
            speak("yes sir, searching to google")
            print("")
            User()

        elif user == 'download windows 10' or user == 'download windows10' or user == 'driverpack' or user == 'download windows' or user == 'windows 10' or user == 'windows10':
            webbrowser.open("https://www.microsoft.com/en-in/software-download/windows10")
            print("A.I : Searching Windows10 File")
            speak("yes sir, searching to google")
            print("")
            User()

        elif user == 'download windows 11' or user == 'download windows11' or user == 'windows 11' or user == 'windows11':
            webbrowser.open("https://www.microsoft.com/software-download/windows11")
            print("A.I : Searching Windows11 File")
            speak("yes sir, searching to google")
            print("")
            User()

        
        elif user == 'searching annauniversity' or user == 'annauniversity search' or user == 'search annauniversity' or user == 'notes download':
            while True:
                print("")
                search = input("Notes name : ")
                speak("Searching command")
                webbrowser.open("https://annauniversityedu.blogspot.com/search?q="+search)
                print("A.I : Opening Annauniversity official page")
                speak("yes sir, Open Annauniversity official page to search"+ search)
                print("")
                if  cl==1:
                    continue
                else:
                    print("Close Annauniversity website") 
                    speak("Closing Annauniversity website")
                    print("")
                    break
            

            "https://portal.naanmudhalvan.tn.gov.in/students/dashboard"

        elif user == 'nanmuthalvan' or user == 'Nan Muthalvan' or user == 'NanMuthalvan' or user == 'nm':
            print("")
            webbrowser.open("https://portal.naanmudhalvan.tn.gov.in/students/dashboard")
            print("A.I : Opening nanmuthalvan official page")
            speak("yes sir, Open nanmuthalvan official page ")
            print("")
            User()

        elif user == 'blackarch' or user == 'BlackArch' or user == 'BlackArch' or user == 'download black arch':
            print("")
            webbrowser.open("https://blackarch.org/downloads.html")
            print("A.I : Opening BlacArch official page")
            speak("yes sir, Open BlacArch official page ")
            print("")
            User()

        elif user == 'ticket booking' or user == 'booking ticket':
            while True:
                speak("There are three booking options are available")
                print("""
                1.Cinema Tickets
                2.Bus Tickets
                3.Flight, Train & Others""")
                tk=int(input("Enter your choice : "))
                if tk==1:
                    speak("Selected Cinema Tickets Booking")
                    webbrowser.open("https://in.bookmyshow.com/explore/home/chennai")
                    print("")
                elif tk==2:
                    speak("Selected Bus tickets booking")
                    webbrowser.open("https://www.redbus.in/")
                    print("")
                elif tk==3:
                    speak("Flight, Train & Others tickets booking")
                    webbrowser.open("https://www.booking.com/index.en.html?aid=309654;label=hotels-english-en-india-I_3LMGkHqWe_vfh30GlaEQS433577572936:pl:ta:p1:p2:ac:ap:neg:fi:tikwd-101352960:lp9061971:li:dec:dm:ppccp=UmFuZG9tSVYkc2RlIyh9YcsZ-Id2vkzIfTmYhvC5HOg;ws=&gclid=EAIaIQobChMIhuT_yvPq_QIVLZpmAh2rkwwNEAAYASAAEgISw_D_BwE")
                    print("")
                    cl=int(input("Click 1 to continue : "))
                    if  cl==1:
                        continue
                    else:
                        print("Close Youtube") 
                        speak("Closing Youtube")
                        print("")
                        break
                

        
        #////////////////////////////////////
        #\\\\\\opening apps\\\\\\\\\\\\\\\\\
        #////////////////////////////////////

        elif user =='open vscode' or user == 'opening vscode' or user == 'vscode' or user == 'vs code':
            codepath="C:\\Users\\MARTIN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            print("A.I : Opening Visual studio code")
            speak("yes sir, opeing Visual studio code")
            print("")
            User()

        elif user == 'open chrome' or user == 'chrome' or user == 'opening chrome':
            codepath1="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codepath1)
            print("A.I : Opening chrome")
            speak("yes sir, opeing chrome browser")
            print("")
            User()

        #/////////////////////////////////////////////////
        #\\\\\\\\\\\\Sample programming\\\\\\\\\\\\\\\\\\\
        #/////////////////////////////////////////////////
    

        elif user=='sample program for gcd of two numbers' or user=='gcd of two numbers':
            print("""
            Program:
            n1=int(input("Enter the no.1:"))
            n2=int(input("Enter the no.2:"))
            rem=n1%n2
            while rem!=0:
            n1=n2
            n2=rem
            rem=n1%n2
            print("The GCD of given number is: ",n2)
            """)
            print("")
            User()
        elif user=='sample program for square root numbers' or user=='square root numbers':
            print("""
            Program:
            n=float(input("Square root: "))
            x=float(input("Estimate: "))
            final=(0.5*(x+(n/x)))
            print(final)
            for i in range(0,10):
            final=(0.5*(final+(n/final)))
            print(“The square root is: ”,final)
            """)
            print("")
            User()
        elif user=='sample program for exponential of numbers' or user=='exponential of numbers':
            print("""
            Program:
            def power(base,exp):
            if(exp==1):
            return(base)
            if(exp!=1):
            return(base*power(base,exp-1))
            base=int(input("Enter base: "))
            exp=int(input("Enter exponential value: "))
            print("Result:",power(base,exp))""")
            print("")
            User()

        

        #/////////////////////////////////////////////////////
        #\\\\\\\\\\\\\\\\\\\music/////////////////////////////
        #/////////////////////////////////////////////////////
        
        elif user == 'play music' or 'music':
            s=int(input("Enter No : "))
            musicdir="C:\\Users\\MARTIN\\Videos\\Captures"
            songs=os.listdir(musicdir)
            print(songs)
            os.startfile(os.path.join(musicdir,songs[1]))
            print("")
            User()
        elif user == 'play':
            s=int(input("Enter No : "))
            musicdir="C:\\Users\\MARTIN\\Videos\\Captures"
            songs=os.listdir(musicdir)
            print(songs)
            os.startfile(os.path.join(musicdir,songs[s]))
            print("")
            User()

        elif user=='face detector':
            fd()
            print("")
            User()
        else:
            print("A.I : I can do you understand")
            speak("I can do you understand")
            print("")
            User()

        

if __name__  == "__main__":
    main()
    admin()
    User()

    
    
        
       



        


