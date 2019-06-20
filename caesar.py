
def rotate_string(text, rot):
    new_string = ""
    for char in text:
        new_string = new_string + rotate_character(char, rot)
    return new_string

def alphabet_position(letter):
    case_clean = letter.upper()
    return ord(case_clean) - 65

def rotate_character(char, rot):
    if not (char.isalpha()):
        return char
    lower_case = char.islower()
    new_pos = (alphabet_position(char) + (rot % 26)) % 26
    new_char = chr(new_pos+65)
    if lower_case:
        new_char = new_char.lower()
    return new_char

def main():
    message = input("Type a message:\n")
    rotation = int(input("Rotate by:\n"))
    encrypted = rotate_string(message, rotation)
    print(encrypted)

if __name__ == "__main__":
    main()

