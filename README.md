
# Biscayne Bay Water Quality Dashboard

## Project Overview

The Biscayne Bay Water Quality Dashboard is an
interactive web application built using Python
and Streamlit.

The application allows users to explore water
quality measurements collected in Biscayne Bay,
Florida, through interactive tables, Plotly
visualizations, and summary statistics.

This project was developed for CIS3590 to
demonstrate interactive data visualization,
Python application development, and Agile
project management techniques.

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- Visual Studio Code
- Git and GitHub

## Dataset

The application uses the following CSV file:

`data/biscayneBay_waterquality.csv`

The dataset contains 942 records and 69 columns,
including measurements related to:

- Water temperature (°C)
- pH
- Turbidity (NTU)
- Salinity (ppt)
- Dissolved oxygen (mg/L)
- Geographic coordinates

The dashboard displays selected measurements
from the dataset.

Note: The original measurements have not been
fully quality-controlled. Some values may
reflect sensor errors or measurement limitations.

## Features

### Interactive Measurement Selection

Users can select from five water quality
measurements using a dropdown menu.

### Record Count Slider

Users can adjust the number of records
displayed in the table and chart.

### Interactive Data Table

The application displays the selected
measurements in a sortable data table.

### Plotly Visualization

An interactive line chart displays the
selected water quality measurement.

Users can hover over chart points,
zoom, and explore variations in the data.

### Summary Statistics

The application calculates:

- Average
- Minimum
- Maximum

These statistics update based on the
selected measurement and record count.

### User Instructions

An expandable instruction section helps
users navigate the dashboard.

## How to Run Locally

1. Install Python.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Create and activate a Python virtual environment.
5. Install dependencies:

   python -m pip install -r requirements.txt

6. Start the application:

   python -m streamlit run app.py

7. Open the local URL shown in the terminal,
   usually http://localhost:8501.

## Agile Development Process

The project uses an Agile development approach
with three short sprints.

### Sprint 1: Setup and Data Integration
- Set up the development environment.
- Organized project files.
- Loaded the Biscayne Bay CSV dataset.
- Displayed data using Streamlit.

### Sprint 2: Visualization and Interactivity
- Implemented measurement selection.
- Added a record count slider.
- Created interactive Plotly charts.
- Added summary statistics.

### Sprint 3: Testing and User Experience
- Tested dashboard functionality.
- Added expandable user instructions.
- Reviewed application usability.
- Prepared the project for deployment.

Detailed Agile documentation is available
in `agile_plan.md`.

## Future Improvements

Possible enhancements include:

- Integration with live water quality APIs.
- AI-generated explanations of measurements.
- Geographic visualization of sampling locations.
- Additional data filtering options.

These features may be explored in Project 2.

## Deployment

The application is publicly deployed using
Streamlit Community Cloud.

Live Application:
https://ymsuhenn7pti3pfrqgakzn.streamlit.app/

GitHub Repository:
https://github.com/cyrusAv/water-quality-dashboard
## Author

Cyrus Avendano
CIS3590
FIU