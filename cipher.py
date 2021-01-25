def caeser_cipher(string, shift):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " ", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8",
                "9", "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}",
                "|", ";", ":", "'", '"', ",", "<", ">", "/", "?"]
    new_string = ""
    shift = shift % 26
    special_chars = [" ", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "`", "~", "!", "@", "#", "$", "%", "^",
                     "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", '"', ",", "<", ">",
                     "/", "?"]
    for letter in string:
        for comp in alphabet:
            if comp == letter:
                if comp in special_chars:
                    new_string += special_chars[special_chars.index(comp)]
                else:
                    caps = 0
                    if letter == letter.upper():
                        caps = 26
                    add = alphabet[(alphabet.index(comp) + shift) % 26 + caps]
                    new_string += add
    return new_string


def decode_without_shift(string):
    import re
    short_string = re.split('[,./<>?;:"\'\[\]|{}`~!@#%&*-=_+\s]', string)[0]
    short_string = re.sub("", "", short_string)
    words = open("words.txt", "r", encoding='utf-8')
    outcomes = []
    for i in range(27):
        outcomes.append(caeser_cipher(short_string, -i).lower())
    new_words = []
    for word in words:
        word = word.rstrip("\n").lower()
        new_words.append(word)
    # print(new_words)
    for outcome in outcomes:
        for new_word in new_words:
            if new_word == outcome:
                shift = outcomes.index(outcome)
                return {"text": caeser_cipher(string, -shift), "shift": shift}
