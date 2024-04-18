# MLOpsKubeflow
Pipeline de MLOps con kubeflow

## Estructura de archivos
```
project/
│
├── kubeflow/
│   ├── pipeline.yaml
│   └── components/
│       ├── preprocesamiento1.yaml
│       └── preprocesamiento2.yaml
│       └── modeloscoring.yaml
│
├── python_scripts/
│   ├── preprocesamiento1.py
│   ├── preprocesamiento2.py
│   └── modeloscoring.py
│
├── docker_images/
│   ├── Dockerfile_preprocesamiento1
│   ├── Dockerfile_preprocesamiento2
│   └── Dockerfile_modeloscoring
│
├── requirements.txt
├── pipelineKubeflow.py
└── README.md
``` 

