'''To print and play twinkle twinkle little star'''
import pyttsx3
engine = pyttsx3.init()
rhyme = '''Twinkle, twinkle, little star, How I wonder what you are.
         Up above the world so high, Like a diamond in the sky.
         When the blazing sun is gone, When he nothing shines upon,
         Then you show your little light, Twinkle, twinkle, all the night.
         Then the traveller in the dark, Thanks you for your tiny spark,
         He could not see which way to go, If you did not twinkle so.
         In the dark blue sky you keep, And often through my curtains peep,
         For you never shut your eye, ‘Till the sun is in the sky.
         As your bright and tiny spark, Lights the traveller in the dark.
         Though I know not what you are, Twinkle, twinkle, little star.
         Twinkle, twinkle, little star. How I wonder what you are.
         Up above the world so high, Like a diamond in the sky.
         Twinkle, twinkle, little star. 
         How I wonder what you are.  How I wonder what you are.'''
print(rhyme)
engine.say(rhyme)
engine.runAndWait()