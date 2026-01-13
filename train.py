import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv("house_price.csv")

# Pilih fitur (X) dan target (y)
X = data[
    [
        'Square_Footage',
        'Num_Bedrooms',
        'Num_Bathrooms',
        'Year_Built',
        'Lot_Size',
        'Garage_Size',
        'Neighborhood_Quality'
    ]
]

y = data['House_Price']

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Simpan model
with open("model_house_price.pkl", "wb") as f:
    pickle.dump((model, scaler), f)

print("Model berhasil disimpan!")
