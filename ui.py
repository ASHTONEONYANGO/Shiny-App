from shiny import ui

def create_ui():
    app_ui = ui.page_fluid(
        # App Title
        ui.h1("Data Analysis App"),
        
        # Layout with sidebar and main panel
        ui.row(
            # Sidebar panel
            ui.column(4,
                ui.input_file("file", "Upload CSV File", 
                            accept=[".csv"]),
                
                # First dropdown
                ui.input_select("var1", "Select First Variable", 
                              choices=[]),
                
                # Second dropdown
                ui.input_select("var2", "Select Second Variable", 
                              choices=[]),
                
                # Text input for plot title
                ui.input_text("plot_title", "Enter Plot Title", 
                            value="My Plot")
            ),
            
            # Main panel with tabs
            ui.column(8,
                ui.navset_tab(
                    ui.nav_panel("Data Table",
                        ui.output_table("table")
                    ),
                    ui.nav_panel("Plot",
                        ui.output_plot("plot")
                    )
                )
            )
        )
    )
    return app_ui