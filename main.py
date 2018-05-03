####################
# HOTWORD DETECTOR #
####################
import snowboydecoder, signal

interrupted = False
sensitivity = 0.5
model = 'guanjia.pmdl'
detector = snowboydecoder.HotwordDetector(model, sensitivity=sensitivity)

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

def listen():
    print("Standby...")
    signal.signal(signal.SIGINT, signal_handler) # capture SIGINT signal, e.g., Ctrl+C
    detector.start(detected_callback=main,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)

####################
#  CORE FUNCTIONS  #
####################
import sys, random, recognizer, tts, time, vlc
from weather import ask_weather
from intent_recognition import IntentClassifier

classifier = IntentClassifier()
features = {'weather': ask_weather}

def play_file():
    p = vlc.MediaPlayer("output.mp3")
    p.play()
    time.sleep(1)
    while p.is_playing():
        time.sleep(1)

def trainAI():
    classifier.train()
    classifier.save("c_classifier.pickle")
    print(classifier.test())
    print('Trained classifier')

def testAI():
    while True:
        text = input("Test utterance: ")
        print(classifier.classify(text))

def loadAI():
    classifier = IntentClassifier.load("c_classifier.pickle")

def main():
    # Turn off hotword detector
    detector.terminate()

    # Ask
    replies = ["是，主人", "有什麼吩咐嗎", "是"]
    tts.speak(random.choice(replies))
    play_file()

    # Listen
    print("Listening...")
    sentence = recognizer.recognize()

    # Processing
    print("Processing...")
    success = sentence[0]
    userSays = " ".join(sentence[1])
    if success:
        confidence = classifier.getProbability(
            userSays, classifier.classify(userSays))
        intention = classifier.classify(userSays)
        print(confidence)

        # FEATURES
        if intention in features and confidence > 0.70: # confidence boundary
            answer = features[intention]()
        # CONVERSATION
        elif confidence > 0.70:             
            response = classifier.response(userSays)
            answer = response
        # NO ANSWER
        else:
            answer = "對不起，我聽不太懂"

        if tts.speak(answer):
            play_file()
    else:
        if tts.speak(userSays):
            play_file()

    # Turn back on hotword detector
    listen()

    # translated = translator.translate(sentence)['message']['result']['translatedText']
    # print('Translation: %s' % translated) #DEBUG

if __name__ == "__main__":
    trainAI()
    # testAI()
    loadAI()

    listen()

