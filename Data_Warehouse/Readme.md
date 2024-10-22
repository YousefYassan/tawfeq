![SCHEMA_MODELING](https://github.com/user-attachments/assets/4a29875c-6523-4d34-8fb3-d8b4e6e1a22e)


## Slowly Changing Dimension (SCD) Type 2
Introduction
This project demonstrates the implementation of Slowly Changing Dimension (SCD) Type 2 in a data warehouse environment. SCD Type 2 is used to track historical changes in dimension records over time, allowing you to maintain both current and historical data in a single table.

# What is SCD Type 2?
SCD Type 2 preserves the history of changes in dimensional data by creating a new version of a record each time the source data changes. This method allows for the tracking of historical data and ensures that previous versions of dimension records are not overwritten.

# Key Features
Historical Tracking: Multiple versions of a dimension record are stored, allowing queries to reflect the correct data at any point in time.
Surrogate Keys: Each version of a dimension record is assigned a unique surrogate key.
Validity Dates: Each record has Start Date and End Date columns that represent the validity period of that version.
Current Record Flag: A flag (Current Flag) is used to indicate the most recent version of a record.


#  Data Warehouse on Dedicated SQL Pool - Specific Description
In this project, the Data Warehouse is implemented using a Dedicated SQL Pool within Azure Synapse Analytics. A Dedicated SQL Pool is a highly scalable, fully managed data warehousing solution that enables fast and complex analytical queries on large datasets. The data warehouse serves as the central repository for storing, querying, and analyzing business data processed through the ETL pipeline.

# Dedicated SQL Pool Overview:
Massively Parallel Processing (MPP):

The Dedicated SQL Pool uses MPP (Massively Parallel Processing) architecture, which distributes data and query workloads across multiple compute nodes. This allows for high-performance querying and processing of large volumes of data.
Queries are broken down into smaller tasks and executed in parallel across the compute nodes, reducing query execution time and improving efficiency.
Data Storage:

Data is stored in a columnar format within the dedicated pool, which optimizes the performance of read-heavy analytical workloads. The columnar storage reduces disk I/O by reading only the required columns, which leads to faster query execution.
The data in the dedicated pool is partitioned to enable quick data retrieval based on query patterns, ensuring that data retrieval is highly efficient even for very large datasets.
Integration with Azure Data Lake:

The Dedicated SQL Pool is closely integrated with Azure Data Lake and the Medallion Architecture. After data moves from the Gold Layer in the data lake, it is loaded into the dedicated pool using Copy Data activities in Azure Data Factory.
This integration allows for seamless movement of cleaned, structured, and enriched data from the Gold Layer in the lake into the dedicated pool, where it becomes available for downstream analytical processing.
Data Querying and Analytics:

The Dedicated SQL Pool is optimized for large-scale analytical queries, allowing users to run complex aggregations, joins, and calculations on high-dimensional data. The data warehouse can be queried using T-SQL.
Business intelligence tools such as Power BI can be directly connected to the pool to generate reports and dashboards, providing real-time insights based on the processed and enriched data.
Data Loading:

The data is loaded from the Azure Data Lake (Gold Layer) into the Dedicated SQL Pool using PolyBase or Copy Data activities in Azure Data Factory. The use of PolyBase allows for high-performance loading of data from external sources, such as Parquet files stored in the data lake, into the dedicated pool.
The loading process includes optimizing table structures, such as indexing and partitioning, to ensure that queries run efficiently on large datasets.
Concurrency and Scalability:

The Dedicated SQL Pool supports high levels of concurrency, allowing multiple users or applications to query the data simultaneously without performance degradation.
The pool is also highly scalable, with the ability to scale up or down the number of compute resources (Data Warehousing Units, or DWUs) based on the workload requirements. This ensures cost efficiency while maintaining high performance for heavy analytical workloads.
Security:

The Dedicated SQL Pool integrates with Azure Active Directory (AAD) for user authentication and role-based access control (RBAC), ensuring that only authorized users have access to the data.
Data encryption at rest and in transit is enforced to protect sensitive business data from unauthorized access.
# Benefits of Using a Dedicated SQL Pool:
High Performance: The MPP architecture allows the data warehouse to handle large volumes of data and complex queries with high speed and efficiency.

Scalability: The dedicated pool can scale resources up or down to accommodate varying workloads, ensuring performance optimization and cost management.

Seamless Integration: Integration with Azure Data Lake and Azure Data Factory ensures smooth data flow from the Medallion Architecture pipeline into the data warehouse.

Optimized Storage: Columnar storage and partitioning techniques are employed to minimize I/O and enhance query performance, especially for large datasets.

Business Intelligence: The dedicated pool serves as the backbone for reporting tools like Power BI, enabling real-time dashboards, reports, and data-driven decision-making for business users.
