CREATE TABLE [dbo].[ProductDimension] (
    [product_id] NVARCHAR (50)     NOT NULL,
    [title]      NVARCHAR (255) NULL,
    [brand]      NVARCHAR (255) NULL,
    [os]         NVARCHAR (255) NULL,
    [ram]         FLOAT  NULL,
    [cpu]        NVARCHAR (255) NULL,
    [storage]     FLOAT NULL,
    
    [model]      NVARCHAR (255) NULL,
    [color]      NVARCHAR (255) NULL,
    [camera]     NVARCHAR (50)  NULL,
    [img]        NVARCHAR (4000) NULL,  -- Change MAX to 4000 (or a suitable size)
    CONSTRAINT [PK_product] PRIMARY KEY NONCLUSTERED ([product_id] ASC) NOT ENFORCED
)
WITH
(
    DISTRIBUTION = HASH (product_id),
    CLUSTERED COLUMNSTORE INDEX
)
GO
