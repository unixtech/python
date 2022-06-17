import pyttsx3


speaker = pyttsx3.init()

with open('text.txt', 'r') as w:
    text = w.readlines()
    # speaker.say(text)
    speaker.runAndWait()


speaker.save_to_file(text, 'audiobook.mp3')
speaker.runAndWait()
