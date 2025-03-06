#!/usr/bin/env python3
import argparse
import os
from app import text_to_speech

def main():
    parser = argparse.ArgumentParser(description='Convert text to speech')
    parser.add_argument('text', help='Text to convert to speech')
    parser.add_argument('-o', '--output', default='output.mp3', help='Output filename (default: output.mp3)')
    
    args = parser.parse_args()
    
    print(f"Converting text to speech: '{args.text}'")
    text_to_speech(args.text, args.output)
    print(f"Speech saved to '{args.output}'")

if __name__ == '__main__':
    main()