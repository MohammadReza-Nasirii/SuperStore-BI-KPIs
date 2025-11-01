# 🧠 Superstore KPI & Predictive Business Intelligence Project

## 📊 Project Overview
This project focuses on **analyzing, visualizing, and predicting key business KPIs** using the popular **Superstore dataset**.  
The main goal is to simulate a **real-world business intelligence workflow** — from **data preprocessing and KPI extraction** to **predictive modeling and customer segmentation**.

The project blends **data analytics**, **machine learning**, and **business insight generation** into a complete BI workflow.

---

## 🚀 Objectives
1. Perform **data cleaning and preprocessing** on real-world sales data.  
2. Calculate **key business performance metrics (KPIs)** across different dimensions (Sales, Profit, Customers, Regions, etc.).  
3. Build **predictive models** to forecast revenue and identify customer churn.  
4. Use **unsupervised learning (K-Means)** for customer segmentation.  
5. Deliver **actionable insights** that can drive strategic business decisions.

---

## 📁 Project Structure
```
SuperStore-Analyze/
│
├── DataSet/
│   ├── Superstore.csv
│   ├── Superstore_Featured.csv
│   ├── Customer_Segmentation_Labeled.csv
│
├── EDA/
│   ├── EDA.py
│
├── KPIs/
│   ├── Descriptive/
│   ├── Predictive/
│   │   ├── CLV_Prediction.py
│   │   ├── Churn_Rate.py
│   │   ├── Customer_Segmentation.py
│
├── Docs/
│   ├── KPI_Guide.pdf
│   ├── Predictive_KPIs.pdf
│   ├── Segmentation_Report.pdf
│
└── README.md
```

---

## 🧩 Tools & Technologies
| Category | Tools / Libraries |
|-----------|------------------|
| **Programming** | Python 3.12 |
| **Data Analysis** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Machine Learning** | Scikit-learn, XGBoost |
| **Data Source** | Kaggle – Superstore Dataset |
| **Environment** | Jupyter / PyCharm |
| **Version Control** | Git + GitHub |

---

## 📈 KPIs Implemented
### **Descriptive KPIs**
| KPI | Description |
|------|-------------|
| **Total Sales** | Sum of all sales transactions. |
| **Total Profit** | Revenue minus cost for all sales. |
| **Average Discount** | Mean discount given per order. |
| **Average Order Value (AOV)** | `Total Sales / Total Orders`. |
| **Profit Margin** | `Profit / Sales * 100`. |
| **Sales Growth Rate** | Percentage increase vs previous period. |

---

### **Customer KPIs**
| KPI | Description |
|------|-------------|
| **Customer Retention Rate** | Active customers who continue buying. |
| **Customer Lifetime Value (CLV)** | Predicts total expected profit from each customer. |
| **Customer Churn Rate** | Percentage of customers who stopped purchasing. |
| **Recency, Frequency, Monetary (RFM)** | Used to segment customers by engagement level. |

---

### **Predictive KPIs**
| KPI | Description | Model Used |
|------|-------------|-------------|
| **CLV Prediction** | Predicts customer lifetime value. | XGBoost |
| **Churn Prediction** | Classifies customers as churned or active. | Random Forest |
| **Customer Segmentation** | Groups customers with similar patterns. | K-Means |

---

## 🤖 Machine Learning Models
| Model | Type | Purpose |
|--------|------|----------|
| **XGBoost Regressor** | Supervised | Predicting CLV (continuous values). |
| **Random Forest Classifier** | Supervised | Predicting churned vs active customers. |
| **K-Means Clustering** | Unsupervised | Customer segmentation. |

---

## 📊 Predictive Model Results
| Model | MAE | RMSE | Accuracy |
|--------|-----|------|-----------|
| **XGBoost (CLV)** | 238.52 | 748.84 | — |
| **Random Forest (Churn)** | — | — | 100% |
| **K-Means (Segmentation)** | — | — | 4 Distinct Clusters |

---

## 🧠 Customer Segmentation Insights
| Cluster | Label | Description |
|----------|--------|-------------|
| **0** | Core Loyal Customers | Long-term buyers with low churn. |
| **1** | At-Risk Customers | Haven’t purchased recently, high churn. |
| **2** | High-Value Customers | Generate large sales and profit. |
| **3** | Active Growing Customers | Recently active with potential to become VIPs. |

---

## 📉 Visual Insights
- **Elbow Curve** → Optimal cluster number selection.  
- **Sales vs Profit Scatter Plot** → Cluster visualization.  
- **Feature Importance Charts** → For both CLV and Churn models.  
- **Error Distribution Plot** → Model residuals validation.  

---

## 🧾 Key Business Takeaways
✅ Identify high-value customers (VIPs) for loyalty programs.  
✅ Detect churn risk early using predictive models.  
✅ Segment customers for targeted marketing.  
✅ Optimize discounts based on profitability.  
✅ Forecast sales & profit trends for planning.  

---

## 💾 Saving Results
```python
customer_df.to_csv('../../DataSet/Customer_Segmentation_Labeled.csv', index=False)
```

---

## 🧮 Future Work
- Integration with Power BI dashboard.  
- Deploy models as APIs for real-time analytics.  
- Automate monthly KPI reports.  

---

## 👨‍💻 Author
**Developer:** [Your Name]  
**GitHub:** [Your GitHub Profile Link]  
**Project Duration:** 10 Days (3 hours/day)  
**Skills Demonstrated:**  
`Python`, `Machine Learning`, `EDA`, `KPI Design`, `Predictive Modeling`, `Customer Analytics`, `Business Intelligence`

---

## 🌟 Final Thoughts
This project represents a **complete end-to-end BI workflow** — from raw data to actionable intelligence.  
It not only measures what happened but also predicts what will happen and why, enabling **data-driven business growth**.
