from kfp import dsl
from kfp import compiler
import pipelineKubeflow as ppkb

### definir un componente
@dsl.container_component
def say_hello():
    return dsl.ContainerSpec(image='alpine', command=['echo'], args=['Hello'])


### definir un pipeline
@dsl.pipeline
def hello_pipeline(person_to_greet: str) -> str:
    # greeting argument is provided automatically at runtime!
    hello_task = say_hello(name=person_to_greet)
    return hello_task.outputs['greeting']

compiler.Compiler().compile(hello_pipeline, 'pipeline.yaml')


### Tranformar el pipeline en un paquete YALM (creo) --- Aquí es para subir el pipeline cuando este listo


from kfp.client import Client
client = Client(host='https://console.cloud.google.com/storage/browser/pract_kubeflow')
#client.create_run_from_pipeline_package('pipeline.yaml', arguments={'param': 'a', 'other_param': 2}) Este parece ser solo para YaML
client.create_run_from_pipeline_func(ppkb.xgb_train_pipeline_local(), arguments={'param': 'a', 'other_param': 2}) 