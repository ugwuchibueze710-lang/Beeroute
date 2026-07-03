# BeeRoute Speech to Text (placeholder system)

class SpeechToText:
    def __init__(self):
        self.active = True

    def listen(self):
        # Placeholder for future microphone input system
        return "Listening... (voice system not implemented yet)"

    def transcribe(self, audio_input):
        return f"Transcribed text: {audio_input}"


if __name__ == "__main__":
    stt = SpeechToText()
    print(stt.listen())
    print(stt.transcribe("test audio"))
