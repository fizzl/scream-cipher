import unicodedata
import sys

# Please provide a PR if you can improve this.
scream_cipher = {
    'A': 'A', 
    'B': 'Ȧ', 
    'C': 'Ą', 
    'D': 'A̱', 
    'E': 'Á', 
    'F': 'A̮',
    'G': 'A̋', 
    'H': 'A̰', 
    'I': 'Ả', 
    'J': 'A̓', 
    'K': 'Ạ', 
    'L': 'Ă',
    'M': 'Ǎ', 
    'N': 'Â', 
    'O': 'Å', # Ruotsalainen O, neat
    'P': 'A̯', 
    'Q': 'A̤', 
    'R': 'Ȃ',
    'S': 'Ã', 
    'T': 'Ā', 
    'U': 'Ä', 
    'V': 'À', 
    'W': 'Ȁ', 
    'X': 'Ẵ', # I can't figure out what this is supposed to be
    'Y': 'A̦', 
    'Z': 'Ⱥ'
}

# Reverse mapping for decoding
reverse_scream_cipher = {v: k for k, v in scream_cipher.items()}

def encode_scream(text):
    text = text.upper()
    encoded_text = ''.join(scream_cipher.get(char, char) for char in text)
    return encoded_text

def decode_scream(text):
    decoded_text = ''.join(reverse_scream_cipher.get(char, char) for char in text)
    return decoded_text

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scream.py [encode|decode] text...")
        sys.exit(1)

    command = sys.argv[1].lower()
    text = ' '.join(sys.argv[2:])

    if command == 'encode':
        print(encode_scream(text))
    elif command == 'decode':
        print(decode_scream(text))
    else:
        print("Invalid command. Use 'encode' or 'decode'")
        sys.exit(1)

