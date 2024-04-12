# RMSE Calculator

This Python script calculates the Root Mean Square Error (RMSE) for a given set of predictions and actual values, and saves the result to a JSON file.

## Introduction

RMSE (Root Mean Square Error) is a widely-used metric in regression analysis and machine learning for evaluating the accuracy of predictive models. It measures the average magnitude of the errors between predicted values and actual values. RMSE is particularly useful as it penalizes larger errors more heavily, providing a balanced assessment of model performance.

## Usage

1. **Clone the repository:**
    ```sh
    git clone <repository_url>
    ```

2. **Navigate to the project directory:**
    ```sh
    cd RMSE_Calculator
    ```

3. **Create a JSON input file:**

    Create a file named `input.json` in the project directory with the following structure:
    ```json
    {
      "P": [10, 15, 20, 25, 30],
      "R": [12, 18, 22, 28, 32]
    }
    ```

    - Replace the values in the `P` array with your predicted values and the values in the `R` array with the corresponding actual values.

4. **Run the script:**
   
    ```sh
    python rmse_calculator.py
    ```

    This will calculate the RMSE using the data from `input.json` and save the result to `output.json`.

## RMSE Explanation

RMSE is calculated as the square root of the average of the squared differences between predicted values (P) and actual values (R). Mathematically, it is expressed as:

RMSE = sqrt(mean((P - R)^2))



- `P` represents the array of predicted values.
- `R` represents the array of actual values.
- `mean` calculates the average of the squared differences.
- `sqrt` takes the square root of the result.

RMSE provides a single, interpretable metric to assess the overall performance of a regression model. A lower RMSE value indicates that the model's predictions are closer to the actual values, while a higher RMSE value suggests larger prediction errors.

## Requirements

- Python 3.x

Ensure that you have Python 3.x installed on your system to run the script.

