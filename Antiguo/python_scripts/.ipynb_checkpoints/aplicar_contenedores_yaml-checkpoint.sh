#!/bin/bash

# Instalar kubectl si no está instalado
if ! command -v kubectl &> /dev/null; then
    echo "kubectl no está instalado. Instalando..."
    curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
    chmod +x ./kubectl
    sudo mv ./kubectl /usr/local/bin/kubectl
fi

# Autenticar con Google Cloud si no se ha hecho
if ! gcloud auth list | grep -q ACTIVE &> /dev/null; then
    echo "No estás autenticado con Google Cloud. Autenticando..."
    gcloud auth login
fi

# Autenticar con el cluster de Kubeflow si no se ha hecho
if ! kubectl config current-context | grep -q <nombre-cluster> &> /dev/null; then
    echo "No estás autenticado con el cluster de Kubeflow. Autenticando..."
    gcloud container clusters get-credentials <nombre-cluster> --zone <zona-cluster> --project <id-proyecto>
fi

# Aplicar los archivos YAML al cluster de Kubeflow
echo "Aplicando archivos YAML al cluster de Kubeflow..."
kubectl apply -f preprocesamiento1.yaml
kubectl apply -f preprocesamiento2.yaml
kubectl apply -f modeloScoring.yaml

echo "Proceso completado."
