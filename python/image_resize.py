from PIL import Image
import os

# Input and output directories
input_dir = "old"
output_dir = "new"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Maximum width for resizing
max_width = 500
image_no = 1

# Function to resize and save an image
def resize_and_save_image(input_path, output_path, max_width):
    try:
        with Image.open(input_path) as img:
            # Calculate the new height to maintain aspect ratio
            width_percent = max_width / float(img.size[0])
            new_height = int(float(img.size[1]) * float(width_percent))
            
            # Resize the image using Lanczos filter for quality
            resized_img = img.resize((max_width, new_height), Image.LANCZOS)
            
            # Save the resized image
            resized_img.save(output_path)
        return True
    except Exception as e:
        # Handle errors and log them
        print(f"Error resizing {input_path}: {str(e)}")
        return False

# Process all images in the input directory
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.jpg', '.webp', '.jpeg', '.png', '.gif', '.bmp')):
        input_path = os.path.join(input_dir, filename)
        output_filename = f"min_{filename}"
        output_path = os.path.join(output_dir, output_filename)
        
        # Print progress
        print(f"Processing image_no {image_no}")
        
        # Call the resize_and_save_image function
        if resize_and_save_image(input_path, output_path, max_width):
            print(f"Resized and saved {output_filename}")
            image_no += 1

# Print completion message
print("All images resized and saved.")
