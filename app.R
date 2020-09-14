#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(tidyverse)

veg <- read_csv("./veg_table.csv")
starts <- read_csv("./starts_edited.csv")
indoor <- read_csv("./seed_indoor_edited.csv")
outdoor <- read_csv("./seed_outdoor_edited.csv")
month <- read_csv("./month.csv")


starts <- starts %>% 
    left_join(
    (veg %>% 
    select(veg_id, name))) %>% 
    left_join(month, by = "month_id") %>% 
    select(`Vegetable Name` = name.x, `Month` = name.y, start_date, through_date, best)

indoor <- indoor %>% 
    left_join(
        (veg %>% 
             select(veg_id, name))) %>% 
    left_join(month, by = "month_id") %>% 
    select(`Vegetable Name` = name.x, version, `Month` = name.y, start_date, through_date, best)

outdoor <- outdoor %>% 
    left_join(
        (veg %>% 
             select(veg_id, name))) %>% 
    left_join(month, by = "month_id") %>% 
    select(`Vegetable Name` = name.x, version, `Month` = name.y, start_date, through_date, best)

ui <- fluidPage(
    title = "Examples of DataTables",
    sidebarLayout(
        sidebarPanel(
            conditionalPanel(
                'input.dataset === "Starts"',
                helpText("Click the column header to sort a column. Type in the boxes to filter to a certain vegetable or month. The Best column indicates whether that time is the best time and method to plant that vegetable.")
            ),
            conditionalPanel(
                'input.dataset === "Seed Indoor"',
                helpText("Click the column header to sort a column. Type in the boxes to filter to a certain vegetable or month. The Best column indicates whether that time is the best time and method to plant that vegetable. The seeds column indicates the form of seeds (seeds, bulb, etc).")
            ),
            conditionalPanel(
                'input.dataset === "Seed Outdoor"',
                helpText("Click the column header to sort a column. Type in the boxes to filter to a certain vegetable or month. The Best column indicates whether that time is the best time and method to plant that vegetable. The seeds column indicates the form of seeds (seeds, bulb, etc).")
            )
        ),
        mainPanel(
            tabsetPanel(
                id = 'dataset',
                tabPanel("Starts", DT::dataTableOutput("mytable1")),
                tabPanel("Seed Indoor", DT::dataTableOutput("mytable2")),
                tabPanel("Seed Outdoor", DT::dataTableOutput("mytable3"))
            )
        )
    )
)

server <- function(input, output) {
    output$mytable1 = DT::renderDataTable({
        starts},
        filter = "top"
    )
    
    output$mytable2 = DT::renderDataTable({
        indoor},
        filter = "top"
    )
    
    output$mytable3 = DT::renderDataTable({
        outdoor},
        filter = "top"
    )
}

# Run the application 
shinyApp(ui = ui, server = server)
