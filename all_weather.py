import plotly.express as px
import pandas as pd

# Sample data
data = {
    'Day': ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7', 'Day 8', 'Day 9', 'Day 10'],
    'Avg Temperature (°C)': [24, 26, 22, 23, 27, 25, 21, 28, 26, 24],
    'Rainfall (mm)': [10, 5, 0, 7, 15, 2, 0, 20, 3, 12],
    'Wind Speed (km/h)': [15, 12, 20, 18, 10, 22, 25, 8, 16, 14]
}

# Creating a dataframe
df = pd.DataFrame(data)

# Plotting interactive line chart with Plotly
fig = px.line(df, x='Day', y=['Avg Temperature (°C)', 'Rainfall (mm)', 'Wind Speed (km/h)'],
              title='Weather Data Comparison Over 10 Days')

# Show interactive plot
fig.show()
