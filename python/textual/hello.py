
from textual.app import App
from textual.widgets import Label

class HelloWorldApp(App):

    CSS_PATH = "hello.css"
    
    def compose(self):
        yield Label("hello there")


if __name__ == "__main__":
    app = HelloWorldApp()
    app.run()



