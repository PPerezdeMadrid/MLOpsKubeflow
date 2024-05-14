from kfp.dsl.types import GCSPath
@component(
    base_image="python:3.7", # Use a different base image.
    packages_to_install=['google-cloud-bigquery','google-cloud-storage','tensorflow','tensorflow-io']

)


def generar_tablon( nombretabla:str, 
    features_input:str) -> NamedTuple(
    "Outputs",
    [
        ("output_table", str),
        ("output_table_total", str)# Return parameter.
    ],
):
    from google.cloud import bigquery
    import logging
    logging.getLogger().setLevel(logging.INFO)
    from tensorflow.python.lib.io import file_io

    
    def caip_uri_to_fields(uri):
        #uri = uri[5:]
        project, dataset, table = uri.split('.')
        return project, dataset, table
    
    ## 1º GENERACION DE TABLA TEMPORAL CON ÚNICAMENTE LAS VARIABLES QUE PROCESAMOS 
    ## deberíamos leer el esquema de las columnas de seleccion de variables de train generado en el otro notebook
    ## aquí, por 'rapidez' voy a crear y a hacer la tabla a mi manera
    import json
    with file_io.FileIO(features_input, 'r') as f:
        variables = json.load(f)
    features = list(variables.keys())

    variablesentran = ''
    for el in features:
         variablesentran+= 'CAST ('+el+' AS FLOAT64) AS ' +el+','
    variablesentran=variablesentran[:-1]
        # Converts string to list
        #variables = json.load(features)
    
    project, dataset, tabla = caip_uri_to_fields(nombretabla)
    logging.info(variablesentran)
    logging.info(nombretabla)
    bq_client = bigquery.Client(project = 'XXXXXX')
    
    query="""   


        SELECT """+ variablesentran+""",target_en_eop
                                        FROM `"""+nombretabla+"""` a 
                                """


    # TODO(developer): Set table_id to the ID of the destination table.
    # table_id = "your-project.your_dataset.your_table_name"
    job_config = bigquery.QueryJobConfig()
    job_config.write_disposition = bigquery.WriteDisposition().WRITE_TRUNCATE

    job_config.destination =project+"."+dataset+".tablon_entrenamiento_simplificado"

    sql = query
    logging.info(query)

    # Start the query, passing in the extra configuration.
    query_job = bq_client.query(sql, job_config=job_config)  # Make an API request.
    query_job.result()  # Wait for the job to complete.
    output_table = project+"."+dataset+".tablon_entrenamiento_simplificado"
    output_message='zote el que lo lea'
    return (output_table,output_message)

        