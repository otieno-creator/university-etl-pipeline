\# University Data ETL Pipeline



\##  Project Overview

This is a modular \*\*ETL (Extract, Transform, Load)\*\* pipeline built with Python. It automates the process of fetching university data from a public REST API, processing it into a structured format using Pandas, and exporting the final dataset for analysis.



\##  Features

\* \*\*Extraction\*\*: Real-time data retrieval from the \*Universities List API\*.

\* \*\*Transformation\*\*: 

&#x20;   \* Filtered relevant columns (Name, Country, State, Website).

&#x20;   \* Handled missing data (Null value imputation for State/Province).

&#x20;   \* Standardized URL formatting for easy access.

&#x20;   \* Injected processing timestamps for data auditing.

\* \*\*Loading\*\*: Generates a clean, ready-to-use `.csv` file.



\##  Tech Stack

\* \*\*Language\*\*: Python 3.x

\* \*\*Libraries\*\*: 

&#x20;   \* `Pandas`: Data manipulation and structuring.

&#x20;   \* `Requests`: Handling API calls.

&#x20;   \* `Datetime`: Metadata generation.



\##  How to Run

1\. Clone the repository:

&#x20;  ```bash

&#x20;  git clone \[https://github.com/otieno-creator/university-etl-pipeline.git](https://github.com/otieno-creator/university-etl-pipeline.git)

