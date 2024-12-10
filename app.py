from flask import Flask, request, render_template, send_from_directory
from pytube import YouTube
from transformers import pipeline
import os
import whisper
import ssl

app = Flask(__name__)

# Downloads directory
DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

ssl._create_default_https_context = ssl._create_unverified_context

def download_audio(video_url, output_path=DOWNLOAD_FOLDER):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    try:
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        
        print(f"Downloading audio from: {yt.title}")
        print(f"Author: {yt.author}")
        
        audio_file = audio_stream.download(output_path, filename="audio.mp4")
        print(f"Download successful! File saved at: {audio_file}")
        return audio_file
    except Exception as e:
        print(f"Download error: {e}")
        return None

def transcribe_audio(audio_path):
    try:
        model = whisper.load_model("base")
        print("Transcribing audio...")
        result = model.transcribe(audio_path)
        return result['text']
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None
    
def summarize_text(text):
    try:
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        print("Generating summary...")
        summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print(f"Error during summarization: {e}")
        return None

# Flask Routes
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_url = request.form.get("video_url")
        if not video_url:
            return render_template("index.html", error="Please provide a YouTube video URL.")
        
        # Download audio
        audio_path = download_audio(video_url)
        if not audio_path:
            return render_template("index.html", error="Failed to download audio.")
        
        # Transcribe audio
        transcript = transcribe_audio(audio_path)
        if not transcript:
            return render_template("index.html", error="Failed to transcribe audio.")
        
        # Summarize text
        summary = summarize_text(transcript)
        if not summary:
            return render_template("index.html", error="Failed to summarize text.")
        
        # Remove audio file after use (optional)
        os.remove(audio_path)
        
        return render_template("index.html", summary=summary, transcript=transcript)
    
    return render_template("index.html")

@app.route("/downloads/<filename>")
def downloads(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename)

@app.route("/test")
def test():
    return "Flask is working!"

if __name__ == "__main__":
    app.run(debug=True)
