# Image Text Extraction with Pytesseract

This repository provides a Python code example for using pytesseract to extract text from images and PDF files.

## Installation

Before using the code, you need to install Tesseract OCR engine on your machine. You can download and install it from [the official Tesseract OCR website](https://github.com/tesseract-ocr/tesseract). After installing Tesseract OCR, you can install pytesseract using pip:

```python
pip install pytesseract
```

## Usage

To use the code, simply run the image_to_text.py file in the src directory:

```css
python src/image_to_text.py --image_path path/to/image.png
```

This will extract text from the specified image and print it to the console.

## Customization

You can customize the OCR process by modifying the options passed to the `image_to_string` function. For example, you can specify the language of the text to be extracted using the `lang` parameter, or you can configure the OCR engine using the `config` parameter. See the [pytesseract documentation](https://tesseract-ocr.github.io/tessdoc/) for more information.

## Contributing

Contributions to this repository are welcome. If you find a bug or have an idea for a new feature, please open an issue or submit a pull request.
