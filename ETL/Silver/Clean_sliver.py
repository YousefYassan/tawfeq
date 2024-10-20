{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 92,
      "metadata": {},
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "\n",
        "dfeg=pd.read_csv(\"abfss://##@#######.dfs.core.windows.net/PData.csv\")\n",
        "\n",
        "\n",
        "dfsa=pd.read_csv(\"abfss://##@#######.dfs.core.windows.net/PData_SA.csv\")\n",
        "dfnl=pd.read_csv(\"abfss://##@#######.dfs.core.windows.net/PData_NL.csv\")\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 93,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "dfeg['Region']='Egypt'\n",
        "dfsa['Region']='Saudi Arabia'\n",
        "dfnl['Region']=\"Netherlands\"\n",
        "dfsa.drop(columns=['refresh rate'], inplace=True)\n",
        "dfeg.drop(columns=['refresh rate'], inplace=True)\n",
        "dfnl.drop(columns=['refresh rate'], inplace=True)\n",
        "\n",
        "df=pd.concat([dfnl,dfsa,dfeg],ignore_index=True)\n",
        "df"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 94,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "b={}\n",
        "db=df['brand']\n",
        "db=db.unique()\n",
        "db\n",
        "\n",
        "for i in range(len(db)):\n",
        "    b[db[i]]=i\n",
        "\n",
        "s={}\n",
        "sb=df['storage']\n",
        "sb=sb.unique()\n",
        "sb\n",
        "\n",
        "for i in range(len(sb)):\n",
        "    s[sb[i]]=i\n",
        "\n",
        "\n",
        "c={}\n",
        "cb=df['color']\n",
        "cb=cb.unique()\n",
        "cb\n",
        "\n",
        "for i in range(len(cb)):\n",
        "    c[cb[i]]=i\n",
        "\n",
        "m={}\n",
        "mb=df['model']\n",
        "mb=mb.unique()\n",
        "mb\n",
        "\n",
        "for i in range(len(mb)):\n",
        "    m[mb[i]]=i\n",
        "\n",
        "o={}\n",
        "ob=df['os']\n",
        "ob=ob.unique()\n",
        "ob\n",
        "\n",
        "p={}\n",
        "pb=df['cpu']\n",
        "pb=pb.unique()\n",
        "pb\n",
        "\n",
        "for i in range(len(pb)):\n",
        "    p[pb[i]]=i\n",
        "   \n",
        "\n",
        "for i in range(len(ob)):\n",
        "    \n",
        "    o[ob[i]]=i\n",
        "\n",
        "\n",
        "w={}\n",
        "wb=df['website']\n",
        "wb=wb.unique()\n",
        "wb\n",
        "\n",
        "for i in range(len(wb)):\n",
        "    \n",
        "    w[wb[i]]=i\n",
        "\n",
        "\n",
        "#screansize and resltion and concat to reslution id \n",
        "\n",
        "scr={}\n",
        "scb=df['screen size']\n",
        "scb=scb.unique()\n",
        "scb\n",
        "\n",
        "for i in range(len(scb)):\n",
        "    \n",
        "    scr[scb[i]]=i\n",
        "\n",
        "rs={}\n",
        "res=df['resolution']\n",
        "res=res.unique()\n",
        "res\n",
        "\n",
        "for i in range(len(res)):\n",
        "    \n",
        "    rs[res[i]]=i\n",
        "\n",
        "#wire provie and wire tech and cellular\n",
        "wpt={}\n",
        "wptb=df['wireless provider']\n",
        "wptb=wptb.unique()\n",
        "wptb\n",
        "\n",
        "for i in range(len(wptb)):\n",
        "    \n",
        "    wpt[wptb[i]]=i\n",
        "\n",
        "wtt={}\n",
        "wttb=df['wireless technology']\n",
        "wttb=wttb.unique()\n",
        "wttb\n",
        "\n",
        "for i in range(len(wttb)):\n",
        "    \n",
        "    wtt[wttb[i]]=i\n",
        "\n",
        "\n",
        "ctt={}\n",
        "cttb=df['cellular technology']\n",
        "cttb=cttb.unique()\n",
        "cttb\n",
        "\n",
        "for i in range(len(cttb)):\n",
        "    \n",
        "    ctt[cttb[i]]=i\n",
        "\n",
        "import copy\n",
        "\n",
        "df_cpy=copy.deepcopy(df)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 95,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "df_cpy['Brand'] = df_cpy['brand'].map(b)\n",
        "df_cpy['OS'] = df_cpy['os'].map(o)\n",
        "df_cpy['Model'] = df_cpy['model'].map(m)\n",
        "df_cpy['Cpu'] = df_cpy['cpu'].map(p)\n",
        "df_cpy['Color'] = df_cpy['color'].map(c)\n",
        "df_cpy['Storage'] = df_cpy['storage'].map(s)\n",
        "df_cpy['Website'] = df_cpy['website'].map(w)\n",
        "\n",
        "df_cpy['Screen Size'] = df_cpy['screen size'].map(scr)\n",
        "df_cpy['Resolution'] = df_cpy['resolution'].map(rs)\n",
        "df_cpy['Wireless Provider'] = df_cpy['wireless provider'].map(wpt)\n",
        "df_cpy['Wireless Technology'] = df_cpy['wireless technology'].map(wtt)\n",
        "df_cpy['Cellular Technology'] = df_cpy['cellular technology'].map(ctt)\n",
        "df_cpy\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 96,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "df_cpy['product_id'] = df_cpy[['OS', 'Model', 'Cpu','Brand','Storage','Color']].astype(str).agg('-'.join, axis=1)\n",
        "df_cpy"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 97,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "df_cpy['resolution_id'] = df_cpy[['Screen Size', 'Resolution']].astype(str).agg('-'.join, axis=1)\n",
        "\n",
        "\n",
        "df_cpy['tech_spec_id'] = df_cpy[['Wireless Provider', 'Wireless Technology','Cellular Technology']].astype(str).agg('-'.join, axis=1)\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 98,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "df['product_id']=df_cpy['product_id']\n",
        "df['resolution_id']=df_cpy['resolution_id']\n",
        "df['tech_spec_id']=df_cpy['tech_spec_id']\n",
        "df['website_id']=df_cpy['Website']\n",
        "df"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 99,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "df_cpy['website_id']=df_cpy['Website']\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 100,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "new_column_names = {\n",
        "    'Region': 'region',\n",
        "    'Brand': 'brand_id',\n",
        "    'OS': 'os_id',\n",
        "    'Model': 'model_id',\n",
        "    'Cpu': 'cpu_id',\n",
        "    'Color': 'color_id',\n",
        "    'Storage': 'storage_id',\n",
        "    'Website': 'website_id',\n",
        "    'Screen Size': 'screen size_id',\n",
        "    'Resolution': 'Resolution ID',\n",
        "    'Wireless Provider': 'wireless provider_id',\n",
        "    'Wireless Technology': 'wireless technology_id',\n",
        "    'Cellular Technology': 'cellular technology_id'\n",
        "    \n",
        "}\n",
        "\n",
        "df_cpy.rename(columns=new_column_names, inplace=True)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 101,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "df_cpy.columns"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 102,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "#df_cpy.drop(columns=['ProductID'], inplace=True)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 103,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "#df_cpy.drop(columns=['ProductID'], inplace=True)\n",
        "df_cpy.rename(columns={'Resolution ID':'resolution_id2f'}, inplace=True)\n",
        "\n",
        "df_cpy.columns"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 104,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "df_cpy.rename(columns={'Resolution ID':'resolution_id2f'}, inplace=True)\n",
        "df_cpy\n",
        "df_cpy.columns\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 105,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "df_cpy.drop(columns=['website_id'], inplace=True)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 106,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "df_cpy['website_id'] = df_cpy['website'].map(w)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 107,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "df=df_cpy"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 108,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "df['product_id'] = df['product_id'].astype(str)\n",
        "df['resolution_id'] = df['resolution_id'].astype(str)\n",
        "df['tech_spec_id'] = df['tech_spec_id'].astype(str)\n",
        "df['website_id'] = df['website_id'].astype(str)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 109,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "df.columns"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 110,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "fact=df[['product_id','resolution_id','tech_spec_id','website_id','cellular technology_id','wireless technology_id','wireless provider_id','brand_id', 'os_id', 'model_id', 'cpu_id', 'color_id',\n",
        "       'storage_id', 'screen size_id', 'resolution_id2f','price', 'price before promotion', 'rate']]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 111,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "product=df[['title', 'brand', 'os', 'ram', 'cpu', 'storage', 'model', 'color','camera', 'img','product_id']]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 112,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "reso=df[[ 'width resolution', 'height resolution','resolution','screen size','resolution_id']]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 113,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "webs=df[[ 'url', 'reviews','region','website','currancy','website_id' ]]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 114,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "tecsp=df[['wireless technology','wireless provider',\n",
        "       'cellular technology', 'sim count','tech_spec_id']]\n",
        "\n",
        "       "
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 115,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "webs"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 116,
      "metadata": {
        "jupyter": {
          "outputs_hidden": false,
          "source_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      },
      "outputs": [],
      "source": [
        "fact.to_parquet('abfss://######@######.dfs.core.windows.net/Fact_Table.parquet', index=False)\n",
        "product.to_parquet('abfss://######@######.dfs.core.windows.net/Product_Dimsion.parquet', index=False)\n",
        "reso.to_parquet('abfss://######@######.dfs.core.windows.net/Resolution_Dimsion.parquet', index=False)\n",
        "webs.to_parquet('abfss://######@######.dfs.core.windows.net/Website_Dimsion.parquet', index=False)\n",
        "tecsp.to_parquet('abfss://######@######.dfs.core.windows.net/Tech_special_Dimion.parquet', index=False)\n"
      ]
    }
  ],
  "metadata": {
    "description": null,
    "language_info": {
      "name": "python"
    },
    "save_output": true
  },
  "nbformat": 4,
  "nbformat_minor": 2
}
