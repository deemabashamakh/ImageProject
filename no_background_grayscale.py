import os
import cv2

def convert_to_grayscale_nested(input_dir, output_base_dir='grayscale_images'):
    # Ensure the base directory for output exists
    if not os.path.exists(output_base_dir):
        os.makedirs(output_base_dir)

    # Walk through all directories and subdirectories in the input directory
    for root, dirs, files in os.walk(input_dir):
        # Construct the path for the new directory
        rel_path = os.path.relpath(root, input_dir)  # Get relative path to maintain directory structure
        output_dir = os.path.join(output_base_dir, rel_path)

        # Prepare the output directory
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Process each file in the current directory
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):  # Check for image files
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_dir, file)
                
                # Read the image in grayscale
                img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
                
                # Save the grayscale image
                cv2.imwrite(output_path, img)

# Usage example:
convert_to_grayscale_nested('background_removed')
