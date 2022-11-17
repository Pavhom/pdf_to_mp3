from gtts import gTTS
from PyPDF2 import PdfReader
import os


def pdf_to_mp3(file, language):
    if os.path.isfile(file) and os.path.splitext(file)[1] == '.pdf':
        print("I'm working, just wait...")
        pdf_reader = PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()

        text = text.replace('\n', '')

        voice = gTTS(text, lang=language)
        voice.save(f'{os.path.splitext(file)[0]}.mp3')
        print('Done!')
    else:
        print("Check the file name, extension and the presence of the file itself in the folder")


def main():
    print('Hey!')
    file = input('Enter the path to your pdf file: ')
    language = input('Enter your file language, for example "en": ')
    pdf_to_mp3(file, language)


if __name__ == '__main__':
    main()
