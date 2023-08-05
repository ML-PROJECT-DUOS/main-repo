from playsound import playsound as PS
import speech_recognition as s_r
from googletrans import Translator as Trans
from gtts import gTTS as googleTranslatorService
import gtts
import os

lang_set = ['afrikaans', 'af', 'albanian', 'sq',
       'amharic', 'am', 'arabic', 'ar',
       'armenian', 'hy', 'azerbaijani', 'az',
       'basque', 'eu', 'belarusian', 'be',
       'bengali', 'bn', 'bosnian', 'bs', 'bulgarian',
       'bg', 'catalan', 'ca', 'cebuano',
       'ceb', 'chichewa', 'ny', 'chinese (simplified)',
       'zh-cn', 'chinese (traditional)',
       'zh-tw', 'corsican', 'co', 'croatian', 'hr',
       'czech', 'cs', 'danish', 'da', 'dutch',
       'nl', 'english', 'en', 'esperanto', 'eo',
       'estonian', 'et', 'filipino', 'tl', 'finnish',
       'fi', 'french', 'fr', 'frisian', 'fy', 'galician',
       'gl', 'georgian', 'ka', 'german',
       'de', 'greek', 'el', 'gujarati', 'gu',
       'haitian creole', 'ht', 'hausa', 'ha',
       'hawaiian', 'haw', 'hebrew', 'he', 'hindi',
       'hi', 'hmong', 'hmn', 'hungarian',
       'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian',
       'id', 'irish', 'ga', 'italian',
       'it', 'japanese', 'ja', 'javanese', 'jw',
       'kannada', 'kn', 'kazakh', 'kk', 'khmer',
       'km', 'korean', 'ko', 'kurdish (kurmanji)',
       'ku', 'kyrgyz', 'ky', 'lao', 'lo',
       'latin', 'la', 'latvian', 'lv', 'lithuanian',
       'lt', 'luxembourgish', 'lb',
       'macedonian', 'mk', 'malagasy', 'mg', 'malay',
       'ms', 'malayalam', 'ml', 'maltese',
       'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian',
       'mn', 'myanmar (burmese)', 'my',
       'nepali', 'ne', 'norwegian', 'no', 'odia', 'or',
       'pashto', 'ps', 'persian', 'fa',
       'polish', 'pl', 'portuguese', 'pt', 'punjabi',
       'pa', 'romanian', 'ro', 'russian',
       'ru', 'samoan', 'sm', 'scots gaelic', 'gd',
       'serbian', 'sr', 'sesotho', 'st',
       'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si',
       'slovak', 'sk', 'slovenian', 'sl',
       'somali', 'so', 'spanish', 'es', 'sundanese',
       'su', 'swahili', 'sw', 'swedish',
       'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu',
       'te', 'thai', 'th', 'turkish',
       'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur',
       'ug', 'uzbek', 'uz',
       'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
       'yiddish', 'yi', 'yoruba',
       'yo', 'zulu', 'zu']

def takeInput(inp="ta"):
    r1 = s_r.Recognizer()
    with s_r.Microphone() as source:
        print("listening to the voice...")
        r1.pause_threshold = 1
        audio = r1.listen(source)

    try:
        print("Recognizing the voice...")
        print(inp)
        task = r1.recognize_google(audio, language=inp)
        print(f"user said? {task}\n")
    except Exception as ep:
        print("The user is requested to please say that again...")
        return "None"
    return task
def destination_language():
    lang_to_be_converted=input("Please enter the language in which you want to convert the above input \
    : Ex. English, Hindi, German, French etc.")
    return lang_to_be_converted

inpLang = input("Enter language to speak in : ")
task=takeInput(inpLang)
while task=="None":
    task=takeInput()
lang_to_be_converted = destination_language()
while lang_to_be_converted not in lang_set:
    print("The language is not available , pls request some other language")
    print()
    lang_to_be_converted = destination_language()
lang_to_be_converted = lang_set[lang_set.index(lang_to_be_converted) + 1]
translator1 = Trans()
text_to_translate_1 = translator1.translate(task, dest=lang_to_be_converted)
text_converted = text_to_translate_1.text
speak = googleTranslatorService(text=text_converted, lang=lang_to_be_converted, slow=False)
speak.save("captured_voice.mp3")
PS('captured_voice.mp3')
os.remove('captured_voice.mp3')
print(text_converted)
sound = googleTranslatorService(text_converted,lang=lang_to_be_converted)   
sound.save("first.mp3")
