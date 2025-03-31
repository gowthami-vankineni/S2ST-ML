import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the translator
translator = Translator()

# Function to recognize English speech from the microphone
def recognize_english():
    with sr.Microphone() as source:
        print("Speak in English:")
        audio = recognizer.listen(source)

        try:
            print("Transcribing...")
            # Recognize speech in English
            english_text = recognizer.recognize_google(audio)
            print("English Text:", english_text)
            return english_text

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

# Function to translate English text to Telugu and synthesize as audio file
def translate_and_synthesize_audio(english_text):
    try:
        # Translate English text to Telugu
        translation = translator.translate(english_text, src="en", dest="te")
        telugu_text = translation.text
        print("Telugu Text:", telugu_text)

        # Synthesize Telugu text as audio
        tts = gTTS(telugu_text, lang='te')
        tts.save("translated_audio.mp3")
        print("Audio file saved as 'translated_audio.mp3'")

        # Play the audio file
        os.system("start translated_audio.mp3")

    except Exception as e:
        print("Translation Error:", e)

# Recognize English speech from the microphone
english_text = recognize_english()

# Translate English text to Telugu and synthesize as audio file
if english_text:
    translate_and_synthesize_audio(english_text)
