# OCR Application

This Optical Character Recognition (OCR) application is designed to extract text from images and return the extracted content as a downloadable text file.

## Features

- Easy to use drag-and-drop interface for image files.
- Supports 'browse file from device' option for file selection.
- Quick text extraction with a simple click of the 'EXTRAIRE' button.

## How to Use

1. Navigate to the app's webpage.
2. Drag and drop your image file into the dashed rectangle area or click 'Parcourir...' to select an image file from your device.
3. Click the 'EXTRAIRE' button to start the text extraction process.
4. Once the text is extracted, a `.txt` file will be available to download with the recognized text.

## Installation

To set up the OCR application on your local machine, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python installed, along with the `flask` and `easyocr` libraries.
3. Navigate to the app's directory and run `flask run` to start the server.
4. The app will be served at `http://127.0.0.1:5000/` by default.

## Screenshot

![OCR Application Interface](templates/Front.png)
