import tkinter
import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("780x240")
app.title("Instructions")
app.wm_attributes("-topmost", 1)

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

instructions_var = tkinter.StringVar()
instructions_var.set("Press F11 in VSCODE to fullscreen (like in Chrome). Type \"powershell\" in Command Prompt to use powershell.")

def change_fc():
   change_to = str(change.get())
   instructions_var.set(change_to)

label_1 = customtkinter.CTkLabel(master=frame_1, text="Instructions:", justify=tkinter.LEFT)
label_1.pack(pady=12, padx=10)
label_2 = customtkinter.CTkLabel(master=frame_1, textvariable=instructions_var, justify=tkinter.LEFT)
label_2.pack(pady=12, padx=10)

change = customtkinter.CTkEntry(master=frame_1, placeholder_text="Change to ", placeholder_text_color="lightgray")
change.pack(pady=9, padx=9)
button = customtkinter.CTkButton(master=frame_1, text="Change", command=change_fc)
button.pack(pady=9, padx=9)

app.mainloop()