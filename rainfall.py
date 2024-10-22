import matplotlib.pyplot as plt

# Sample data
days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7', 'Day 8', 'Day 9', 'Day 10']
rainfall = [10, 5, 0, 7, 15, 2, 0, 20, 3, 12]

# Plotting bar chart
plt.bar(days, rainfall, color='blue')

# Adding labels and title
plt.xlabel('Days')
plt.ylabel('Rainfall (mm)')
plt.title('Daily Rainfall Over 10 Days')

# Show the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
