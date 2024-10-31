from fastapi import FastAPI, HTTPException, Query, Path
from typing import List, Optional
from database import container
from models import Usuarios, Proyectos
from azure.cosmos import exceptions
from datetime import datetime


app = FastAPI(tittle='Api de Gestion de Proyectos')

#### Endpoint de Eventos

@app.get("/")
def home():
    return "Hola Mundo"