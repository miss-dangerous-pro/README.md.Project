import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyautogui
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty ('voice', voices[1].id)
def speak (audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Orwa!")
        print("Good Morning Orwa!")
    elif hour>=12 and hour<18:
        speak ("Good Afternoon Orwa!")
        print("Good Afternoon Orwa!")
    elif hour<=18 and hour>23:
        speak("Good Evening Orwa!")
        print("Good Evening Orwa!")
    else:
        speak("Hello Orwa!")
        print("Hello Orwa!")
    speak ("I am Zira. How can i help you")
    print   ("I am Zira. How can i help you")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r. listen(source)
    try:
        print("recognizing....")
        query = r.recognize_google(audio , language='en=in')
        print(f"user said:{query}\n")
    except Exception as e:
        print(e)
        print("Say that again please....")
        return"None"
    return query
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia")
            results = wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("youtube is open")
            print("youtube is open")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak(" google is open ")
            print(" google is open ")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("stackoverflow is open ")
            print("stackoverflow is open ")
        elif 'play music' in query:
             music_dir = 'E:\\my playlist'
             songs = os.listdir(music_dir)
             print (songs)
             os.startfile(os.path.join(music_dir,songs[3]))
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strtime}")
            print(f"the time is {strtime}")
        elif 'open visual studio code' in query:
            path = "C:\\Users\\ASAD COMPUTERS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak('visual studio code is open')
            print('visual studio code is open')
            os.startfile(path)
        elif'open github' in query:
            webbrowser.open("github.com")
            speak(" github is open ")
            print(" github is open ")
        elif'open chatgpt' in query:
            webbrowser.open("chatgpt.com")
            speak(" chatgpt is open ")
            print(" chatgpt is open ")
        elif'open w3 school' in query:
            webbrowser.open("w3 school.com")
            speak("w3 school is open ")
            print("w3 schoolis open ")
        elif'open ai quizer' in query:
            path = "C:\\Program Files (x86)\\AI Quizzer\\AiQuizzer.exe"
            speak('ai quizer is open')
            print('ai quizer is open')
            os.startfile(path)
        elif'open adobe photoshop' in query:
            path = "C:\\Program Files\\Adobe\\Adobe Photoshop 2024\\Photoshop.exe"
            speak('adobe photoshop is open')
            print('adobe photoshop is open')
            os.startfile(path)
        elif'pause' in query:
            pyautogui.press("k")
            print("Yeah the video is paused")
            speak("Yeah the video is paused ")   
        elif'play' in query:
            pyautogui.press("k")
            print("the video is play")
            speak("the video is play") 
        elif'mute' in query:
            pyautogui.press("m")
            print("the video is muted")   
            speak("the video is muted")    
        elif'goodbye' in query:
            print("GoodBye orwa, Have a Nice day!")
            speak("GoodBye orwa, Have a Nice day!")
            exit()  
        elif'good night' in query:
            print("Good Night ! Have a sweet dreams")
            speak("Good Night ! Have a sweet dreams") 
            exit()
