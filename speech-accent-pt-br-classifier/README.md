---
title: Speech-accent-pt-br-classifier
emoji: 🎙️🤖🇧🇷
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "4.12.0"
app_file: app.py
pinned: false
---

# Speech Portuguese (Brazilian) Accent Classifier

This project is a speech accent classifier that distinguishes between Portuguese (Brazilian) and other accents.

## Project Overview

This application uses a trained model to classify speech accents into two categories:
1. Portuguese (Brazilian)
2. Other

The model is based on the author's work [(results) brazil pt accent] and utilizes the Portuguese portion of the Common Voice dataset (version 11.0) from Mozilla Foundation.

## Dataset

The project uses the Portuguese subset of the Common Voice dataset:
- Dataset: "mozilla-foundation/common_voice_11_0", "pt"

Brazilian accents included in the dataset:
- Português do Brasil, Região Sul do Brasil
- Paulistano
- Paulista, Brasileiro
- Carioca
- Mato Grosso
- Mineiro
- Interior Paulista
- Gaúcho
- Nordestino
- And various regional mixes

## Technical Details

The project utilizes the following model and processor:
- Model: "facebook/wav2vec2-base-960h"
- Processor: Wav2Vec2Processor.from_pretrained

## License

ecl

## Developer Information

Developed by Ramon Mayor Martins (2024)
- Email: rmayormartins@gmail.com
- Homepage: https://rmayormartins.github.io/
- Twitter: @rmayormartins
- GitHub: https://github.com/rmayormartins

## Acknowledgements

Special thanks to Instituto Federal de Santa Catarina (Federal Institute of Santa Catarina) IFSC-São José-Brazil.

## Contact

For any queries or suggestions, please contact the developer using the information provided above.