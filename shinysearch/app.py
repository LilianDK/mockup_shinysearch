from shiny import App, render, ui
from htmltools import css
import matplotlib.pyplot as plt
import numpy as np
import requests
import pandas as pd   



url = "http://localhost:8001/search"
headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}





# Nest Python functions to build an HTML interface
app_ui = ui.page_fixed( # Layout the UI with Layout Functions
    ui.panel_title("Mockup Searchbar", "Shinysearch"),
    ui.input_text_area(id="nlq", label="Suchanfrage", value="World", width='800px', height='50px'),

    ui.card(  
        ui.card_header("Suchergebnis 1"),
        ui.output_ui("result_1", inline=True),
        "Quelle: ",
        ui.output_text("source_1"),
        ui.accordion(  
            ui.accordion_panel("Technische Angaben", "TBD",
                               ),  
        ),  
    ),
    ui.card(  
        ui.card_header("Suchergebnis 2"),
        ui.output_ui("result_2", inline=True),
        "Quelle: ",
        ui.output_text("source_2")
    ),
)





def server(input, output, session):

    @render.text
    def result_1():
        """
        Result text 1 from the search 
        """
        data = {"nlq": input.nlq()}

        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][0]["document_passages"][0]["passage_text"]

        df = df.replace("<em>","<mark>").replace("</em>", "</mark>")
        return df
    
    @render.text
    def source_1():
        """
        Result text 1 from the search 
        """
        data = {"nlq": input.nlq()}

        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][0]["metadata"]["source"]["url"]

        return df
    
    @render.text
    def document_1():
        """
        Result text 1 from the search 
        """
        data = {"nlq": input.nlq()}

        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][0]["document_id"]

        return df
    
    @render.text
    def result_2():
        """
        Result text 2 from the search 
        """
        data = {"nlq": input.nlq()}

        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][1]["document_passages"][0]["passage_text"]

        df = df.replace("<em>","<mark>").replace("</em>", "</mark>")
        return df

    @render.text
    def source_2():
        """
        Result text 1 from the search 
        """
        data = {"nlq": input.nlq()}

        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][1]["metadata"]["source"]["url"]

        return df
    
# Call App() to combine app_ui and server() into an interactive app
app = App(app_ui, server)