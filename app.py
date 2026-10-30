
import streamlit as st
import pandas as pd
import plotly.express as px

# Configure the application
st.set_page_config(
    page_title="Biscayne Bay Water Quality Dashboard",
    page_icon="💧",
    layout="wide"
)

# Application title
st.title("💧 Biscayne Bay Water Quality Dashboard")

# User instructions
with st.expander("How to Use This Dashboard"):
    st.write(
        """
        1. Select a water quality measurement
           using the dropdown menu.
        2. Adjust the slider to control how
           many records are displayed.
        3. Review the filtered data table.
        4. Explore the interactive Plotly chart.
        5. Hover over data points for details.
        6. Review the summary statistics.
        7. Read any data quality warnings.
        """
    )

st.write(
    "Explore water quality measurements collected "
    "in Biscayne Bay, Florida."
)

# Load the CSV dataset
df = pd.read_csv("data/biscayneBay_waterquality.csv")

# Select relevant water quality columns
water_quality = df[
    [
        "Date",
        "Time hh:mm:ss",
        "Latitude",
        "Longitude",
        "Temp C",
        "pH",
        "Turbid+ NTU",
        "Sal ppt",
        "ODO mg/L"
    ]
].copy()

# Overview Section
st.header("Overview")

st.write(
    "This dashboard displays measurements of "
    "temperature, pH, turbidity, salinity, "
    "and dissolved oxygen in Biscayne Bay."
)

# Display dataset statistics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Records", len(water_quality))

with col2:
    st.metric("Measurements", 5)

with col3:
    st.metric("Dataset Columns", len(df.columns))

# Interactive Controls Section
st.header("Interactive Controls")

st.write(
    "Use the controls below to select a water "
    "quality measurement and change how many "
    "records are displayed."
)

# Define the measurement options
measurements = {
    "Water Temperature (°C)": "Temp C",
    "pH Level": "pH",
    "Turbidity (NTU)": "Turbid+ NTU",
    "Salinity (ppt)": "Sal ppt",
    "Dissolved Oxygen (mg/L)": "ODO mg/L"
}

# Dropdown for measurement selection
selected_measurement = st.selectbox(
    "Select a water quality measurement:",
    options=list(measurements.keys())
)

# Get the CSV column corresponding to the selection
selected_column = measurements[selected_measurement]

# Slider for number of records to display
record_count = st.slider(
    "Number of records to display:",
    min_value=10,
    max_value=len(water_quality),
    value=min(50, len(water_quality)),
    step=1
)

# Data Display Section
st.header("Water Quality Data")

st.write(
    f"Displaying the first {record_count} records "
    f"for {selected_measurement}."
)

# Filter the dataset based on user selections
filtered_data = water_quality[
    ["Date", "Time hh:mm:ss", selected_column]
].head(record_count).copy()

# Reset displayed row numbers to start at 1
filtered_data.index = range(1, len(filtered_data) + 1)

# Display filtered data
st.dataframe(
    filtered_data,
    use_container_width=True
)


# Data Visualization Section
st.header("Interactive Data Visualization")

st.write(
    "The chart below displays the selected water "
    "quality measurement across the currently "
    "selected records."
)

# Prepare data for visualization
chart_data = filtered_data.copy()

# Add a measurement number for the horizontal axis
chart_data["Measurement Number"] = range(
    1, len(chart_data) + 1
)

# Create an interactive line chart
fig = px.line(
    chart_data,
    x="Measurement Number",
    y=selected_column,
    title=f"{selected_measurement} in Biscayne Bay",
    labels={
        "Measurement Number": "Measurement Number",
        selected_column: selected_measurement
    },
    markers=True
)

# Add a legend label
fig.update_traces(name=selected_measurement, showlegend=True)

# Improve the chart layout
fig.update_layout(
    xaxis_title="Measurement Number",
    yaxis_title=selected_measurement,
    legend_title="Water Quality Measurement",
    hovermode="x unified"
)

# Display Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Insights Section
st.header("Insights")

st.write(
    f"Summary statistics for {selected_measurement} "
    "across the records currently displayed:"
)

# Calculate statistics
average_value = filtered_data[selected_column].mean()
minimum_value = filtered_data[selected_column].min()
maximum_value = filtered_data[selected_column].max()

# Display statistics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Average", f"{average_value:.2f}")

with col2:
    st.metric("Minimum", f"{minimum_value:.2f}")

with col3:
    st.metric("Maximum", f"{maximum_value:.2f}")

st.caption(
    "Source: Biscayne Bay water quality CSV. "
    "Results are descriptive and have not been "
    "quality-controlled."
)
