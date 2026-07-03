# BeeRoute Core System Controller

from ai.brain import Brain
from navigation.router import Router
from maps.map_engine import MapEngine
from voice.speech_to_text import SpeechToText
from voice.text_to_speech import TextToSpeech


class BeeRouteCore:
    def __init__(self):
        self.ai = Brain()
        self.router = Router()
        self.maps = MapEngine()
        self.stt = SpeechToText()
        self.tts = TextToSpeech()

    def process_command(self, user_input):
        # AI interprets command
        ai_response = self.ai.respond(user_input)

        # Simple routing demo (placeholder logic)
        route = self.router.calculate_route("Current Location", "Destination")

        # Voice output
        spoken = self.tts.speak(ai_response)

        return {
            "ai": ai_response,
            "route": route,
            "voice": spoken
        }


if __name__ == "__main__":
    app = BeeRouteCore()

    print("BeeRoute Core Online 🐝")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            break

        result = app.process_command(user_input)

        print("\nAI:", result["ai"])
        print("\nROUTE:", result["route"])
        print("\nVOICE:", result["voice"])
        print("\n----------------------\n")
