from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

# CORS SETTING
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # boleh dari mana saja
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
with open("model_house_price.pkl", "rb") as f:
    model, scaler = pickle.load(f)

class HouseInput(BaseModel):
    Square_Footage: float
    Num_Bedrooms: int
    Num_Bathrooms: int
    Year_Built: int
    Lot_Size: float
    Garage_Size: int
    Neighborhood_Quality: int

@app.post("/predict")
def predict_price(data: HouseInput):
    input_data = np.array([[
        data.Square_Footage,
        data.Num_Bedrooms,
        data.Num_Bathrooms,
        data.Year_Built,
        data.Lot_Size,
        data.Garage_Size,
        data.Neighborhood_Quality
    ]])

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    return {"predicted_house_price": float(prediction[0])}
