# Extract Food Facts

Leveraging LLM and OCR technologies, this tool efficiently extracts text from food product images, including nutrition details, and converts it into structured JSON data. It offers precise content extraction in a user-friendly format, ideal for data enthusiasts engaged in health tracking or research. You can access the app in www.extractfoodfacts.com

![OCR Application Interface](static/front.png)


## Features

- Drag-and-drop and file browsing options.
- Quick text extraction with the 'EXTRAIRE' button.

## Usage

1. Visit the app's webpage.
2. Upload an image via drag-and-drop or by clicking 'Parcourir...'.
3. Click 'EXTRAIRE' to extract text.
4. Download the `.txt` file with the extracted text.

## Setup

```bash
python3 -m venv ocr-env
source ocr-env/bin/activate
pip install -r requirements.txt
pip uninstall torch torchvision torchaudio
pip install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu

## Start the app

```bash
cd src
python app.py
