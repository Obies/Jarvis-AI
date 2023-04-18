# This is a speak function that can use audio output for our speak function
# import pyttsx3 module to use in the code file-module to access the device hardware
# import datetime to get the date and time from my device
# import speech-recognition to convert audio to text
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import requests
import json
import webbrowser
import os
import pywhatkit as kit
import smtplib
engine = pyttsx3.init('sapi5')  # voice module of Windows systems

# voices variable
voices = engine.getProperty('voices')

# print voices and select a voice-female or male
engine.setProperty('voice', voices[1].id)
# print(voices[1].id) - prints out voices

# author variable
author = 'Obakeng'

# Function to speak using AUDIO- uses pyttsx3 module to use hardware speakers


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to send email using voice command from smtplib


def sendEmail(to, content):
    server = smtplib.SMTP('smt.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your gmail address', 'your password')
    server.sendmail('your gmail address', to, content)
    server.close()

# WishMe function- wishes "good morning" and "good afternoon" during specific times
# if condition is used to determine what to say based on the time


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good morning {author}")
    elif hour >= 12 and hour < 18:
        speak(f"Good afternoon {author}")
    else:
        speak(f"Good evening {author}")

    speak(
        f"Hello {author}, my name is Betty, Please tell me how may i help you?")


def takeCommand():
    # Takes microphone input from the user and returns a string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1.5
        audio = r.listen(source)

    try:
        print("recognizing")
        query = r.recognize_google(audio, language='en-za')
        print(f"User said: {query} \n")

    except Exception as e:
        print(f"Sorry {author}, Say that again...")
        return "None"

    return query


# main function where all other functions from the code are called
# Calls the speak function inside the code
if __name__ == "__main__":
    # speak(f"Welcome {author}, my name is Betty")
    wishMe()
    # takeCommand()

    # using if function to search Wikipedia as it listens first then gives results based on input-output needed

    if 1:
        query = takeCommand().lower()
        # Who triggers the wikipedia search
        if 'wikipedia' and 'who' in query:
            speak("Searching Wikipedia..")  # takes voice input
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            # another speak function
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'news' in query:
            speak("News Headlines")
            query = query.replace("news", "")
        # API Key to get news updates
            url = "https://newsapi.org/v2/top-headlines?country=za&apiKey=422c94d72f6e4068b6ae6b607f3d7e3c"
            news = requests.get(url).text
            news = json.loads(news)  # converts json file to Python
            art = news['articles']
            for article in art:
                print(article['title'])
                speak(article['title'])

                print(article['description'])
                speak(article['description'])
                speak("Moving on to the next news")

        # elif uses voice command to open Google
        elif 'open google' in query:
            webbrowser.open("google.com")

        # Also opens YouTube using voice command
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        # Takes voice command and searches it on specified browser
        elif 'search browser' in query:
            speak("What should i search?")
            um = takeCommand().lower()
            webbrowser.open(f"{um}")

        # Voice command to get IP address using selected site
        elif 'ip address' in query:
            ip = requests.get('http://api.ipify.org').text
            print(f"Your ip is {ip}")
            speak(f"Your ip is {ip}")

        # open application using voice command-code does not work in opening apps but runs
        elif 'open command prompt' in query:
            os.system("start cmd")

        # Application 1
        elif 'open media player' in query:
            codepath = "C:\\Program Files\\Windows Media Player\wmplayer.exe"
            os.startfile(codepath)

        # Application 2
        elif 'open up' in query:
            codepath = "C:\\Program Files\\7-Zip\\7zFM.exe"
            os.startfile(codepath)

        # Elif condition to play music on laptop
        elif 'play music' in query:
            music_dir = 'C:\\Users\\User\\Music\\Naika'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        # elif condition to play search result on YouTube
        elif 'play youtube' in query:
            speak("What should i search?")
            cm = takeCommand().lower()
            kit.playonyt(f"{cm}")

        # elif condition to send whatsapp messages via voice command
        # Remember to login to web.whatsapp.com first-opens whatsapp but doesn't send message
        elif 'send message' in query:
            speak("Who do you want to send the message to?")
            num = input("Enter the number please: \n")
            speak("What message do you want to send the user?")
            msg = takeCommand().lower()
            speak("Please enter the time.")
            H = int(input("Enter the hour: \n"))
            M = int(input("Enter the minute: \n"))
            kit.sendwhatmsg(num, msg, H, M)

        # Elif condition sends email using voice command
        elif 'send email' in query:
            speak("What should i send sir")
            content = takeCommand().lower()
            speak("Who should i send the email to? and please enter the address")
            to = input("Please enter the email address? \n")
            sendEmail(to, content)
