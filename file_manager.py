import os
import uuid
from datetime import datetime
import mutagen

class FileManager:
    def __init__(self, recordings_dir="recordings", transcriptions_dir="transcriptions"):
        self.recordings_dir = recordings_dir
        self.transcriptions_dir = transcriptions_dir
        os.makedirs(self.recordings_dir, exist_ok=True)
        os.makedirs(self.transcriptions_dir, exist_ok=True)
        self.audio_files = self.get_audio_files()

    def generate_filename(self):
        unique_id = str(uuid.uuid4())
        return os.path.join(self.recordings_dir, f"recorded_audio_{unique_id}.wav")

    def add_audio_file(self, filename):
        self.audio_files.append(os.path.basename(filename))

    def get_audio_files(self):
        return [f for f in os.listdir(self.recordings_dir) if f.endswith('.wav')]

    def get_audio_metadata(self, audio_file):
        full_path = os.path.join(self.recordings_dir, audio_file)
        audio = mutagen.File(full_path)
        duration = audio.info.length
        creation_time = datetime.fromtimestamp(os.path.getctime(full_path))
        is_transcribed = os.path.exists(os.path.join(self.transcriptions_dir, f"{audio_file}.txt"))
        
        return {
            "Duration": f"{duration:.2f} seconds",
            "Recorded": creation_time.strftime("%Y-%m-%d %H:%M:%S"),
            "Transcribed": "Yes" if is_transcribed else "No"
        }

    def save_transcription(self, audio_file, transcription):
        transcription_file = os.path.join(self.transcriptions_dir, f"{audio_file}.txt")
        with open(transcription_file, 'w') as f:
            f.write(transcription)

    def load_transcription(self, audio_file):
        transcription_file = os.path.join(self.transcriptions_dir, f"{audio_file}.txt")
        if os.path.exists(transcription_file):
            with open(transcription_file, 'r') as f:
                return f.read()
        return "Transcription not found. Please transcribe the audio first."