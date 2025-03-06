# Text-to-Speech Application

A simple Text-to-Speech application using Google's TTS service.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python cli.py "Hello, this is a text to speech conversion"
```

Or specify an output file:

```bash
python cli.py "Custom message" -o custom.mp3
```

## Testing

To run tests:

```bash
pytest
```

## Features

- Convert text to natural-sounding speech
- Save output to MP3 file
- Simple command-line interface
