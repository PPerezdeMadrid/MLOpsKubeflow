#!/bin/bash

# Carpeta actual
CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Build para modeloScoring
echo "Building modeloScoring..."
docker build -t modelo_scoring_image "$CURRENT_DIR/modeloScoring"

# Build para preprocesamiento1
echo "Building preprocesamiento1..."
docker build -t preprocesamiento1_image "$CURRENT_DIR/preprocesamiento1"

# Build para preprocesamiento2
echo "Building preprocesamiento2..."
docker build -t preprocesamiento2_image "$CURRENT_DIR/preprocesamiento2"

echo "Builds completadas."
