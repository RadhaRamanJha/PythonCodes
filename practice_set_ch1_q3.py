# after typing "pip install pyttsx3"
# importing the package
# errororeous program import pyttsx3

# engine=pyttsx3.init()

# text=input("Talking to you is fun Radha Raman")

# s=engine.getProperty("voices")
# engine.setProperty("voice",s[0],11)
# engine.setProperty("rate",15,50)
# engine.say(text)
# engine.runAndWait()

# importing the pyttsx library
import pyttsx3
  
# initialisation
engine = pyttsx3.init()
  
# testing
engine.say('''
This is how texte is converted to speech ''')
engine.runAndWait()