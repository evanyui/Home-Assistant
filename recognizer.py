import speech_recognition as sr

def recognize():
    r = sr.Recognizer()
    try: 
        with sr.Microphone() as source:
            # Set wait time until first speech is 5secs, max time foor speech is 5secs
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        sentence = r.recognize_google(audio, language="cmn-Hant-TW")
        print('You said: %s' % sentence)
        return (True, sentence)
    except sr.RequestError:
        return (False, "網絡好像有點問題")
    except sr.WaitTimeoutError:
        return (False, "怎麼了嗎?")
    except:
        return (False, "不好意思，我沒聽懂")
