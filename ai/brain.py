class Brain:
    def respond(self, user_input):
        return {
            "text": f"You said: {user_input}",
            "route": None
        }
