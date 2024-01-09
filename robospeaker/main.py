#import package for speech output in windows system
import pyttsx3

if __name__ == '__main__':
    print("HELLOW EVERYONE MY NAME IS SACHIN RATHOD ,IAM MCA STUDENT ")
    print("WELCOME TO ROBO SPEAKER 2.0")
    engine = pyttsx3.init()
    while True:
        x = input("Enter your message to speak (or 'q' to quit): ")

        if x.lower() == "q":
            break
            #actual intered command or text is speeks
        engine.say(x)
        engine.runAndWait()
