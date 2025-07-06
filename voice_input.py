import speech_recognition as sr



def listen_command():
    recognizer =  sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError:
        print("Speech service is unavailable.")
        return ""
