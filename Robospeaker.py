##Robospeaker BY Nishant.

import pyttsx3

if __name__ == '__main__':
    print('Welcome to robospeaker 1.1 created by Nishant')
    engine = pyttsx3.init()

    while True:
        x = input("Enter what you want me to speak (type 'q' to quit): ")
        if x.lower() == "q":
            engine.say('Goodbye! Have a great day.')
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()



