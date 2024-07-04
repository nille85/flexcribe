# Flexcribe

Flexcribe is an innovative audio recording and transcription tool designed to liberate knowledge workers from their desks. It enables users to capture, transcribe, and edit meeting content with flexibility, promoting a more active and dynamic work environment.

## About

Flexcribe was born from the need to reduce sedentary work habits while ensuring efficient meeting documentation. It allows users to record meetings without being tied to a desk for note-taking, transcribe the audio automatically, and later review and edit the transcriptions as needed.

## Main Features

- **Audio Recording**: Start and stop recording meetings with ease.
- **Automatic Transcription**: Convert recorded audio to text using advanced AI.
- **Transcription Editing**: Review and correct transcriptions for accuracy.
- **Audio Playback**: Listen to recorded meetings alongside transcriptions.
- **Metadata Display**: View information about each recording, including duration and creation time.
- **User-Friendly Interface**: Intuitive Gradio-based UI for easy interaction.


## Installation

### Prerequisites

- Python 3.11 or higher
- [Poetry](https://python-poetry.org/docs/#installation)

### Steps

1. Clone the repository: 
    * `git clone https://github.com/nille85/flexcribe.git`
    * `cd flexcribe`
2. Install dependencies using Poetry:
    * `poetry install` : This command will create a virtual environment and install all the dependencies specified in the `pyproject.toml` file
3. Activate the virtual environment:
    * `poetry shell`

## Data Storage

By default, the application stores data in the following locations:

- Recordings: `data/recordings/`
- Transcriptions: `data/transcriptions/`

These directories need to be created manually before running the application. If you wish to use different locations, you can modify the paths in the `AppService` class.

## Running Flexcribe

To start the application, ensure you're in the Poetry shell and run: `python main.py`
This will launch the Gradio interface in your default web browser.


## Contributing

We welcome contributions to Flexcribe! Please feel free to submit issues, fork the repository and send pull requests!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



---

Happy Flexcribing! Move more, sit less, and never miss a word from your meetings.