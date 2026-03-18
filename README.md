#  University Data ETL Pipeline

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)](https://www.python.org)
[![Pandas](https://img.shields.io/badge/Library-Pandas-orange?style=flat)](https://pandas.pydata.org)

##  Project Overview
This project is a modular **ETL (Extract, Transform, Load)** pipeline designed to automate the lifecycle of academic data. It fetches real-time university information from a public REST API, cleanses it using the Pandas library, and structures it for high-level analytical reporting.

---

##  Key Features

###  Extraction
* **Real-time Retrieval:** Automated data fetching from the *Universities List API*.
* **Seamless Integration:** Designed to handle live JSON responses efficiently.

###  Transformation
* **Precision Filtering:** Selects high-value columns (Name, Country, State, Website) for cleaner datasets.
* **Data Integrity:** Implements **Null Value Imputation** for missing State/Province entries to ensure consistency.
* **Standardization:** Automated URL formatting for uniform link access across the dataset.
* **Audit Ready:** Injects processing timestamps for full data lineage and auditing.

###  Loading
* **Structured Export:** Generates finalized datasets optimized for downstream analysis and visualization.

---

##  Tech Stack
* **Language:** Python 3.x
* **Data Processing:** Pandas
* **API Interaction:** Requests
* **Version Control:** Git & GitHub

##  How to Use
1. Clone the repository.
2. Install dependencies: `pip install pandas requests`
3. Run the main script: `python main.py`
