import pandas as pd
productdim = pd.read_parquet("abfss://files@datalake73btp14.dfs.core.windows.net/Product_Dimsion.parquet")
resdimm = pd.read_parquet("abfss://files@datalake73btp14.dfs.core.windows.net/Resolution_Dimsion.parquet")
techdim = pd.read_parquet("abfss://files@datalake73btp14.dfs.core.windows.net/Tech_special_Dimion.parquet")
webdim = pd.read_parquet("abfss://files@datalake73btp14.dfs.core.windows.net/Website_Dimsion.parquet")
fact = pd.read_parquet("abfss://files@datalake73btp14.dfs.core.windows.net/Fact_Table.parquet")
productdim[["ram","storage"]] = productdim[["ram","storage"]].fillna(0.0)
fact[["price","price_before_promotion","rate"]] =fact[["price","price_before_promotion","rate"]].fillna(0.0)
resdimm[["width_resolution","height_resolution","screen_size","resolution"]]=resdimm[["width_resolution","height_resolution","screen_size","resolution"]].fillna(0.0)
resdimm

techdim
resdimm.dtypes


fact.columns
fact.dtypes

#fact = fact.astype({'cellular technology_id': 'str', 'wireless technology_id': 'str','wireless provider_id':'str','brand_id':'str','os_id':'str','model_id':'str','cpu_id':'str','color_id':'str','storage_id':'str','screen size_id':'str','resolution_id2f':'str'})

webdim.dtypes
techdim.dtypes
resdimm.dtypes
productdim.dtypes
fact.dtypes
resdimm.dtypes
resdimm
# fact.columns = fact.columns.str.replace(' ', '_')
# fact.columns


# resdimm.columns = resdimm.columns.str.replace(' ', '_')
# techdim.columns = techdim.columns.str.replace(' ', '_')
# webdim.columns = webdim.columns.str.replace(' ', '_')
# productdim.columns = productdim.columns.str.replace(' ', '_')
# productdim.columns


productdim.to_parquet("abfss://files@datalake73btp14.dfs.core.windows.net/Product_Dimsion.parquet",index=False)
#resdimm.to_parquet("abfss://files@datalake73btp14.dfs.core.windows.net/Resolution_Dimsion.parquet",index=False)
techdim.to_parquet("abfss://files@datalake73btp14.dfs.core.windows.net/Tech_special_Dimion.parquet",index=False)
webdim.to_parquet("abfss://files@datalake73btp14.dfs.core.windows.net/Website_Dimsion.parquet",index=False)
fact.to_parquet("abfss://files@datalake73btp14.dfs.core.windows.net/Fact_Table.parquet",index=False)
# Convert any specific columns that may be problematic
#resdimm['resolution'] = resdimm['resolution'].astype(str)  # if necessary

#engine='pyarrow'
resdimm.to_parquet("abfss://files@datalake73btp14.dfs.core.windows.net/Resolution_Dimsion.parquet",index=False)
