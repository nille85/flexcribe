import whisper

class AudioTranscriber:
    def __init__(self, model_size="large"):
        self.model = whisper.load_model(model_size)

    def transcribe(self, audio_file_path, progress_callback=None):
        result = self.model.transcribe(audio_file_path, fp16=False)
        segments = result["segments"]
        
        full_transcription = ""
        for i, segment in enumerate(segments):
            full_transcription += segment["text"] + " "
            if progress_callback:
                progress_callback((i + 1) / len(segments))
        
        return full_transcription.strip()