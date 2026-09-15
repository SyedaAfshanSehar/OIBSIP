import datetime
import webbrowser

import pyttsx3
import speech_recognition as sr


def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
        except sr.WaitTimeoutError:
            speak("I did not hear anything. Please try again.")
            return ""

    try:
        text = recognizer.recognize_google(audio).lower()
        print(f"You: {text}")
        return text
    except sr.UnknownValueError:
        speak("Sorry, I could not understand that. Please repeat.")
    except sr.RequestError:
        speak("The speech recognition service is unavailable right now.")
    return ""


def handle_command(command):
    if not command:
        return True

    if command in {"hello", "hi", "hey"} or "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        speak(datetime.datetime.now().strftime("The current time is %I:%M %p."))
    elif "date" in command or "today" in command:
        speak(datetime.datetime.now().strftime("Today is %A, %B %d, %Y."))
    elif command.startswith("search "):
        topic = command.replace("search ", "", 1).strip()
        if topic:
            speak(f"Searching the web for {topic}.")
            webbrowser.open("https://www.google.com/search?q=" + topic.replace(" ", "+"))
        else:
            speak("Please tell me what you want to search for.")
    elif command in {"exit", "quit", "stop", "goodbye"}:
        speak("Goodbye!")
        return False
    else:
        speak("I can greet you, tell the time or date, and search the web. Please try again.")
    return True


engine = pyttsx3.init()
speak("Voice assistant started. Say hello, ask for the time or date, or say search followed by a topic.")

while True:
    if not handle_command(listen()):
        break
