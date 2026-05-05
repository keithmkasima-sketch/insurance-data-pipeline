# Insurance Data Pipeline

## Overview  
Goal: Get data from a CSV file, clean it, convert it to the right data types, create a database and store it in the database.  

This project shows a full **ETL (Extract, Transform, Load) pipeline** using Python, pandas, and SQLite.  
The dataset contains insurance customer demographics and charges.  


## GOAL

1. **Locate the data**  
-Insurance dataset stored in `data/insurance_Dataset.csv`.  

2. **Extract**  
-Load CSV file using pandas.  

3. **Remove duplicate values**  
-Drop duplicate rows to ensure unique records.  

4. **Handle missing values**  
-Drop rows missing critical values (`age`, `sex`, `smoker`, `charges`).  
-Fill missing BMI with mean.  
-Fill missing region with `"unknown"`.  

5. **Convert to the right data types**  
-`age` → integer  
-`children` → integer  
-`bmi` → float  
-`charges` → float  

6. **Standardize text**  
-Strip whitespace and lowercase values for `sex`, `smoker`, and `region`.  

7. **Create a database**  
-SQLite database file: `insurance_clean.db`.  

8. **Load the clean data into a database table**  
-Store transformed dataset in SQLite for structured queries.  

## How to Run  
1. Clone the repository:  
   ```bash
   git clone https://github.com/keithmkasima-sketch/insurance-data-pipeline.git
   cd insurance-data-pipeline
