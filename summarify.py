from pytube import YouTube
from transformers import pipeline
import os
import whisper

# os.environ["OPENAI_API_KEY"] = "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"

# ssl._create_default_https_context = ssl._create_unverified_context

def download_audio(video_url, output_path="downloads"):
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

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    output_path = "downloads"
    
    # audio download
    audio_path = download_audio(video_url, output_path)
    if not audio_path:
        print("Failed to download audio. Exiting.")
        exit()

    # audio transcript
    transcript = transcribe_audio(audio_path)
    if not transcript:
        print("Failed to transcribe audio. Exiting.")
        exit()

    # print("Transcript:", transcript)

    # audio summary
    summary = summarize_text(transcript)
    if not summary:
        print("Failed to generate summary. Exiting.")
        exit()

    print("Summary:", summary)

