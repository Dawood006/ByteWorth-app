# ByteWorth-app

🔗 **Live Applications:**  
- **Main App (Random Forest Model):** [Laptop Worth Predictor](https://laptoworth.streamlit.app/)  
- **Alternative App (Linear Regression Model):** [Laptop Value Estimator](https://laptovaluex.streamlit.app/)  

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Main Application: Random Forest Model](#main-application-random-forest-model)
- [Alternative Model: Linear Regression](#alternative-model-linear-regression)
- [Web Scraping Module](#web-scraping-module)
- [Requirements](#requirements)
- [Usage](#usage)
- [License](#license)

## Overview

ByteWorth is a machine-learning-powered application designed to estimate laptop prices based on their specifications. It features two predictive models:

1. **Random Forest Model** (Main App) - A robust and accurate model for price prediction.
2. **Linear Regression Model** (Alternative App) - A simpler model that underperforms compared to Random Forest.

Both applications are deployed using **Streamlit**, making them accessible via the links provided above.

## Project Structure

The repository is organized as follows:

- `.devcontainer/` → Configuration files for development container setups.
- `Linear model/` → Contains the Linear Regression model app.
- `RF_model/` → Houses the main Random Forest model app.
- `Web Scrape/` → Scripts and notebooks for web scraping laptop data.
- `LICENSE` → Project licensing details.
- `README.md` → This documentation file.
- `requirements.txt` → Lists the dependencies required for the project.

## Main Application: Random Forest Model

📌 **Directory:** `RF_model/`  
📌 **Live Demo:** [Laptop Worth Predictor](https://laptoworth.streamlit.app/)  

This is the **primary** machine learning model used for predicting laptop prices. It utilizes a **Random Forest algorithm**, known for its superior performance in regression tasks. Users can enter laptop specifications to receive an estimated price.

**Key Files:**
- `RF_model.py` → The main Streamlit application file.
- `rf_model.pkl` → Pre-trained Random Forest model.
- `data/` → Training dataset used for model development.

## Alternative Model: Linear Regression

📌 **Directory:** `Linear model/`  
📌 **Live Demo:** [Laptop Value Estimator](https://laptovaluex.streamlit.app/)  

This app implements a **Linear Regression** model for price prediction. However, due to its simplicity, it does not perform as well as the Random Forest model.

**Key Files:**
- `Linear_model.py` → Streamlit app for Linear Regression.
- `linear_model.pkl` → Pre-trained Linear Regression model.
- `data/` → Training dataset.

## Web Scraping Module

📌 **Directory:** `Web Scrape/`  

A web scraping tool is included to gather real-world laptop pricing data for model training and updates from [Flipkart](www.flipkart.com)🛒

**Key Files:**
- `web_scrape.py` → Python script to extract laptop pricing data.
- `laptop_data.csv` → Collected dataset.

## Requirements

Install the necessary dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

To run the **Random Forest** model app locally:

```bash
streamlit run RF_model/RF_model.py
```

To run the **Linear Regression** model app locally:

```bash
streamlit run Linear_model/Linear_model.py
```

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

