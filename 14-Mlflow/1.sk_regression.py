# Traning a basic Regression Model using Sklearn
import warnings
import argparse
import logging
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

# RMSE to be as low as possible (closer to 0)
# MAE to be as low as possible (closer to 0)
# R2 to be as high as possible (closer to 1.0)

#get arguments from command
parser = argparse.ArgumentParser()
parser.add_argument("--alpha", type=float, required=False, default=0.5)
parser.add_argument("--l1_ratio", type=float, required=False, default=0.5)
args = parser.parse_args()

#evaluation function
# Why to use numpy here ?
# You used np.sqrt(mean_squared_error(actual, pred)) to calculate RMSE because that's the very definition of Root Mean Squared Error.

# mean_squared_error(actual, pred): This part calculates the Mean Squared Error (MSE). As the name suggests, it first finds the difference between actual and predicted values, then squares each difference, and finally takes the mean (average) of those squared differences.
# np.sqrt(...): This part calculates the square root of the result from mean_squared_error.
# So, np.sqrt(mean_squared_error(...)) directly implements the "Root Mean Squared Error" formula.

def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


if __name__ == "__main__":
    warnings.filterwarnings("ignore")

# Why is it used here np.random.seed(40)?

# The most direct reason in your code is for the train_test_split(data) function:

# train_test_split: This function by default shuffles the data before splitting it into training and testing sets. If you don't set a random_state (which train_test_split also has as a parameter) or a global NumPy seed, every time you run your script, the data will be shuffled differently. This means your train and test sets will be slightly different each time, which can lead to slightly different model training outcomes and evaluation metrics.

# By setting np.random.seed(40), you guarantee that:

# The shuffling done by train_test_split will be the same every time you run the script.
# Consequently, the train and test datasets will be identical across multiple runs.

    np.random.seed(40)

    # Read the wine-quality csv file from local, Copying the data in data dir to be safe
    data = pd.read_csv("red-wine-quality.csv")
    data.to_csv("data/red-wine-quality.csv", index=False)

    # Split the data into training and test sets. (0.75, 0.25) split.
    # 100 row data , 75 will be used for training and , 25 rows will be used for testing the model
    train, test = train_test_split(data) # test set -> 0.25

    # The predicted column is "quality" which is a scalar from [3, 9]
    # Seperating the features of training and testing dataset
    # dropping the "quality" column from train_x and test_x is crucial because it ensures your model learns to predict the quality based only on the input features, simulating a real-world scenario where you don't know the quality beforehand.

    # We started with a train DataFrame that had all features and the 'quality' label.

# We then created train_x by removing 'quality' from train.
# We simultaneously created train_y by selecting only 'quality' from train.
# We are effectively separating the original train (and test) dataframes into two distinct parts for training and testing:

# _x DataFrames: Containing only the features (inputs).
# _y DataFrames: Containing only the labels (outputs you want to predict).
# This is the standard way to prepare your data for a supervised machine learning model: you feed the features (train_x) and their corresponding labels (train_y) to the model during training, and then you ask the trained model to predict labels when given new features (test_x).
    
    # quality column is removed from _x variables
    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1) # 25 % of data for testing

    # _y selecting only the quality column
    train_y = train[["quality"]]
    test_y = test[["quality"]]

    alpha = args.alpha
    l1_ratio = args.l1_ratio


# short explanation:
# 1.  `lr = ElasticNet(...)`: This line **sets up your learning model (ElasticNet) with its specific learning rules** (`alpha`, `l1_ratio`). Think of it as choosing a student and telling them *how* to learn.
# 2.  `lr.fit(train_x, train_y)`: This line **trains the model**. You give the model the **features (data inputs)** and the **correct answers (labels)**, and it learns the patterns between them. It's like the student studying the textbook examples with their solutions.

    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
    lr.fit(train_x, train_y)

    predicted_qualities = lr.predict(test_x)

    # its the time of result
    (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)

    print("Elasticnet model (alpha={:f}, l1_ratio={:f}):".format(alpha, l1_ratio))
    print("  RMSE: %s" % rmse)
    print("  MAE: %s" % mae)
    print("  R2: %s" % r2)
