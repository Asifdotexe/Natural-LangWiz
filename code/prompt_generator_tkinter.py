import tkinter as tk
from tkinter import scrolledtext, font
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv('API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get a response from Gemini API
def get_response(user_input):
    try:
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Function to handle user input and update the chat window
def send_message():
    user_input = user_entry.get()
    if user_input.strip() != "":
        # Display user message in the chat window
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "You: " + user_input + "\n", 'user')
        
        # Get response from the model
        response = get_response(user_input)
        chat_window.insert(tk.END, "Gemini: " + response + "\n", 'bot')
        chat_window.config(state=tk.DISABLED)
        
        # Clear the input field
        user_entry.delete(0, tk.END)

        # Auto-scroll to the bottom of the chat
        chat_window.yview(tk.END)

# Set up the main Tkinter window
root = tk.Tk()
root.title("Gemini Chat Interface")
root.geometry("600x600")
root.config(bg='#282c34')

# Set custom fonts
user_font = font.Font(family="Helvetica", size=10, weight='bold')
bot_font = font.Font(family="Helvetica", size=10)
input_font = font.Font(family="Helvetica", size=12)

# Chat display window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, bg="#f0f0f0", fg="#000", padx=10, pady=10)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Add tags for styling user and bot messages
chat_window.tag_config('user', foreground="#008080", font=user_font)  # Teal color for user messages
chat_window.tag_config('bot', foreground="#0000ff", font=bot_font)    # Blue color for bot messages

# User input field
user_entry = tk.Entry(root, font=input_font, width=80, bg="#e0e0e0", fg="#000", bd=2)
user_entry.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.X, expand=True)

# Send button to submit the user input
send_button = tk.Button(root, text="Send", command=send_message, bg="#61afef", fg="white", font=input_font, relief="raised")
send_button.pack(padx=10, pady=10, side=tk.RIGHT)

# Run the Tkinter event loop
root.mainloop()