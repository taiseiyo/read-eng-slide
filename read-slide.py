#!/usr/bin/env python3
from gtts import gTTS
import os
from PIL import Image
import pyocr
import pyocr.builders


def read_name():
    tools = pyocr.get_available_tools()
    tool = tools[0]  # tesseract
    langs = tool.get_available_languages()
    lang = langs[0]  # english

    txt = tool.image_to_string(
        Image.open('./photo.png'),
        lang=lang,
        builder=pyocr.builders.TextBuilder())

    return txt.lower()


def trimming():
    pic = Image.open('./name.png')
    pic.crop((50, 70, 1200, 730)).save('./photo.png', quality=100)


def main():
    trimming()
    text = read_name()
    text = text.replace(">", "").strip()
    gTTS(text=text, lang="en").save("thesis.mp4")
    os.system("mpg321 thesis.mp4")


main()
