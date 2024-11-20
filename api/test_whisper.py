import whisper

try:
    print("Loading Whisper model...")
    model = whisper.load_model("base", device="cpu")
    print("Model loaded successfully.")
    
    # Test transcription with a sample audio file
    result = model.transcribe("sample_audio.wav")
    print("Transcription: ", result['text'])
except Exception as e:
    print("Error loading Whisper model:", e)
