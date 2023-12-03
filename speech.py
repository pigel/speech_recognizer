import speech_recognition
import pyttsx3

# sr = speech_recognition.Recognizer()
# sr.pause_threshold = 0.5
#
# def greeting():
#     return 'привет'


# with speech_recognition.Microphone() as mic:
#     sr.adjust_for_ambient_noise(source=mic, duration=0.5)
#     audio = sr.listen(source=mic)
#     query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()


engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in engine.getProperty('voices'):
    print(voice)
engine.setProperty('voice', voices[12].id)

engine.say('hello alexa')
engine.runAndWait()
# print(query)
# if query == 'привет':
#     print(greeting())
# else:
#     print('прожуй потом разговаривай')
