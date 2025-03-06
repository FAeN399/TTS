import pytest
import os
from app import text_to_speech

def test_text_to_speech_creates_file():
    output_file = "test_output.mp3"
    test_text = "Hello, this is a test"
    
    text_to_speech(test_text, output_file)
    
    assert os.path.exists(output_file)
    assert os.path.getsize(output_file) > 0
    
    # Cleanup
    os.remove(output_file)

def test_text_to_speech_handles_empty_text():
    with pytest.raises(ValueError):
        text_to_speech("")
