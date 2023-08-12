# import sys
import pyttsx4
import speech_recognition as sr

class main:
    @staticmethod
    def text_to_speech(text):
        engine = pyttsx4.init()
        # volume = engine.getProperty('volume')
        engine.setProperty('volume', 1.0)
        # voices = engine.getProperty('voices')
        # for voice in voices:
        #     print(voice)
        engine.setProperty('voice', 'com.apple.speech.synthesis.voice.fiona')
        # engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Alex')
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 30)

        try:
            engine.say(text)
            engine.runAndWait()
        except ValueError:
            print("ValueError")
        except IOError:
            print("IOError")
        finally:
            # print("UnknownError")
            engine.stop()

    @staticmethod
    def speech_to_text():
        rec = sr.Recognizer()
        text = ""
        with sr.Microphone() as mic:
            voice = rec.listen(mic)

            try:
                text = rec.recognize_google(voice)
                # text = rec.recognize_whisper(voice, language="english")
                # text = rec.recognize_sphinx(voice)
                # text = rec.recognize_amazon(voice)
                # text = rec.recognize_bing(voice)
            except sr.UnknownValueError:
                print("E: Can't not understand")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return text

    print("Say Something....")
    microphone_names = sr.Microphone.list_microphone_names()
    working_microphones = sr.Microphone.list_working_microphones()
    text_to_speech("Say Something....")
    while True:
        speech_text = speech_to_text()

        if speech_text in ['hi', 'hello', 'hey']:
            print(f"You Say: {speech_text}")
            print("Hello, How are you?")
            text_to_speech("Hello, I'm your personal assistant, How are you?")
        elif speech_text in ['good','very good',  'well', "i'm good", "i'm fine", 'fine', 'great']:
            print(f"You Say: {speech_text}")
            print("Very well, I'm So Happy for you.")
            text_to_speech("Very well, I'm So Happy for you.")
        elif speech_text in ['bad', 'very bad', "so bad", 'tired', 'sad', 'so sad', 'angry']:
            print(f"You Say: {speech_text}")
            print("OK, try to relax and do something positive.")
            text_to_speech("OK, try to relax and do something positive.")
        elif speech_text in ['exit', 'bye', 'bye bye', 'goodbye', 'close']:
            print(f"You Say: {speech_text}")
            print("Good bye my friend.")
            text_to_speech("Good bye my friend.")
            # sys.exit(0)
            break
        else:
            print(f"You Say: {speech_text}")
            print("I can't understand,, please repeat wat you say?")
            text_to_speech("I can't understand,, please repeat wat you say?")

    print("........")