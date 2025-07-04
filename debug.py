import tkinter as tk

def echo_message():
    userInput = input_field.get
    if userInput != "":
        message_label.config(text="You typed: " + userInput)
    else:
        message_label.config(text="Please type something")

windows = tk.Tk()
windows.title("Echo app")
windows.geometry("300x200")

input_field = tk.Entry(windows, width=30)
input_field.pack(pady=10)

echo_button = tk.Button(text="Echo", command=echo_message)
echo_button.pack()


message_label = tk.Label(windows, text="")
message_label.pack()

windows.mainloop()
