import speech_recognition as sr
import  openai
from openai import Completion
import time
from googletrans import Translator

translator = Translator()

# Translate from English to French
#translation = translator.translate('Hello10', src='en', dest='ta')

#print(translation.origin, ' -> ', translation.text)

#import speech_recognition as sr
openai.api_key = "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"


def recognize_speech():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="ta-IN")
        translation = translator.translate(text, src='ta', dest='en')
        print(translation.origin)
       
        def generate_text():
                    response = openai.Completion.create(
                    engine="text-davinci-002",
                    prompt=translation.text,
                    max_tokens=2000,
                    top_p=1,
                    temperature=0,
                    frequency_penalty=0,
                    presence_penalty=0)
                    return response.choices[0].text

        return generate_text ()
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service: {0}".format(e))

print(recognize_speech())


