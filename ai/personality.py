class BeePersonality:
    def navigation_speak(self, text):
        return f"🐝 Bee: {text}"

    def format_navigation_output(self, instruction, distance=None, eta=None):
        text = instruction

        if distance:
            text += f". In about {distance}"
        if eta:
            text += f". ETA is {eta}"

        text = text.replace("Go from", "Head from")
        text = text.replace("to", "towards")

        return f"🐝 Bee: {text}"
