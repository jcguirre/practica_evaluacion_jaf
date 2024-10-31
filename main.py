from fastapi import FastAPI, HTTPException, Query, Path
from typing import List, Optional
from database import Container_Usuarios,Container_Proyectos
from models import Usuarios, Proyectos
from azure.cosmos import exceptions
from datetime import datetime


app = FastAPI(tittle='Api de Gestion de Proyectos')

#### Endpoint de Usuario

##Lista Usuario
@app.get("/Usuarios/", response_model=List[Usuarios])
def list_user():
    
    try:
        query = "SELECT * FROM c WHERE 1=1"
        items = list(Container_Usuarios.query_items(query=query, enable_cross_partition_query=True))
        return items
    except exceptions.CosmosResourceNotFoundError:
        raise HTTPException(status_code=404, detail='No se puede listar')
    except exceptions.CosmosHttpResponseError as e:
        raise HTTPException(status_code=400, detail=str(e))

##Crear Usuario
@app.post("/Usuarios/", response_model=Usuarios, status_code=201)
def create_user(user: Usuarios):
    try:
        Container_Usuarios.create_item(body=user.dict())
        return user
    except exceptions.CosmosResourceExistsError:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    except exceptions.CosmosHttpResponseError as e:
        raise HTTPException(status_code=400, detail=str(e))


##Elimina Usuario
@app.delete("/Usuarios/{user_id}", status_code=204)
def delete_user(user_id: str):
    try:
        Container_Usuarios.delete_item(item=user_id, partition_key=user_id)
        return
    except exceptions.CosmosResourceNotFoundError:
        raise HTTPException(status_code=404, detail='Usuario No encontrado')
    except exceptions.CosmosHttpResponseError as e:
        raise HTTPException(status_code=400, detail=str(e))

##Actualizar Usuario
@app.put("/Usuarios/{user_id}", response_model=Usuarios)
def update_user(user_id: str, update_user: Usuarios):

    try:
        existing_user = Container_Usuarios.read_item(item=user_id, partition_key=user_id)
        
        print(update_user.dict(exclude_unset=True))
        # Actualiza campos
        existing_user.update(update_user.dict(exclude_unset=True))
       
        Container_Usuarios.replace_item(item=user_id, body=existing_user)
        return existing_user
    except exceptions.CosmosResourceNotFoundError:
        raise HTTPException(status_code=404, detail="Usuario No Encontrado")
    except exceptions.CosmosHttpResponseError as e:
        raise HTTPException(status_code=400, detail=str(e))