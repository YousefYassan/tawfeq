![1694401816348](https://github.com/user-attachments/assets/d76195f4-cb36-4e17-be6c-c63d01870e22)

![image](https://github.com/user-attachments/assets/474ee1ad-0166-4b77-8453-dcee721e20ee)

![image](https://github.com/user-attachments/assets/a24ebfea-a751-4af8-8253-333de4fc17bf)

![Screenshot 2024-10-19 215657](https://github.com/user-attachments/assets/d2bb0a2d-bbd5-4446-b313-8d6821b8f86b)

![second_pipline](https://github.com/user-attachments/assets/0d71a83e-3c29-42d4-bcc8-dbbab5ee0c75)


![Screenshot 2024-10-20 192431](https://github.com/user-attachments/assets/9ca62930-4055-48bb-bae8-812e81380aa7)


# Data Engineering Project: Tawfeq
Project Overview:
The Tawfeq Data Engineering Project aims to build a scalable data pipeline that ingests, processes, and stores data from multiple sources into a structured format suitable for analysis and reporting. The project leverages Azure Data Lake, Azure SQL Data Warehouse, and Apache Spark for efficient data processing, transformation, and loading. Additionally, the project creates Parquet files to facilitate fast querying and efficient storage.

# Objectives:
Ingest data from various sources into the Azure Data Lake.
Transform raw data into a clean, structured format.
Load the transformed data into the Azure SQL Data Warehouse.
Create Parquet files for optimized data storage and access.
Automate the entire process using Azure Data Factory.

# Project Structure:
/src: Contains the Python and PySpark scripts for data processing and transformation.
/data: Holds raw and processed data in both CSV and Parquet formats.
/docs: Contains project documentation, including this README.
/notebooks: Jupyter notebooks for exploratory data analysis.
/config: Configuration files for data pipeline settings.


# Technology Stack
Azure Data Lake: For storing large volumes of raw data.
Azure SQL Data Warehouse: For structured storage of processed data.
Apache Spark: For data processing and transformation.
Azure Data Factory: For orchestration and automation of the ETL pipeline.
Python: For data manipulation and orchestration logic.
Pandas: For handling dataframes and performing data cleaning.
Parquet: For efficient data storage.
SQL Data Warehouse: Used for storing transformed data in structured formats.
ETL Medallion Architecture: A three-tier approach for data transformation and enrichment.

# Azure Functions: Data Scraping and Bronze Cleaning
Azure Functions are leveraged to automate the data scraping process. These serverless functions fetch data from various sources and immediately clean the data during ingestion to the Bronze Layer. The cleaning process includes removing duplicates, handling missing values, and ensuring format consistency before storing the data in the raw data layer.

# ETL Pipeline
The ETL pipeline follows the Medallion Architecture, which consists of three key layers:

Bronze Layer (Raw Data): This layer contains raw, unprocessed data ingested from multiple sources such as databases, APIs, or file systems. The data is stored in its original format and is mainly used for historical reference or future reprocessing.

Silver Layer (Cleaned Data): The data from the Bronze layer is processed and cleaned in the Silver layer. This involves transformations such as data type conversions, handling missing values, and filtering unnecessary records to ensure data consistency and usability for analysis.

Gold Layer (Aggregated Data): In this layer, the clean data from the Silver layer is further aggregated or enriched to create meaningful insights. It is optimized for reporting, analytics, and business intelligence tools.

# Data Pipeline
1. Data Ingestion
Data is ingested from the following sources:

CSV files: Stored in the Azure Data Lake.
APIs: External data sources pulled using Python scripts.
2. Data Transformation
The raw data is processed and transformed in multiple stages:

Cleaning: Removing duplicates, handling missing values, and fixing data types.
Standardization: Renaming columns, converting units, and applying formatting.
Enrichment: Adding calculated fields such as rates, averages, and growth metrics.
3. Data Loading
 Processed data is loaded into:

Azure SQL Data Warehouse: For querying and reporting.
Parquet Files: For storing optimized, structured data in the data lake.


# Why Use Proxies and IP Rotation?
When scraping data from websites, especially at scale, it's common to encounter anti-scraping mechanisms, such as:

IP Blocking: Sites can block or throttle requests from the same IP address.
Rate Limits: Some websites limit the number of requests from a single IP address over a specific time.

# By using IP rotation and proxy services, we ensure:

Anonymity: Requests appear to come from different IP addresses, avoiding detection.
Continuous Operation: If one IP gets blocked, another can be used without disrupting the scraping process.
Proxy Service and IP Rotation
We implemented IP rotation using a proxy provider that offers dynamic IPs from a global pool. The proxy service automatically assigns a different IP for each request, ensuring the scraper remains undetected.

# Steps for Implementation
Set Up Proxy: We configured our scraper to route requests through a proxy server.
Integrate IP Rotation: IP addresses were automatically rotated for each HTTP request to bypass rate limits and avoid detection.
Handle Errors and Retrying: Built-in mechanisms for retries and error handling in case of failed requests or blocked IPs.
# Technologies Used
Bypass Proxy: A proxy provider that supports IP rotation for large-scale scraping.
Python (requests/BeautifulSoup/Selenium): For making HTTP requests and parsing HTML content.


# Data Flow
Data Source (Azure Data Lake Storage Gen2 - Bronze Layer):

Raw data is stored in the Bronze Layer of the Data Lake. This raw data may come from different sources, such as scraping or transactional systems, and requires further processing and cleaning.
Bronze Layer: Contains raw, unstructured, or semi-structured data in Parquet, JSON, or CSV formats.
Copy Data Activity:

The Copy Data activity in Azure Data Factory extracts data from the Data Lake's Bronze Layer and copies it into the Silver Layer. During this process, data undergoes basic cleaning and transformation (e.g., type casting, format changes) to prepare it for downstream use.
This operation is highly scalable and can handle large volumes of data in parallel.
Data Transformation (Silver Layer):

Data in the Silver Layer is now structured and ready for deeper transformation. Here, more advanced cleaning and transformation are performed, including aggregations, deduplication, and joining with other datasets.
This layer serves as a staging area for refined and ready-to-analyze data.
Load to Data Warehouse (Gold Layer):

The processed data is loaded from the Silver Layer into the Data Warehouse (Gold Layer) for analysis and reporting.
Azure Synapse Analytics or another SQL-based data warehouse is used to store the clean, structured data for end-user access.
In this phase, the Copy Data activity writes data into the Gold Layer in a structured format (e.g., fact and dimension tables), ready for reporting and analysis.



# Key Tables
Product_Dimension: Contains product metadata such as brand, model, and specifications.
Resolution_Dimension: Captures screen resolution details like width, height, and resolution.
Tech_Special_Dimension: Stores technical specifications including cellular technology, wireless capabilities, and provider info.
Website_Dimension: Information about websites, including region, currency, and reviews.
Fact: All ideas,Price,Price_before,rate

# Key Features
Data Ingestion: Automates data ingestion from various structured and unstructured sources.
Data Transformation: Cleanses and transforms data into usable formats while maintaining a history of raw data.
Data Storage: Efficiently stores data in a structured format, ready for querying and analysis.
Error Handling: Captures errors during the data load process for easy debugging and reprocessing.

# Model Training and Development
# Data Preparation
The model is trained on a dataset that includes various device features and their corresponding prices.
Data preprocessing involves handling missing values, encoding categorical variables, and scaling numerical features to improve model performance.
# Model Selection
Multiple regression algorithms were evaluated, including:
Linear Regression: The primary algorithm used for predictions.
K-Nearest Neighbors (KNN): An alternative model for comparison.
Random Forest: Used for its robustness and ability to handle non-linear relationships.
Support Vector Regression (SVR): Evaluated for potential performance improvements.
# Performance Metrics
The model's performance is evaluated using the Root Mean Squared Error (RMSE), which provides insights into the model's accuracy on training and testing datasets.

# Contributing
Contributions to the project are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -m 'Add a new feature').
Push to the branch (git push origin feature-branch).
Open a pull request.

# Error Handling
Common errors handled in this project include:

Column Mapping Errors: Ensuring proper column names and mapping between source and target systems.
Data Type Mismatch: Resolving issues related to improper data types, particularly in numerical columns.
Missing Data: Handling missing or null values by applying appropriate transformations (e.g., imputation or default values).
