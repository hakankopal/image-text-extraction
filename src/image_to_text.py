import argparse
from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'


def image_to_text(image_path):
    """
    Takes the path of an image file as input and returns the extracted text.
    """
    # Open the image file using PIL
    with Image.open(image_path) as image:
        # Convert the image to grayscale
        grayscale_image = image.convert('L')
        # Use Pytesseract to extract text from the image
        text = pytesseract.image_to_string(grayscale_image)
        return text

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Extract text from an image using OCR')
    parser.add_argument('image_path', type=str, help='Path to the image file')
    args = parser.parse_args()

    # Call the image_to_text function with the image path
    text = image_to_text(args.image_path)
    print(text)