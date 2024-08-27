from game import Game

if __name__ == "__main__":
    game = Game()
    
    # Prüfen, ob ein gespeicherter Spielstand existiert
    try:
        with open("game_save.json", "r") as save_file:
            load_choice = input("Möchtest du das gespeicherte Spiel laden? (ja/nein): ").strip().lower()
            if load_choice == "ja":
                game.load_game()
                print("Gespeichertes Spiel geladen.")
            else:
                print("Neues Spiel gestartet.")
    except FileNotFoundError:
        print("Kein gespeichertes Spiel gefunden. Neues Spiel gestartet.")
    
    game.start_game()
