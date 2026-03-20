# ML-Projects

This repository includes three self-contained ML applications with Streamlit UI and notebooks for training, evaluation, and deployment.

## Projects

1. **Calorie Prediction** (`Calorie Prediction/`)
   - Uses `exercise.csv` + `calories.csv` to predict calories burned.
   - EDA and modeling in `calorie-prediction.ipynb`.
   - Final model: `XGBRegressor` saved as `Calorie_model.pkl`.
   - `app.py`: user feature input (`gender`, `age`, `height`, `weight`, `duration`, `heart_rate`, `body_temp`), scaling, and prediction.
   - README files updated with details and quick run steps.

2. **Insurance Predictor** (`Insurance Predictor/`)
   - Uses `insurance.csv` to predict insurance charges.
   - Notebook: `Insurance.ipynb` includes EDA, target rename (`expenses` -> `charges`), pre-processing, and model comparisons.
   - Model candidates: `LinearRegression`, `Ridge`, `RandomForestRegressor`, `SVR`, `XGB` and best model chosen as `RandomForestRegressor`.
   - Saved model: `random_forest_model.pkl`.
   - `app.py`: streaming input, OHE of categories, scaling numeric features, prediction output.

3. **Penguin Island Prediction** (`Penguin Island Prediction/`)
   - Uses `penguins.csv` to classify species (`Adelie`, `Chinstrap`, `Gentoo`).
   - `app.py` performs data loading, one-hot encoding, label mapping, and `RandomForestClassifier` training + prediction in app session.
   - Includes interactive visualizations and data diagnostics sections.

## How to run a project

1. `cd "<Project Folder>"`
2. install dependencies (example):

```bash
pip install pandas numpy scikit-learn streamlit xgboost seaborn matplotlib
```

3. run the app:

```bash
streamlit run app.py
```

