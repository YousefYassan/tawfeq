CREATE TABLE [dbo].[TechSpecialDimension] (
    [tech_spec_id]        NVARCHAR (255)            NOT NULL,
    [wireless_technology] NVARCHAR (255) NULL,
    [wireless_provider]   NVARCHAR (255) NULL,
    [cellular_technology] NVARCHAR (255) NULL,
    [sim_count]           NVARCHAR (255)            NULL,
    CONSTRAINT [PK_tecsp] PRIMARY KEY NONCLUSTERED ([tech_spec_id] ASC) NOT ENFORCED
)
WITH
(
    DISTRIBUTION = HASH (tech_spec_id),
    CLUSTERED COLUMNSTORE INDEX
)
GO
