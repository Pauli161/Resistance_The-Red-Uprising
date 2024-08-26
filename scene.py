
import time

class Scene:
    def __init__(self, description, choices):
        self.description = description
        self.choices = choices

    def show(self, state):
        print(self.description)
        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice['text']}")

        choice = input("> ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(self.choices):
            next_scene = self.choices[int(choice) - 1]["next_scene"]
            state.update_progress(next_scene)
        else:
            print("Ungültige Wahl, bitte versuche es erneut.")
            self.show(state)
