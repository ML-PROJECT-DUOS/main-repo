import gtts
import playsound

print("please enter the text \n"
      "To end recording Press Ctrl+d on Linux/Mac on Crtl+z on Windows")
lines = []
try:
    while True:
        lines.append(input())
except EOFError:
    pass

text = "\n".join(lines)

sound = gtts.gTTS(text, lang="ta")
sound.save("first.mp3")
playsound.playsound("first.mp3")