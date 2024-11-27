
# 🎥 YouTube Audio Summarizer  

This project downloads the audio from YouTube videos, transcribes the content using the **Whisper** model, and generates a summary of the transcribed text using **Transformers** with the `facebook/bart-large-cnn` model.  

## 🚀 Features  

- **Audio Download**: Extracts only the audio from a YouTube video.  
- **Transcription**: Converts the audio to text using the Whisper model.  
- **Summarization**: Produces a concise summary of the transcription using Transformers.  

## 🛠️ Technologies Used  

- [Python](https://www.python.org/)  
- [Pytube](https://pytube.io/) - For downloading audio from YouTube.  
- [Whisper](https://github.com/openai/whisper) - For audio transcription.  
- [Transformers](https://huggingface.co/transformers/) - For text summarization.  
- [Hugging Face Model](https://huggingface.co/facebook/bart-large-cnn) - The `facebook/bart-large-cnn` model for summarization.  

## 📝 Prerequisites  

Ensure **Python 3.8 or higher** is installed and install the required libraries:  

```bash  
pip install pytube whisper transformers torch  
```  

## 📂 Project Structure  

```  
📦 YouTube Audio Summarizer  
 ┣ 📂 downloads  
 ┃ ┗ 📜 (Downloaded audio files will be saved here)  
 ┣ 📜 main.py  
 ┗ 📜 README.md  
```  

## ▶️ How to Run  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/yourusername/YouTube-Audio-Summarizer.git  
   cd YouTube-Audio-Summarizer  
   ```  

2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. Run the script:  
   ```bash  
   python main.py  
   ```  

4. Enter the YouTube video URL when prompted.  

5. The summary will be displayed in the terminal!  

## 🔧 Customizations  

- Change the output directory for downloaded audio files:  
  - Modify the `output_path` value in the `download_audio` function.  

- Adjust the summary length:  
  - Update the `max_length` and `min_length` parameters in the `summarize_text_with_transformers` function.  

## 📜 License  

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.  

---

Ready to collaborate or improve this project? Have questions? Let me know! 😊
