import os
import pandas as pd
import matplotlib.pyplot as plt

# Set the path to your dataset directory
dataset_dir = 'copied images'

# Dictionary to hold the count of files in each subdirectory
class_distribution = {}

# Walk through the dataset directory
for root, dirs, files in os.walk(dataset_dir):
    if root == dataset_dir:
        continue  # Skip the root directory itself
    class_name = os.path.basename(root)  # Get the class name from the folder name
    class_distribution[class_name] = len(files)  # Number of files in this directory

# Convert dictionary to a pandas DataFrame for easy plotting
df = pd.DataFrame(list(class_distribution.items()), columns=['Class', 'Count'])

# Sort the DataFrame by count for better visualization
df = df.sort_values(by='Count', ascending=False)

# Plotting
plt.figure(figsize=(12, 8))  # Set the figure size
plt.bar(df['Class'], df['Count'], color='blue')  # Create a bar chart
plt.xlabel('Class Name')  # Set the x-label
plt.ylabel('Number of Images')  # Set the y-label
plt.title('Distribution of Classes in Dataset')  # Set the title
plt.xticks(rotation=45)  # Rotate class names for better visibility
plt.show()  # Display the plot
