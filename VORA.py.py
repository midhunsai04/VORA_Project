from __future__ import with_statement
import pyttsx3  
import speech_recognition as sr  
import datetime 
import wikipedia 
import webbrowser 
import os 
import random 
import cv2 
import pywhatkit as kit 
import sys 
import pyautogui 
import time 
import operator 
import requests 

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) 
engine.setProperty('rate', 150) 

def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 

def wishMe(): 
    hour = int(datetime.datetime.now().hour) 
    if hour >= 0 and hour < 12: 
        speak("Morning!!! Boss") 
    elif hour >= 12 and hour < 18: 
        speak("Afternoon!!! Boss")    
    else: 
        speak("Good Evening!!! Boss") 
    speak("System Ready, At your service boss") 

def takeCommand(): 
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        print("Listening...") 
        r.pause_threshold = 1 
        audio = r.listen(source) 
    try: 
        print("Recognizing...")     
        query = r.recognize_google(audio, language='en-in') 
        print(f"User  said: {query}\n") 
    except Exception as e:     
        print("Say that again please...")   
        speak("Say that again please...")
        return "None" 
    return query 

def writeToNotepad(text):
    # Open Notepad and write the text
    pyautogui.hotkey('win') 
    time.sleep(1) 
    pyautogui.write('notepad') 
    time.sleep(1) 
    pyautogui.press('enter') 
    time.sleep(1) 
    pyautogui.write(text, interval=0.1)

if __name__ == "__main__": 
    wishMe() 
    while True: 
        query = takeCommand().lower() 

         # Write everything you say into Notepad
        if 'write' in query:
            text_to_write = query.replace("write", "").strip()
            if text_to_write:
                writeToNotepad(text_to_write)
                speak("I have written that in Notepad.")
            else:
                speak("What should I write?")
                
        elif 'wikipedia' in query: 
            speak('Searching Wikipedia...') 
            query = query.replace("wikipedia", "") 
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia") 
            print(results) 
            speak(results) 
        elif "college" in query: 
            webbrowser.open("https://www.velhightech.com/") 
        elif 'search on youtube' in query: 
            query = query.replace("search on youtube", "") 
            webbrowser.open(f"www.youtube.com/results?search_query={query}") 
        elif 'open youtube' in query: 
            speak("What would you like to watch?") 
            qrry = takeCommand().lower() 
            kit.playonyt(f"{qrry}") 
        elif 'close chrome' in query: 
            os.system("taskkill /f /im chrome.exe") 
        elif 'close youtube' in query: 
            os.system("taskkill /f /im chrome.exe") 
        elif 'open google' in query: 
            webbrowser.open("https://www.google.com/")
        elif 'search' in query:    
            query = query.replace("search", "")
            #query = takeCommand().lower() 
            webbrowser.open(f"https://www.google.com/search?q={query}") 
            results = wikipedia.summary(query, sentences=2) 
            speak(results)
            print(results)
        elif 'tell me about' in query:    
            query = query.replace("tell me about", "")
            #query = takeCommand().lower() 
            webbrowser.open(f"https://en.wikipedia.org/wiki/{query}") 
            results = wikipedia.summary(query, sentences=2) 
            speak(results)
            pyautogui.hotkey('win') 
            time.sleep(1) 
            pyautogui.write('notepad') 
            time.sleep(1) 
            pyautogui.press('enter') 
            time.sleep(1) 
            pyautogui.write(results, interval=0.1)

        elif 'close google' in query: 
            os.system("taskkill /f /im chrome.exe")

        elif 'play music' in query: 
            music_dir = 'E:\\Musics' 
            songs = os.listdir(music_dir)     
            os.startfile(os.path.join(music_dir, random.choice(songs))) 
        elif 'play iron man movie' in query: 
            npath = "E:\\ironman.mkv"     
            os.startfile(npath) 
        elif 'close movie' in query: 
            os.system("taskkill /f /im vlc.exe") 
        elif 'close music' in query: 
            os.system("taskkill /f /im vlc.exe") 
        elif 'the time' in query: 
            strTime = datetime.datetime.now().strftime("%H:%M:%S")     
            speak(f"Sir, the time is {strTime}") 
        elif "shut down the system" in query: 
            os.system("shutdown /s /t 5") 
        elif "restart the system" in query: 
            os.system("shutdown /r /t 5") 
        elif "lock the system" in query: 
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0") 
        elif "close notepad" in query: 
            os.system("taskkill /f /im notepad.exe") 
        elif "open command prompt" in query: 
            os.system("start cmd") 
        elif "close command prompt" in query: 
            os.system("taskkill /f /im cmd.exe")
        elif "open camera" in query: 
            cap = cv2.VideoCapture(0) 
            while True: 
                ret, img = cap.read() 
                cv2.imshow('webcam', img) 
                k = cv2.waitKey(50) 
                if k == 27: 
                    break 
            cap.release() 
            cv2.destroyAllWindows() 
        # Time Command
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The current time is {time}")
        
        # Date command
        elif 'date' in query:
            date = datetime.datetime.now().strftime('%A, %B %d, %Y')
            speak(f"Today is {date}")

        elif "go to sleep" in query: 
            speak('Pleasure is mine Boss') 
            sys.exit() 
        elif "take screenshot" in query: 
            speak('Tell me a name for the file') 
            name = takeCommand().lower() 
            time.sleep(3) 
            img = pyautogui.screenshot()   
            img.save(f"{name}.png")   
            speak("Screenshot saved") 
        elif "calculate" in query: 
            r = sr.Recognizer() 
            with sr.Microphone() as source: 
                speak("Ready") 
                print("Listening...") 
                r.adjust_for_ambient_noise(source) 
                audio = r.listen(source) 
                my_string = r.recognize_google(audio) 
                print(my_string) 
                def get_operator_fn(op): 
                    return { 
                        '+' : operator.add, 
                        '-' : operator.sub, 
                        'x' : operator.mul, 
                        'divided' : operator.__truediv__, 
                    }[op] 
                def eval_binary_expr(op1, oper, op2): 
                    op1, op2 = int(op1), int(op2) 
                    return get_operator_fn(oper)(op1, op2) 
                speak("Your result is") 
                speak(eval_binary_expr(*(my_string.split()))) 
        elif "what is my ip address" in query: 
            speak("Checking") 
            try: 
                ipAdd = requests.get('https://api.ipify.org').text 
                print(ipAdd) 
                speak("Your IP address is") 
                speak(ipAdd) 
            except Exception as e: 
                speak("Network is weak, please try again some time later") 
        elif "volume up" in query: 
            for _ in range(15): 
                pyautogui.press("volumeup") 
        elif "volume down" in query: 
            for _ in range(15): 
                pyautogui.press("volumedown") 
        elif "mute" in query: 
            pyautogui.press("volumemute") 
        elif "refresh" in query: 
            pyautogui.moveTo(1551, 551, 2) 
            pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right') 
            pyautogui.moveTo(1620, 667, 1) 
            pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left') 
        elif "scroll down" in query: 
            pyautogui.scroll(1000) 
        elif "scroll up" in query:
            pyautogui.scroll(1000) 
        elif "close paint" in query: 
            os.system("taskkill /f /im mspaint.exe") 
        #Introduction
        elif "who are you" in query: 
            print('My Name Is vora')  
            speak('My Name Is vora') 
            print('I am developed to be your personal AI assistant, capable of doing many things') 
            speak('I am developed to be your personal AI assistant, capable of doing many things')
        
        #elif "open notepad and write my channel name" in query: 
            pyautogui.hotkey('win') 
            time.sleep(1) 
            pyautogui.write('notepad') 
            time.sleep(1) 
            pyautogui.press('enter') 
            time.sleep(1) 
            pyautogui.write("VORA Voice Oriented Response Assistant", interval=0.1)  
        elif 'type' in query: 
            query = query.replace("type", "") 
            pyautogui.write(f"{query}") 

# Chrome Automation Source Code 
import pyttsx3  
import speech_recognition as sr 
import pyautogui 
import time 
import os 

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id) 
engine.setProperty('rate', 150) 

def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 

def takeCommand(): 
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        print("Listening...") 
        r.pause_threshold = 1 
        audio = r.listen(source) 
    try: 
        print("Recognizing...")     
        query = r.recognize_google(audio, language='en-in') 
        print(f"User  said: {query}\n") 
    except Exception as e:     
        print("Say that again please...")
        speak("Can you repeat that for me again...")
        return "None" 
    return query 

if __name__ == "__main__": 
    while True: 
        query = takeCommand().lower() 
        if 'open chrome' in query: 
            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe") 
        elif 'maximize this window' in query: 
            pyautogui.hotkey('alt', 'space') 
            time.sleep(1) 
            pyautogui.press('x') 
        elif 'google search' in query: 
            query = query.replace("google search", "") 
            pyautogui.hotkey('alt', 'd') 
            pyautogui.write(f"{query}", 0.1) 
            pyautogui.press('enter') 
        elif 'youtube search' in query: 
            query = query.replace("youtube search", "") 
            pyautogui.hotkey('alt', 'd') 
            time.sleep(1) 
            pyautogui.press('tab', presses=4) 
            time.sleep(1) 
            pyautogui.write(f"{query}", 0.1) 
            pyautogui.press('enter') 
        elif 'open new window' in query: 
            pyautogui.hotkey('ctrl', 'n') 
        elif 'close chrome' in query: 
            os.system("taskkill /f /im chrome.exe")

        