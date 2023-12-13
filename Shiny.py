import pyttsx3 as s
import webbrowser
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = s.init()
client = wolframalpha.Client('LRWJW6-436RP7LH87')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
r = sr.Recognizer()
def response():
    print()
def speak(audio):
    print('S.H.I.N.Y. : ' + audio)
    engine.say(audio)
    engine.runAndWait()
def greetme():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 10 and currentH < 3:
        speak('Hi Sir,Good Morning!')
        print('The time is', currentH)

    if currentH >= 3 and currentH < 15:
        speak('Hi Sir,Good Afternoon!')
        print('The time is', currentH)
    if currentH >= 15 and currentH != 19:
        speak('Hi Sir,Good Evening!')
        print('The time is', currentH)

    if currentH >= 19 and currentH != 10:
        speak('Good Night sir! It is night')
        print('The time is', currentH)
        speak('May i help you?')


greetme()
speak("HI! I AM SHINY YOUR BEST COMPANION")
speak("HOW MAY I HELP YOU")

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        text = r.listen(source)
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=2)
        audio = r.listen(source)
        r.pause_threshold = 1
        try:
            query = r.recognize_google(audio).lower()
            print('Creator: ' + query + '\n')

        except sr.UnknownValueError:

    return query


if __name__ == '__main__':

    while True:
        query = myCommand()
        query = query.lower()
        if 'open google' in query:
            speak('I AM PROCEEDING')
            webbrowser.open("www.google.com")

        elif 'open youtube' in query:
            speak('I AM PROCEEDING')
            webbrowser.open("www.youtube.com")
            
        elif 'read some news' in query:
            speak('I AM PROCEEDING')
            webbrowser.open("www.indiatoday.in")

        elif 'tell me a joke' in query or 'i want to hear joke' in query:
            speak('I AM PROCEEDING')
            jokes = ['Why did the chicken cross the road?\n To get to the other side',
                    'Knock, knock\nWho’s there?\nLettuce\nLettuce who?\nLettuce in, it’s cold out here\n“Lettuce in” sounds like “Let us in.”'
                    'How many Apple employees does it take to change a light bulb?\nSeven. One to change the bulb and six to design the T-shirt']
            speak(random.choice(jokes))
            
        elif 'what i can call you' in query:
            speak("CALL ME AS SHINY")
            
        elif 'open games' in query:
            speak('I AM PROCEEDING')
            webbrowser.open("www.friv.co.in")

        elif 'i want to buy things' in query:
            speak("I AM PROCEEDING")
            webbrowser.open("www.amazon.com")
            
        elif 'open instagram' in query:
            speak('I AM PROCEEDING')
            webbrowser.open("www.instagram.com")

        elif 'show my email jarvis' in query:
            speak('okay')
            speak('I AM PROCEEDING')
            webbrowser.open('www.gmail.com')
        #elif "play my favourite songs" in query or 'i am in jolly mood' in query:
            #speak("YES SIR SURE")
            #music_folder = 'folder location'
            #random_music = os.listdir(music_folder)
            #print(random_music)
            #os.startfile(os.path.join(music_folder, random.choice(random_music)))
            #sys.exit()

        elif 'what is the time jarvis' in query or 'time jarvis' in query:
            speak("The current time is" + (str(datetime.datetime.now().strftime('%H:%M:%S'))))
        elif 'what is the date jarvis' in query or 'date jarvis' in query:
            speak('The current time is ' + (str(datetime.datetime.now().strftime('%H:%M:%S'))))

        elif 'boring' in query or 'i am bored' in query:
            speak("ok ")
            speak("LET ME SHOW YOU SOME ENTERTAINING WORKS")
            char4 = input("WHICH GAME YOU WANT")
            if char4 == 'random game':
                speak("okay participants")
                speak("I AM PROCEEDING ")
                speak("WRITE YOUR NAME BELOW")
                speak("""okay 'ARE YOU READY',
                        here comes the rules,
                        1 YOU HAVE BEEN THREE CHANCES, 
                        2 YOU HAVE TO FIND THE NUMBER WHICH I AM THINKING,
                        3 IF YOU WIN YOU ARE GREAT IN GUESSING THE NUMBERS,
                        !!!!!!!OKAY HERE WE GO!!!!!!""")
                name = input("ENTER THE NAME:")
                speak(name)
                n = random.randint(0, 15)
                NUM = int(input("ENTER THE NUMBER:"))
                if n > NUM:
                    speak("your number is less than mine")
                elif n == NUM:
                    speak("your number is equal to mine")
                else:
                    speak("your number is greater than mine")

                NUM2 = int(input("ENTER THE NUMBER"))
                if n < NUM2:
                    speak("your number is greater than mine")
                elif n == NUM2:
                    speak("your number is equal to mine")
                else:
                    speak("your number is less than mine")

                NUM3 = int(input("ENTER THE NUMBER"))
                if n != NUM3:

                    speak("sorry!,you have lost the game")

                else:

                        speak("you have successfully won the game")

                print(n)
            else:
                speak("okay participants")
                speak("I AM PROCEEDING")
                speak("WRITE YOUR NAME BELOW")
                speak("""okay 'ARE YOU READY',
                        here comes the rules,
                        1 YOU WANT TO GUESS THE WORDS 
                        2 HINT WILL BE GIVEN 
                        3 YOU WANT TO GUESS THE WORD WHICH I AM THINKING
                        !!!!!!!OKAY HERE WE GO!!!!!!""")
                speak("     WELCOME TO PLAY HANGMAN    ")
                name = input("ENTER THE NAME:")
                speak(name)

                speak("     LET US TEST YOUR EAGERNESS    ")
                word = ['absurd', 'dislocation', 'fracture', 'yoked', 'memento']
                A = random.choice(word)
                print("guess the character")
                guesses = ''
                turns = 10
                while turns > 0:
                    failed = 0
                    for char in A:
                        if char in guesses:
                            print("char")
                        else:
                            print("_"),
                            failed += 1
                    if failed == 0:
                        print("You won and you saved him")
                        break
                    guess = input("guess a character:")
                    guesses += guess
                    if guess not in A:
                        turns -= 1
                        print("Wrong")
                        print("You have", + turns, 'more guesses')
                        if A == "absurd":
                            print("HINT!!!! MEANING - ILLOGICAL,UNREASONABLE")
                        elif A == "dislocation":
                            print("HINT!!!! MEANING - WRONG LOCATION")
                        elif A == "fracture":
                            print("HINT!!!! MEANING - GETTING HURT WHILE GOT ACCIDENT")
                        elif A == "yoked":
                            print("HINT!!!! MEANING - USED TO PLOUGH THE FARM")
                        else:
                            print("HINT!!!! MEANING - A ENGLISH MOVIE OF SHORT-TEMPER")

                            print("SORRY!!YOU HAVE KILLED HIM")

                        print("THE CORRECT ANSWER IS", A)
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('google says - ')
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=3)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                webbrowser.open('www.google.com')

        if char2 == 'm':
            speak('any Command!')
