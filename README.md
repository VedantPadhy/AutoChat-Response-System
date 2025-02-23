# Automated Chat Response System

This project demonstrates how to use Python libraries to automate chat responses. The script utilizes pyautogui for GUI automation, pyperclip for clipboard management, and OpenAI's API to generate AI responses.

## Requirements

- Python 3.x
- `pyautogui`
- `time`
- `pyperclip`
- `openai`

## Installation

To install the required libraries, use the following commands:

```bash
pip install pyautogui
pip install pyperclip
pip install openai
Setup
Before running the project, ensure you have the following:

A valid OpenAI API key.

Replace the placeholder in the code with your actual key.

Usage
Run the script using the following command:

bash
python <script_name>.py
Code Overview
API Initialization: Initializes the OpenAI client with the provided API key.

GUI Automation: Uses pyautogui to interact with the Chrome browser and capture chat messages.

Clipboard Management: Uses pyperclip to copy and paste chat messages.

AI Response Generation: Uses OpenAI's GPT-3.5-turbo model to generate intelligent responses based on chat history.

Message Sending: Automates the process of sending AI-generated responses.

Steps
Click on Chrome Icon: Opens the Chrome browser.

Select Text: Selects chat messages using GUI automation.

Copy Text: Copies the selected text to the clipboard.

Retrieve Copied Text: Retrieves the copied text from the clipboard.

Check Sender: Checks if the last message is from a specific sender (e.g., "Nishant Bhai").

Generate AI Response: Uses OpenAI's API to generate a response if the sender matches.

Copy Response: Copies the AI response to the clipboard.

Send Message: Pastes and sends the response in the chat.

Troubleshooting
Ensure the OpenAI API key is valid and not expired.

Ensure the Chrome browser is open and accessible.

Ensure the coordinates used in pyautogui commands match your screen setup.

Handle exceptions and fail-safe mechanisms as needed.

Acknowledgements
This project is built using various Python libraries and OpenAI's API.

Happy Coding!
