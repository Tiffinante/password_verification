# Version
version = "Version 1.0"

# Title
window_title = "Tiffinante's Password-Überprüfer"

# List of the most frequently used passwords
passwords = {"123456", "123456789", "12345678", "passw0rd", "passw0rt", "password", "passwort", "1234567",
             "123123", "1234567890", "111111", "abc123", "00000", "123", "abc", "000000123456", "123456789",
             "password", "adobe123", "12345678", "qwerty", "1234567", "111111", "photoshop", "123123",
             "1234567890", "000000", "abc123", "1234", "adobe1", "macromedia", "azerty", "iloveyou", "aaaaaa",
             "654321", "12345", "666666", "sunshine", "123321", "letmein", "monkey", "asdfgh", "password1",
             "shadow", "princess", "dragon", "adobeadobe", "daniel", "computer", "drowssap ", "michael", "121212",
             "charlie", "master", "superman", "qwertyuiop", "112233", "asdfasdf", "jessica", "1q2w3e4r",
             "welcome", "1qaz2wsx", "987654321", "fdsa", "753951", "chocolate", "fuckyou", "soccer", "tigger",
             "asdasd", "thomas", "asdfghjkl", "internet", "michelle", "football", "123qwe", "zxcvbnm",
             "dreamweaver", "7777777", "maggie", "qazwsx", "baseball", "jennifer", "jordan", "abcd1234",
             "trustno1", "buster", "555555", "liverpool", "abc", "whatever", "11111111", "102030", "123123123",
             "andrea", "pepper", "nicole", "killer", "abcdef", "hannah", "test", "alexander", "andrew", "222222",
             "joshua", "freedom", "samsung", "asdfghj", "purple", "ginger", "123654", "matrix", "secret",
             "summer", "1q2w3e", "snoopy1"}

# String with every character that can appear in a password
characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!§$%&/\\()|=?'<>,.;:-_#+*@€{[]}"

# Selection for the drop down menu
options_drop_len = ["35"]
for i in range(50, 10, -5):
    options_drop_len.append(str(i))
