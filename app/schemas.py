from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class AsteroidFeatures(BaseModel):
    name: str = Field(..., min_length=1, examples=["Apophis"])
    diameter_km: float = Field(..., gt=0, description="Diametro estimado en kilometros")
    velocity_kms: float = Field(..., gt = 0, description="Velocidad relativa en km/s")
    miss_distance_km: float = Field(..., gt=0, description="Distancia minima a la Tierra en km")

class PredictionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    is_hazardous: bool
    hazard_probability: float
    risk_level: str
    created_at: datetime

