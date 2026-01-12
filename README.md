# Student Performance Project 📊

## 📌 Project Overview
This is a **modular Python project** for analyzing student academic performance.  
It focuses on **structured data ingestion, cleaning, validation, feature engineering, and predictive analysis**, built with **scalability in mind** for future analytics and risk assessment.

---

## 🛠 Key Features
- **Modular Structure:** All core functionality organized under `src/` for maintainability.  
- **Data Loading:** Efficient CSV loading for raw student data (marks, attendance, assignments).  
- **Data Cleaning & Validation:** Ensures data integrity before analysis.  
- **Feature Engineering:** Prepares data for predictive modeling.  
- **ML Predictions:** Predicts dropout probability and risk levels.  
- **Visualization:** Generates charts for dropout probability and risk level distribution.  
- **Future-ready:** Placeholder modules for advanced risk scoring.

---

## 📂 Project Structure
student-performance-project/
│
├── data/
│ └── student_academic_data.csv # Raw student data
├── src/
│ ├── init.py
│ ├── data_cleaner.py # Clean and preprocess data
│ ├── data_loader.py # Load CSV into DataFrame
│ ├── data_validator.py # Validate data integrity
│ ├── feature_engineering.py # Prepare features for ML models
│ ├── ml_prediction.py # Predict dropout probability
│ └── risk_labeling.py # Risk scoring and labeling logic
├── main.py # Entry point for analysis
├── .gitignore # Ignore virtual env, pycache, etc.
├── dropout_probability_distribution.png # Sample output chart
└── risk_level_distribution.png # Sample output chart


---

## 🚀 Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/pushpanjali316/student-performance-project.git


2. **Navigate to the project folder**
  cd student-performance-project

3. **Install dependencies (if required)**
  pip install -r requirements.txt

4. **Run the main program**

5. **python main.py**

This will load, clean, validate, and analyze student data, producing charts for dropout probability and risk levels.

📌 Author

Pushpanjali Vandavasi
