import matplotlib.pyplot as plt

# Sample data
days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7', 'Day 8', 'Day 9', 'Day 10']
temperature = [24, 26, 22, 23, 27, 25, 21, 28, 26, 24]
rainfall = [10, 5, 0, 7, 15, 2, 0, 20, 3, 12]
wind_speed = [15, 12, 20, 18, 10, 22, 25, 8, 16, 14]

# Plotting the data
plt.plot(days, temperature, label='Avg Temp (°C)', marker='o', color='r')
plt.plot(days, rainfall, label='Rainfall (mm)', marker='s', color='b')
plt.plot(days, wind_speed, label='Wind Speed (km/h)', marker='^', color='g')

# Adding labels and title
plt.xlabel('Days')
plt.ylabel('Values')
plt.title('Weather Data Comparison Over 10 Days')
plt.legend()

# Show the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
