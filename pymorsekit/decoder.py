from .mappings import REVERSE_MORSE_CODE

def decode(morse: str) -> str:
    return "".join(
        REVERSE_MORSE_CODE[code]
        for code in morse.split()
        if code in REVERSE_MORSE_CODE
    )