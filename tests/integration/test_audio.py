import os
import pytest
from app import text_to_speech

def test_audio_file_properties():
    output_file = "test_audio.mp3"
    test_text = "Test audio generation"
    
    text_to_speech(test_text, output_file)
    
    # Verify the file exists and has content
    assert os.path.exists(output_file)
    assert os.path.getsize(output_file) > 0
    
    # Cleanup
    os.remove(output_file)