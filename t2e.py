import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak in Telugu:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='te-IN')  # 'te-IN' is the language code for Telugu
        print("You said (Telugu):", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Error making the request; {e}")
        return None

def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, src='te', dest=target_language)  # 'te' is the language code for Telugu
    print(f"Translation to {target_language}: {translation.text}")
    return translation.text

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    os.system("start output.mp3")

def main():
    original_text = speech_to_text()
    if original_text:
        translated_text = translate_text(original_text)
        text_to_speech(translated_text, lang='en')

if __name__ == "__main__":
    main()
