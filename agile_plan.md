
# Agile Development Plan

## Project Name
Biscayne Bay Water Quality Dashboard

## Project Goal
Develop an interactive Streamlit web application
that allows users to explore water quality data
through interactive controls, visualizations,
and summary statistics.

## Agile Methodology

This project follows a lightweight, Scrum-inspired
Agile development process.

Development is divided into three short sprints.
Each sprint focuses on delivering functional
features that can be tested and improved.

The process includes:
- Product backlog
- User stories
- Sprint planning
- Incremental development
- Functional testing
- Sprint reviews
- Retrospectives

## Product Backlog

- [x] Set up Python and VS Code
- [x] Configure virtual environment
- [x] Install required libraries
- [x] Import Biscayne Bay CSV dataset
- [x] Display interactive data table
- [x] Create measurement dropdown
- [x] Create record count slider
- [x] Calculate descriptive statistics
- [x] Create interactive Plotly chart
- [x] Add application instructions
- [ ] Complete functional testing
- [ ] Finalize project documentation
- [ ] Upload project to GitHub
- [ ] Deploy to Streamlit Community Cloud

## User Stories

1. As a user, I want to select a water quality
   measurement so that I can explore specific data.

2. As a user, I want to adjust the number of
   displayed records so that I can control
   how much data I examine.

3. As a user, I want interactive charts so
   that I can visualize measurement patterns.

4. As a user, I want summary statistics so
   that I can understand the selected data.

5. As a new user, I want instructions so
   that I can understand the application.

## Sprint 1: Setup and Data Integration

### Sprint Goal
Establish the development environment and
successfully load the water quality dataset.

### Development Tasks
- Configured Python development environment.
- Created the project structure.
- Installed Streamlit, Pandas, and Plotly.
- Loaded the Biscayne Bay CSV file.
- Displayed water quality data in a table.

### Sprint Review
The initial application successfully loaded
and displayed the dataset.

### Sprint Retrospective
The project initially used a sample dataset.
After switching to the Biscayne Bay dataset,
the application required updates to match
the actual column names.

## Sprint 2: Visualization and Interactivity

### Sprint Goal
Make the dashboard interactive and visually
useful for exploring water quality data.

### Development Tasks
- Added a measurement selection dropdown.
- Added a record count slider.
- Implemented dynamic data filtering.
- Created an interactive Plotly line chart.
- Added descriptive summary statistics.

### Sprint Review
Users can select measurements, change the
number of displayed records, and explore
interactive charts.

### Sprint Retrospective
Reusing the dropdown and slider selections
for both the data table and the chart helped
keep the application consistent.

## Sprint 3: Testing and User Experience

### Sprint Goal
Improve usability and verify that the
application functions correctly.

### Development Tasks
- Added expandable user instructions.
- Reviewed application layout.
- Prepared a functional testing checklist.

### Functional Testing
- [ ] Application opens without errors.
- [ ] Measurement dropdown works.
- [ ] Record slider works.
- [ ] Plotly chart updates correctly.
- [ ] Summary statistics update correctly.
- [ ] User instructions expand correctly.

### Sprint Review
The application includes the required
dataset, interactive controls, Plotly chart,
and descriptive sections.

### Sprint Retrospective
The dashboard was kept simple to meet
the assignment requirements and allow
future improvements.

## Definition of Done

A feature is complete when:
1. It performs its intended function.
2. It has been tested successfully.
3. The code is organized and readable.
4. Relevant documentation is updated.

## Future Improvements

Future development may include:
- Live data from external APIs
- AI-generated data insights
- Geographic maps
- Additional filtering options

These improvements could be implemented
as part of Project 2.
