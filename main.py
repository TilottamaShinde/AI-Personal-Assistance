from voice_input import listen_command
from tts_output import speak_text
from symmarizer import summarize_content
from calendar_scheduler import schedule_event

def main():
    speak_text("Hello! How can I assist you today?")
    command = listen_command()

    if not command:
        speak_text("Sorry, I could not hear you properly.")
        return

    if "summarize" in command:
        speak_text("Please say the PDF file or article URL")
        input_str = listen_Command()
        summary = summarize_content(input_str)
        speak_text("Here is the summary.")
        speak_text(summary)

    elif "schedule" in command or "calendar" in command:
        speak_text("Please describe the event")
        event_description = listen_command()
        result = schedule_event(event_description)
        speak_text(result)

    else:
        speak_text("Sorry, I did not understand the request.")

if __name__ == "__main__":
    main()
