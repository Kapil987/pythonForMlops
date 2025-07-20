### Explanation of Key Parameters in GridSearchCV

Here’s what each part means in simple terms:

- **cv=5**  
  This sets the number of cross-validation folds. The data will be split into 5 parts: the model is trained on 4 parts and tested on the remaining 1, repeated 5 times. This helps get a reliable estimate of model performance.

- **scoring='neg_mean_squared_error'**  
  This tells GridSearchCV how to measure model quality. It uses *negative mean squared error*, which means it prefers models with smaller prediction errors. The negative sign is just a technical detail—GridSearchCV expects higher scores to be better, so it negates the error.

- **verbose=2**  
  This controls how much progress text is printed while running. Level 2 means it will print more detailed updates about the search process, but not too much.

- **n_jobs=-1**  
  This tells the function to use *all available CPU cores* to run the search faster (by doing work in parallel).

**In short:**  
- `cv` = how many splits for cross-validation  
- `scoring` = how performance is measured  
- `verbose` = how much information you see during run  
- `n_jobs=-1` = use all CPU power for speed