from flask import Flask, request, send_file, render_template
import easyocr
import io

app = Flask(__name__)

# Initialize EasyOCR reader with desired languages
reader = easyocr.Reader(['en', 'fr'])  # e.g., ['en', 'fr']

@app.route('/')
def home():
    # Serve the HTML page for uploading images
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file:
        # Read the file as bytes directly
        image_bytes = file.read()
        
        # Perform OCR using EasyOCR
        results = reader.readtext(image_bytes, paragraph=True)  # `paragraph=True` may help with grouping text
        
        # Correctly extract the text part from the results
        extracted_text = "\n".join([result[1] for result in results])

        # Create an in-memory text file to return
        mem = io.BytesIO()
        mem.write(extracted_text.encode('utf-8'))
        mem.seek(0)  # Go to the start of the IO stream
        
        return send_file(mem, as_attachment=True, attachment_filename="recognized_text.txt", mimetype="text/plain")

if __name__ == '__main__':
    app.run(debug=True)