# 🧠 SuperStore BI & Predictive Analytics Project

## 📁 Project Overview
This project is an **end-to-end Business Intelligence (BI) and Predictive Analytics pipeline** built on the **Superstore dataset**.  
The goal is to explore, analyze, and extract **insightful and predictive KPIs (Key Performance Indicators)** that reflect customer behavior, sales performance, profitability, and future trends.

---

## 📂 Project Structure

```
SuperStore-Analyze/
│
├── .venv/                         # Virtual environment
│
├── DataSet/                       # Data files
│   ├── Superstore.csv
│   ├── Superstore_Featured.csv
│   ├── Customer_Segmentation_Labeled.csv
│   ├── customers.csv
│   ├── initial_data.py
│
├── EDA/
│   └── EDA.py                     # Data exploration and initial preprocessing
│
├── KPIs/
│   ├── Insightive/                # Descriptive & Diagnostic KPIs
│   │   ├── Basic.py               # Base metrics (Revenue, Profit, Discount, etc.)
│   │   ├── customer_KPIs.py       # Customer-related KPIs (Frequency, Retention, AOV)
│   │   ├── P&C_KPIs.py            # Product & Category KPIs (Top Products, Profitability)
│   │   └── product_KPIs.py        # Product-level advanced metrics
│   │
│   ├── Predictive/                # Predictive & Advanced KPIs
│   │   ├── CLV.py                 # Customer Lifetime Value prediction (XGBoost)
│   │   ├── Churn_Rate.py          # Churn prediction model (Random Forest)
│   │   └── Customer_Segmentation.py # Customer clustering (KMeans)
│
├── README.md                      # Project documentation (this file)
```

---

## 📊 KPIs Extracted

### 🔹 Basic KPIs
| KPI | Description | Formula / Logic |
|-----|--------------|-----------------|
| Total Sales | Total revenue generated | Sum of `Sales` |
| Total Profit | Overall profit | Sum of `Profit` |
| Total Orders | Count of unique orders | Count of `Order ID` |
| Average Discount | Mean of discount applied | Mean of `Discount` |
| Profit Margin | Profit-to-sales ratio | `Profit / Sales` |

---

### 🔹 Customer KPIs
| KPI | Description | Purpose |
|------|-------------|----------|
| Average Order Value (AOV) | Average sales per order | Measures order profitability |
| Purchase Frequency | Orders per customer | Evaluates customer engagement |
| Retention Rate | Returning customers ratio | Indicates loyalty |
| Customer Lifetime Value (CLV) | Predicts total value per customer | Long-term profitability measure |
| Recency | Days since last purchase | Used in churn analysis |
| Customer Age | Active duration of a customer | Indicates relationship longevity |

---

### 🔹 Product & Category KPIs
| KPI | Description | Insight |
|------|-------------|----------|
| Top Selling Products | Products with highest sales | Guides inventory decisions |
| Most Profitable Categories | Highest margin product categories | Supports marketing prioritization |
| Discount Effect on Profit | Analyzes impact of discounts | Determines optimal pricing strategy |

---

### 🔹 Predictive KPIs
| KPI | Model | Description | Metric |
|------|--------|-------------|---------|
| CLV Prediction | XGBoost Regressor | Predicts future sales value per customer | MAE, RMSE |
| Churn Prediction | Random Forest Classifier | Classifies customers as Active or Churned | Accuracy, Recall |
| Customer Segmentation | KMeans Clustering | Groups customers into distinct behavioral clusters | Cluster Inertia, Silhouette Score |

---

## 🤖 Machine Learning Models Used

| Model | Type | Purpose | Key Notes |
|--------|------|----------|------------|
| **XGBoost Regressor** | Supervised | Predict Customer Lifetime Value | Handles non-linear relationships, robust to outliers |
| **Random Forest Classifier** | Supervised | Predict customer churn | High interpretability, prevents overfitting |
| **KMeans Clustering** | Unsupervised | Group customers into behavioral clusters | Used for market segmentation and personalized strategies |

---

## 🧮 Example Cluster Labels (Customer Segmentation)

| Cluster | Description | Characteristics |
|----------|--------------|----------------|
| **Cluster 0** | Mid-tier steady buyers | Moderate sales, consistent engagement |
| **Cluster 1** | Dormant or lost customers | Low recency, high churn rate |
| **Cluster 2** | High-value premium customers | High sales and profit |
| **Cluster 3** | Loyal, frequent small buyers | Stable purchases, low churn |

---

## 🧰 Tools and Libraries
- **Python 3.10+**
- **Pandas, NumPy**
- **Matplotlib, Seaborn**
- **Scikit-learn**
- **XGBoost**
- **KaggleHub (for dataset management)**

---

## ⚙️ How to Run the Project

```bash
# Clone the repository
git clone https://github.com/<your_username>/SuperStore-Analyze.git
cd SuperStore-Analyze

# Activate environment
source .venv/bin/activate  # (Linux/Mac)
# or
.venv\Scripts\activate   # (Windows)

# Run EDA
python EDA/EDA.py

# Run KPIs
python KPIs/Insightive/Basic.py
python KPIs/Insightive/customer_KPIs.py
python KPIs/Predictive/CLV.py
python KPIs/Predictive/Churn_Rate.py
python KPIs/Predictive/Customer_Segmentation.py
```

---

## 🧾 Business Insights
- **High-value customers** (Cluster 2) generate over **3× more revenue** than average.
- **Churn rate** for dormant customers exceeds **80%**, signaling potential retention issues.
- **CLV model** shows strong correlation between **Sales per Day** and **Customer Profitability**.
- **Discount impact analysis** indicates that aggressive discounting **reduces profit margin by ~18%**.

---

## 📈 Project Summary
This project simulates a **real-world retail BI pipeline**, from **data preparation → KPI extraction → predictive modeling → customer segmentation**.  
It provides a foundation for integrating **data science with business strategy**, enabling smarter, data-driven decision-making.

---

## 👨‍💻 Author
**Developed by:** [Your Name]  
**GitHub:** [https://github.com/YourUsername](https://github.com/YourUsername)  
**Date:** 2025  
