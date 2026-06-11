# PyMorseKit

> A lightweight Python library for encoding and decoding Morse code — simple API, zero dependencies.

[![PyPI version](https://img.shields.io/pypi/v/PyMorseKit.svg)](https://pypi.org/project/PyMorseKit/)
[![Python versions](https://img.shields.io/pypi/pyversions/PyMorseKit.svg)](https://pypi.org/project/PyMorseKit/)
[![License](https://img.shields.io/pypi/l/PyMorseKit.svg)](LICENSE)

---

## Features

- Encode plain text to Morse code
- Decode Morse code back to text
- Supports letters, numbers, and common punctuation
- Lightweight with no external dependencies

---

## Installation

```bash
pip install PyMorseKit
```

---

## Quick Start

```python
from pymorsekit import encode, decode

# Encode text to Morse code
print(encode("SOS"))
# Output: ... --- ...

# Decode Morse code to text
print(decode("... --- ..."))
# Output: SOS
```

---

## API Reference

### `encode(text: str) -> str`

Converts a plain-text string into Morse code. Words are separated by `/` and characters by spaces.

```python
encode("HELLO WORLD")
# .... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

### `decode(morse: str) -> str`

Converts a Morse code string back into plain text. Expects characters separated by spaces and words separated by `/`.

```python
decode(".... . .-.. .-.. --- / .-- --- .-. .-.. -..")
# HELLO WORLD
```

---

## Supported Characters

| Category    | Examples                                                                |
| ----------- | ----------------------------------------------------------------------- |
| Letters     | A–Z (case-insensitive)                                                  |
| Numbers     | 0–9                                                                     |
| Punctuation | `.` `,` `?` `!` `'` `/` `(` `)` `&` `:` `;` `=` `+` `-` `_` `"` `$` `@` |

---

## Contributing

Contributions, bug reports, and feature requests are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a pull request

Please open an [issue](https://github.com/Fmasterpro27/PyMorseKit/issues) before submitting large changes.

---

## Author

Developed and maintained by **JackMa**
GitHub: [@Fmasterpro27](https://github.com/Fmasterpro27)

---

## License

This project is licensed under the [Apache License 2.0](LICENSE).
