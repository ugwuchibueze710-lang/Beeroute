# BeeRoute AI Brain (Ollama-powered local intelligence)
# This is the reasoning layer before Bee formats output

import subprocess
import json


class Brain:
    def __init__(self, model="llama3"):
        self.model = model

    def _call_ollama(self, prompt):
        """
        Calls local Ollama model safely
        """
        try:
            result = subprocess.run(
                ["ollama", "run", self.model, prompt],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                return result.stdout.strip()

            return "Ollama error: model not responding"

        except Exception as e:
            return f"Ollama not available: {str(e)}"

    def respond(self, user_input):
        """
        Converts user input into structured navigation + AI response
        """

        system_prompt = f"""
You are BeeRoute Brain.

You are inside a driving navigation system.

User input:
{user_input}

Return ONLY valid JSON in this format:
{{
  "text": "natural driving assistant response",
  "route": "simple route description if needed",
  "distance": "optional distance in meters or miles",
  "eta": "optional time in minutes"
}}

Rules:
- Keep responses short and useful for driving
- If user asks for directions, include route hints
- If not navigation related, just respond conversationally
"""

        output = self._call_ollama(system_prompt)

        # fallback safety parsing
        try:
            data = json.loads(output)
        except:
            data = {
                "text": output,
                "route": "unstructured route",
                "distance": None,
                "eta": None
            }

        return data
