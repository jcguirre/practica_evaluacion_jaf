from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
 
class Usuarios(BaseModel):
    id: str = Field(..., example='User_1')
    nombre: str= Field(..., example='joel')
    email: EmailStr = Field(..., example='joel@example.com')
    edad: int = Field(..., example=30)
 
 
class Proyectos(BaseModel):
    id: str = Field(..., example='Proy_1')
    nombre: str = Field(..., example='Proyecto 1')
    Descripcion: Optional[str] = Field(None, example='Proyecto de tecnologia')
    Id_usuario: str = Field(..., example='User_1')
    Fecha_Creacion: str = Field(..., example='2024-10-30T20:00:00Z')
