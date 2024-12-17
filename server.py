from shiny import render, reactive, ui
import pandas as pd
import matplotlib.pyplot as plt

def create_server():
    def server(input, output, session):
        # Update dropdowns when file is uploaded
        @reactive.Effect
        def _():
            file = input.file()
            if file is not None:
                # Read the uploaded file
                df = pd.read_csv(file[0]['datapath'])
                choices = list(df.columns)
                ui.update_select("var1", choices=choices, session=session)
                ui.update_select("var2", choices=choices, session=session)
        
        # Render the data table
        @output
        @render.table
        def table():
            file = input.file()
            if file is None:
                return None
            return pd.read_csv(file[0]['datapath'])
        
        # Render the plot
        @output
        @render.plot
        def plot():
            file = input.file()
            if file is None:
                return None
            
            df = pd.read_csv(file[0]['datapath'])
            
            # Create matplotlib scatter plot
            plt.figure(figsize=(10, 6))
            plt.scatter(df[input.var1()], df[input.var2()])
            plt.xlabel(input.var1())
            plt.ylabel(input.var2())
            plt.title(input.plot_title())
            
            return plt.gcf()
    
    return server