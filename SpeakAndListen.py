import pyttsx3  # For text-to-speech conversion
import speech_recognition as sr  # For capturing and recognizing speech

# Initialize the text-to-speech engine with SAPI5 (Microsoft Speech API)
engine = pyttsx3.init("sapi5")

# Function to convert text to speech and print to console
def speak(text):
    engine.say(text)  # Queue the text for speech synthesis
    print(f"Bot: {text}")  # Print the text to the console for logging
    engine.runAndWait()  # Process the voice command and speak it


# Function to listen to the user's voice command and extract the message and recipient
def listen():
    # Create a recognizer instance for speech recognition
    recognizer = sr.Recognizer()

    # Adjust pause and ambient energy thresholds (improves performance in noisy environments)
    recognizer.pause_threshold = 1.5  # Wait a bit longer after speaking to assume pause
    recognizer.energy_threshold = 500  # Adjust for ambient noise level

    # Open the default microphone as the audio source
    with sr.Microphone() as mic:
        # Adjust microphone settings for ambient noise for 1 second
        recognizer.adjust_for_ambient_noise(mic, duration=1)

        print("Listening...")
        # Listen for a phrase from the user
        audio = recognizer.listen(mic)
        print("Recognizing...")

        try:
            # Convert the audio to text using Google's speech recognition API
            command = recognizer.recognize_google(audio)
            print(f"Recognized command: {command}")

            # Check if the command includes the keywords "send" and "to"
            if "send" in command.lower() and "to" in command.lower():
                parts = command.split()  # Split the recognized command into words
                try:
                    # Find the index after the word "send" as the start of the message
                    message_index = parts.index("send") + 1
                    # Find the index of the word "to", which marks the end of the message and start of the recipient
                    to_index = parts.index("to")

                    # Extract the message by joining words between "send" and "to"
                    message = " ".join(parts[message_index:to_index])
                    # Extract the recipient's name by joining the words after "to"
                    recipient_name = " ".join(parts[to_index + 1:])

                    return message, recipient_name  # Return the extracted message and recipient name
                except Exception as e:
                    print(f"Error parsing message and recipient: {e}")
                    return None, None  # Return None values if parsing fails
            else:
                # Inform the user if the command doesn't follow the expected format
                speak("Command not recognized. Please follow the format 'send [message] to [name]'.")
                return None, None
        except Exception as e:
            # Handle exceptions in speech recognition and inform the user
            print(f"Error in recognition: {e}")
            speak("I can't hear that, sorry!")
            return None, None
