# Step-by-Step Tutorial: Using Azure AI to Predict Product Supply Quantities

## Introduction
This tutorial will guide you through setting up and using Azure Artificial Intelligence (AI) services to predict the quantity of products your supply chain needs throughout the year, considering factors like sales trends, holidays, and special dates. We'll integrate Azure Machine Learning with a SQL database for data storage and management.

## Prerequisites
- An active [Azure account](https://azure.microsoft.com/free/).
- Access to a SQL database with historical sales data.
- Basic understanding of Python and SQL.
- Azure Machine Learning workspace configured.

## Steps

### Step 1: Prepare Your SQL Database
1. Ensure your SQL database includes:
   - Historical sales data (e.g., date, product ID, sales quantity).
   - Additional features like holiday indicators and special event dates.
2. Connect to your SQL database using a client tool or Azure Data Studio to verify data availability.

### Step 2: Create an Azure Machine Learning Workspace
1. Log in to the Azure portal.
2. Search for "Machine Learning" and click **Create**.
3. Fill in the required details (Subscription, Resource Group, Workspace Name, Region) and click **Review + Create**.

### Step 3: Set Up Data Connection
1. In the Azure Machine Learning Studio, navigate to **Data** and click **Create**.
2. Select **Datastore** and configure the connection to your SQL database.
3. Provide the SQL database connection string, username, and password.

### Step 4: Prepare the Data
1. Create a Python script to query and preprocess data from your SQL database. Example:


   ```


   import pyodbc
   import pandas as pd

   # Connect to the SQL database


   connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                               'SERVER=your_server;'
                               'DATABASE=your_database;'
                               'UID=your_username;'
                               'PWD=your_password;')

   # Query data


   query = """
   SELECT Date, ProductID, SalesQuantity, HolidayIndicator, SpecialEvent
   FROM SalesData
   """
   data = pd.read_sql(query, connection)

   # Preprocess data


   data['Date'] = pd.to_datetime(data['Date'])
   data = data.sort_values(by='Date')




2. Save the preprocessed data to a CSV file or directly upload it to Azure Blob Storage.


### Step 5: Train a Predictive Model
 

In Azure Machine Learning Studio, navigate to Notebooks and create a new notebook.

Use Python libraries like scikit-learn or Azure AutoML to train a time-series forecasting model. Example:

  ```
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


  ```

### Step 6: Deploy the Model


1. Register the trained model in Azure Machine Learning.
2. Create a real-time inference endpoint for predictions.
3. Use Azure ML SDK or REST API to connect your application to the endpoint.


### Step 7: Automate Predictions


1. Create a scheduled pipeline in Azure Machine Learning to automate predictions.
2. Connect the pipeline to your SQL database to update supply forecasts periodically.


### Step 8: Visualize Results


1. Use tools like Power BI or Tableau to visualize predicted vs. actual sales trends.
2. Set up dashboards to monitor performance and adjust as needed.


# Conclusion


By following this tutorial, you can leverage Azure's AI capabilities to optimize your supply chain. Make adjustments to the model based on performance and include additional data features to improve accuracy.


