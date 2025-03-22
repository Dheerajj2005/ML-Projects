# Penguin Island Prediction App

This repository contains the code for a Streamlit web application that predicts the species of penguins (Adelie, Chinstrap, or Gentoo) based on their physical characteristics.

## Project Description

This project utilizes a machine learning model to predict the species of penguins (Adelie, Chinstrap, or Gentoo) based on features such as island of origin, bill length, bill depth, flipper length, body mass, and gender. The application provides an interactive interface to input these features and visualize the prediction results.

## Features

* **Interactive Input:** Users can input penguin characteristics through sliders and dropdown menus for:
    * **Island:** Select from available islands (e.g., Biscoe).
    * **Bill Length (mm):** Input the bill length using a slider.
    * **Bill Depth (mm):** Input the bill depth using a slider.
    * **Flipper Length (mm):** Input the flipper length using a slider.
    * **Body Mass (g):** Input the body mass using a slider.
    * **Gender:** Select the gender (male/female).
* **Species Prediction:**
    * Displays the predicted species (Adelie, Chinstrap, or Gentoo) based on the input features.
    * Shows the probability scores for each species, indicating the model's confidence in its predictions.
    * Highlights the species with the highest probability.
* **Data Visualization (Optional):**
    * This tab (if implemented) would include interactive visualizations of the penguin dataset.
    * Possible visualizations:
        * Scatter plots showing relationships between different features (e.g., bill length vs. bill depth).
* **Data Preparation (Optional):**
    * This tab (if implemented) would provide details on the data preprocessing steps taken before training the model.
    * It might include information about:
        * Handling missing values.
        * Encoding categorical features (e.g., one-hot encoding).
        * Scaling or normalizing numerical features.
        * Feature selection or engineering.


## Usage

1.  Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

2.  The application will open in your web browser.

3.  Input the penguin's characteristics using the sliders and dropdown menus in the "Input Features" section.

4.  The application will display the predicted species and the probability scores for each species in the "Predicted Species" section.

5.  Explore the "Data Visualization" and "Data Preparation" tabs (if available) to gain insights into the data and model.


## Dependencies

* `streamlit`
* `pandas`
* `scikit-learn`
* `numpy`
* `matplotlib` (optional, for visualization)
* `seaborn` (optional, for visualization)

## Model

The machine learning model used in this project can be any suitable classification algorithm, such as Random Forest, Support Vector Machine, or Logistic Regression. The choice of model may depend on the specific characteristics of the dataset and the desired performance.


## Contributing

Contributions are welcome! If you have any suggestions or improvements, please feel free to submit a pull request.
