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


# Error Handling
Common errors handled in this project include:

Column Mapping Errors: Ensuring proper column names and mapping between source and target systems.
Data Type Mismatch: Resolving issues related to improper data types, particularly in numerical columns.
Missing Data: Handling missing or null values by applying appropriate transformations (e.g., imputation or default values).
