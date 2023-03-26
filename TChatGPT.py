import openai
import pyaudio
import pyttsx3
engine = pyttsx3.init()
import speech_recognition as sr
listener = sr.Recognizer()

openai.api_key = "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"

while True:
    with sr.Microphone() as source:
        print("Speak Now...")
        voice = listener.listen(source)
        user = listener.recognize_google(voice)
    model = "text-davinci-003"
    if "exit" in user:
        break

    completion = openai.Completion.create(model = "text-davinci-003",
    prompt = user,
    max_tokens = 2048,
    temperature = 0.2,
    n = 1,
    stop = None
    )
    response = completion.choices[0].text
    choice = int(input("Enter 1 to print the response or Enter 2 to print and hear the response\n"))

    if choice == 1:
        print(response)
    
    else:
        print(response)
        engine.say(response)
        engine.runAndWait()

    repeat = input("Do You Want To Ask More Questions?\n")
    if repeat in ["NO", "no", "No", "nO"]:
        break
