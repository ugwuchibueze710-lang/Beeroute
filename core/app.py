from core.orchestrator import BeeOrchestrator


class BeeRouteCore:
    def __init__(self):
        self.system = BeeOrchestrator()

    def run(self):
        print("🐝 BeeRoute Online")

        while True:
            user_input = input("You: ")

            if user_input in ["exit", "quit"]:
                break

            print(self.system.handle(user_input))


if __name__ == "__main__":
    BeeRouteCore().run()
