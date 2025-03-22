# VoiceBot_Messenger-
VoiceBot Messenger is a Python-based tool that lets you send WhatsApp messages using voice commands. It integrates speech recognition, text-to-speech, and GUI automation for hands-free messaging. Users can simply say commands like "send [message] to [recipient]," enabling efficient communication. The script listens for a command of the form:

It then opens WhatsApp, searches for the recipient, and sends the message. An optional feature allows you to send the message multiple times based on your confirmation.

## Features

- **Text-to-Speech:** Utilizes `pyttsx3` (using the SAPI5 engine) for verbal feedback.
- **Speech Recognition:** Uses the `SpeechRecognition` module with the Google Web Speech API.
- **Voice Command Parsing:** Extracts the message and recipient using keywords.
- **GUI Automation:** Automates WhatsApp interactions using `pyautogui` and `AppOpener`.
- **User Interaction:** Supports sending messages repeatedly if desired.

## Flow Chart

The following flow chart outlines the script's process:

       +--------------------------+
       |   Start & Greet User     |
       +-----------+--------------+
                   |
                   v
       +--------------------------------------------+
       | Listen for Command ("send [message] to [name]")  |
       +-----------+--------------+
                   |
                   v
       +--------------------------+
       | Successful Extraction?   |
       +-----+----------+---------+
             |          |
            Yes         No
             |          |
             v          v
      +---------------------+   +----------------------------------+
      | Ask: "Send message  |   | Speak: "Failed to extract command.  |
      | multiple?"          |   | Please try again."                |
      +--------+------------+   +----------------------------------+
               |
               v
         +-------------+
         | Listen for  |
         | Yes/No      |
         +------+------+ 
                |
          +-----+-----+
         Yes           No
          |             |
          v             v
  
## Installation

1. **Clone the repository or download the code.**

2. **Install dependencies.** Run the following command to install the required Python packages:

   ```bash
   pip install -r Requirements.txt

---

## License

This project is licensed under the [MIT License](LICENSE).

### requirements.txt

```txt
pyttsx3
SpeechRecognition
AppOpener
pyautogui
