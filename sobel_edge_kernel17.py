import os
import cv2
import numpy as np

def sobel_edge_detection(input_dir, output_base_dir='sobel_edges'):
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
                image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
                
                # Sobel Edge Detection
                sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=17)
                sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=17)

                # Calculate the gradient magnitude
                gradient_magnitude = np.sqrt(sobelx**2 + sobely**2)

                # Convert the magnitude image to uint8
                gradient_magnitude = np.uint8(255 * gradient_magnitude / np.max(gradient_magnitude))

                # Save the processed image
                cv2.imwrite(output_path, gradient_magnitude)

# Usage example:
sobel_edge_detection('grayscale_images')
