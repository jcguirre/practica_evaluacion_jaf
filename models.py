from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
 
class Usuarios(BaseModel):
    id: str = Field(..., example='u1')
    nombre: str= Field(..., example='joel')
    email: EmailStr = Field(..., example='joel@example.com')
    edad: int = Field(..., example=30)
 
 
class Proyectos(BaseModel):
    id: str = Field(..., example='e1')
    nombre: str = Field(..., example='Proyecto 1')
    Descripcion: Optional[str] = Field(None, example='Proyecto de tecnologia')
    Id_usuario: List[Usuarios] = Field(default_factory=list)
    Fecha_Creacion: str = Field(..., example='2024-10-30T20:00:00Z')
