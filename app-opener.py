import os
import tkinter
import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

w = 400
h = 410
app_len = str(w) + "x" + str(h)
app = customtkinter.CTk()
app.geometry(app_len)
app.title("App Opener")
app.wm_attributes("-topmost", 1)
app.resizable(False, False)

def settings():
    os.startfile("pc-settings.html")

def snip():
    os.startfile("snip.html")

def store():
    os.startfile("store.html")

def explorer():
    os.startfile("C:\Windows\explorer.exe")

def notepad():
    os.startfile("C:\Windows\System32\\notepad.exe")

def ctrl():
    os.startfile("C:\Windows\System32\control.exe")

def task():
    os.startfile("C:\Windows\System32\Taskmgr.exe")

def cmd():
    os.startfile("C:\Windows\System32\cmd.exe")

def ins():
    os.startfile("instructions.lnk")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, text="Open apps!", justify=tkinter.LEFT)
label_1.pack(pady=6, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, text="Settings", command=settings)
button_1.pack(pady=6, padx=10)

button_8 = customtkinter.CTkButton(master=frame_1, text="Snip and Sketch", command=snip)
button_8.pack(pady=6, padx=10)

button_9 = customtkinter.CTkButton(master=frame_1, text="MS Store", command=store)
button_9.pack(pady=6, padx=10)

button_2 = customtkinter.CTkButton(master=frame_1, text="Explorer", command=explorer)
button_2.pack(pady=6, padx=10)

button_3 = customtkinter.CTkButton(master=frame_1, text="Notepad", command=notepad)
button_3.pack(pady=6, padx=10)

button_4 = customtkinter.CTkButton(master=frame_1, text="Control Panel", command=ctrl)
button_4.pack(pady=6, padx=10)

button_5 = customtkinter.CTkButton(master=frame_1, text="Task Manager", command=task)
button_5.pack(pady=6, padx=10)

button_6 = customtkinter.CTkButton(master=frame_1, text="Command Prompt", command=cmd)
button_6.pack(pady=6, padx=10)

button_7 = customtkinter.CTkButton(master=frame_1, text="Instructions", command=ins)
button_7.pack(pady=6, padx=10)

app.mainloop()