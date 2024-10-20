CREATE TABLE [dbo].[ResolutionDimension] (
    [resolution_id]             NVARCHAR (255)            NOT NULL,
    [width_resolution]  FLOAT            NULL,
    [height_resolution] FLOAT            NULL,
    [resolution]      NVARCHAR (255)  ,
    [screen_size]      FLOAT  NULL,
    CONSTRAINT [PK_reso] PRIMARY KEY NONCLUSTERED ([resolution_id] ASC) NOT ENFORCED
)
WITH
(
    DISTRIBUTION = HASH (resolution_id),
    CLUSTERED COLUMNSTORE INDEX
)
GO
