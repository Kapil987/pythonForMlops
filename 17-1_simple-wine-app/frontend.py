from flask import Flask, render_template, request
import subprocess
# No need for numpy or pandas in this file anymore
# import numpy as np 
# import pandas as pd

app = Flask(__name__)

# ... (Your homePage and training routes remain the same) ...
@app.route('/',methods=['GET'])
def homePage():
    return render_template("index.html")

@app.route('/train',methods=['GET'])
def training():
    # Consider using subprocess here as well for better error handling
    try:
        subprocess.run(['python', 'train.py'], check=True)
        return "Training Successful!"
    except subprocess.CalledProcessError as e:
        return f"Training Failed: {e}"


@app.route('/predict',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        try:
            # --- 1. Read the string inputs given by the user ---
            # We keep them as strings because they will be passed as command-line arguments.
            form_values = [
                request.form['fixed_acidity'],
                request.form['volatile_acidity'],
                request.form['citric_acid'],
                request.form['residual_sugar'],
                request.form['chlorides'],
                request.form['free_sulfur_dioxide'],
                request.form['total_sulfur_dioxide'],
                request.form['density'],
                request.form['pH'],
                request.form['sulphates'],
                request.form['alcohol']
            ]

            # --- 2. Construct the command to run the prediction script ---
            # The first item is the python interpreter, the second is our script,
            # followed by all the feature values from the form.
            command = ['python', 'predict.py'] + form_values
            
            # --- 3. Run the script and capture its output ---
            # `text=True` ensures the output is decoded as a string.
            # `check=True` will raise an exception if the script returns an error.
            result = subprocess.check_output(command, text=True, stderr=subprocess.STDOUT)
            
            print('result from prediction is',result)
            # The captured output will be the value printed by predict.py.
            # We use .strip() to remove any potential leading/trailing whitespace or newlines.
            prediction_result = result.strip()

            # --- 4. Render the result on the webpage ---
            return render_template('results.html', prediction=prediction_result)

        except subprocess.CalledProcessError as e:
            # This will catch errors if predict.py fails (e.g., model not found, wrong data)
            # The error message printed to stderr in predict.py will be in e.output
            print('The subprocess failed with output: ', e.output)
            return f'An error occurred during prediction. Details: <pre>{e.output}</pre>'
        except Exception as e:
            # Catches other potential errors (e.g., form field missing)
            print('The Exception message is: ', e)
            return 'An unexpected error occurred. Please check the application logs.'

    else:
        # For a GET request, just show the input form
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) # Changed port to 5000 as 500 can be a privileged port
