import speech_recognition as sr
import pyttsx3
from chatbot_logic import chatbot_response

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Speed of speech
engine.setProperty("volume", 1.0)  # Volume (0.0 to 1.0)

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing...")
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "I couldn't understand that. Please try again."
        except sr.RequestError:
            return "I couldn't connect to the speech recognition service."
        except sr.WaitTimeoutError:
            return "You didn't say anything. Please try again."

# Main chatbot loop
def main():
    speak("Hello! I am your voice chatbot. How can I assist you today?")
    while True:
        user_input = listen()
        if user_input.lower() in ["exit", "quit", "bye"]:
            speak("Goodbye! Have a great day!")
            break
        print(f"You said: {user_input}")
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
        speak(response)

if __name__ == "__main__":
    main()
