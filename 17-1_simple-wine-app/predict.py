import joblib
import pandas as pd
import sys

def predict_from_cli_args():
    """
    Loads a pre-trained model, makes a prediction based on command-line arguments,
    and prints the result to standard output.
    """
    # --- 1. Check for the correct number of input arguments ---
    # sys.argv includes the script name itself, so we expect 12 items total (1 script + 11 features).
    if len(sys.argv) != 12:
        print("Error: Incorrect number of features provided.", file=sys.stderr)
        print(f"Usage: python predict.py [11 feature values]", file=sys.stderr)
        sys.exit(1) # Exit with an error code

    try:
        # --- 2. Load the pre-trained model ---
        model_filename = "randomforest_model.joblib"
        loaded_model = joblib.load(model_filename)

        # --- 3. Prepare input data from command-line arguments ---
        # The first argument (sys.argv[0]) is the script name, so we start from index 1.
        # Convert all feature arguments from string to float.
        features = [float(arg) for arg in sys.argv[1:]]

        # Define the column names in the same order as the model was trained.
        feature_columns = [
            'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
            'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
            'pH', 'sulphates', 'alcohol'
        ]

        # Create a pandas DataFrame from the input features.
        # The model expects a 2D array-like structure, so we wrap `features` in a list.
        sample_data = pd.DataFrame([features], columns=feature_columns)

        # --- 4. Make the prediction ---
        prediction = loaded_model.predict(sample_data)

        # --- 5. Print the final result to standard output ---
        # This is the *only* print statement that goes to stdout.
        # The Flask app will capture this value.
        # We access the first element of the prediction array.
        print(prediction[0])

    except FileNotFoundError:
        print(f"Error: Model file not found at '{model_filename}'", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        # Print any other errors to standard error for debugging.
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    predict_from_cli_args()
