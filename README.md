# Land Price Predictor Using ML Model
This project aims to predict land prices based on various factors that influence land value. Due to the unavailability of an actual dataset, fictional data has been generated using the numpy library. The project also demonstrates the model’s capability to extract data from a webpage using web scraping techniques. Exploratory Data Analysis (EDA) has been performed using pandas, with data visualization done using matplotlib and seaborn. The model is created and trained using the sklearn library.

## Project Overview
The objective of this project is to predict land prices by considering various influencing factors such as land area, crime rate, and distance to the city center. The project encompasses data generation, web scraping, EDA, data visualization, and model training.

## Project Highlights
1. <b>Data Generation</b>: Created functional data for Nagpur city's land prices for analysis purposes (Synthetic data due to limited access to real data).
2. <b>Static Webpage Creation</b>: Crafted a static webpage showcasing Nagpur's areas/lands, incorporating generated data.
3. <b>Web Scraping</b>: Scraped webpage data, stored in CSV, demonstrating the model's adaptability to various data sources (Can be avoided if dataset is available).
4. <b>Model Training</b>: Trained a linear regression model (from sklearn library), predicting prices, evaluating with Mean Squared Error, and visualising results.
5. <b>Prediction</b>: Loaded the trained model, processed new data, and saved predictions in 'ml_generated_price.csv.'
6. <b>Displaying Results</b>: User-friendly display of predictions based on provided location.
7. <b>Analysis</b>: Utilised Matplotlib and Seaborn for in-depth analysis and graph generation on the ML-generated dataset.
