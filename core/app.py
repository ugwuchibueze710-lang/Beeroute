# BeeRoute Core Launcher
# This file ONLY starts the system

from core.orchestrator import BeeOrchestrator


class BeeRouteCore:
    def __init__(self):
        self.system = BeeOrchestrator()

    def run(self):
        print("🐝 BeeRoute Online - Full System Active")

        while True:
            user_input = input("\nYou: ")

            if user_input.lower() in ["exit", "quit"]:
                print("Shutting down BeeRoute...")
                break

            result = self.system.handle(user_input)

            print("\nBee:", result)
            print("\n----------------------\n")


if __name__ == "__main__":
    app = BeeRouteCore()
    app.run()
