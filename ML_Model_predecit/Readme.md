

![Screenshot 2024-10-20 192431](https://github.com/user-attachments/assets/a7216a7f-a7a7-4812-a888-3284298f0d79)

# Model Training and Development


# Device Price Prediction Model

## Project Overview

The **Device Price Prediction Model** is an advanced machine learning application designed to estimate the prices of electronic devices based on a comprehensive set of features. By leveraging various algorithms, including Linear Regression, this model aims to provide accurate price predictions, assisting consumers, retailers, and manufacturers in making informed decisions.

The application is built using **FastAPI**, which enables the creation of a high-performance RESTful API. This model integrates data preprocessing steps, ensuring that the input features are appropriately transformed before being fed into the predictive algorithms.

## Key Features

- **Real-Time Price Prediction**: The API allows users to submit device specifications and receive immediate price predictions.
- **Comprehensive Data Processing**: The application incorporates robust preprocessing pipelines that handle missing values, normalize numerical features, and encode categorical variables.
- **Multiple Machine Learning Algorithms**: The model is designed to be extensible, supporting various algorithms for price prediction, with Linear Regression as the primary choice.
- **Input Validation**: Utilizes **Pydantic** for data validation, ensuring that user inputs conform to expected types and formats, reducing errors during predictions.
- **Documentation and User-Friendly API**: Detailed API documentation is generated automatically, making it easier for users to interact with the application.

## Installation and Setup

### Prerequisites

- **Python**: Version 3.7 or higher
- **pip**: Python package installer




# Data Preparation
The model is trained on a dataset that includes various device features and their corresponding prices.
Data preprocessing involves handling missing values, encoding categorical variables, and scaling numerical features to improve model performance.
# Model Selection
Multiple regression algorithms were evaluated, including:
Linear Regression: The primary algorithm used for predictions.
K-Nearest Neighbors (KNN): An alternative model for comparison.
Random Forest: Used for its robustness and ability to handle non-linear relationships.
Support Vector Regression (SVR): Evaluated for potential performance improvements.
# Performance Metrics
The model's performance is evaluated using the Root Mean Squared Error (RMSE), which provides insights into the model's accuracy on training and testing datasets.

# Contributing
Contributions to the project are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -m 'Add a new feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
