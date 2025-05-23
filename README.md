# 🏞️ Real Estate Price Predictor Using ML Model

This project predicts land prices based on various influencing factors using a Machine Learning model. It features end-to-end workflow — from data generation and web scraping to model training and prediction — built primarily using Python libraries such as **NumPy**, **pandas**, **scikit-learn**, **matplotlib**, **seaborn**, and **streamlit**.

> ⚠️ *Note: To further increase my understanding of NumPy and Pandas instead of real datasets, synthetic data has been generated for demonstration and understanding purposes.*

---

## 📌 Project Overview

The model aims to estimate land prices by considering key attributes such as:
- Land Area
- Crime Rate
- Location

Key components of the project include:
- Synthetic dataset creation
- Static webpage and web scraping
- Exploratory Data Analysis (EDA)
- Model training and evaluation
- Result visualization and display
- Streamlit POC UI

---

## 🚀 Project Highlights

> 🧪 *Extensive Exploratory Data Analysis (EDA) was conducted on the dataset to identify correlations, distributions, and patterns before model training.*

### 1. 📊 Data Generation
- Generated synthetic land pricing data for **Nagpur city** using NumPy.
- Simulates realistic land metrics and economic indicators.

### 2. 🌐 Static Webpage Creation
- Designed a basic webpage listing various land locations and features.
- Demonstrates practical HTML-based data sources.

### 3. 🕸️ Web Scraping
- Scraped the static webpage to retrieve land data using **BeautifulSoup**.
- Stored extracted data in a structured `.csv` format.
> 🔁 *Can be bypassed if an actual dataset is available.*

### 4. 🧠 Model Training
- Trained a **Linear Regression** model using **scikit-learn**.
- Evaluated performance using **Mean Squared Error (MSE)**.
- Visualized prediction accuracy and regression line.

### 5. 📈 Prediction
- Saved model-generated prices in `ml_generated_price.csv`.
- Accepts new input data for dynamic price prediction.

### 6. 🖥️ Displaying Results
- Outputs user-friendly prediction results for selected Nagpur localities.
- Maps values to the original data for better interpretability.
- Using streamlit to display the results in a a user friendly format.

### 7. 📉 Exploratory Data Analysis (EDA)
- Conducted comprehensive EDA on the generated dataset.
- Identified trends, outliers, and correlations that influence land prices.
- Utilized **matplotlib** and **seaborn** for:
- Utilized **matplotlib** and **seaborn** for:
  - Correlation heatmaps
  - Price trend graphs
  - Feature distribution plots

---

## 🛠️ Tech Stack

| Component         | Tool/Library        |
|------------------|---------------------|
| Language          | Python              |
| Data Analysis     | NumPy, pandas       |
| Visualization     | matplotlib, seaborn |
| Machine Learning  | scikit-learn        |
| Web Scraping      | BeautifulSoup       |
| Webpage (Static)  | HTML                |
| UI                | streamlit           |

---

## 📂 File Structure

```
Land_Price_Predictor_Using_ML_Model/
├── Data Generation/
│   ├── Data_Generation.ipynb
│   └── land_price_data.csv
├── EDA/
│   ├── Data_Generation.ipynb
│   └── land_price_data.csv
├── Model/
│   ├── Model.ipynb
│   ├── ml_generated_price.csv
│   ├── model.csv
│   ├── predicted_prices_all.csv
│   └── trained_model_all_data.joblib
├── UI/
│   ├── UI_Output.png
│   ├── app.py
│   ├── model.csv
│   └── trained_model_all_data.joblib
├── Web Scrapping/
│   ├── Webscraping Data.ipynb
│   ├── index.html
│   └── model.csv
├── README.md
└── requirements.txt
```

---

## ✅ How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kshitij7704/Land_Price_Predictor
   cd Land-Price-Predictor
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate Data & Web Scraping (Optional if using a dataset):**
   ```bash
   python scripts/generate_data.py
   python scripts/scrape_webpage.py
   ```

4. **Train Model:**
   ```bash
   python scripts/train_model.py
   ```

5. **Run Prediction:**
   ```bash
   python scripts/predict.py
   ```

6. **View Results:**
   - Check `ml_generated_price.csv` for predicted land prices.
   - Explore visualizations in the `visualizations/` folder.

---

## 📈 Sample Output

```
Location         Area(sq.ft)   Crime Rate   Distance(km)   Predicted Price (in ₹ Lakhs)
---------------------------------------------------------------------------------------
Shankar Nagar     1800         0.04         2.5            56.23
Dharampeth        2400         0.03         3.0            68.10
```

---

## 🎨 UI Preview

![UI Preview](UI/UI_Output.png)

*The app features a clean sidebar for inputs and a modern card layout for your predicted price.*

---

## 📢 Future Enhancements

- Integrate real-time data from public APIs or government land records.
- Deploy the model as a web application using Flask or Streamlit.
- Expand feature set to include infrastructure, schools, and transport availability.

---

## 🧠 Author

**Kshitij Kashyap**  
🌐 [LinkedIn](https://www.linkedin.com/in/kshitij-kashyap-133205264/) <br>
💻 [GitHub](https://github.com/kshitij7704)
