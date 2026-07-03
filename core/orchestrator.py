# BeeRoute Orchestrator (System Glue Layer)
# Connects Brain → Map → Router → Bee → Voice

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

    def handle(self, user_input):
        """
        FULL SYSTEM PIPELINE
        """

        # 1. Brain understands intent
        response = self.brain.respond(user_input)

        text = response.get("text", "")

        # 2. Detect navigation intent (simple rule for now)
        if "go to" in user_input or "navigate" in user_input:
            destination = user_input

            # fallback start (will be GPS later)
            start = "current_location"

            self.active_route = self.router.calculate_route(
                start,
                destination
            )

            route_text = self.active_route["steps"][0]

            final = self.bee.navigation_speak(route_text)

        else:
            final = self.bee.navigation_speak(text)

        # 3. Speak output
        self.tts.speak(final)

        return final
