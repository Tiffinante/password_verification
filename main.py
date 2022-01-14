import random
import tkinter as tk
import tkinter.ttk as ttk

import STATICS


def check_password():
    text = ""

    letter_upper = 0
    letter_lower = 0
    letter_digit = 0
    letter_special = 0

    fail_count = 0

    password = entry_password.get()
    print('\nUser überprüft:' + password)

    if password.lower() == "penis":
        print("ACHTUNG! Ihr Passwort ist zu kurts!")
        label_password_status.config(text="Ihr Passwort ist zu kurts!\n", fg="red")
        return None
    elif password == "":
        print("Bitte geben Sie ein Password ein!")
        label_password_status.config(text="Bitte geben Sie ein Password ein!\n", fg="red")
        return None
    elif not (" " in password) or password.isprintable():
        print("Password wird überprüft\n")
    else:
        print("Bitte verwenden sie keine leerzeichen und nur zeichen die 'regulär' verwendbar sind")
        label_password_status.config(
            text="Bitte verwenden sie keine leerzeichen und nur zeichen die 'regulär' verwendbar sind\n", fg="red")
        return None

    for letter in password:
        if letter.isdigit():
            letter_digit += 1
        elif letter.isupper():
            letter_upper += 1
        elif letter.islower():
            letter_lower += 1
        else:
            letter_special += 1

    password_len = len(password)

    print("Tipps für ihr Passwort:")
    text += "\nTipps für ihr Passwort:\n"

    for i in STATICS.passwords:
        if i in password or i == password:
            fail_count += 1
            print("Verwenden sie ein eigenes Password")
            text += "Verwenden sie ein eigenes Password\n"
            break
    if letter_lower < 2:
        fail_count += 1
        print("Verwenden sie (mehr) kleine Buchstaben")
        text += "Verwenden sie (mehr) kleine Buchstaben\n"
    if letter_upper < 3:
        fail_count += 1
        print("Verwenden sie (mehr) Große Buchstaben")
        text += "Verwenden sie (mehr) Große Buchstaben\n"
    if letter_digit < 4:
        fail_count += 1
        print("Verwenden sie (mehr) Zahlen")
        text += "Verwenden sie (mehr) Zahlen\n"
    if letter_special < 3:
        fail_count += 1
        print("Verwenden sie (mehr) Sonderzeichen")
        text += "Verwenden sie (mehr) Sonderzeichen\n"
    if password.istitle():
        fail_count += 1
        print("Verwenden sie Keine Wortähnlichen buchstaben ketten")
        text += "Verwenden sie Keine Wortähnlichen buchstaben ketten\n"
    if password.isalnum():
        fail_count += 1
        print("Verwenden sie keine reinfolge wie 'abc' oder '123'")
        text += "Verwenden sie keine reinfolge wie 'abc' oder '123'\n"

    if password_len < 10:
        fail_count += 1
        print("Verwenden sie ein längeresw Passwort")
        text += "Verwenden sie ein längeresw Passwort\n"

    if fail_count == 0:
        print("Ihr Password erfüllt die Kirterien")
        text += "Ihr Password erfüllt die Kirterien\n"

    label_password_tipps.config(text=text)
    text, fg = "", ""

    print("")
    print('-' * 45)
    text += ("-" * 45) + "\n"

    if fail_count >= 5:
        print("ACHTUNG! Ihr Passwort ist SEHR Schlecht")
        text += "ACHTUNG! Ihr Passwort ist SEHR Schlecht\n"
        fg = 'red'
    elif fail_count >= 3:
        print("Achtung! Ihr Passwort ist Schwach")
        text += "Achtung! Ihr Passwort ist Schwach\n"
        fg = 'orange'
    elif fail_count >= 1:
        print("Ihr Passwort ist Sicher")
        text += "Ihr Passwort ist Sicher\n"
        fg = 'green'
    elif fail_count == 0:
        print("Ihr Passwort ist SEHR Sicher")
        text += "Ihr Passwort ist SEHR Sicher\n"
        fg = 'green'

    print('-' * 45)
    text += ("-" * 45) + "\n\n\n"

    label_password_status.config(text=text, fg=fg)


def generate_password():
    gen_password = ""
    for i in range(int(user_len_password.get())):
        gen_password += STATICS.characters[random.randrange(len(STATICS.characters))]
    label_gen_password.config(text=gen_password, fg="green")
    print("\nUser genneriert:\n" + str(gen_password))


def show():
    entry_password.configure(show='')
    check_hide_password.configure(command=hide, text='Verberge Passwort')


def hide():
    entry_password.configure(show='*')
    check_hide_password.configure(command=show, text='Zeige Passwort')


if __name__ == '__main__':
    window = tk.Tk()

    # window settings
    window.iconbitmap("images/password-24px.ico")
    window.title(STATICS.window_title)
    window.geometry('400x550')
    window.minsize(width=400, height=550)
    window.resizable(width=False, height=False)

    # build widgets
    # Description for the Entry
    frame_label_check = tk.Frame()
    label_password_input = tk.Label(master=frame_label_check, text='Bitte geben sie ein Passwort ein:')
    label_password_input.pack()

    # Text input
    frame_password = tk.Frame()
    entry_password = ttk.Entry(master=frame_password, show="*")
    entry_password.pack()

    check_hide_password = ttk.Checkbutton(master=frame_password, text='Zeige Passwort', command=show)
    check_hide_password.pack()

    # password feedback
    frame_password_feedback = tk.Frame()
    label_password_tipps = tk.Label(master=frame_password_feedback)
    label_password_tipps.pack()

    label_password_status = tk.Label(master=frame_password_feedback)
    label_password_status.pack()

    # Button to start verification
    frame_button_check = tk.Frame()
    button_check = ttk.Button(master=frame_button_check, text='Überprüfen', command=check_password)
    button_check.pack()

    # Description for the Generate button
    frame_label_gen = tk.Frame()
    label_password_gen = tk.Label(master=frame_label_gen, text='Generieren sie ein Passwort mit ')
    label_password_gen.grid(column=0, row=0)
    # Drop-Down Menu
    user_len_password = tk.StringVar()
    drop_len = ttk.OptionMenu(frame_label_gen, user_len_password, *STATICS.options_drop_len)
    drop_len.grid(column=1, row=0)
    # end of sentence
    label_password_gen = tk.Label(master=frame_label_gen, text='stellen.')
    label_password_gen.grid(column=2, row=0)

    # Button Generated
    frame_button_gen = tk.Frame()
    button_gen = ttk.Button(master=frame_button_gen, text='Generieren', command=generate_password)
    button_gen.pack()

    # Generated password
    frame_label_gen_password = tk.Frame()
    label_gen_password = tk.Label(master=frame_label_gen_password)
    label_gen_password.pack()

    # Copyright line at the bottom
    frame_copyright = tk.Frame()
    copyright_line = tk.Label(master=frame_copyright, text="© 2022 Tiffinante" + " - " + STATICS.version)
    copyright_line.pack(fill="x")

    # place widgets in window
    # Check password
    frame_label_check.pack(padx=0, pady=0)
    frame_password.pack(padx=0, pady=0)
    entry_password.configure(width=30)
    frame_button_check.pack(padx=0, pady=10)
    frame_password_feedback.pack(padx=0, pady=0)

    # Generate password
    frame_label_gen.pack(padx=0, pady=0)
    frame_button_gen.pack(padx=0, pady=10)
    frame_label_gen_password.pack(padx=0, pady=25)

    frame_copyright.pack(side="bottom", fill="x")

    window.mainloop()
