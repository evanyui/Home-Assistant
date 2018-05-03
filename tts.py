from gtts import gTTS

def speak(s): 
    try:
        tts = gTTS(text = s, lang = 'zh-tw')
        tts.save("output.mp3") 
        return True
    except:
        return False 
