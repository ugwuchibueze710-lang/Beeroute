# BeeRoute Main Entry Point

from core.app import BeeRouteCore


def main():
    print("Starting BeeRoute System 🐝")

    app = BeeRouteCore()

    print("System Ready. Type commands below.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Shutting down BeeRoute...")
            break

        result = app.process_command(user_input)

        print("\n--- RESPONSE ---")
        print("AI:", result["ai"])
        print("ROUTE:", result["route"])
        print("VOICE:", result["voice"])
        print("----------------\n")


if __name__ == "__main__":
    main()
