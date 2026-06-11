from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="PyMorseKit",
    version="0.1.0",
    author="fmasterpro27",
    description="A lightweight Python toolkit for encoding, decoding, and working with Morse code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fmasterpro27/PyMorseKit",
    packages=find_packages(),
    python_requires=">=3.8",
    license="Apache-2.0",
)
