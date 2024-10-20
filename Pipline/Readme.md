![Screenshot 2024-10-19 215657](https://github.com/user-attachments/assets/f06e3e69-e3ea-40da-bdc0-514438ed03ab)


Pipeline Steps:
Data Ingestion (Bronze Layer):

Source: Data is scraped from various websites using Azure Functions with an IP rotation strategy via proxies (e.g., Bright Data Proxy) to prevent blocking and ensure reliable scraping.
Process: Azure Functions execute the scraping tasks and perform basic cleaning on the raw data. This includes handling missing values, format inconsistencies, and duplicates.
Storage: The raw and minimally cleaned data is stored in Azure Data Lake (Bronze Layer) in Parquet format for further processing.
Data Transformation (Silver Layer):

Process: The raw data from the Bronze Layer undergoes more advanced transformations. These include:
Data type casting (e.g., converting strings to integers, dates, etc.).
Joining multiple datasets (fact and dimension tables) to create a coherent structure.
Cleaning any additional inconsistencies and normalizing the data.
Tools: These transformations are handled using Azure Data Factory (ADF) Copy Data activities to map and transform columns.
Storage: The processed data is then stored in the Silver Layer of the Data Lake in a curated format.
Data Aggregation and Loading (Gold Layer):

Process: In the final stage, the data is aggregated and loaded into the Data Warehouse. This includes:
Summarizing data for analysis (e.g., total sales, average prices).
Fact and Dimension table creation following the star schema data model.
Loading: Data is loaded into the SQL Data Warehouse using ADF's Copy Data activities, ensuring high-performance data transfers and column mapping.
Optimization: Data Warehouse structures are optimized for reporting, including partitioning and indexing for query efficiency.
Data Storage:

Data Lake: Stores raw (Bronze), processed (Silver), and curated (Gold) data.
Data Warehouse: The final data is stored in a star schema structure, designed to optimize analytics and reporting.
Monitoring and Logging:

Azure Monitor: Tracks the pipeline's execution, ensuring that any failures or errors are logged and alerted.
Retry Logic: The pipeline includes robust retry logic for any failed jobs, especially during data ingestion and transformation, ensuring data reliability.
