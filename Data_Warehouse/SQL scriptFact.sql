CREATE TABLE [dbo].[Fact] (
    [product_id]             NVARCHAR (255)             NOT NULL,
    [resolution_id]          NVARCHAR (255)             NOT NULL,
    [tech_spec_id]           NVARCHAR (255)             NOT NULL,
    [website_id]             NVARCHAR (255)             NOT NULL,
    [cellular_technology_id] NVARCHAR (255)             NOT NULL,
    [wireless_technology_id] NVARCHAR (255)             NOT NULL,
    [wireless_provider_id]   NVARCHAR (255)             NOT NULL,
    [brand_id]               NVARCHAR (255)             NOT NULL,
    [os_id]                  NVARCHAR (255)             NOT NULL,
    [model_id]               NVARCHAR (255)             NOT NULL,
    [cpu_id]                 NVARCHAR (255)             NOT NULL,
    [color_id]               NVARCHAR (255)             NOT NULL,
    [storage_id]             NVARCHAR (255)             NOT NULL,
    [screen_size_id]         NVARCHAR (255)             NOT NULL,
    [resolution_id2f]        NVARCHAR (255)             NOT NULL,
    [price]                 FLOAT NULL,
    [price_before_promotion] FLOAT NULL,
    [rate]                   FLOAT  NULL

    -- Surrogate Key with NOT ENFORCED constraint
)
