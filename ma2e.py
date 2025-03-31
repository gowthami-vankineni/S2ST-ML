import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the translator
translator = Translator()

# Function to recognize Malayalam speech from the microphone
def recognize_malayalam():
    with sr.Microphone() as source:
        print("Speak in Malayalam:")
        audio = recognizer.listen(source)

        try:
            print("Transcribing...")
            # Recognize speech in Malayalam
            malayalam_text = recognizer.recognize_google(audio, language="ml-IN")
            print("Malayalam Text:", malayalam_text)
            return malayalam_text

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

# Function to translate Malayalam text to English and synthesize as audio file
def translate_and_synthesize_audio(malayalam_text):
    try:
        # Translate Malayalam text to English
        translation = translator.translate(malayalam_text, src="ml", dest="en")
        english_text = translation.text
        print("English Text:", english_text)

        # Synthesize English text as audio
        tts = gTTS(english_text, lang='en')
        tts.save("translated_audio.mp3")
        print("Audio file saved as 'translated_audio.mp3'")

        # Play the audio file
        os.system("start translated_audio.mp3")

    except Exception as e:
        print("Translation Error:", e)

# Recognize Malayalam speech from the microphone
malayalam_text = recognize_malayalam()

# Translate Malayalam text to English and synthesize as audio file
if malayalam_text:
    translate_and_synthesize_audio(malayalam_text)
