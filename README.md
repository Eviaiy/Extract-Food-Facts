# Extract Food Facts

This application is designed to seamlessly extract text from images, offering the convenience of converting the extracted content into a downloadable text file. Specializing in the extraction of nutrition tables and information from any food product images, it further enhances the utility by structuring this data into a JSON file format. Leveraging advanced OCR (Optical Character Recognition) technology, the app ensures accuracy and efficiency in data extraction, making the structured information readily accessible and highly usable for data enthusiasts. Whether for personal health tracking, academic research, or commercial analysis, this tool simplifies the process of obtaining and utilizing nutritional data, turning complex images into easily manageable and analyzable datasets.

![OCR Application Interface](static/front.png)


## Features

- Drag-and-drop and file browsing options.
- Quick text extraction with the 'EXTRAIRE' button.

## Usage

1. Visit the app's webpage.
2. Upload an image via drag-and-drop or by clicking 'Parcourir...'.
3. Click 'EXTRAIRE' to extract text.
4. Download the `.txt` file with the extracted text.

## Installation

1. Clone the repository.
2. Install Python, `flask`, and `easyocr`.
3. Run `flask run` in the app directory.
4. Access at `http://127.0.0.1:5000/`.

## Setup

```bash
python3 -m venv ocr-env
source ocr-env/bin/activate
pip install -r requirements.txt
pip uninstall torch torchvision torchaudio
pip install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu
