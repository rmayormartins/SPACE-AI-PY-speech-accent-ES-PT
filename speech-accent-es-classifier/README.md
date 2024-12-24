---
title: Speech-accent-es-classifier
emoji: 🎙️🤖🇪🇸
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: "4.12.0"
app_file: app.py
pinned: false
---

# Clasificador de Sotaques en Español

Este proyecto es un clasificador de acentos que distingue entre el español y otros acentos.

## Resumen del Proyecto

Esta aplicación utiliza un modelo entrenado para clasificar acentos de habla en dos categorías:
1. Español
2. Otro

El modelo se basa en el trabajo del autor y utiliza la parte en español del conjunto de datos Common Voice (versión 11.0) de la Fundación Mozilla.

## Conjunto de Datos

El proyecto utiliza el subconjunto en español del conjunto de datos Common Voice:
- Conjunto de datos: "mozilla-foundation/common_voice_11_0", "es"

Acentos españoles incluidos en el conjunto de datos:
- España
- México
- Colombia
- Argentina
- Chile
- Perú
- Venezuela
- Cuba
- República Dominicana
- Uruguay
- Paraguay
- Bolivia
- Ecuador
- Guatemala
- Honduras
- El Salvador
- Nicaragua
- Costa Rica
- Panamá
- Puerto Rico

## Detalles Técnicos

El proyecto utiliza el siguiente modelo y procesador:
- Modelo: "facebook/wav2vec2-base-960h"
- Procesador: Wav2Vec2Processor.from_pretrained

## Licencia

ecl

## Información del Desarrollador

Desarrollado por Ramon Mayor Martins, Ph.D. (2024)
- Correo electrónico: rmayormartins@gmail.com
- Página web: https://rmayormartins.github.io/
- Twitter: @rmayormartins
- GitHub: https://github.com/rmayormartins

## Agradecimientos

Agradecimientos especiales al Instituto Federal de Santa Catarina (Instituto Federal de Santa Catarina) IFSC-São José-Brasil.

## Contacto

Para cualquier consulta o sugerencia, por favor contacte al desarrollador usando la información proporcionada arriba.
