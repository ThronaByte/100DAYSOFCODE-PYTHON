import matplotlib.pyplot as plt
import numpy as np

# Define the days and their activities
days = [
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday", 
    "Saturday", 
    "Sunday"
]

# Activities arranged in a grid-like structure
activities = [
    [
        "7:00 AM - Pray\n7:30 AM - Meditate\n8:00 AM - Chores\n8:30 AM - Wash Up\n9:00 AM - Study (4h)\n1:00 PM - Meditate on Study\n1:30 PM - Work (8h)\n9:30 PM - Free Time\n10:30 PM - Meditate"
    ],
    [
        "7:00 AM - Pray\n7:30 AM - Meditate\n8:00 AM - Chores\n8:30 AM - Wash Up\n9:00 AM - Study (4h)\n1:00 PM - Meditate on Study\n1:30 PM - Work (8h)\n9:30 PM - Free Time\n10:30 PM - Meditate"
    ],
    [
        "7:00 AM - Pray\n7:30 AM - Meditate\n8:00 AM - Chores\n8:30 AM - Wash Up\n9:00 AM - Study (4h)\n1:00 PM - Meditate on Study\n1:30 PM - Work (8h)\n9:30 PM - Free Time\n10:30 PM - Meditate\n7:00 PM - Personal Growth Post"
    ],
    [
        "7:00 AM - Pray\n7:30 AM - Meditate\n8:00 AM - Chores\n8:30 AM - Wash Up\n9:00 AM - Study (4h)\n1:00 PM - Meditate on Study\n1:30 PM - Work (8h)\n9:30 PM - Free Time\n10:30 PM - Meditate"
    ],
    [
        "7:00 AM - Pray\n7:30 AM - Meditate\n8:00 AM - Chores\n8:30 AM - Wash Up\n9:00 AM - Study (4h)\n1:00 PM - Meditate on Study\n1:30 PM - Work (8h)\n9:30 PM - Free Time\n10:30 PM - Meditate\n7:00 PM - Nature & Tech Post"
    ],
    [
        "7:00 AM - Pray\n7:30 AM - Meditate\n8:00 AM - Chores\n8:30 AM - Wash Up\n9:00 AM - Study (4h)\n1:00 PM - Meditate on Study\n1:30 PM - Work (8h)\n9:30 PM - Free Time\n10:30 PM - Meditate\n7:00 PM - Tech Trends Post"
    ],
    [
        "7:00 AM - Pray\n7:30 AM - Meditate\n8:00 AM - Chores\n8:30 AM - Wash Up\n9:00 AM - Study (4h)\n1:00 PM - Meditate on Study\n1:30 PM - Work (8h)\n9:30 PM - Free Time\n10:30 PM - Meditate\n7:00 PM - Coding Project Showcase"
    ]
]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 10))

# Create a table to display activities
table_data = []
for i in range(len(days)):
    row = [days[i]] + activities[i]
    table_data.append(row)

# Create the table
table = ax.table(cellText=table_data, 
                 colLabels=["Day", "Activities"], 
                 cellLoc='center', 
                 loc='center')

# Adjust table aesthetics
table.auto_set_font_size(False)
table.set_fontsize(12)

# Set fixed width for the columns to ensure alignment
table.scale(1.2, 1.5)  # Scale table size

# Adjust column widths
for key, cell in table.get_celld().items():
    cell.set_edgecolor('black')  # Add borders
    cell.set_facecolor('#f2f2f2')  # Light gray background for cells
    if key[0] == 0:  # Header row
        cell.set_fontsize(14)
        cell.set_text_props(weight='bold', color='black')
    else:
        cell.set_fontsize(12)

    # Set widths for the first and second columns
    if key[1] == 0:  # First column (Days)
        cell.set_width(0.2)  # Set a width for the day column
    elif key[1] == 1:  # Second column (Activities)
        cell.set_width(0.8)  # Set a width for the activities column

# Set the title
ax.set_title('Weekly Routine and Content Calendar', fontsize=16)

# Hide axes
ax.axis('off')

# Show the plot
plt.tight_layout()
plt.show()
