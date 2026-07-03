# BeeRoute AI Personality Engine (Bee 🐝)
# Human driving companion + navigation translator layer

class BeePersonality:
    def __init__(self):
        self.mode = "driving"  # driving | conversation
        self.style = "human_co_pilot"

    # -----------------------------
    # MODE SWITCHING
    # -----------------------------
    def set_mode(self, mode):
        if mode in ["driving", "conversation"]:
            self.mode = mode

    # -----------------------------
    # HUMANIZE DISTANCE
    # Converts raw numbers into natural speech
    # -----------------------------
    def humanize_distance(self, meters):
        miles = meters / 1609.34

        if miles < 0.1:
            return "right here"
        elif miles < 0.5:
            return "a few blocks away"
        elif miles < 1:
            return "less than a mile away"
        elif miles < 5:
            return f"about {round(miles, 1)} miles away"
        else:
            return f"about {round(miles)} miles out"

    # -----------------------------
    # HUMANIZE TIME
    # -----------------------------
    def humanize_time(self, minutes):
        if minutes < 1:
            return "less than a minute"
        elif minutes < 5:
            return "a couple minutes"
        elif minutes < 15:
            return f"about {minutes} minutes"
        else:
            return f"around {round(minutes / 5) * 5} minutes"

    # -----------------------------
    # NAVIGATION SPEECH STYLE
    # -----------------------------
    def navigation_speak(self, instruction, distance_text=None):
        if self.mode == "driving":
            # calm, short, human-like driving instructions

            if distance_text:
                return f"{instruction}, {distance_text}"

            return instruction

        else:
            # conversational mode (more personality)
            return f"Alright — {instruction}"

    # -----------------------------
    # CONTEXTUAL RESPONSES
    # -----------------------------
    def respond_to_question(self, question, data=None):
        q = question.lower()

        if "gas" in q:
            return "There’s one coming up ahead — I’ll guide you to the closest one on your route."

        if "how far" in q:
            if data:
                return f"It’s {self.humanize_distance(data)} from here."
            return "Let me check the route ahead for you."

        if "time" in q:
            return "You’re on track — I’ll keep updating your ETA as we go."

        return "Got you — I’m checking that for you."
