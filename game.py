import time
import json
from state import State
from scene import Scene

class Game:
    def __init__(self):
        """Initialisiert das Spiel, indem der Spielzustand und die Szenen geladen werden."""
        self.state = State()  # Initialisiert den Spielzustand
        self.scenes = self.load_scenes()  # Lädt alle Szenen aus der JSON-Datei

    def load_scenes(self):
        """Lädt die Szenen aus einer JSON-Datei und erstellt eine Scene-Instanz für jede Szene."""
        with open('scenes/scenes.json', encoding='utf-8') as f:
            scenes_data = json.load(f)
        
        scenes = {}
        for scene_name, scene_info in scenes_data.items():
            description = scene_info["description"]  # Beschreibung der Szene
            choices = scene_info["choices"]  # Mögliche Entscheidungen in der Szene
            scenes[scene_name] = Scene(description, choices)  # Erstellt eine Scene-Instanz und speichert sie in einem Dictionary
        
        return scenes

    def start_game(self):
        """Startet das Spiel, zeigt eine Einführung an, lädt den Spielstand und führt den Spieler durch die Szenen."""
        print("\nWillkommen zu 'Resistance: The Red Uprising'")
        time.sleep(1)
        print("Du bist Rick, ein junger Antifaschist in Deutschland im Jahr 2025.")
        time.sleep(1)
        print("Deine Mission: Kämpfe gegen den aufkommenden Faschismus und rette dein Land.")
        print("\n---\n")

        # Laden des gespeicherten Fortschritts (falls vorhanden)
        self.load_game()

        while True:
            current_scene = self.scenes.get(self.state.progress)  # Holt die aktuelle Szene basierend auf dem Fortschritt
            if current_scene:
                # Szene spielen und Fortschritt anzeigen
                next_scene = self.play_scene(current_scene)  # Spielt die Szene ab und holt die nächste Szene
                if next_scene:
                    self.state.update_progress(next_scene)  # Aktualisiert den Fortschritt basierend auf der Auswahl
                    self.save_game()  # Speichert den aktuellen Spielstand
                else:
                    print("Ungültige Auswahl. Bitte versuche es erneut.")
            else:
                print("Ende des Spiels")
                break

    def save_game(self):
        """Speichert den aktuellen Spielzustand in einer JSON-Datei."""
        with open("game_save.json", "w") as save_file:
            json.dump(self.state.__dict__, save_file)
        print("Spiel gespeichert.")

    def load_game(self):
        """Lädt einen gespeicherten Spielstand, falls vorhanden."""
        try:
            with open("game_save.json", "r") as save_file:
                self.state.__dict__ = json.load(save_file)
                print("Gespeicherter Spielstand geladen.")
        except FileNotFoundError:
            print("Kein gespeichertes Spiel gefunden. Ein neues Spiel wird gestartet.")

    def display_progress(self):
        """Zeigt den aktuellen Fortschritt des Spielers an, basierend auf den Fortschrittswerten für Antifaschismus und rechte Seite."""
        antifascism_progress = self.state.get_variable("antifascism_progress", 0)
        right_side_progress = self.state.get_variable("right_side_progress", 0)
        total_progress = antifascism_progress + right_side_progress
        
        if total_progress > 0:
            antifascism_percent = (antifascism_progress / total_progress) * 100
            right_side_percent = (right_side_progress / total_progress) * 100
        else:
            antifascism_percent = right_side_percent = 50  # Falls keine Fortschritte erzielt wurden, beide Werte auf 50% setzen
        
        print("\n--- Fortschritt ---")
        print(f"Antifaschismus: [{int(antifascism_percent)}%]")
        print(f"Rechte Seite: [{int(right_side_percent)}%]")

    def check_unlocks(self):
        """Überprüft, ob bestimmte Fortschrittswerte erreicht wurden, um neue Szenen oder Ereignisse freizuschalten."""
        antifascism_progress = self.state.get_variable("antifascism_progress", 0)
        right_side_progress = self.state.get_variable("right_side_progress", 0)
        
        if antifascism_progress > 50 and not self.state.get_variable("secret_operation_unlocked", False):
            print("\nNeue Szene freigeschaltet: 'Geheime Operation'")
            self.state.set_variable("secret_operation_unlocked", True)

        if right_side_progress > 70 and not self.state.get_variable("right_militia_unlocked", False):
            print("\nAchtung! Die Rechte gewinnt an Einfluss.")
            self.state.set_variable("right_militia_unlocked", True)

    def play_scene(self, scene):
        """Zeigt die aktuelle Szene an, lässt den Spieler eine Wahl treffen, aktualisiert den Fortschritt und gibt die nächste Szene zurück."""
        print(f"--- Szene: {scene.description} ---")
        for index, choice in enumerate(scene.choices, start=1):
            print(f"  {index}. {choice['text']}")

        selected = input("\nDeine Wahl: ").strip()
        if selected.isdigit() and 1 <= int(selected) <= len(scene.choices):
            choice = scene.choices[int(selected) - 1]
            
            # Aktualisiert die Fortschrittswerte basierend auf der getroffenen Wahl
            antifascism_change = choice.get('antifascism_change', 0)
            right_side_change = choice.get('right_side_change', 0)
            
            self.state.set_variable("antifascism_progress", self.state.get_variable("antifascism_progress", 0) + antifascism_change)
            self.state.set_variable("right_side_progress", self.state.get_variable("right_side_progress", 0) + right_side_change)
            
            # Zeigt den Fortschritt an und überprüft auf Freischaltungen
            self.display_progress()
            self.check_unlocks()
            
            return choice.get("next_scene")  # Gibt die nächste Szene zurück
        else:
            print("Ungültige Wahl. Bitte versuche es erneut.")
        return None
