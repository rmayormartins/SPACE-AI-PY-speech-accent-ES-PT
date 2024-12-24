import gradio as gr
import torch
import numpy as np
import librosa
from transformers import Wav2Vec2Processor, Wav2Vec2ForSequenceClassification
from safetensors.torch import load_file

# Caminho para o modelo e processador
model_name = 'results'
processor = Wav2Vec2Processor.from_pretrained(model_name)

# Carregar o modelo do arquivo safetensors
state_dict = load_file(f"{model_name}/model.safetensors")
model = Wav2Vec2ForSequenceClassification.from_pretrained(model_name, state_dict=state_dict)

def classify_accent(audio):
    if audio is None:
        return "Error: No se recibió audio"

    try:
        # Verificar se o áudio é um caminho de arquivo
        if isinstance(audio, str):
            audio_array, sample_rate = librosa.load(audio, sr=None)
        else:
            raise ValueError("Formato de áudio inesperado.")

        print(f"Forma del audio: {audio_array.shape}, Frecuencia de muestreo: {sample_rate}")

        # Converter o áudio para float32
        audio_array = audio_array.astype(np.float32)

        # Resample para 16kHz, se necessário
        if sample_rate != 16000:
            audio_array = librosa.resample(audio_array, orig_sr=sample_rate, target_sr=16000)

        input_values = processor(audio_array, return_tensors="pt", sampling_rate=16000).input_values

        # Inferência
        with torch.no_grad():
            logits = model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1).item()

        # IDs de sotaque
        labels = ["Español", "Otro"]
        return labels[predicted_ids]

    except Exception as e:
        return f"Error al procesar el audio: {str(e)}"

# Interface do Gradio
description_html = """
<p>Prueba con grabación o cargando un archivo de audio. Para probar, recomiendo una palabra.</p>
<p>Ramon Mayor Martins: <a href="https://rmayormartins.github.io/" target="_blank">Website</a> | <a href="https://huggingface.co/rmayormartins" target="_blank">Spaces</a></p>
"""

# Interface do Gradio
interface = gr.Interface(
    fn=classify_accent,
    inputs=gr.Audio(type="filepath"),
    outputs="label",
    title="Clasificador de Sotaques (Español vs Otro)",
    description=description_html
)

interface.launch(debug=True)
