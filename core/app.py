# BeeRoute Core System Controller (FULL VOICE INTEGRATION)

from ai.personality import BeePersonality
from ai.brain import Brain
from navigation.router import Router
from maps.map_engine import MapEngine
from voice.speech_to_text import SpeechToText
from voice.text_to_speech import TextToSpeech


class BeeRouteCore:
    def __init__(self):
        self.bee = BeePersonality()
        self.brain = Brain()
        self.router = Router()
        self.maps = MapEngine()
        self.stt = SpeechToText()
        self.tts = TextToSpeech()

    def process_command(self, user_input):
        """
        Full pipeline:
        Voice/Text → Brain → Bee → Route → Voice Output
        """

        # 1. AI brain response
        ai_response = self.brain.respond(user_input)

        text = ai_response.get("text", "I’m not sure yet.")
        distance = ai_response.get("distance", None)
        eta = ai_response.get("eta", None)

        # 2. Bee humanization
        bee_text = self.bee.navigation_speak(text)

        final_output = self.bee.format_navigation(
            bee_text,
            distance=distance,
            eta=eta
        )

        # 3. Speak output
        spoken = self.tts.speak(final_output)

        return {
            "ai": final_output,
            "route": ai_response.get("route", "no route yet"),
            "voice": spoken
        }

    def voice_loop(self):
        """
        Hands-free driving mode (continuous listening loop)
        """

        print("BeeRoute Voice Mode Active 🐝")

        while True:
            user_input = self.stt.listen()

            if user_input.lower() in ["exit", "quit", "stop"]:
                print("Voice mode shutting down...")
                break

            result = self.process_command(user_input)

            print("\nAI:", result["ai"])
            print("\n----------------------\n")


if __name__ == "__main__":
    app = BeeRouteCore()

    print("BeeRoute Core Online 🐝")
    print("Type or say 'voice' to start voice mode")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            break

        if user_input.lower() == "voice":
            app.voice_loop()
            continue

        result = app.process_command(user_input)

        print("\nAI:", result["ai"])
        print("\nROUTE:", result["route"])
        print("\nVOICE:", result["voice"])
        print("\n----------------------\n")
