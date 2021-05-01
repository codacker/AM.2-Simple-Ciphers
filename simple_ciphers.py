
import sys

DICTIONARY_FILEPATH = "some_words.txt"

def main():
    if len(sys.argv) == 1:
        print("Usage:")
        print("simple_ciphers.py encode (input filepath) [optional rot val] [optional rot shift]")
        print("simple_ciphers.py decode (input filepath)")
    else:
        mode = sys.argv[1]
        input_filepath = sys.argv[2]
        fin = open(input_filepath,"r")
        input_text = fin.read()
        fin.close()
        
        if mode == "encode":
            rot_val = 3
            if len(sys.argv) > 3:
                rot_val = int(sys.argv[3])
            rot_shift = 0
            if len(sys.argv) > 4:
                rot_shift = int(sys.argv[4])
            print(cipher(input_text,rot_val,rot_shift))
        elif mode == "decode":
            print(decipher(input_text))

def cipher(input_text,rot_val,rot_shift):
     #Generate the related plain text 
    result = ''
    rot_val = (rot_val + rot_shift) % 26
    for char in input_text:
        if char.isalpha():
            result += rotate_character(rot_val, char)
        else:
            result += char
    return result

def decipher(input_text):
    #Set two loops and decipher the words within the range of 0-25 
    words = read_dictionary(DICTIONARY_FILEPATH)
    result = 0
    cur_val = 0
    for rot_val in range(0, 26):
        for rot_shift in range(0, 26):
            dec_val = cipher(input_text, rot_val, rot_shift)
            cur_val = grade_message(dec_val, words)
            if cur_val > result:
                result = cur_val
    return result

def rotate_character(the_character,rot_val):
    #Rotate the values and loop around the range of A-Z & a-z
    result = ""
    # % by 26 in-order to rotate between 0-25
    if the_character.isupper():
        result += chr((ord(the_character) + rot_val - 65) % 26 + 65)
    else:
        result += chr((ord(the_character) + rot_val - 97) % 26 + 97)
    return result
    
def read_dictionary(filepath):
    #Read the file and drop them into a set which will then return the set
    words = set()
    with open(filepath, 'r') as file:
    # File closes after completion of loop
        for line in file:
            words.add(str(line).replace('\n', ''))
    return words


def grade_message(plaintext,known_words):
    #reads through the plain text and marks that which is case sensitive 
    #...is present in known words which would then return that number
    match = 0 
    for word in plaintext.split(''):
        if word.upper() in known_words:
            match += 1
    return match

if __name__ == "__main__":
    main()
    
