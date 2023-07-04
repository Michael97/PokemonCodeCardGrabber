import os

# Create a directory for images to be processed
os.makedirs('image', exist_ok=True)

# Create a directory for failed images
os.makedirs('failed_images', exist_ok=True)

# Create a directory for completed images
os.makedirs('completed_images', exist_ok=True)