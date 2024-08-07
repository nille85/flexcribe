import gradio as gr
from app_service import AppService
import os

def create_gradio_interface():
    app = AppService()
    
    def stop_and_refresh_audio_files():
        status = app.stop_recording()
        dropdown =  gr.Dropdown(label="Select Audio File", choices=app.get_audio_files())
        return [status,dropdown]


    with gr.Blocks() as interface:
        gr.Markdown("# Flexcribe")
        
        with gr.Row():
            start_btn = gr.Button("Start Recording")
            stop_btn = gr.Button("Stop Recording")
        
        status_output = gr.Textbox(label="Status")
        
        with gr.Row():
            audio_files_dropdown = gr.Dropdown(label="Select Audio File", choices=app.get_audio_files())
           
        
        audio_player = gr.Audio(label="Audio Player", type="filepath")
        audio_metadata = gr.JSON(label="Audio Metadata")
        
        transcribe_btn = gr.Button("Transcribe Selected Audio")
        transcription_output = gr.Textbox(label="Transcription", lines=10)
        
        save_transcription_btn = gr.Button("Save Edited Transcription")
        save_status = gr.Textbox(label="Save Status")
        
        start_btn.click(app.start_recording, outputs=status_output)
        stop_btn.click(stop_and_refresh_audio_files, outputs=[status_output, audio_files_dropdown])
        
   
        


        def update_audio_player_and_metadata(audio_file):

            if audio_file:
                full_path = os.path.join(app.file_manager.recordings_dir, audio_file)
                metadata = app.get_audio_metadata(audio_file)
                return full_path, metadata
            return None, None
        
        

        audio_files_dropdown.select(
            update_audio_player_and_metadata,
            inputs=audio_files_dropdown,
            outputs=[audio_player, audio_metadata]
        )
        
        transcribe_btn.click(
            app.transcribe_audio,
            inputs=audio_files_dropdown,
            outputs=[transcription_output, audio_metadata],
            show_progress=True,
        )
        
        audio_files_dropdown.select(app.load_transcription, inputs=audio_files_dropdown, outputs=transcription_output)
        
        save_transcription_btn.click(
            app.save_edited_transcription,
            inputs=[audio_files_dropdown, transcription_output],
            outputs=save_status
        )
    
    return interface