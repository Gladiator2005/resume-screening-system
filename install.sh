#!/bin/bash

# Update package lists
sudo apt-get update

# Install poppler-utils and tesseract-ocr
sudo apt-get install -y poppler-utils tesseract-ocr

# Install Python packages from requirements.txt
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm
