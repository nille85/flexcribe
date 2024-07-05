import pyaudio
import wave

class AudioRecorder:
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.is_recording = False
        self.frames = []
        self.current_filename = None

    def start_recording(self, filename):
        if self.is_recording:
            return "Already recording. Stop the current recording first."
        self.current_filename = filename
        self.is_recording = True
        self.frames = []
        self.stream = self.audio.open(format=pyaudio.paInt16,
                                      channels=1,
                                      rate=44100,
                                      input=True,
                                      frames_per_buffer=1024,
                                      stream_callback=self.callback)
        self.stream.start_stream()
        return f"Recording started: {self.current_filename}"

    def stop_recording(self):
        if not self.is_recording:
            return "No active recording to stop."
        
        self.stream.stop_stream()
        self.stream.close()
        self.is_recording = False
        self.save_audio()
        return f"Recording stopped and saved: {self.current_filename}"

    def callback(self, in_data, frame_count, time_info, status):
        self.frames.append(in_data)
        return (in_data, pyaudio.paContinue)

    def save_audio(self):
        wf = wave.open(self.current_filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(self.frames))
        wf.close()


    def __del__(self):
        self.audio.terminate()