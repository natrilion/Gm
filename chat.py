import tkinter as tk
from tkinter import scrolledtext
import g4f

# --- функція відправки повідомлення ---
def send_message():
    user_text = entry.get()
    if not user_text.strip():
        return

    chat.insert(tk.END, "You: " + user_text + "\n")
    entry.delete(0, tk.END)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-4",
            messages=[{
                "role": "user",
                "content": user_text
            }]
        )

        chat.insert(tk.END, "Bot: " + response + "\n\n")

    except Exception as e:
        chat.insert(tk.END, f"Error: {e}\n\n")

    chat.yview(tk.END)


# --- GUI ---
root = tk.Tk()
root.title("Chat Bot")
root.geometry("400x500")

chat = scrolledtext.ScrolledText(root, wrap=tk.WORD)
chat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root)
entry.pack(padx=10, pady=5, fill=tk.X)

send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack(pady=5)

# Enter = відправити
root.bind('<Return>', lambda event: send_message())

root.mainloop()