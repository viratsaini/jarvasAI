import os
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser as w
import pywhatkit
import random
import smtplib
import openai
from config import apikey

#insatll all modules-import os,pyttsx3,speech_recognition,datetime,webbrowser,pywhatkit,random,smtplib,openai 

chatStr = ""

def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr += f"Virat:{query}\n Jarvis: "
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt= chatStr,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
    except:
        return None
    try:
        speech(response["choices"][0]["text"])
        chatStr += f"{response['choices'][0]['text']}\n"
        return response["choices"][0]["text"]
    except Exception as e:
         speech("Sorry virat bhai. I don't understand")


def ai(prompt):
    openai.api_key = apikey
    text=f"{query}\n**********************\n\n"
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": prompt
        }  
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    text=text+(response["choices"][0]["message"]["content"])
    if not os.path.exists("openai"):
        os.mkdir("openai")
    with open(f'openai/{"".join(query.split("using ai")[1:])}.txt',"w") as f:
        f.write(text)

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speech("good morning sir")
    elif hour >= 12 and hour < 18:
        speech("good afternoon sir")
    else:
        speech("good evening sir")
    speech(" i am Jarvis, please tell me how may i help you")

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty(voices, voices[1].id)
def speech(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
         print("Say that again please...")
         return "None"
    return query
p={
    " virat":"+918273436552"
}
d = {
    " virat": "coe213057.ai.coe@cgc.edu.in",
    " project email": "vprojectsaini@gmail.com",
    " shailendra": "shailsingh999@gmail.com",
    "shivang":"shivang28.sg@gmail.com"
}
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("viratsaini.vr@gmail.com", "yulbxlodofmoqdxx")
    server.sendmail("viratsaini.vr@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wishme()
    while True:
        query=takecommand().lower()
        if "quit" in query:
            speech("quiting sir")
            exit() 
        elif "search on google maps" in query:
            speech("Searching sir... ")
            q = query.replace("search on google maps", "")
            v=(f"https://www.google.com/maps/search/{q}/@30.6884668,76.6540152,14z/data=!3m1!4b1.com")
            w.open(v)  
        elif f"open" in query:
            sites=[["youtube","youtube.com"],["google","google.com"]]    
            for site in sites:
                if f"open {site[0]}" in query:
                    speech(f"Opening {site[0]}... ")
                    w.open(site[1])              
        elif "search on google" in query:
            speech("searching....")
            q = query.replace("search on google", "")
            w.open(q)
        elif "play on youtube " in query:
            speech("Playing sir... ")
            q = query.replace("play on youtube", "")
            pywhatkit.playonyt(query)            
        elif "send whatsapp message to" in query:
            try:
                q = str(query.replace("send whatsapp message to", ""))
                speech("What should I say?")
                content = takecommand()
                to = p[q]
                speech("Sending sir... ")
                pywhatkit.sendwhatmsg_instantly(f"{to}", f"{content}")
            except:
                speech("i don't have his mobile number ")    
        elif "send email to" in query:
            try:
                q = str(query.replace("send email to", ""))
                speech("What should I say?")
                content = takecommand()
                to = d[q]
                sendEmail(to, content)
                speech("Email has been sent!")
            except Exception as e:
                speech("Sorry virat bhai. I am not able to send this email")    
        
        elif "play movie" in query:
            r = random.randint(1, 7)
            movie_dir = "C:\\Users\\virat\\Videos"
            movie = os.listdir(movie_dir)
            speech("playing...")
            os.startfile(os.path.join(movie_dir, movie[r]))

        elif "play music" in query:
            r = random.randint(0, 2)
            music_dir = "C:\\Users\\virat\\Music"
            songs = os.listdir(music_dir)
            speech("playing...")
            os.startfile(os.path.join(music_dir, songs[r]))

        elif "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speech(f"sir,the time {time}")   
        elif "using ai" in query:
            ai(query) 
        elif "reset chat".lower() in query.lower():
            chatStr = ""
        else:
            print("Chatting...")
            chat(query)     