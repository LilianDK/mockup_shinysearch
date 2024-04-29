from shiny import App, render, ui
from htmltools import css
import requests


url_1 = "http://localhost:8001/search"
url_2 = "http://localhost:8001/search2"
url_3 = "http://localhost:8001/search3"
headers = {"accept": "application/json", "Content-Type": "application/json"}

app_ui = ui.page_navbar(  

################################################################################################################################
            ui.nav_panel("A", 

            ui.row(     
                ui.column(12,       
                    ui.input_text_area(
                        id="nlq", label="Suchanfrage", value="Welche Baumaßnahmen wurden Januar 2024 durchgeführt", width="800px", height="50px"
                    ),
                ),
            ),
            
            # UI output card 1
            ui.card(
                ui.card_header("Suchergebnis 1"),
                ui.output_ui("result_1", inline=True),
                "Quelle: ",
                ui.output_text("source_1"),
                ui.accordion(
                    ui.accordion_panel(
                        "Technische Angaben",
                        "Title: ", ui.output_text("title_1", inline=True),
                        ui.panel_title("", ""),
                        "Confidence: ", ui.output_text("confidence_1", inline=True),
                        ui.panel_title("", ""),
                        "Filesize: ", ui.output_text("filesize_1", inline=True),
                        ui.panel_title("", ""),
                        "Date: ", ui.output_text("date_1", inline=True),
                    ),
                ),
            ),
            # UI output card 2
            ui.card(
                ui.card_header("Suchergebnis 2"),
                ui.output_ui("result_2", inline=True),
                "Quelle: ",
                ui.output_text("source_2"),
                ui.accordion(
                    ui.accordion_panel(
                        "Technische Angaben",
                        "Title: ", ui.output_text("title_2", inline=True),
                        ui.panel_title("", ""),
                        "Confidence: ", ui.output_text("confidence_2", inline=True),
                        ui.panel_title("", ""),
                        "Filesize: ", ui.output_text("filesize_2", inline=True),
                        ui.panel_title("", ""),
                        "Date: ", ui.output_text("date_2", inline=True),
                    ),
                ),
            ),
            # UI output card 3
            ui.card(
                ui.card_header("Suchergebnis 3"),
                ui.output_ui("result_3", inline=True),
                "Quelle: ",
                ui.output_text("source_3"),
                ui.accordion(
                    ui.accordion_panel(
                        "Technische Angaben",
                        "Title: ", ui.output_text("title_3", inline=True),
                        ui.panel_title("", ""),
                        "Confidence: ", ui.output_text("confidence_3", inline=True),
                        ui.panel_title("", ""),
                        "Filesize: ", ui.output_text("filesize_3", inline=True),
                        ui.panel_title("", ""),
                        "Date: ", ui.output_text("date_3", inline=True),
                    ),
                ),
            ),
                         ),

################################################################################################################################
            ui.nav_panel("B", 
            
            ui.row(     
                ui.column(6,       
                    ui.input_text_area(
                        id="nlq2", label="Suchanfrage", value="What is the situation in Germany on nationality", width="800px", height="50px"
                    ),
                ),
                ui.column(6,       
                    ui.input_select(  
                        "state2",  
                        "Select an option below:",  
                        {
                            "Country": {"Germany": "Germany", "Ukraine": "Ukraine", "Taiwan": "Taiwan", "Israel": "Israel", "Iran": "Iran"},
                            "Topic": {"Politics": "Politics", "Social": "Social", "Health": "Health", "Religion": "Religion", "Nationality": "Nationality"},
                         },  
                    ),  
                ),
            ),
            
            # UI output card 1
            ui.row(
                ui.column(6,
                    ui.card(
                        ui.card_header("Suchergebnis 1 ohne SDU"),
                        ui.output_ui("result_1b", inline=True),
                        "Quelle: ",
                        ui.output_text("source_1b"),
                        ui.accordion(
                            ui.accordion_panel(
                                "Technische Angaben",
                                "Title: ", ui.output_text("title_1b", inline=True),
                                ui.panel_title("", ""),
                                "Confidence: ", ui.output_text("confidence_1b", inline=True),
                                ui.panel_title("", ""),
                                "Filesize: ", ui.output_text("filesize_1b", inline=True),
                                ui.panel_title("", ""),
                                "Date: ", ui.output_text("date_1b", inline=True),
                            ),
                        ),
                    ),
                ),
                ui.column(6,
                    ui.card(
                        ui.card_header("Suchergebnis 1 mit SDU"),
                        ui.output_ui("result_1c", inline=True),
                        "Quelle: ",
                        ui.output_text("source_1c"),
                        ui.accordion(
                            ui.accordion_panel(
                                "Technische Angaben",
                                "Title: ", ui.output_text("title_1c", inline=True),
                                ui.panel_title("", ""),
                                "Confidence: ", ui.output_text("confidence_1c", inline=True),
                                ui.panel_title("", ""),
                                "Filesize: ", ui.output_text("filesize_1c", inline=True),
                                ui.panel_title("", ""),
                                "Date: ", ui.output_text("date_1c", inline=True),
                            ),
                        ),
                    ),
                ),
            ),
            # UI output card 2
            ui.row(
                ui.column(6,
                    ui.card(
                        ui.card_header("Suchergebnis 2 ohne SDU"),
                        ui.output_ui("result_2b", inline=True),
                        "Quelle: ",
                        ui.output_text("source_2b"),
                        ui.accordion(
                            ui.accordion_panel(
                                "Technische Angaben",
                                "Title: ", ui.output_text("title_2b", inline=True),
                                ui.panel_title("", ""),
                                "Confidence: ", ui.output_text("confidence_2b", inline=True),
                                ui.panel_title("", ""),
                                "Filesize: ", ui.output_text("filesize_2b", inline=True),
                                ui.panel_title("", ""),
                                "Date: ", ui.output_text("date_2b", inline=True),
                            ),
                        ),
                    ),
                ),
                ui.column(6,
                    ui.card(
                        ui.card_header("Suchergebnis 2c mit SDU"),
                        ui.output_ui("result_2c", inline=True),
                        "Quelle: ",
                        ui.output_text("source_2c"),
                        ui.accordion(
                            ui.accordion_panel(
                                "Technische Angaben",
                                "Title: ", ui.output_text("title_2c", inline=True),
                                ui.panel_title("", ""),
                                "Confidence: ", ui.output_text("confidence_2c", inline=True),
                                ui.panel_title("", ""),
                                "Filesize: ", ui.output_text("filesize_2c", inline=True),
                                ui.panel_title("", ""),
                                "Date: ", ui.output_text("date_2c", inline=True),
                            ),
                        ),
                    ),
                ),
            ),
            # UI output card 3
            ui.row(
                ui.column(6,
                    ui.card(
                        ui.card_header("Suchergebnis 3 ohne SDU"),
                        ui.output_ui("result_3b", inline=True),
                        "Quelle: ",
                        ui.output_text("source_3b"),
                        ui.accordion(
                            ui.accordion_panel(
                                "Technische Angaben",
                                "Title: ", ui.output_text("title_3b", inline=True),
                                ui.panel_title("", ""),
                                "Confidence: ", ui.output_text("confidence_3b", inline=True),
                                ui.panel_title("", ""),
                                "Filesize: ", ui.output_text("filesize_3b", inline=True),
                                ui.panel_title("", ""),
                                "Date: ", ui.output_text("date_3b", inline=True),
                            ),
                        ),
                    ),
                ),
                ui.column(6,
                    ui.card(
                        ui.card_header("Suchergebnis 3 mit SDU"),
                        ui.output_ui("result_3c", inline=True),
                        "Quelle: ",
                        ui.output_text("source_3c"),
                        ui.accordion(
                            ui.accordion_panel(
                                "Technische Angaben",
                                "Title: ", ui.output_text("title_3c", inline=True),
                                ui.panel_title("", ""),
                                "Confidence: ", ui.output_text("confidence_3c", inline=True),
                                ui.panel_title("", ""),
                                "Filesize: ", ui.output_text("filesize_3c", inline=True),
                                ui.panel_title("", ""),
                                "Date: ", ui.output_text("date_3c", inline=True),
                            ),
                        ),
                    ),
                ),
            )
                         ),
            ui.nav_panel("C", "Panel C content"),
            title="Mockup Funktionalitätencheck",  
            id="page", 
)


def server(input, output, session):

################################################################################################################################
    # UI output card 1
    @render.text
    def result_1():
        """
        Result result 1 from the search
        """
        data = {"nlq": input.nlq()}
        response = requests.post(url_1, headers=headers, json=data)
        response_data = response.json()
        df = response_data["results"][0]["document_passages"][0]["passage_text"]

        df = df.replace("<em>", "<mark>").replace("</em>", "</mark>")

        return df

    @render.text
    def source_1():
        """
        Result source 1 from the search
        """
        data = {"nlq": input.nlq()}

        response = requests.post(url_1, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][0]["metadata"]["source"]["url"]

        return df

    @render.text
    def title_1():
        """
        Result title 1 from the search
        """
        data = {"nlq": input.nlq()}

        response = requests.post(url_1, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][0]["title"]

        return df

    @render.text
    def confidence_1():
        """
        Result confidence 1 from the search
        """
        data = {"nlq": input.nlq()}

        response = requests.post(url_1, headers=headers, json=data)
        response_data = response.json()
        
        df = response_data["results"][0]["result_metadata"]["confidence"]

        return df
    
    @render.text
    def date_1():
        """
        Result date 1 from the search
        """
        data = {"nlq": input.nlq()}

        response = requests.post(url_1, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][0]["metadata"]["Date"]

        return df
    
    @render.text
    def filesize_2():
        """
        Result filesize 2 from the search
        """
        data = {"nlq": input.nlq()}

        response = requests.post(url_1, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][0]["metadata"]["FileSize"]

        return df
    
    # UI output card 2
    @render.text
    def result_2():
        """
        Result result 2 from the search
        """
        data = {"nlq": input.nlq()}

        response = requests.post(url_1, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][1]["document_passages"][0]["passage_text"]

        df = df.replace("<em>", "<mark>").replace("</em>", "</mark>")

        return df

    @render.text
    def source_2():
        """
        Result source 1 from the search
        """
        data = {"nlq": input.nlq()}

        response = requests.post(url_1, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][1]["metadata"]["source"]["url"]

        return df

    @render.text
    def title_2():
        """
        Result title 2 from the search
        """
        data = {"nlq": input.nlq()}

        response = requests.post(url_1, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][1]["title"]

        return df
    
    @render.text
    def confidence_2():
        """
        Result confidence 2 from the search
        """
        data = {"nlq": input.nlq()}

        response = requests.post(url_1, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][1]["result_metadata"]["confidence"]

        return df

    @render.text
    def date_2():
        """
        Result date 2 from the search
        """
        data = {"nlq": input.nlq()}

        response = requests.post(url_1, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][1]["metadata"]["Date"]

        return df

    @render.text
    def filesize_2():
        """
        Result filesize 2 from the search
        """
        data = {"nlq": input.nlq()}

        response = requests.post(url_1, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][1]["metadata"]["FileSize"]

        return df
    
    # UI output card 3
    @render.text
    def result_3():
        """
        Result result 3 from the search
        """
        data = {"nlq": input.nlq()}

        response = requests.post(url_1, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][2]["document_passages"][0]["passage_text"]

        df = df.replace("<em>", "<mark>").replace("</em>", "</mark>")

        return df

    @render.text
    def source_3():
        """
        Result source 3 from the search
        """
        data = {"nlq": input.nlq()}

        response = requests.post(url_1, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][2]["metadata"]["source"]["url"]

        return df

    @render.text
    def title_3():
        """
        Result title 3 from the search
        """
        data = {"nlq": input.nlq()}

        response = requests.post(url_1, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][2]["title"]

        return df
    
    @render.text
    def confidence_3():
        """
        Result confidence 3 from the search
        """
        data = {"nlq": input.nlq()}

        response = requests.post(url_1, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][2]["result_metadata"]["confidence"]

        return df

    @render.text
    def date_3():
        """
        Result date 3 from the search
        """
        data = {"nlq": input.nlq()}

        response = requests.post(url_1, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][2]["metadata"]["Date"]

        return df

    @render.text
    def filesize_3():
        """
        Result filesize 3 from the search
        """
        data = {"nlq": input.nlq()}

        response = requests.post(url_1, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][2]["metadata"]["FileSize"]

        return df

################################################################################################################################
    # UI output card 1
    @render.text
    def result_1b():
        """
        Result result 1 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_2, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][0]["document_passages"][0]["passage_text"]

        df = df.replace("<em>", "<mark>").replace("</em>", "</mark>")

        return df

    @render.text
    def source_1b():
        """
        Result source 1 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_2, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][0]["metadata"]["source"]["url"]

        return df

    @render.text
    def title_1b():
        """
        Result title 1 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_2, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][0]["title"]

        return df

    @render.text
    def confidence_1b():
        """
        Result confidence 1 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_2, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][0]["result_metadata"]["confidence"]

        return df
    
    @render.text
    def date_1b():
        """
        Result date 1 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_2, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][0]["metadata"]["Date"]

        return df
    
    @render.text
    def filesize_1b():
        """
        Result filesize 2 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_2, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][0]["metadata"]["FileSize"]

        return df
    
    # UI output card 2
    @render.text
    def result_2b():
        """
        Result result 2 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_2, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][1]["document_passages"][0]["passage_text"]

        df = df.replace("<em>", "<mark>").replace("</em>", "</mark>")

        return df

    @render.text
    def source_2b():
        """
        Result source 1 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_2, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][1]["metadata"]["source"]["url"]

        return df

    @render.text
    def title_2b():
        """
        Result title 2 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_2, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][1]["title"]

        return df
    
    @render.text
    def confidence_2b():
        """
        Result confidence 2 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_2, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][1]["result_metadata"]["confidence"]

        return df

    @render.text
    def date_2b():
        """
        Result date 2 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_2, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][1]["metadata"]["Date"]

        return df

    @render.text
    def filesize_2b():
        """
        Result filesize 2 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_2, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][1]["metadata"]["FileSize"]

        return df
    
    # UI output card 3
    @render.text
    def result_3b():
        """
        Result result 3 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_2, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][2]["document_passages"][0]["passage_text"]

        df = df.replace("<em>", "<mark>").replace("</em>", "</mark>")

        return df

    @render.text
    def source_3b():
        """
        Result source 3 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_2, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][2]["metadata"]["source"]["url"]

        return df

    @render.text
    def title_3b():
        """
        Result title 3 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_2, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][2]["title"]

        return df
    
    @render.text
    def confidence_3b():
        """
        Result confidence 3 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_2, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][2]["result_metadata"]["confidence"]

        return df

    @render.text
    def date_3b():
        """
        Result date 3 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_2, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][2]["metadata"]["Date"]

        return df

    @render.text
    def filesize_3b():
        """
        Result filesize 3 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_2, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][2]["metadata"]["FileSize"]

        return df


    @render.text
    def result_1c():
        """
        Result result 1 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_3, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][0]["document_passages"][0]["passage_text"]

        df = df.replace("<em>", "<mark>").replace("</em>", "</mark>")

        return df

    @render.text
    def source_1c():
        """
        Result source 1 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_3, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][0]["metadata"]["source"]["url"]

        return df

    @render.text
    def title_1c():
        """
        Result title 1 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_3, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][0]["title"]

        return df

    @render.text
    def confidence_1c():
        """
        Result confidence 1 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_3, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][0]["result_metadata"]["confidence"]

        return df
    
    @render.text
    def date_1c():
        """
        Result date 1 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_3, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][0]["metadata"]["Date"]

        return df

    @render.text
    def result_2c():
        """
        Result result 2 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_3, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][1]["document_passages"][0]["passage_text"]

        df = df.replace("<em>", "<mark>").replace("</em>", "</mark>")

        return df

    @render.text
    def source_2c():
        """
        Result source 1 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_3, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][1]["metadata"]["source"]["url"]

        return df

    @render.text
    def title_2c():
        """
        Result title 2 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_3, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][1]["title"]

        return df
    
    @render.text
    def confidence_2c():
        """
        Result confidence 2 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_3, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][1]["result_metadata"]["confidence"]

        return df

    @render.text
    def date_2c():
        """
        Result date 2 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_3, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][1]["metadata"]["Date"]

        return df

    @render.text
    def filesize_2c():
        """
        Result filesize 2 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_3, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][1]["metadata"]["FileSize"]

        return df

    @render.text
    def result_3c():
        """
        Result result 3 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_3, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][2]["document_passages"][0]["passage_text"]

        df = df.replace("<em>", "<mark>").replace("</em>", "</mark>")

        return df

    @render.text
    def source_3c():
        """
        Result source 3 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_3, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][2]["metadata"]["source"]["url"]

        return df

    @render.text
    def title_3c():
        """
        Result title 3 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_3, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][2]["title"]

        return df
    
    @render.text
    def confidence_3c():
        """
        Result confidence 3 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_3, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][2]["result_metadata"]["confidence"]

        return df

    @render.text
    def date_3c():
        """
        Result date 3 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_3, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][2]["metadata"]["Date"]

        return df

    @render.text
    def filesize_3c():
        """
        Result filesize 3 from the search
        """
        data = {"nlq": input.nlq2(), "state": input.state2()}

        response = requests.post(url_2, headers=headers, json=data)
        response_data = response.json()

        df = response_data["results"][2]["metadata"]["FileSize"]

        return df

# Call App() to combine app_ui and server() into an interactive app
app = App(app_ui, server)

#shiny run shinysearch/app.py