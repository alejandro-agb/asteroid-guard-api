import numpy as np

def sigmoid(z: float) -> float:
    return float(1.0 / (1.0 + np.exp(-z)))

def predict_asteroid_hazard(
        diameter_km: float,
        velocity_kms: float,
        miss_distance_km: float
) -> tuple[bool, float, str]:
    """
    Calcula la probabilidad de peligro usando una combinación lineal normalizada
    y activación sigmoide.
    """

    norm_diameter = diameter_km / 0.14
    norm_velocity = velocity_kms / 20.0
    norm_distance = 7500000.0 / miss_distance_km

    features = np.array([norm_diameter, norm_velocity, norm_distance], dtype=np.float64)
    weights = np.array([1.8, 0.7, 2.2], dtype=np.float64)
    bias = -4.2

    logit = float(np.dot(features, weights) + bias)
    probability = round(sigmoid(logit), 4)
    is_hazardous = probability >= 0.5

    if probability >= 0.75:
        risk_level = "HIGH"
    elif probability >= 0.50:
        risk_level = "MODERATE"
    else:
        risk_level = "LOW"

    return is_hazardous, probability, risk_level