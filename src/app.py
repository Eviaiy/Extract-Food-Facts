import io
import json
import os

from flask import Flask, render_template, request, send_file
import easyocr
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage


# Calculate the absolute path to the 'src' directory
src_dir = os.path.abspath(os.path.dirname(__file__))

# Calculate the absolute path to the root directory of your project
project_root = os.path.join(src_dir, '..')

# Specify the static and templates directories paths
static_dir = os.path.join(project_root, 'static')
template_dir = os.path.join(project_root, 'templates')

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)


reader = easyocr.Reader(['en'])  # Initialize EasyOCR reader

def get_mistral_response(user_content):
    api_key = os.getenv('MISTRAL_API_KEY')
    if not api_key:
        raise ValueError("Mistral API key not found in environment variables")

    client = MistralClient(api_key=api_key)
    model = "mistral-small"  # Adjust as necessary

    prompt = """
    Here is the text extracted from an image of a nutrition facts label:
    {}
    Convert this information into a JSON object with the following fields:
    id, product, ingredients, and nutrition.
    """.format(user_content)

    messages = [ChatMessage(role="user", content=prompt)]
    chat_response = client.chat(model=model, messages=messages)

    response_content = chat_response.choices[0].message.content if chat_response.choices else ""

    return response_content

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file:
        image_bytes = file.read()
        ocr_results = reader.readtext(image_bytes, paragraph=True)
        extracted_text = "\n".join([result[1] for result in ocr_results])

        json_response = get_mistral_response(extracted_text)

        mem = io.BytesIO()
        mem.write(json_response.encode('utf-8'))
        mem.seek(0)

        return send_file(mem, as_attachment=True, attachment_filename="extracted_data.json", mimetype="application/json")

if __name__ == '__main__':
    app.run(debug=True)
