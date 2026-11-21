from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import engine, Base, get_db
from app.models import AsteroidPrediction
from app.schemas import AsteroidFeatures, PredictionResponse
from app.predictor import predict_asteroid_hazard

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AsteroidGuard API",
    description="Microservicio de prediccion de riesgo de asteroides cercanos a la Tierra",
    version="1.1.0"
)

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "asteroid-guard-api"}

@app.post("/predict", response_model=PredictionResponse, status_code=201)
def predict(asteroid: AsteroidFeatures, db: Session = Depends(get_db)) -> AsteroidPrediction:
    is_hazardous, probability, risk_level = predict_asteroid_hazard(
        diameter_km = asteroid.diameter_km,
        velocity_kms = asteroid.velocity_kms,
        miss_distance_km = asteroid.miss_distance_km,
    )

    db_prediction = AsteroidPrediction(
        name=asteroid.name,
        diameter_km=asteroid.diameter_km,
        velocity_kms=asteroid.velocity_kms,
        miss_distance_km=asteroid.miss_distance_km,
        is_hazardous=is_hazardous,
        hazard_probability=probability,
        risk_level=risk_level,
    )
    db.add(db_prediction)
    db.commit()
    db.refresh(db_prediction)
    return db_prediction

@app.get("/history", response_model=list[PredictionResponse])
def get_history(limit: int = 20, db: Session = Depends(get_db)) -> list[AsteroidPrediction]:
    return (
        db.query(AsteroidPrediction)
        .order_by(AsteroidPrediction.created_at.desc())
        .limit(limit)
        .all()
    )