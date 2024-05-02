#!/bin/bash

# Carpeta actual
CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# GCP project ID
PROJECT_ID="your-project-id" # EL DE ORIANNA QUE LO ESTAMOS HACIENDO ES SU ORDENADOR

# Región para el Artifact Registry
REGION="europe-west2"

# Registro en Artifact Registry
ARTIFACT_REGISTRY="${REGION}-docker.pkg.dev/${PROJECT_ID}"

# Función para construir y subir una imagen Docker a Artifact Registry
build_and_push_image() {
  local node=$1
  echo "Building $node..."
  docker build -t "$ARTIFACT_REGISTRY/$node:latest" "$CURRENT_DIR/$node"
  echo "Pushing $node to Artifact Registry..."
  docker push "$ARTIFACT_REGISTRY/$node:latest"
}

# Lista de nodos
nodes=("modeloScoring" "preprocesamiento1" "preprocesamiento2")

# Construir y subir cada imagen Docker
for node in "${nodes[@]}"; do
  build_and_push_image "$node"
done

echo "Builds y push a Artifact Registry completados."
