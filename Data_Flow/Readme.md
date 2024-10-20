![second_pipline](https://github.com/user-attachments/assets/e1df2cb0-aa09-4229-ae45-7d4b9a36685d)


# Data Flow Description
The data flow for this project follows a structured ETL (Extract, Transform, Load) process using the Medallion Architecture. It moves data from the raw data source through various stages of processing before being loaded into a Data Warehouse for analytics. Below is the detailed data flow:


2. Data Transformation (Silver Layer)
Transformation Process:
Cleansing: Raw data is transformed to ensure consistency, handle missing values, and remove duplicates.
Normalization: Column formats are standardized, and necessary data type conversions are performed (e.g., converting text fields to numeric or datetime formats).
Joining: Fact and dimension tables are joined as needed, based on key relationships. For example, product data is linked with its respective technical specifications, resolution, and website details.
Tools: Data transformations are conducted using Azure Data Factory (ADF), where Copy Data activities are used to implement column mapping and data cleansing.
Storage: Transformed data is stored in the Silver Layer of the Data Lake. This data is now clean and organized, ready for aggregation.
3. Data Aggregation and Enrichment (Gold Layer)
Enrichment: In this phase, data is aggregated to create meaningful insights, such as total sales, average price, or product performance. Advanced calculations and summarizations are done here.
Fact and Dimension Tables: The data is modeled into Fact Tables (e.g., Fact_Sales) and Dimension Tables (e.g., Dim_Product, Dim_Technology). The star schema is applied to optimize querying and reporting performance.
Tools: The Azure Data Factory pipeline is used to load the curated data from the Silver Layer into the Gold Layer in the Data Lake.
4. Data Loading into Data Warehouse
Loading: The curated data from the Gold Layer is loaded into the SQL Data Warehouse for final storage. The Azure Data Factory (ADF) pipeline ensures high-speed data transfer and transformation as the data is ingested into the Data Warehouse.
Column Mapping: ADF Copy Data activities map the columns from the Silver/Gold Layer to the corresponding tables and columns in the Data Warehouse.
Optimization: The Data Warehouse is optimized for query performance by partitioning large datasets and creating appropriate indexes.
5. Consumption
Access: Once data is loaded into the Data Warehouse, it is ready for analysis and reporting. Data analysts and business intelligence tools can query the warehouse to generate insights, reports, and dashboards.
Tools: Analytics can be performed using tools such as Power BI, querying the warehouse directly for business insights and performance metrics.
