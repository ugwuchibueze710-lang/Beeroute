# BeeRoute Speech-to-Text Engine
# Handles voice input for hands-free driving commands

import speech_recognition as sr


class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self):
        """
        Listens for user voice input and converts to text
        """

        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                print("Listening...")

                audio = self.recognizer.listen(source)

            text = self.recognizer.recognize_google(audio)
            return text

        except sr.UnknownValueError:
            return "I didn't catch that."

        except sr.RequestError:
            return "Speech service unavailable."

        except Exception as e:
            return f"STT error: {str(e)}"
