from fastapi import FastAPI
from app.schemas import AsteroidFeatures, PredictionResponse
from app.predictor import predict_asteroid_hazard

app = FastAPI(
    title="AsteroidGuard API",
    description="Microservicio de prediccion de riesgo de asteroides cercanos a la Tierra",
    version="1.0.0"
)

predictions_history: list[PredictionResponse] = []

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "asteroid-guard-api"}

@app.post("/predict", response_model=PredictionResponse, status_code=201)
def predict(asteroid: AsteroidFeatures) -> PredictionResponse:
    is_hazardous, probability, risk_level = predict_asteroid_hazard(
        diameter_km = asteroid.diameter_km,
        velocity_kms = asteroid.velocity_kms,
        miss_distance_km = asteroid.miss_distance_km,
    )

    result = PredictionResponse(
        name=asteroid.name,
        is_hazardous = is_hazardous,
        hazard_probability = probability,
        risk_level = risk_level,
    )
    predictions_history.append(result)
    return result

@app.get("/history", response_model=list[PredictionResponse])
def get_history() -> list[PredictionResponse]:
    return predictions_history