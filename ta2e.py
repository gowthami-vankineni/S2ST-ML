import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the translator
translator = Translator()

# Function to recognize Tamil speech from the microphone
def recognize_tamil():
    with sr.Microphone() as source:
        print("Speak in Tamil:")
        audio = recognizer.listen(source)

        try:
            print("Transcribing...")
            # Recognize speech in Tamil
            tamil_text = recognizer.recognize_google(audio, language="ta-IN")
            print("Tamil Text:", tamil_text)
            return tamil_text

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

# Function to translate Tamil text to English and synthesize as audio file
def translate_and_synthesize_audio(tamil_text):
    try:
        # Translate Tamil text to English
        translation = translator.translate(tamil_text, src="ta", dest="en")
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

# Recognize Tamil speech from the microphone
tamil_text = recognize_tamil()

# Translate Tamil text to English and synthesize as audio file
if tamil_text:
    translate_and_synthesize_audio(tamil_text)
