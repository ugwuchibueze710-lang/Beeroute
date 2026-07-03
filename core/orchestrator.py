from ai.brain import Brain
from ai.personality import BeePersonality
from navigation.router import Router
from maps.map_engine import MapEngine
from voice.text_to_speech import TextToSpeech


class BeeOrchestrator:
    def __init__(self):
        self.brain = Brain()
        self.bee = BeePersonality()
        self.router = Router()
        self.map = MapEngine()
        self.tts = TextToSpeech()

        self.active_route = None

    def parse_intent(self, text):
        text = text.lower()
        keywords = ["go to", "navigate", "take me", "drive to", "route to"]
        return "navigation" if any(k in text for k in keywords) else "chat"

    def handle(self, user_input):
        intent = self.parse_intent(user_input)

        # ---------------- NAVIGATION ----------------
        if intent == "navigation":
            start = self.map.location or "A"
            destination = "B"

            self.active_route = self.router.calculate_route(start, destination)

            steps = self.active_route.get("steps", [])

            return {
                "type": "navigation",
                "bee": self.bee.navigation_speak("Navigation started."),
                "steps": steps,
                "raw": self.active_route
            }

        # ---------------- CHAT ----------------
        response = self.brain.respond(user_input)
        text = response["text"]

        bee_msg = self.bee.navigation_speak(text)
        self.tts.speak(bee_msg)

        return {
            "type": "chat",
            "bee": bee_msg,
            "steps": [],
            "raw": response
        }
