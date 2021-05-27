# import pyttsx3
# speaker = pyttsx3.init()
# speaker.say('hello there')
# speaker.runAndWait()

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")
        speak("I am jarvis sir.Please tell me how many I help you")


def takeCommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password')  #email secure allow acess first
    server.sendmail('youremail@gmail.com',to,content)


if __name__ == "__main__":
    speak("shubham is a good boy")
    wishMe()
    # while True:
if 1:
    query = takeCommand().lower()
    # Logic for executing tasks on quer
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    elif 'open github' in query:
        webbrowser.open("github.com")
    elif 'play music' in query:
        webbrowser.open("spotify.com")
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir,the time is {strTime}")
    elif 'open code' in query:
        codepath = "C:\\Users\\Darshan26\\OneDrive\\Desktop\\javascript"
        os.startfile(codepath)

    elif 'email to harry' in query:
        try:
            speak("What should i say?")
            content = takeCommand()
            to = "shubham.v.pakhale@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
        speak("Sorry my friend shubham bhai.I am not able to send this email")
