import warnings
import argparse
import logging
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
import joblib

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

# --- Function to evaluate model metrics ---
def eval_metrics(actual, pred):
    """Calculates and returns RMSE, MAE, and R2 score."""
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

# --- Main execution block ---
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)

    # --- 1. Load and prepare the data ---
    try:
        data = pd.read_csv("red-wine-quality.csv")
    except FileNotFoundError:
        logger.error("Error: 'red-wine-quality.csv' not found. Please make sure the file is in the correct directory.")
        exit()

    if "Unnamed: 0" in data.columns:
        data = data.drop("Unnamed: 0", axis=1)

    # Separate features (X) from the target (y) before splitting
    X = data.drop(["quality"], axis=1)
    y = data["quality"].values.ravel() # Use ravel() to convert y to the correct shape for the model

    # Split the data into training and test sets
    train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.25, random_state=42)

    # --- 2. Define the Model ---
    # We will use RandomForestRegressor directly. It does not require feature scaling.
    model = RandomForestRegressor(random_state=42)
    
    # --- 3. Hyperparameter Tuning using GridSearchCV ---
    # Define a grid of parameters to search for Random Forest
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [10, 20, 30],
        'min_samples_split': [2, 5]
    }

    # Set up GridSearchCV to find the best parameters using 5-fold cross-validation
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, n_jobs=-1, scoring='neg_mean_squared_error', verbose=2)
    
    print("--- Starting hyperparameter tuning for Random Forest... ---")
    grid_search.fit(train_x, train_y)
    
    # The best model is found by grid_search
    best_model = grid_search.best_estimator_
    
    print("--- Hyperparameter tuning complete! ---")
    print(f"Best Parameters found: {grid_search.best_params_}")

    # --- 4. Evaluate the Best Model ---
    predicted_qualities = best_model.predict(test_x)
    (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)

    print("\n--- Best Model Evaluation ---")
    print("  RMSE: %s" % rmse)
    print("  MAE: %s" % mae)
    print("  R2: %s" % r2)

    # --- 5. Save the best model ---
    model_filename = "randomforest_model.joblib"
    joblib.dump(best_model, model_filename)
    print(f"\nModel training completed and saved to '{model_filename}'")
