from fastapi import FastAPI, HTTPException, UploadFile, File
import pandas as pd
import utils

app = FastAPI()
app.title = "K-Means Algorithm" 
app.version = "0.0.1" 

@app.post("/upload/", tags=['CSV File'])
async def upload_csv(file: UploadFile = File(...)):
    try:
        data_csv = pd.read_csv(file.file)
        data, kmeans = utils.k_means_algorithm(data_csv)

        # Crear un diccionario con la información
        resultado_dict = {
            'centroides': kmeans.cluster_centers_.tolist(),
            'Data con clúster': data.to_dict(orient='records')
        }

        return resultado_dict
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))