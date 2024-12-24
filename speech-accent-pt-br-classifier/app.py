import gradio as gr
import torch
import numpy as np
from transformers import Wav2Vec2Processor, Wav2Vec2ForSequenceClassification

# modelo e o processador
model_name = "results"
processor = Wav2Vec2Processor.from_pretrained(model_name)
model = Wav2Vec2ForSequenceClassification.from_pretrained(model_name)

def classify_accent(audio):
    if audio is None:
        return "Erro: Nenhum áudio recebido"

    # entrada
    print(f"Tipo de entrada de áudio: {type(audio)}")

    # áudio
    print(f"Received audio input: {audio}")

    try:
        audio_array = audio[1]  # O áudio no segundo da tupla
        sample_rate = audio[0]  # A taxa de amostragem no primeiro da tupla

        print(f"Shape do áudio: {audio_array.shape}, Taxa de amostragem: {sample_rate}")

        # 
        audio_array = audio_array.astype(np.float32)

        # taxa de amostragem
        if sample_rate != 16000:
            import librosa
            audio_array = librosa.resample(audio_array, orig_sr=sample_rate, target_sr=16000)

        input_values = processor(audio_array, return_tensors="pt", sampling_rate=16000).input_values
        # Inf
        with torch.no_grad():
            logits = model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1).item()

        # Mapeamento
        labels = ["Brazilian", "Other"]
        return labels[predicted_ids]

    except Exception as e:
        return f"Erro ao processar o áudio: {str(e)}"

# 
description_html = """
<p>Test with recording or uploading an audio file. To test, I recommend short sentences.</p>
<p>Ramon Mayor Martins: <a href="https://rmayormartins.github.io/" target="_blank">Website</a> | <a href="https://huggingface.co/rmayormartins" target="_blank">Spaces</a></p>
"""

# 
interface = gr.Interface(
    fn=classify_accent, 
    inputs=gr.Audio(type="numpy"), 
    outputs="label",
    title="Speech Accent Classifier (Portuguese-Brazilian) v1.3",
    description=description_html
)

interface.launch()
