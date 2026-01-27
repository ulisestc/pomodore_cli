from textual.app import App
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Container

class MainMenu(Static):
    def compose(self):
        yield Static("POMODORE TUI", id="title")
        yield Button("START SESSION")
        yield Button("SETTINGS")

class PomodoreTUI(App):
    CSS_PATH = "styles.css"

    BINDINGS = [
        ("s","start_session", "Start Session"),
        ("t","go_to_settings", "Go to Settings")
    ]

    def compose(self):
        yield Header()
        yield Footer()

        with Container(id ="menu"):
            yield MainMenu()

    def action_start_session(self):
        pass

    def action_go_to_settings(self):
        pass

if __name__ == "__main__":
    app = PomodoreTUI()
    app.run()