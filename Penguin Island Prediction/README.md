# Penguin Island Prediction App

This project predicts penguin species (`Adelie`, `Chinstrap`, `Gentoo`) from biometric inputs using an in-app `RandomForestClassifier`.

## Project structure

- `penguins.csv`: input dataset with species and measurement features.
- `app.py`: Streamlit app that performs data preprocessing, model training, and prediction in one run.

## Features

- interactive input of:
  - `island`: Biscoe / Dream / Torgersen
  - `bill_length_mm`, `bill_depth_mm`, `flipper_length_mm`, `body_mass_g`
  - `sex`: male / female
- shows raw and combined data sections
- one-hot encodes categorical fields (`island`, `sex`)
- maps species to numeric labels (`Adelie`=0, `Chinstrap`=1, `Gentoo`=2)
- trains `RandomForestClassifier` on full dataset at runtime
- outputs prediction probabilities and most likely species

## Data flow in `app.py`

1. read `penguins.csv`
2. drops target `species` from input features
3. append current input row to dataset so encoding is consistent
4. one-hot encode `island`, `sex` using `pd.get_dummies`
5. train `RandomForestClassifier` on encoded features and label-encoded target
6. predict class and probability on current input row

## Notes / known behavior

- in code, `bill_length_mm` is incorrectly assigned from `bill_depth_mm` when building `data`; fix this in `app.py` for true bill length use.
- model is retrained every app interaction; this is fine for POC but not for production.
- no saved model artifact (`.pkl`) is used.

## Usage

1. install dependencies:

```bash
pip install streamlit pandas numpy scikit-learn
```

2. run app:

```bash
streamlit run app.py
```

3. use controls to enter penguin features and review prediction output.

## Dependencies

- streamlit
- pandas
- numpy
- scikit-learn

## What changed from generic README

- explicit model: `RandomForestClassifier`
- training-in-app approach documented
- data encoding and inference path specified

## Contribution

Feedback or improvements are welcome. If you want to externalize model training (not in app), add notebook or model serialization step.
