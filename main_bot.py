import pyautogui
import time
import pyperclip
from openai import OpenAI

# OpenAI client setup (Make sure your API key is valid and not expired)
client = OpenAI(api_key="<YOUR_OPEN_API_KEY")

def is_last_message_from_sender(chat_log, sender_name="Nishant Bhai"):
    """Check if the last message in the chat is from a specific sender."""
    messages = chat_log.strip().split("/2024] ")[-1]
    return sender_name in messages

# Disable fail-safe (Use with caution)
pyautogui.FAILSAFE = False

# Step 1: Click on Chrome icon
pyautogui.click(1639, 1412)
time.sleep(3)  # Ensure Chrome opens

while True:
    try:
        time.sleep(5)  # Wait before capturing text

        # Step 2: Select text
        pyautogui.moveTo(1340, 940)  # Move to start position
        pyautogui.dragTo(963, 135, duration=2.0, button='left')  # Drag to select

        # Step 3: Copy text
        pyautogui.hotkey('ctrl', 'c')  
        time.sleep(1)  # Wait for clipboard update
        pyautogui.hotkey('ctrl', 'c')  # Double copy (ensures text is copied)
        time.sleep(2)  # Extra wait

        # Step 4: Retrieve copied text
        chat_history = pyperclip.paste()
        
        if not chat_history.strip():
            print("No text copied! Retrying...")
            continue  # Restart loop if no text is copied
        
        print(f"Copied Chat: {chat_history}")  # Verify copied text

        # Step 5: Click elsewhere (if needed)
        pyautogui.click(1994, 281)

    except pyautogui.FailSafeException:
        print("Fail-safe triggered! Exiting loop.")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        break

    # Step 6: Check if the last message is from "Nishant Bhai"
    if is_last_message_from_sender(chat_history):
        print("Detected message from Nishant Bhai. Generating response...")

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a person named Vedant who speaks Hindi and English, and you are from Mumbai, India. You are a university student at Somaiya. You analyze and respond like Vedant.Output should be the next chat response (text message only)"},
                {"role": "user", "content": chat_history}
            ]
        )

        # Step 7: Extract OpenAI response
        response = completion.choices[0].message.content
        print(f"AI Response: {response}")

        # Step 8: Copy response to clipboard
        pyperclip.copy(response)

        # Step 9: Click on the message box
        pyautogui.click(1129, 986)
        time.sleep(1)  # Ensure focus on input box

        # Step 10: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  

        # Step 11: Press Enter to send message
        pyautogui.press('enter')

        print("Message sent successfully!")

    else:
        print("Last message is NOT from Nishant Bhai. Skipping response.")

