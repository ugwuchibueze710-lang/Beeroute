# BeeRoute Text-to-Speech Engine
# Handles spoken output for Bee (driving assistant)

import pyttsx3


class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 175)  # natural speaking speed
        self.engine.setProperty("volume", 1.0)

    def speak(self, text):
        """
        Convert text to speech and also return it for system use
        """

        if not text:
            return ""

        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            return f"TTS error: {str(e)}"

        return text
