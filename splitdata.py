import os
import shutil
from sklearn.model_selection import train_test_split

# Paths
dataset_dir = 'RGB ArSL dataset'
train_dir = 'train'
test_dir = 'test'

# Ensure training and testing directories exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Split ratio
test_size = 0.2  # 20% of the data will be used for testing

# Process each class
for class_name in os.listdir(dataset_dir):
    class_dir = os.path.join(dataset_dir, class_name)
    if not os.path.isdir(class_dir):
        continue  # Skip any non-directory entries

    # Get all file names
    files = [os.path.join(class_dir, f) for f in os.listdir(class_dir) if os.path.isfile(os.path.join(class_dir, f))]
    
    # Split files into train and test
    train_files, test_files = train_test_split(files, test_size=test_size, random_state=42)

    # Create class directories in train and test directories
    os.makedirs(os.path.join(train_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(test_dir, class_name), exist_ok=True)

    # Move files
    for f in train_files:
        shutil.move(f, os.path.join(train_dir, class_name))
    for f in test_files:
        shutil.move(f, os.path.join(test_dir, class_name))

print("Dataset successfully split into train and test directories.")
