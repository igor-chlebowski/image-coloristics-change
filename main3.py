from PIL import Image, ImageEnhance, ImageOps, ImageDraw
import random

def apply_random_color_overlay(image):
    # Create a copy of the original image
    overlayed_image = image.copy()

    # Generate random RGBA values for the overlay color
    overlay_color = (
        random.randint(0, 255),  # Red
        random.randint(0, 255),  # Green
        random.randint(0, 255),  # Blue
        random.randint(100, 192)  # Alpha (semi-transparent range)
    )

    # Create a new image with the same size as the original, filled with the random overlay color
    overlay = Image.new('RGBA', image.size, overlay_color)

    # Blend the overlay with the original image using alpha blending
    overlayed_image = Image.alpha_composite(overlayed_image.convert('RGBA'), overlay)

    # Convert the result back to RGB mode
    return overlayed_image.convert('RGB')

def main():
    # Load an image
    image_path = 'image_path.png'  # Replace with the path to your image file
    image = Image.open(image_path)

    # Apply a completely random color overlay to the image
    overlayed_image = apply_random_color_overlay(image)

    # Save or display the transformed image
    overlayed_image.show()  # Display the image

if __name__ == '__main__':
    main()
