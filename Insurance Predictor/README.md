# Insurance Charges Predictor

This project predicts health insurance charges using regression models and a Streamlit-based inference app.

## Project files

- `insurance.csv`: input dataset with features and target.
- `Insurance.ipynb`: EDA, preprocessing, model selection, training, cross-validation, and model export.
- `app.py`: Streamlit app for taking user input and predicting charges in real-time.
- `random_forest_model.pkl`: saved best model from notebook.

## Data schema

Features:
- `age` (numeric)
- `sex` (`male`, `female`)
- `bmi` (numeric)
- `children` (int)
- `smoker` (`yes`, `no`)
- `region` (`southwest`, `southeast`, `northwest`, `northeast`)

Target:
- `charges` (numeric)

## Notebook workflow

1. load data and clean duplicates
2. EDA (distribution, correlation, boxplots, etc.)
3. split `X`, `y` and train/test split (20% test)
4. one-hot encode `sex`, `smoker`, `region` using `OneHotEncoder(drop='first')`
5. baseline `LinearRegression` and k-fold CV
6. scale numeric fields (`age`, `bmi`) with `StandardScaler` and/or `MinMaxScaler`
7. test models with `GridSearchCV` including:
   - `Ridge`
   - `RandomForestRegressor`
   - `SVR`
8. best model chosen: `RandomForestRegressor` with tuned hyperparameters
9. save model:
   - `pickle.dump(model, open('random_forest_model.pkl', 'wb'))`

## App inference (`app.py`)

- loads `insurance.csv` for encoder/transformer fit
- collects user inputs by Streamlit widgets
- applies one-hot encoding and feature scaling same as training
- loads `random_forest_model.pkl` and predicts cost
- output displayed as `Predicted Insurance Charges: $...`

## How to run

1. install dependencies

   ```bash
   pip install pandas numpy scikit-learn streamlit seaborn matplotlib xgboost
   ```

2. run app

   ```bash
   streamlit run app.py
   ```

## Notes

- Keep `random_forest_model.pkl` in project root for app to work.
- The production pipeline relies on exact encoding and scaling used during training.
- Projects are intended as POC rather than production-grade system.

