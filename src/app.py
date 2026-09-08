from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Container
from textual.screen import Screen

class SettingsScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Static("SETTINGS SCREEN")

class TimerScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Static("TIMERSCREEN")

class SplashScreen(Screen):
    ASCII = r'''
    ______   ____   _____   ____   __| _/___________   ____  
    \____ \ /  _ \ /     \ /  _ \ / __ |/  _ \_  __ \_/ __ \ 
    |  |_> >  <_> )  Y Y  (  <_> ) /_/ (  <_> )  | \/\  ___/ 
    |   __/ \____/|__|_|  /\____/\____ |\____/|__|    \___  >
    |__|                                                     
    '''

    def compose (self) -> ComposeResult:
        yield Static(self.ASCII)

    def on_mount(self):
        self.set_timer(1.0, self.go_to_timer)

    def go_to_timer(self):
        self.app.pop_screen()

class PomodoreTUI(App):
    CSS_PATH = "styles.css"

    def on_mount(self) -> None:
        self.push_screen(TimerScreen())
        self.push_screen(SplashScreen())

if __name__ == "__main__":
    app = PomodoreTUI()
    app.run()