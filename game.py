import json
from state import State
from scene import Scene
import time  # <-- Diesen Import hinzufügen

class Game:
    def __init__(self):
        self.state = State()
        self.scenes = self.load_scenes()

    def load_scenes(self):
        with open('scenes/scenes.json') as f:
            scenes_data = json.load(f)
        
        scenes = {}
        for scene_name, scene_info in scenes_data.items():
            description = scene_info["description"]
            choices = scene_info["choices"]
            scenes[scene_name] = Scene(description, choices)
        
        return scenes

    def start_game(self):
        print("\nWillkommen zu 'Resistance: The Red Uprising'")
        time.sleep(1)
        print("Du bist Rick, ein junger Antifaschist in Deutschland im Jahr 2025.")
        time.sleep(1)
        print("Deine Mission: Kämpfe gegen den aufkommenden Faschismus und rette dein Land.")
        print("\n---\n")

        while True:
            current_scene = self.scenes.get(self.state.progress)
            if current_scene:
                current_scene.show(self.state)
            else:
                print("Ende des Spiels")
                break

    def save_game(self):
        with open("game_save.json", "w") as save_file:
            json.dump(self.state.__dict__, save_file)
        print("Spiel gespeichert.")

    def load_game(self):
        try:
            with open("game_save.json", "r") as save_file:
                self.state.__dict__ = json.load(save_file)
        except FileNotFoundError:
            print("Kein gespeichertes Spiel gefunden.")
