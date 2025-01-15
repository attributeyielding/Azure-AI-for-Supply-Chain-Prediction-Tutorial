from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Split data into training and testing sets


X = data[['ProductID', 'HolidayIndicator', 'SpecialEvent']]
y = data['SalesQuantity']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model


model = RandomForestRegressor()
model.fit(X_train, y_train)

# Evaluate the model


predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")
