import time

class Scene:
    def __init__(self, description, choices):
        self.description = description
        self.choices = choices

    def show(self, state):
        print(self.description)
        for key, _ in self.choices.items():
            print(f"{key}. {self.choices[key]}")  # Text der Auswahl anzeigen

        choice = input("> ").strip()
        next_scene = self.choices.get(choice)
        if next_scene:
            state.update_progress(next_scene)
        else:
            print("Ungültige Wahl, bitte versuche es erneut.")
            self.show(state)
