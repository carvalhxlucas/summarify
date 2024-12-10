# 🎥 Summarify

This project is a web-based tool that downloads the audio from YouTube videos, transcribes the content using the **Whisper** model, and generates a summary of the transcribed text using **Transformers** with the `facebook/bart-large-cnn` model.

## 🚀 Features

- **Web Interface**: A simple and intuitive interface for users to input a YouTube video URL and view the results directly in their browser.
- **Audio Download**: Extracts only the audio from a YouTube video.
- **Transcription**: Converts the audio to text using the Whisper model.
- **Summarization**: Produces a concise summary of the transcription using Transformers.

## 🔧 Technologies Used

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/) - For building the web interface.
- [Pytube](https://pytube.io/) - For downloading audio from YouTube.
- [Whisper](https://github.com/openai/whisper) - For audio transcription.
- [Transformers](https://huggingface.co/transformers/) - For text summarization.
- [Hugging Face Model](https://huggingface.co/facebook/bart-large-cnn) - The `facebook/bart-large-cnn` model for summarization.

## 🗒 Prerequisites

Ensure **Python 3.8 or higher** is installed and install the required libraries:

```bash
pip install flask pytube whisper transformers torch
```

## 📂 Project Structure

```
📆 Summarify
 ├── 🗂 downloads
 │   └── (Downloaded audio files will be saved here)
 ├── 🗂 templates
 │   └── index.html
 ├── 🗂 static
 │   └── styles.css
 ├── app.py
 ├── requirements.txt
 └── README.md
```

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/carvalhxlucas/summarify.git
   cd Summarify
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

4. Open your web browser and go to `http://127.0.0.1:5000`.

5. Enter the YouTube video URL in the input field and click "Submit" to get the summary.

## 🔧 Customizations

- **Change the Output Directory**:
  - Modify the `DOWNLOAD_FOLDER` variable in `app.py` to set a different path for downloaded audio files.

- **Adjust the Summary Length**:
  - Update the `max_length` and `min_length` parameters in the `summarize_text` function in `app.py`.

## 🔧 Adding Styles

- The web interface styling is handled by `static/styles.css`. Feel free to update this file to customize the appearance of the page.

---

Ready to collaborate or improve this project? Have questions? Let me know! 😊

