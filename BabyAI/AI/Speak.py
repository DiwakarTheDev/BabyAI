import pyttsx3

def Say(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    engine.setProperty('rate',140)
    print("    ")
    print(f"A.i.:- {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("    ")