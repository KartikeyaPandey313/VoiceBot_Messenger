from AppOpener import open as openApp  # For opening applications (like WhatsApp)
import pyautogui  # For automating keyboard and mouse actions
import time  # For adding delays when needed
from SpeakAndListen import speak  # For making program speak
from SpeakAndListen import listen  # For making program listen

# Set a pause duration between PyAutoGUI commands to make automation smoother
pyautogui.PAUSE = 0.6

if __name__ == "__main__":
    # Greet the user with a friendly message
    speak("Hello sir")

    # Listen for the voice command to extract the message and recipient's name
    message, recipient_name = listen()

    # Ask the user if they want to send the message multiple times
    speak('Do you want me send the message multiple time?')
    # Note: The same listen() function is used even though it expects a specific command format.
    # For more robust behavior, consider creating a separate function for yes/no responses.
    yes_no = input("Y/n: ")

    # If the recognized response contains "yes"
    if 'yes' in yes_no:
        # Ask the user for the number of times to send the message
        speak('How many times?')
        # Use keyboard input for the number of times since speaking numbers reliably is challenging
        times = int(input('How many times: '))

        # Proceed only if both message and recipient_name were successfully extracted
        if message and recipient_name:
            speak(f"Sending the given message to {recipient_name}")

            # 1. Open WhatsApp using the AppOpener package
            openApp('Whatsapp', output=True)

            # Wait a short while to ensure WhatsApp is launched and ready
            time.sleep(1)

            # 2. Search for the recipient by typing the name in the search bar
            pyautogui.typewrite(recipient_name)
            pyautogui.press('down')  # Navigate in the search results
            pyautogui.press('enter')  # Select the recipient from the search results

            # 3. Type the message and send it repeatedly
            # Note: "range(times+1)" sends one extra message; consider using "range(times)" if one message per count is desired
            for i in range(times + 1):
                pyautogui.typewrite(message)
                pyautogui.press('enter')
        else:
            # Inform the user if message or recipient name could not be extracted
            speak("Failed to extract command. Please try again.")
    else:
        # If the response isn't "yes", only send the message once
        if message and recipient_name:
            speak(f"Sending the given message to {recipient_name}")

            # 1. Open WhatsApp using the AppOpener package
            openApp('Whatsapp', output=True)

            # Wait for WhatsApp to load
            time.sleep(1)

            # 2. Search for the recipient
            pyautogui.typewrite(recipient_name)
            pyautogui.press('down')  # Navigate to the recipient in the search results
            pyautogui.press('enter')  # Open the recipient's chat

            # 3. Type the message and send it
            pyautogui.typewrite(message)
            pyautogui.press('enter')
        else:
            # Notify the user if the extraction of command details fails
            speak("Failed to extract command. Please try again.")
