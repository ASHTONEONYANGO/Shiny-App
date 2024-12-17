from shiny import App
from ui import create_ui
from server import create_server

# Create the Shiny app
app = App(create_ui(), create_server()) 