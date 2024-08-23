import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import scrolledtext, messagebox
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)

# Define a function to send the prompt to Google Generative AI and display the response
def get_ai_response():
    prompt = prompt_entry.get()
    if not prompt.strip():
        messagebox.showwarning("Input Error", "Please enter a prompt.")
        return
    
    try:
        # Send the prompt to Google Generative AI and get the response
        response = genai.generate_text(prompt=prompt)
        response_text = response.result  # Get the generated text from the response
    except Exception as e:
        response_text = f"Error: {str(e)}"
    
    # Display the response in the text area
    response_area.config(state=tk.NORMAL)
    response_area.delete(1.0, tk.END)
    response_area.insert(tk.END, response_text)
    response_area.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Google Generative AI Interface")
root.geometry("500x400")

# Add a label and entry widget for the prompt
tk.Label(root, text="Enter your prompt:").pack(pady=5)
prompt_entry = tk.Entry(root, width=50)
prompt_entry.pack(pady=5)

# Add a button to send the prompt to the AI
submit_button = tk.Button(root, text="Generate", command=get_ai_response)
submit_button.pack(pady=10)

# Add a scrolled text area to display the response
response_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, height=15)
response_area.pack(pady=10, fill=tk.BOTH, expand=True)

# Start the Tkinter event loop
root.mainloop()