# pip install matplotlib
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Property Price Estimator", layout="centered")
st.title("🏠 Linear Regression for Property Price Estimation")
st.write("Using a simple model: price = 5 + 0.02×area + 2×bedrooms + 2×bathrooms + 5×parking")

# Sample data
X = np.array([
    [1000, 2, 1, 1],
    [1200, 2, 2, 1],
    [1500, 3, 2, 2],
    [800, 1, 1, 1],
    [2000, 4, 3, 2]
])

y = np.array([
    int(5 + 0.02*1000 + 2*2 + 2*1 + 5*1),   # 39
    int(5 + 0.02*1200 + 2*2 + 2*2 + 5*1),   # 54
    int(5 + 0.02*1500 + 2*3 + 2*2 + 5*2),   # 69
    int(5 + 0.02*800 + 2*1 + 2*1 + 5*1),    # 30
    int(5 + 0.02*2000 + 2*4 + 2*3 + 5*2),   # 79
])

# Add bias column
X_b = np.c_[np.ones((X.shape[0], 1)), X]

# Linear regression using normal equation
theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# User input
st.subheader("🔍 Predict Price for a New Property")
area = st.number_input("📐 Area (in sq.ft)", value=1200, step=100)
bedrooms = st.slider("🛏 Number of Bedrooms", 1, 5, value=2)
bathrooms = st.slider("🛁 Number of Bathrooms", 1, 4, value=2)
parking = st.slider("🚗 Number of Parking Spaces", 0, 3, value=1)

# Predict
x_new = np.array([1, area, bedrooms, bathrooms, parking])
predicted_price = x_new.dot(theta)
st.success(f"💰 Predicted Price: ₹{predicted_price:.2f} lakhs")

# Plotting
st.subheader("📊 Actual vs Predicted Price Plot")
y_pred = X_b.dot(theta)

fig, ax = plt.subplots()
ax.scatter(y, y_pred, color='blue', label='Predicted vs Actual')
ax.plot([min(y), max(y)], [min(y), max(y)], color='red', linestyle='--', label='Perfect Fit')
ax.set_xlabel("Actual Price (lakhs)")
ax.set_ylabel("Predicted Price (lakhs)")
ax.set_title("Model Fit")
ax.grid(True)
ax.legend()
st.pyplot(fig)