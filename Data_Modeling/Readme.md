![ERD_MODELING](https://github.com/user-attachments/assets/4142b413-1828-4fad-a12e-c56fd992da90)

# Data Modeling
The data modeling approach in this project is centered around creating an efficient and scalable structure that supports both analytical and reporting needs. The data model is designed using a Star Schema architecture, which simplifies querying, enhances performance, and allows for easy data retrieval by end-users.

1. Fact Tables
Fact Tables contain the transactional and measurable data of the system. They are designed to hold the key business metrics that are analyzed, such as sales, prices, and performance rates. These tables are optimized for aggregations and joins with dimension tables.
Key Features:
Granularity: Each row represents a unique transaction or event, such as a product sale.
Foreign Keys: The Fact Tables contain foreign keys that reference the dimension tables, enabling the creation of relationships between facts and descriptive attributes.
Example: The Fact_Sales table contains fields like product_id, resolution_id, tech_spec_id, website_id, and measurable attributes like price, promotion_price, and quantity_sold.
2. Dimension Tables
Dimension Tables hold the descriptive data that provides context to the facts. These tables include attributes that define the various entities such as products, technology specifications, resolutions, websites, and customer segments.
Key Features:
Denormalization: Dimension tables are typically denormalized to provide a flat structure for querying, enhancing performance by reducing the need for multiple joins.
Hierarchies: Some dimensions include hierarchies that allow for deeper analytical insights, such as grouping products by brand or categorizing technologies by type.
Example:
The Dim_Product table contains attributes like product_name, brand_id, os_id, model_id.
The Dim_Technology table stores attributes like tech_spec_id, wireless_technology, cellular_technology, and sim_count.
3. Star Schema Design
The core design pattern of this model is a Star Schema, where the Fact Tables form the "center" of the star, and the Dimension Tables radiate outward. This structure allows for fast querying and simple relationships between facts and dimensions, which is ideal for analytic workloads.
Benefits:
Query Performance: The star schema optimizes performance by minimizing joins and simplifying SQL queries.
Ease of Use: Business users can easily understand and query the data model, as it mirrors natural language questions like “What is the total sales by product and technology type?”
4. Surrogate Keys
Surrogate keys are used as primary keys in the dimension tables. These are typically integer keys that uniquely identify each record and provide faster joins with the Fact Tables.
Example: The Dim_Product table would have a surrogate key like product_id that serves as the primary key and connects to the product_id foreign key in the Fact_Sales table.
5. Model Optimization
Partitioning: The large Fact Tables are partitioned by time (e.g., daily, monthly) or other relevant dimensions to improve query performance.
Indexing: Appropriate indexing strategies are applied to the Fact and Dimension Tables to optimize joins and queries.
Compression: Data compression techniques are used in the Data Warehouse to reduce storage footprint while maintaining query performance.
6. Handling Slowly Changing Dimensions (SCD)
To handle changing attributes in Dimension Tables, such as product prices or specifications, the model supports Slowly Changing Dimensions (SCD). For example, when product specifications change, the model can store historical values alongside current ones.
SCD Type 2 is used to capture historical data by creating new rows in the dimension table with new surrogate keys when changes occur.
