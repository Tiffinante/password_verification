import list
import random
import tkinter as tk


def check_password():
    letter_upper = 0
    letter_lower = 0
    letter_digit = 0
    letter_special = 0

    fail_count = 0

    password = text_password.get('1.0', tk.END)
    print('User überprüft: ', password)

    if password.lower() == "penis":
        print("ACHTUNG! Ihr Passwort ist zu kurts!")
        labelpasswordfeedback = tk.Label(master=frame_password_feedback, text="ACHTUNG! Ihr Passwort ist zu kurts!")
        labelpasswordfeedback.pack()
    elif not (" " in password) and password.isprintable():
        print("")
        labelpasswordfeedback = tk.Label(master=frame_password_feedback, text="")
        labelpasswordfeedback.pack()
    else:
        print("Bitte verwenden sie keine leerzeichen und nur zeichen die 'regulär' verwendbar sind")
        labelpasswordfeedback = tk.Label(master=frame_password_feedback, text="Bitte verwenden sie keine "
                                                                              "leerzeichen und nur zeichen die "
                                                                              "'regulär' verwendbar sind")
        labelpasswordfeedback.pack()

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
    labelpasswordfeedback = tk.Label(master=frame_password_feedback, text="Tipps für ihr Passwort:")
    labelpasswordfeedback.pack()

    for i in list.passwords:
        if i in password or i == password:
            fail_count += 1
            print("Verwenden sie ein eigenes Password")
            labelpasswordfeedback = tk.Label(master=frame_password_feedback,
                                             text="Verwenden sie ein eigenes Password")
            labelpasswordfeedback.pack()
            break
    if letter_lower < 2:
        fail_count += 1
        print("Verwenden sie (mehr) kleine Buchstaben")
        labelpasswordfeedback = tk.Label(master=frame_password_feedback,
                                         text="Verwenden sie (mehr) kleine Buchstaben")
        labelpasswordfeedback.pack()
    if letter_upper < 3:
        fail_count += 1
        print("Verwenden sie (mehr) Große Buchstaben")
        labelpasswordfeedback = tk.Label(master=frame_password_feedback, text="Verwenden sie (mehr) Große Buchstaben")
        labelpasswordfeedback.pack()
    if letter_digit < 4:
        fail_count += 1
        print("Verwenden sie (mehr) Zahlen")
        labelpasswordfeedback = tk.Label(master=frame_password_feedback, text="Verwenden sie (mehr) Zahlen")
        labelpasswordfeedback.pack()
    if letter_special < 3:
        fail_count += 1
        print("Verwenden sie (mehr) Sonderzeichen")
        labelpasswordfeedback = tk.Label(master=frame_password_feedback, text="Verwenden sie (mehr) Sonderzeichen")
        labelpasswordfeedback.pack()

    if password.istitle():
        fail_count += 1
        print("Verwenden sie Keine Wortähnlichen buchstaben ketten")
        labelpasswordfeedback = tk.Label(master=frame_password_feedback,
                                         text="Verwenden sie Keine Wortähnlichen buchstaben ketten")
        labelpasswordfeedback.pack()
    if password.isalnum():
        fail_count += 1
        print("Verwenden sie keine reinfolge wie 'abc' oder '123'")
        labelpasswordfeedback = tk.Label(master=frame_password_feedback,
                                         text="Verwenden sie keine reinfolge wie 'abc' oder '123'")
        labelpasswordfeedback.pack()

    if password_len < 10:
        fail_count += 1
        print("Verwenden sie ein längeresw Passwort")
        labelpasswordfeedback = tk.Label(master=frame_password_feedback, text="Verwenden sie ein längeresw Passwort")
        labelpasswordfeedback.pack()

    if fail_count == 0:
        print("Ihr Password erfüllt die Kirterien")
        labelpasswordfeedback = tk.Label(master=frame_password_feedback, text="Ihr Password erfüllt die Kirterien")
        labelpasswordfeedback.pack()

    print("")
    labelpasswordfeedback = tk.Label(master=frame_password_feedback, text='')
    labelpasswordfeedback.pack()
    print('-' * 45)
    labelpasswordfeedback = tk.Label(master=frame_password_feedback, text='-' * 45)
    labelpasswordfeedback.pack()
    print("Sie haben " + str(fail_count) + " mängel im Password")
    labelpasswordfeedback = tk.Label(master=frame_password_feedback,
                                     text="Sie haben " + str(fail_count) + " mängel im Password")
    labelpasswordfeedback.pack()

    if fail_count >= 5:
        print("ACHTUNG! Ihr Passwort ist SEHR Schlecht")
        labelpasswordfeedback = tk.Label(master=frame_password_feedback,
                                         text="ACHTUNG! Ihr Passwort ist SEHR Schlecht")
        labelpasswordfeedback.pack()
    elif fail_count >= 3:
        print("Achtung! Ihr Passwort ist Schwach")
        labelpasswordfeedback = tk.Label(master=frame_password_feedback, text="Achtung! Ihr Passwort ist Schwach")
        labelpasswordfeedback.pack()
    elif fail_count >= 1:
        print("Ihr Passwort ist Sicher")
        labelpasswordfeedback = tk.Label(master=frame_password_feedback, text="Ihr Passwort ist Sicher")
        labelpasswordfeedback.pack()
    elif fail_count == 0:
        print("Ihr Passwort ist SEHR Sicher")
        labelpasswordfeedback = tk.Label(master=frame_password_feedback, text="Ihr Passwort ist SEHR Sicher")
        labelpasswordfeedback.pack()

    print('-' * 45)
    labelpasswordfeedback = tk.Label(master=frame_password_feedback, text='-' * 45)
    labelpasswordfeedback.pack()


def generate_password():
    gen_password = ""
    for i in range(30):
        gen_password += list.characters[random.randrange(len(list.characters))]
    labelgenpassword = tk.Label(master=frame_label_gen_password, text=gen_password)
    labelgenpassword.pack()
    print(gen_password)


if __name__ == '__main__':
    window = tk.Tk()

    frame_top = tk.Frame()
    top_title = tk.Label(master=frame_top, text="Tiffinante's Password-Überprüfer!")
    top_title.pack()

    frame_label_check = tk.Frame()
    label_password_input = tk.Label(master=frame_label_check, text='Bitte geben sie ihr Passwort ein:')
    label_password_input.pack()

    frame_password = tk.Frame()
    text_password = tk.Text(master=frame_password, width=50, height=1)
    text_password.pack()

    frame_button_check = tk.Frame()
    button_check = tk.Button(master=frame_button_check, text='Überprüfen', width=20, height=1,
                             bg='grey', fg='white', command=check_password)
    button_check.pack()

    frame_password_feedback = tk.Frame()
    label_password_feedback = tk.Label(master=frame_password_feedback)
    label_password_feedback.pack()

    frame_label_gen = tk.Frame()
    label_password_gen = tk.Label(master=frame_label_gen, text='\n\nWollen sie ein Passwort Generieren lassen?')
    label_password_gen.pack()

    frame_button_gen = tk.Frame()
    button_gen = tk.Button(master=frame_button_gen, text='Generieren', width=20, height=1,
                           bg='green', fg='white', command=generate_password)
    button_gen.pack()

    frame_label_gen_password = tk.Frame()
    label_gen_password = tk.Label(master=frame_label_gen_password)
    label_gen_password.pack()

    frame_top.pack(padx=80, pady=10)

    frame_label_check.pack(padx=80, pady=0)
    frame_password.pack(padx=80, pady=0)
    frame_button_check.pack(padx=80, pady=30)
    frame_password_feedback.pack(padx=80, pady=0)

    frame_label_gen.pack(padx=80, pady=0)
    frame_button_gen.pack(padx=80, pady=20)
    frame_label_gen_password.pack(padx=80, pady=10)

    window.mainloop()

'''
class ColorCodes:
    BLUE = '\033[94m'
    TURQUOISE = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'  # WHITE
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


letter_upper = 0
letter_lower = 0
letter_digit = 0
letter_special = 0

fail_count = 0

while True:
    password = input("\nIhr Passwort:")
    if password.lower() == "penis":
        print(ColorCodes.RED + "ACHTUNG! Ihr Passwort ist zu kurts!" + ColorCodes.RESET)
    elif not (" " in password) and password.isprintable():
        print("")
        break
    else:
        print("Bitte verwenden sie keine leerzeichen und nur zeichen die 'regulär' verwendbar sind")
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

print(ColorCodes.UNDERLINE + "Tipps für ihr Passwort:" + ColorCodes.RESET)

for i in list.passwords:
    if i in password or i == password:
        fail_count += 1
        print("Verwenden sie ein eigenes Password")
        break
if letter_lower < 2:
    fail_count += 1
    print("Verwenden sie (mehr) kleine Buchstaben")
if letter_upper < 3:
    fail_count += 1
    print("Verwenden sie (mehr) Große Buchstaben")
if letter_digit < 4:
    fail_count += 1
    print("Verwenden sie (mehr) Zahlen")
if letter_special < 3:
    fail_count += 1
    print("Verwenden sie (mehr) Sonderzeichen")

if password.istitle():
    fail_count += 1
    print("Verwenden sie Keine Wortähnlichen buchstaben ketten")
if password.isalnum():
    fail_count += 1
    print("Verwenden sie keine reinfolge wie 'abc' oder '123'")

if password_len < 10:
    fail_count += 1
    print("Verwenden sie ein längeresw Passwort")

if fail_count == 0:
    print("Ihr Password erfüllt die Kirterien")

print("")
print('-' * 45)
print(ColorCodes.TURQUOISE + "Sie haben " + ColorCodes.BLUE + ColorCodes.BOLD + ColorCodes.UNDERLINE + str(
    fail_count) + ColorCodes.RESET + ColorCodes.TURQUOISE +
      " mängel im Password" + ColorCodes.RESET)

if fail_count >= 5:
    print(ColorCodes.RED + "ACHTUNG! Ihr Passwort ist SEHR Schlecht" + ColorCodes.RESET)
elif fail_count >= 3:
    print(ColorCodes.YELLOW + "Achtung! Ihr Passwort ist Schwach" + ColorCodes.RESET)
elif fail_count >= 1:
    print(ColorCodes.GREEN + "Ihr Passwort ist Sicher" + ColorCodes.RESET)
elif fail_count == 0:
    print(ColorCodes.GREEN + "Ihr Passwort ist SEHR Sicher" + ColorCodes.RESET)

print('-' * 45)

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!§$%&/()|=?'<>,.;:-_#+*@€{[]}"
password = ""
for i in range(30):
    password = password + alphabet[random.randrange(len(alphabet))]
print("\nEin Password vorschlag von uns für sie:")
print(ColorCodes.BLUE + password + ColorCodes.RESET)
'''
