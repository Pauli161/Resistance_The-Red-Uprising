
import time

class Scene:
    def show(self, state):
        # Szene Beschreibung
        print("\n" + self.description + "\n")

        # Entscheidungsoptionen
        for index, choice in enumerate(self.choices, start=1):
            print(f"  {index}. {choice['text']}")
        
        # Benutzereingabe
        choice = input("\n> Deine Wahl: ").strip()
        
        # Nächste Szene bestimmen
        if choice.isdigit() and 1 <= int(choice) <= len(self.choices):
            next_scene = self.choices[int(choice) - 1]["next_scene"]
            state.update_progress(next_scene)
        else:
            print("Ungültige Wahl, bitte versuche es erneut.")
            self.show(state)
