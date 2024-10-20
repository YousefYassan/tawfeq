IF NOT EXISTS (SELECT * FROM sys.external_file_formats WHERE name = 'SynapseParquetFormat') 
	CREATE EXTERNAL FILE FORMAT [SynapseParquetFormat] 
	WITH ( FORMAT_TYPE = PARQUET)
GO

IF NOT EXISTS (SELECT * FROM sys.external_data_sources WHERE name = '######################') 
	CREATE EXTERNAL DATA SOURCE [######################] 
	WITH (
		LOCATION = 'abfss://###@#######.dfs.core.windows.net' 
	)
GO

CREATE EXTERNAL TABLE dbo.VISP (
	[title] nvarchar(4000),
	[brand] nvarchar(4000),
	[os] nvarchar(4000),
	[ram] float,
	[cpu] nvarchar(4000),
	[storage] float,
	[screen size] float,
	[resolution] nvarchar(4000),
	[cpu speed] nvarchar(4000),
	[model] nvarchar(4000),
	[wireless provider] nvarchar(4000),
	[cellular technology] nvarchar(4000),
	[color] nvarchar(4000),
	[refresh rate] nvarchar(4000),
	[sim count] nvarchar(4000),
	[wireless technology] nvarchar(4000),
	[price] float,
	[price before promotion] float,
	[rate] float,
	[camera] nvarchar(4000),
	[img] nvarchar(4000),
	[website] nvarchar(4000),
	[currancy] nvarchar(4000),
	[url] nvarchar(4000),
	[reviews] nvarchar(4000),
	[width resolution] float,
	[height resolution] float
	)
	WITH (
	LOCATION = 'PDataConcatData.parquet',
	DATA_SOURCE = [files_datalake73btp14_dfs_core_windows_net],
	FILE_FORMAT = [SynapseParquetFormat]
	)
GO


SELECT TOP 100 * FROM dbo.VISP
GO