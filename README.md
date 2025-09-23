
# Olist E-commerce Data Analysis

##  Project Overview

This project analyzes the **Olist E-commerce Dataset** to uncover patterns in customer behavior, seller performance, product categories, and overall marketplace dynamics.
It is built using a **modular pipeline structure** with **data cleaning, loading, and analysis components**, and includes **logging** for tracking each step.

---

##  Objectives

* Clean and transform raw data for analysis.
* Load cleaned data into a MySQL database.
* Automate the pipeline with `main.py`.
* Perform **SQL + Python-based analysis** for insights.
* Provide **business recommendations** based on findings.

---

## Project Structure

```
olist-ecommerce-analysis/
│── data/                     # Raw datasets
│── logs/                     # Logs for each step
|   │──logger_config.py       # Configuration of logger
│── config/                   # Database configuration
│── scripts/
│   │── clean_data.py         # Class for data cleaning
│   │── load_data.py          # Class for data loading into MySQL
│   │── analysis.ipynb        # SQL + Python analysis functions
│── main.py                   # Runs the full pipeline
│── requirements.txt          # Dependencies
│── README.md                 # Project documentation
```

---

##  Tech Stack

* **Language:** Python
* **Database:** MySQL
* **ORM:** SQLAlchemy
* **Libraries:** Pandas, NumPy, Matplotlib, Seaborn
* **Logging:** Python logging module

---

## Pipeline Workflow

1. **Loading (`loading.py`)**

   * Loads datasets into MySQL tables.
   * Ensures correct schema mapping.
   * Logs database operations.

2. **Cleaning (`cleaning.py`)**

   * Handles missing values, duplicates, and datatype conversions.
   * Creates new columns (e.g., extracting dates from timestamps).
   * Logs every operation for reproducibility.

3. **Analysis (`analysis.py`)**

   * Executes **SQL queries via SQLAlchemy**.
   * Aggregates and transforms data with Pandas.
   * Generates **visualizations**.

4. **Pipeline Runner (`main.py`)**

   * Orchestrates the cleaning → loading → analysis pipeline.
   * One command runs the entire workflow.

---

## 📊 Key Analyses

* **Revenue Trends:** Monthly and yearly revenue.
* **Customer Retention:** Repeat vs one-time customers.
* **Payment Insights:** Most used payment types & installment behavior.
* **Product Categories:** Revenue leaders and low performers.
* **Review Analysis:** Correlation with delivery days & freight cost.
* **Seller Analysis:** High-performing vs poor-review sellers.

---

## 📈 Insights (Sample)

* **Credit cards dominate transactions** (\~80% of revenue).
* **Retention rate is very low** (\~3%) → loyalty programs needed.
* **High freight costs & long delivery times lead to poor reviews**.
* **Health & Beauty, Watches & Gifts, Bed & Bath** are top categories.



The Olist dataset is a large Brazilian e-commerce public dataset of ~100,000 orders between 2016–2018, containing tables for orders, order items, payments, reviews, products, customers, and sellers

. The business objective was to analyze sales and customer behavior on Olist’s marketplace, answering questions about product categories, seller performance, payment habits, delivery and review dynamics, customer retention, seasonality, and installment behavior, to inform strategic decisions (marketing, seller management, logistics, etc.).

Data Pipeline

Data Loading: We created a data loading component (e.g. a DataLoader class or ETL script) that ingests the raw CSV files and loads them into a SQL database. This involves parsing each Olist table and storing it in SQL tables, enabling efficient querying.

Data Cleaning: After loading, a DataCleaner class or script processes the SQL tables to fix data issues. This includes removing duplicates, handling missing values, standardizing formats, and converting data types. All cleaning steps log their actions (e.g. number of rows dropped, anomalies found) to ensure transparency.

Sequence: The pipeline runs in order: (1) load raw data into SQL, (2) then clean the loaded data. This ensures we never alter the raw source directly and maintain a clear audit trail via logs.

Business Questions Addressed

We addressed key business questions, including:

Which product categories generate the most revenue?

Which sellers perform best or worst based on reviews and sales?

What are the most preferred payment methods and how do they relate to order value?

How do review scores correlate with delivery time and freight cost?

Customer retention: what fraction of customers are repeat buyers vs one-time?

Is there seasonality in orders or revenue (monthly/quarterly patterns)?

What is the relationship between order value and payment installment usage?

Key Insights and Visualizations

Top Categories by Revenue: The cama_mesa_banho (bed/bath/table goods) category earned the most revenue (R$1,692,557) in 2016–2018

. It was followed by beleza_saude (health & beauty) and informatica_acessorios (computer accessories)

. (These Portuguese category names are often abbreviated; we give English in parentheses.) This means household and daily-use items (bed & bath) are driving sales. Computer accessories also sold well, with a notable peak in February 2018

. Overall, total revenue over two years (2017-18) was ~R$15–15.9M, peaking in Q2 2018 and dipping by Q3 2018.


. Seller Performance: Sellers rated 3.5-4.5 stars accounted for the bulk of orders and revenue, indicating top-rated sellers perform the best

. Sellers with high review scores have the most orders and highest revenue

. In contrast, low-rated sellers had fewer orders; an interesting anomaly is that one-star sellers had very high average revenue (on limited orders)

. This suggests a strong correlation between good reviews and sales volume. (Worst-performing sellers by reviews tended to have weaker sales.)

Payment Methods: Credit cards dominate: ~76,505 orders used credit card, making it the most common payment method

. Boleto (bank ticket) was second (~19,784 orders), then vouchers (~3,866) and debit cards (~1,528)

. Average order values (AOV) vary by method: credit card orders had the highest AOV (~R$162.70), while voucher-paid orders had the lowest (~R$62.33)
. (Overall AOV was ~R$153.44.) This implies that customers paying by credit are making larger purchases, whereas vouchers tend to be used for smaller orders.

Review Score vs Delivery/Freight: There is a strong negative correlation between delivery time and review score(-0.97)

. Faster deliveries get better reviews: on average, 5-star orders were delivered in ~10.6 days, while 1-star orders took ~21.2 days

. Hence, each day of delay significantly lowers satisfaction. Freight cost is driven by item weight/volume

. Heavier or bulkier items incur higher shipping fees (correlation ~0.61 with weight)

. Data suggests shipping delays (rather than cost alone) are the main driver of low scores

. This indicates logistics critically affect customer satisfaction.

Customer Retention: Repeat buyers are rare. Out of ~96,096 customers, only 2,997 (~3%) made more than one purchase

. A vast majority of customers (~97%) is one-time buyers

. Repeat customers generated only 5.5% of total revenue

. In other words, retention is very low (only ~3% return), highlighting a major growth opportunity: most revenue comes from one-off purchases.

Seasonality: Order and revenue volume show clear peaks and troughs. The end of year and mid-year quarters stood out: November 2017 had the most orders, and overall Q2 2018 was the highest-revenue quarter

. By contrast, September 2018 and December 2016 had anomalously few orders

. Many categories have their own cycles – for example, computer accessories spiked in February 2018

. In general, demand is higher in mid-year (Q2) and around holiday season, with lulls in late 2016 and late 2018.

Order Value vs Installments: Customers using more installments(avg ~6) tend to buy higher-priced items. Overall AOV is ~R$1153

. By category, informatica_acessorios (computers) had the highest AOV, whereas high-volume categories like cama_mesa_banho had low AOV (many small purchases)

. By payment type, credit card purchases had the highest AOV (~R$162.70) and vouchers the lowest (~R$62.33)

. This indicates that larger orders are often paid by credit with multiple installments, whereas small everyday purchases are more likely one-time/voucher transactions.

Recommendations

Target Marketing for Daily-Use Categories: Focus promotions on high-revenue, low-AOV categories (e.g. bed_bath_table / home essentials, health & beauty)

. These are everyday items that many customers buy frequently. Tailored campaigns (e.g. subscription bundles or loyalty points for these categories) could boost order count and customer retention.

Strengthen Low-Performing Sellers: Sellers with low review scores need intervention or corrective action. Since high-rated sellers drive the most sales.
Morever, improving seller practices (e.g. training on customer service, enforcing quality standards) will likely raise overall satisfaction. Implement alerts when a seller’s rating falls below a threshold so issues can be resolved quickly.

Optimize Logistics for Problem Categories: Address delays and costs in categories prone to late deliveries. For example, heavy/bulky goods (furniture, appliances) often incur long transit times and high freight.

Olist should identify routes or items with slow deliveries and consider measures like regional warehouses or faster carriers. Since longer delivery correlates with worse reviews, improving shipping speed and reducing hidden freight costs will directly enhance customer satisfaction.

Conclusion

This comprehensive analysis of the Olist dataset uncovered actionable insights: a few product categories dominate revenue; sellers’ ratings strongly influence sales; payment method and installment choices reflect order size; and customer retention is very low. By targeting marketing to popular daily-use categories, supporting underperforming sellers, and fixing logistics bottlenecks, Olist can increase sales and satisfaction. In sum, data-driven strategies from this analysis can help Olist grow revenue and loyalty in its Brazilian marketplace.
---

## 🚀 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/olist-ecommerce-analysis.git
   cd olist-ecommerce-analysis
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up MySQL database and update credentials in:

   ```
   config/db_config.py
   ```

4. Run the pipeline:

   ```bash
   python main.py
   ```

---

##  Future Enhancements

* Add automated **data validation tests** before loading.
* Deploy interactive **dashboard (Tableau/Power BI/Streamlit)**.
* Build a **churn prediction model**.

---

##  Author

* **Name:** \[Your Name]
* **LinkedIn:** \[Your Profile]
* **GitHub:** \[Your Profile]

---

