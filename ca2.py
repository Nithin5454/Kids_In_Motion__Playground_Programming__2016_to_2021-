import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the file
path = r"C:\Users\velam\OneDrive\Documents\_Kids_In_Motion__Playground_Programming__2016_to_2021.csv"
# Convert dates
data['Start_Date'] = pd.to_datetime(data['Week Start Date'])
data['End_Date'] = pd.to_datetime(data['Week End date'])

# Extract year and month
data['Year'] = data['Start_Date'].dt.year
data['Month'] = data['Start_Date'].dt.month

# Objective 1: Total Attendance Per Year
data.groupby('Year')['Total Attendance'].sum().plot(
    kind='line',
    marker='o',
    color='blue',
    figsize=(10, 6),
    title="Total Attendance Per Year"
)
plt.xlabel("Year")
plt.ylabel("Total Attendance")
plt.grid(True)
plt.tight_layout()
plt.show()

# Objective 2: Average Monthly Attendance Trend
data.groupby('Month')['Total Attendance'].mean().plot(
    kind='bar',
    color='orange',
    figsize=(10, 6),
    title="Average Monthly Attendance"
)
plt.xlabel("Month")
plt.ylabel("Average Attendance")
plt.xticks(
    ticks=range(1, 13),
    labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    rotation=45
)
plt.tight_layout()
plt.show()

# Objective 3: Average Attendance by Day of Week
day_columns = [f"{day}'s Attendance" for day in ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']]
data[day_columns].mean().plot(
    kind='bar',
    color='purple',
    figsize=(10, 6),
    title="Average Attendance by Day of the Week"
)
plt.ylabel("Average Attendance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Objective 4: Number of Programs Offered Per Year
data.groupby('Year').size().plot(
    kind='line',
    marker='o',
    color='red',
    figsize=(10, 6),
    title="Number of Programs Offered Each Year"
)
plt.xlabel("Year")
plt.ylabel("Number of Programs")
plt.grid(True)
plt.tight_layout()
plt.show()

# Objective 5: Program Duration vs Attendance
data['Program_Duration_Days'] = (data['End_Date'] - data['Start_Date']).dt.days
plt.figure(figsize=(10, 6))
plt.scatter(
    data['Program_Duration_Days'],
    data['Total Attendance'],
    alpha=0.6,
    color='teal'
)
plt.title("Program Duration vs Total Attendance")
plt.xlabel("Program Duration (in Days)")
plt.ylabel("Total Attendance")
plt.grid(True)
plt.tight_layout()
plt.show()
