from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from app.database import Base

class AsteroidPrediction(Base):
    __tablename__ = "asteroid_predictions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    diameter_km = Column(Float, nullable=False)
    velocity_kms = Column(Float, nullable=False)
    miss_distance_km = Column(Float, nullable=False)
    is_hazardous = Column(Boolean, nullable=False)
    hazard_probability = Column(Float, nullable=False)
    risk_level = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))