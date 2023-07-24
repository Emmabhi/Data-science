import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import pywhatkit as kit
import pyautogui
import os
import calendar



Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',200)

def Speak(audio):
    print("  ")
    Assistant.say(audio)
    print(f": (audio)")
    print(" ")
    Assistant.runAndWait()
def c():
    print(calendar.calendar(2021,2,1,6))
def ta():
    n=int(input("Enter the number:"))
    for x in range(1,11):
        print(n,'*',x,'=',n*x)

pyautogui.prompt('What is your name?')
e=pyautogui.password('Enter password (text will be hidden)')
if e=='1515':
    def takecommand():
        command=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            command.pause_threshold = 1
            audio= command.listen(source)

            try:
                print("Recognizing....")
                query = command.recognize_google(audio,language='en-in')
                print(f"you said:{query}")

            except Exception as Error:
                return "none"

            return query.lower()




    def TaskExe():

        while True:
            query = takecommand()
            if 'hello' in query:
                Speak("hello abhishek")
                Speak("what should i do")
            elif 'how are you' in query:
                Speak("I am fine")
                Speak("What about you?")
            elif 'I am fine' in query:
                Speak("its good")
            elif 'Tell me about abhishek' in query:
                Speak("Abhishek is a sweet, calm and a wise person not much talkative  ")
            elif 'tell me about abhishek' in query:
                Speak("Abhishek is a sweet, calm and a wise person not much talkative  ")
            elif 'tell me about nikki didi' in query:
                Speak("She is a talkative and a cute girl,laughing everytime")
                Speak("how was my joke,hahahahaha")
                Speak("actually she is a stupid girl")
            elif 'take rest' in query:
                Speak("ok abhishek")
                Speak("call me whenever you need")
                break
            elif 'bye' in query:
                Speak("bye bye")
                break
            elif 'youtube search' in query:
                Speak("ok abhishek ")
                p=takecommand()
                query=query.replace("search",p)
                web="https://www.youtube.com/results?search_query="+p
                webbrowser.open(web)
                Speak("DOne")
            elif 'google search' in query:
                Speak("ok abhishek")
                n=takecommand()
                query=query.replace("search",n)
            
                pywhatkit.search(n)
                Speak("Done")
            elif 'text' in query:
                Speak("ok abhishek")
                a=takecommand()
                kit.text_to_handwriting(a)#not working
            elif 'screenshot' in query:
                Speak("ok abhishek")
                Speak("Take me to the page")
                im=pyautogui.screenshot()
                im.save('ss.png')
            elif 'whatsapp' in query:
                Speak(" Enter number To whom you want to send")
                g=takecommand()
                Speak("Your message")
                h=takecommand()
                Speak("time in hour")
                i=int(takecommand())
                Speak("time in minute")
                j=int(takecommand())
                kit.sendwhatmsg(g,h,i,j)

            elif 'date' in query:
                os.system("date1.py")
            elif 'clock' in query:
                Speak("opening clock")
                os.system("clock.py")
            elif 'contacts' in query:# save not working
                Speak("opening contacts")
                os.system("contacts.py")
            elif 'alarm' in query:# time manage not working
                Speak("wait a while")
                os.system("alarm.py")
            elif 'calendar' in query:
                Speak("Opening 2021 calendar")
                cal=c()
            elif 'table' in query:
                tab=ta()
            elif 'movie' in query:
                Speak("Wait buddy")
                os.system("F:\video")
            else:
                Speak("no command abhishek")

    TaskExe()
else:
    print("incorrect password")
    





        
