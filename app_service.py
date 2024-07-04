from audio_recorder import AudioRecorder
from audio_transcriber import AudioTranscriber
from file_manager import FileManager
import os

class AppService:
    def __init__(self):
        self.file_manager = FileManager(recordings_dir="data/recordings", transcriptions_dir="data/transcriptions")
        self.recorder = AudioRecorder(self.file_manager)
        self.transcriber = AudioTranscriber()

    def start_recording(self):
        return self.recorder.start_recording()

    def stop_recording(self):
        return self.recorder.stop_recording()

    def transcribe_audio(self, audio_file, progress_callback=None):
        full_path = os.path.join(self.file_manager.recordings_dir, audio_file)
        transcription = self.transcriber.transcribe(full_path, progress_callback)
        self.file_manager.save_transcription(audio_file, transcription)
        return transcription, self.file_manager.get_audio_metadata(audio_file)

    def get_audio_files(self):
        return self.file_manager.get_audio_files()

    def get_audio_metadata(self, audio_file):
        return self.file_manager.get_audio_metadata(audio_file)

    def load_transcription(self, audio_file):
        return self.file_manager.load_transcription(audio_file)

    def save_edited_transcription(self, audio_file, edited_text):
        self.file_manager.save_transcription(audio_file, edited_text)
        return f"Edited transcription saved for {audio_file}"