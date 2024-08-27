class State:
    def __init__(self):
        self.progress = "Intro"
        self.variables = {}

    def update_progress(self, progress):
        self.progress = progress

    def set_variable(self, key, value):
        self.variables[key] = value

    def get_variable(self, key, default=None):
        """Gibt den Wert für den Schlüssel zurück, wenn er existiert, andernfalls den Standardwert."""
        return self.variables.get(key, default)
