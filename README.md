# Extract Food Facts

Extract Food Facts leverages advanced LLM (Large Language Models) and OCR (Optical Character Recognition) technologies to efficiently digitize text from food product images, turning them into structured JSON data. This tool specifically targets the extraction of nutritional facts and ingredients, making it an invaluable resource for health enthusiasts and researchers. Access the tool online at [extractfoodfacts.com](https://extractfoodfacts.com).

![OCR Application Interface](static/front.png)

## Features

- **User-Friendly**: Offers both drag-and-drop and file browsing options.
- **Quick Extraction**: Click 'EXTRAIRE' for immediate text conversion.

## Usage

1. Go to [extractfoodfacts.com](https://www.extractfoodfacts.com).
2. Upload an image using drag-and-drop or the 'Parcourir...' option.
3. Click 'EXTRACT' to begin text extraction.
4. Download the `.txt` file with the extracted information.

## Local Setup

Ensure you have Python 3 installed, then follow these steps to set up the application locally:

```bash
# Create a virtual environment
python3 -m venv ocr-env
source ocr-env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Adjust torch package versions as necessary
pip uninstall -y torch torchvision torchaudio
pip install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu
```

### Environment Variable

Before running the application, ensure the `MISTRAL_API_KEY` is set in your environment:

```bash
# Add this line to your .zshrc or .bash_profile, replacing 'your_api_key' with your actual API key
export MISTRAL_API_KEY='your_api_key'
# Then source your profile to load the variable
source ~/.zshrc # or source ~/.bash_profile
```

Alternatively, for a more permanent solution across sessions without needing to source your profile each time, consider adding the environment variable directly to your Supervisor configuration or systemd service file (shown below).

### Running the Application Locally

```bash
# Navigate to the source directory
cd src

# Start the Flask application
python app.py
```

## Deployment in Production on RHEL

For RHEL systems, `supervisor` is not available in the default repositories. We'll use `pip` to install it and manage the process.

### Setting up with Supervisor

1. **Install Supervisor via pip**:

   ```bash
   pip install supervisor
   ```

2. **Create Supervisor Configuration for Extract Food Facts**:

   Create a new file `/etc/supervisord.d/extractfoodfacts.ini` with the following contents:

   ```ini
   [program:extractfoodfacts]
   command=/root/Extract-Food-Facts/ocr-env/bin/gunicorn -w 4 -b 0.0.0.0:5000 app:app
   directory=/root/Extract-Food-Facts/src
   autostart=true
   autorestart=true
   stderr_logfile=/var/log/extractfoodfacts/extractfoodfacts.err.log
   stdout_logfile=/var/log/extractfoodfacts/extractfoodfacts.out.log
   user=root
   environment=MISTRAL_API_KEY="your_actual_api_key"
   ```

   Ensure you replace `"your_actual_api_key"` with the actual Mistral API key.

3. **Create Log Directory**:

   ```bash
   mkdir -p /var/log/extractfoodfacts
   ```

4. **Start Supervisor**:

   If you're not using the system-wide Supervisor service, you can start it manually:

   ```bash
   supervisord -c /etc/supervisord.conf
   ```

   Then control your application with:

   ```bash
   supervisorctl start extractfoodfacts
   ```

### Log Monitoring

To monitor the application logs:

```bash
# For standard output
tail -f /var/log/extractfoodfacts/extractfoodfacts.out.log

# For error output
tail -f /var/log/extractfoodfacts/extractfoodfacts.err.log
```

### Note for Engineers

Ensure the `MISTRAL_API_KEY` environment variable is correctly set in your deployment environment. For a seamless experience, it's recommended to embed this variable directly within your deployment configuration (as shown in the Supervisor example) to avoid having to source environment files manually.

Sure, let's streamline the README sections for credits, license, and contributions into more concise segments.

## License & Credits

**Extract Food Facts** is developed by Meriem Si and is open source, distributed under the MIT License. This license permits free use, modification, and distribution of the software, even for commercial use, with appropriate credit given to the original author.

## Contributing

Contributions to **Extract Food Facts** are welcome! If you have improvements or bug fixes, please follow these steps:

1. **Fork** the repository.
2. **Create** a branch for your changes (`git checkout -b your-branch-name`).
3. **Commit** your improvements (`git commit -am 'Add some feature'`).
4. **Push** to the branch (`git push origin your-branch-name`).
5. Submit a **pull request**.

We appreciate contributions that improve the project's quality and functionality. For significant changes, please open an issue first to discuss what you would like to change.

Ensure your contributions are well-documented and follow the project's code style. By participating in this project, you agree to abide by its terms.
