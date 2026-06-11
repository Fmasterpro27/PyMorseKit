from .mappings import MORSE_CODE

def encode(text: str) -> str:
    return " ".join(
        MORSE_CODE[char]
        for char in text.upper()
        if char in MORSE_CODE
    )