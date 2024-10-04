from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
import pyttsx3
from gtts import gTTS
import tempfile
from playsound import playsound

root = Tk()
root.title("Language Translator")
root.geometry("1500x400")

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)

def translate_now():
    translator = Translator()
    source_lang = lang1[combo1.current()]
    dest_lang = lang1[combo2.current()]
    input_text = text1.get("1.0", "end-1c")

    if input_text.strip() == "":
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return

    translation = translator.translate(input_text, src=source_lang, dest=dest_lang)
    text2.delete("1.0", "end")
    text2.insert("1.0", translation.text)

def listen_text_gtts(text_widget, lang='hi'):
    text_to_speak = text_widget.get("1.0", "end-1c")
    tts = gTTS(text=text_to_speak, lang=lang)
    
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=True) as tmp:
        tmp_filename = f"{tmp.name}.mp3"
        tts.save(tmp_filename)
        playsound(tmp_filename)

def listen_text(text_widget):
    text_to_speak = text_widget.get("1.0", "end-1c")
    
    # Using pyttsx3
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    hindi_voice_found = False
    
    for voice in voices:
        if 'Hindi' in voice.languages:
            engine.setProperty('voice', voice.id)
            hindi_voice_found = True
            break
    
    if hindi_voice_found:
        engine.say(text_to_speak)
        engine.runAndWait()
    else:
        # Use gTTS if Hindi voice is not found
        listen_text_gtts(text_widget)

def listen_text1():
    listen_text(text1)

def listen_text2():
    listen_text(text2)

# Icon
image_icon = PhotoImage(file="google.png")
root.iconphoto(False, image_icon)

# Arrow
arrow_image = PhotoImage(file="arrow.png")
image_label = Label(root, image=arrow_image)
image_label.place(x=460, y=50)

# Language options
language = LANGUAGES
languageV = list(language.values())
lang1 = list(language.keys())

combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="readonly")
combo1.place(x=110, y=20)
combo1.set("ENGLISH")

label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Listen Button for text1
Listen = Button(root, text="Listen", font="Roboto 15 bold italic", activebackground="purple", cursor="hand2", bd=5, bg="red", fg="white", command=listen_text1)
Listen.place(x=150, y=345)

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="readonly")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="SELECT LANGUAGE", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=720, y=50)

f1 = Frame(root, bg="Black", bd=5)
f1.place(x=720, y=118, width=440, height=210)

text2 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Listen Button for text2
Listen1 = Button(root, text="Listen", font="Roboto 15 bold italic", activebackground="purple", cursor="hand2", bd=5, bg="red", fg="white", command=listen_text2)
Listen1.place(x=870, y=345)

# Translate Button
translate_button = Button(root, text="Translate", font="Roboto 15 bold italic", activebackground="purple", cursor="hand2", bd=5, bg="red", fg="white", command=translate_now)
translate_button.place(x=510, y=290)

label_change()

root.configure(bg="white")
root.mainloop()
