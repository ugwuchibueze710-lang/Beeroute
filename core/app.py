# BeeRoute Core System Controller
# Central brain loop of the system

from ai.personality import BeePersonality
from ai.brain import Brain
from navigation.router import Router
from maps.map_engine import MapEngine
from voice.text_to_speech import TextToSpeech


class BeeRouteCore:
    def __init__(self):
        self.bee = BeePersonality()
        self.brain = Brain()
        self.router = Router()
        self.maps = MapEngine()
        self.tts = TextToSpeech()

    def process_command(self, user_input):
        """
        Pipeline:
        User → Brain → Bee → Output
        """

        # 1. Brain interprets user input
        raw_response = self.brain.respond(user_input)

        text = raw_response.get("text", "I’m not sure yet.")
        distance = raw_response.get("distance", None)
        eta = raw_response.get("eta", None)

        # 2. Bee humanizes response
        bee_text = self.bee.navigation_speak(text)

        final_output = self.bee.format_navigation(
            bee_text,
            distance=distance,
            eta=eta
        )

        # 3. Voice output (only final text)
        spoken = self.tts.speak(final_output)

        return {
            "ai": final_output,
            "route": raw_response.get("route", "no route data yet"),
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
