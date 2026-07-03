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

        if intent == "navigation":
            start = "A"
            destination = "B"

            self.active_route = self.router.calculate_route(start, destination)

            return self.start_navigation()

        response = self.brain.respond(user_input)
        text = response["text"]

        final = self.bee.navigation_speak(text)
        self.tts.speak(final)

        return final

    def start_navigation(self):
        route = self.active_route

        while True:
            instruction = self.router.get_next_instruction(route)

            if instruction == "You have arrived at your destination.":
                msg = self.bee.navigation_speak(instruction)
                self.tts.speak(msg)
                return msg

            msg = self.bee.format_navigation_output(instruction)
            self.tts.speak(msg)

            print(msg)
