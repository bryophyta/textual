from textual.app import App
from textual.widgets import Static


class DisplayApp(App):
    CSS = """    
    Screen {
        background: green;
    }
    Static {             
        height: 5;        
        background: white;        
        color: blue;   
        border: heavy blue;     
    }
    Static.remove {
        display: none;
    }
    """

    def compose(self):
        yield Static("Widget 1")
        yield Static("widget 2", classes="remove")
        yield Static("widget 3")


app = DisplayApp()
