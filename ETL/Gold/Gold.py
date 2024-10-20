{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {},
      "outputs": [
        {
          "data": {
            "application/vnd.livy.statement-meta+json": {
              "execution_finish_time": "2024-10-17T17:48:47.6846376Z",
              "execution_start_time": "2024-10-17T17:48:45.8378504Z",
              "livy_statement_state": "available",
              "normalized_state": "finished",
              "parent_msg_id": "44ef9aa2-783b-4039-9f47-e9a705930007",
              "queued_time": "2024-10-17T17:47:56.2629131Z",
              "session_id": "35",
              "session_start_time": "2024-10-17T17:47:56.3300796Z",
              "spark_jobs": null,
              "spark_pool": "tawfeeqpool",
              "state": "finished",
              "statement_id": 2,
              "statement_ids": [
                2
              ]
            },
            "text/plain": [
              "StatementMeta(tawfeeqpool, 35, 2, Finished, Available, Finished)"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "import pandas as pd\n",
        "productdim = pd.read_parquet(\"abfss://#####@######.dfs.core.windows.net/Product_Dimsion.parquet\")\n",
        "resdimm = pd.read_parquet(\"abfss://#####@######.dfs.core.windows.net/Resolution_Dimsion.parquet\")\n",
        "techdim = pd.read_parquet(\"abfss://#####@######.dfs.core.windows.net/Tech_special_Dimion.parquet\")\n",
        "webdim = pd.read_parquet(\"abfss://#####@######.dfs.core.windows.net/Website_Dimsion.parquet\")\n",
        "fact = pd.read_parquet(\"abfss://#####@######.dfs.core.windows.net/Fact_Table.parquet\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
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
      "outputs": [
        {
          "data": {
            "application/vnd.livy.statement-meta+json": {
              "execution_finish_time": "2024-10-17T17:48:48.0343274Z",
              "execution_start_time": "2024-10-17T17:48:47.8661766Z",
              "livy_statement_state": "available",
              "normalized_state": "finished",
              "parent_msg_id": "81de8d2f-1373-44b4-a25a-277a81205b2a",
              "queued_time": "2024-10-17T17:47:56.2638843Z",
              "session_id": "35",
              "session_start_time": null,
              "spark_jobs": null,
              "spark_pool": "tawfeeqpool",
              "state": "finished",
              "statement_id": 3,
              "statement_ids": [
                3
              ]
            },
            "text/plain": [
              "StatementMeta(tawfeeqpool, 35, 3, Finished, Available, Finished)"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "productdim[[\"ram\",\"storage\"]] = productdim[[\"ram\",\"storage\"]].fillna(0.0)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
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
      "outputs": [
        {
          "data": {
            "application/vnd.livy.statement-meta+json": {
              "execution_finish_time": "2024-10-17T17:48:48.3748356Z",
              "execution_start_time": "2024-10-17T17:48:48.2108163Z",
              "livy_statement_state": "available",
              "normalized_state": "finished",
              "parent_msg_id": "da6d5cae-d123-4c7d-af4b-a28db5a55e6a",
              "queued_time": "2024-10-17T17:47:56.2658414Z",
              "session_id": "35",
              "session_start_time": null,
              "spark_jobs": null,
              "spark_pool": "tawfeeqpool",
              "state": "finished",
              "statement_id": 4,
              "statement_ids": [
                4
              ]
            },
            "text/plain": [
              "StatementMeta(tawfeeqpool, 35, 4, Finished, Available, Finished)"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "fact[[\"price\",\"price before promotion\",\"rate\"]] =fact[[\"price\",\"price before promotion\",\"rate\"]].fillna(0.0)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
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
      "outputs": [
        {
          "data": {
            "application/vnd.livy.statement-meta+json": {
              "execution_finish_time": "2024-10-17T17:48:48.6830914Z",
              "execution_start_time": "2024-10-17T17:48:48.5188923Z",
              "livy_statement_state": "available",
              "normalized_state": "finished",
              "parent_msg_id": "12f96413-5c79-46fe-9535-503264f0fc40",
              "queued_time": "2024-10-17T17:47:56.2680383Z",
              "session_id": "35",
              "session_start_time": null,
              "spark_jobs": null,
              "spark_pool": "tawfeeqpool",
              "state": "finished",
              "statement_id": 5,
              "statement_ids": [
                5
              ]
            },
            "text/plain": [
              "StatementMeta(tawfeeqpool, 35, 5, Finished, Available, Finished)"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "resdimm[[\"width resolution\",\"height resolution\",\"screen size\",\"resolution\"]]=resdimm[[\"width resolution\",\"height resolution\",\"screen size\",\"resolution\"]].fillna(0.0)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
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
      "outputs": [
        {
          "data": {
            "application/vnd.livy.statement-meta+json": {
              "execution_finish_time": "2024-10-17T17:48:49.0171137Z",
              "execution_start_time": "2024-10-17T17:48:48.858215Z",
              "livy_statement_state": "available",
              "normalized_state": "finished",
              "parent_msg_id": "8e84e716-f2b3-49aa-ab32-fcb4ecacaba9",
              "queued_time": "2024-10-17T17:47:56.2693319Z",
              "session_id": "35",
              "session_start_time": null,
              "spark_jobs": null,
              "spark_pool": "tawfeeqpool",
              "state": "finished",
              "statement_id": 6,
              "statement_ids": [
                6
              ]
            },
            "text/plain": [
              "StatementMeta(tawfeeqpool, 35, 6, Finished, Available, Finished)"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>width resolution</th>\n",
              "      <th>height resolution</th>\n",
              "      <th>resolution</th>\n",
              "      <th>screen size</th>\n",
              "      <th>resolution_id</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>4.70</td>\n",
              "      <td>0-0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1920.0</td>\n",
              "      <td>1080.0</td>\n",
              "      <td>1920 x 1080</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1-1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1-0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1-0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>128.0</td>\n",
              "      <td>128.0</td>\n",
              "      <td>128x128</td>\n",
              "      <td>2.80</td>\n",
              "      <td>2-2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>517</th>\n",
              "      <td>1080.0</td>\n",
              "      <td>2340.0</td>\n",
              "      <td>1080 x 2340</td>\n",
              "      <td>6.56</td>\n",
              "      <td>26-4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>518</th>\n",
              "      <td>720.0</td>\n",
              "      <td>1612.0</td>\n",
              "      <td>720 x 1612</td>\n",
              "      <td>6.56</td>\n",
              "      <td>26-46</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>519</th>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>6.70</td>\n",
              "      <td>4-0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>520</th>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1-0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>521</th>\n",
              "      <td>1080.0</td>\n",
              "      <td>2400.0</td>\n",
              "      <td>1080 x 2400</td>\n",
              "      <td>6.67</td>\n",
              "      <td>9-5</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>522 rows × 5 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "     width resolution  height resolution   resolution  screen size  \\\n",
              "0                 0.0                0.0          0.0         4.70   \n",
              "1              1920.0             1080.0  1920 x 1080         0.00   \n",
              "2                 0.0                0.0          0.0         0.00   \n",
              "3                 0.0                0.0          0.0         0.00   \n",
              "4               128.0              128.0      128x128         2.80   \n",
              "..                ...                ...          ...          ...   \n",
              "517            1080.0             2340.0  1080 x 2340         6.56   \n",
              "518             720.0             1612.0   720 x 1612         6.56   \n",
              "519               0.0                0.0          0.0         6.70   \n",
              "520               0.0                0.0          0.0         0.00   \n",
              "521            1080.0             2400.0  1080 x 2400         6.67   \n",
              "\n",
              "    resolution_id  \n",
              "0             0-0  \n",
              "1             1-1  \n",
              "2             1-0  \n",
              "3             1-0  \n",
              "4             2-2  \n",
              "..            ...  \n",
              "517          26-4  \n",
              "518         26-46  \n",
              "519           4-0  \n",
              "520           1-0  \n",
              "521           9-5  \n",
              "\n",
              "[522 rows x 5 columns]"
            ]
          },
          "execution_count": 13,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "resdimm\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
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
      "outputs": [
        {
          "data": {
            "application/vnd.livy.statement-meta+json": {
              "execution_finish_time": "2024-10-17T17:48:49.314982Z",
              "execution_start_time": "2024-10-17T17:48:49.1505582Z",
              "livy_statement_state": "available",
              "normalized_state": "finished",
              "parent_msg_id": "5ae7b51e-4ed8-4b4a-abbe-63a62c316735",
              "queued_time": "2024-10-17T17:47:56.2717835Z",
              "session_id": "35",
              "session_start_time": null,
              "spark_jobs": null,
              "spark_pool": "tawfeeqpool",
              "state": "finished",
              "statement_id": 7,
              "statement_ids": [
                7
              ]
            },
            "text/plain": [
              "StatementMeta(tawfeeqpool, 35, 7, Finished, Available, Finished)"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>wireless technology</th>\n",
              "      <th>wireless provider</th>\n",
              "      <th>cellular technology</th>\n",
              "      <th>sim count</th>\n",
              "      <th>tech_spec_id</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>LTE</td>\n",
              "      <td>Unlocked for All Carriers</td>\n",
              "      <td>4G</td>\n",
              "      <td>None</td>\n",
              "      <td>0-0-0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>None</td>\n",
              "      <td>Unlocked for All Carriers</td>\n",
              "      <td>4G</td>\n",
              "      <td>None</td>\n",
              "      <td>0-1-0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>LTE</td>\n",
              "      <td>du</td>\n",
              "      <td>2G</td>\n",
              "      <td>None</td>\n",
              "      <td>1-0-1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>None</td>\n",
              "      <td>Unlocked for All Carriers</td>\n",
              "      <td>5G</td>\n",
              "      <td>Drievoudige simkaart</td>\n",
              "      <td>0-1-2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>None</td>\n",
              "      <td>Unlocked</td>\n",
              "      <td>4G</td>\n",
              "      <td>None</td>\n",
              "      <td>2-1-0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>517</th>\n",
              "      <td>None</td>\n",
              "      <td>Unlocked for All Carriers</td>\n",
              "      <td>4G</td>\n",
              "      <td>None</td>\n",
              "      <td>0-1-0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>518</th>\n",
              "      <td>None</td>\n",
              "      <td>etisalat</td>\n",
              "      <td>4G</td>\n",
              "      <td>None</td>\n",
              "      <td>23-1-0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>519</th>\n",
              "      <td>Wi-Fi</td>\n",
              "      <td>Unlocked for All Carriers</td>\n",
              "      <td>5G</td>\n",
              "      <td>None</td>\n",
              "      <td>0-3-2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>520</th>\n",
              "      <td>None</td>\n",
              "      <td>None</td>\n",
              "      <td>None</td>\n",
              "      <td>None</td>\n",
              "      <td>4-1-4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>521</th>\n",
              "      <td>None</td>\n",
              "      <td>Unlocked for All Carriers</td>\n",
              "      <td>5G</td>\n",
              "      <td>None</td>\n",
              "      <td>0-1-2</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>522 rows × 5 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "    wireless technology          wireless provider cellular technology  \\\n",
              "0                   LTE  Unlocked for All Carriers                  4G   \n",
              "1                  None  Unlocked for All Carriers                  4G   \n",
              "2                   LTE                         du                  2G   \n",
              "3                  None  Unlocked for All Carriers                  5G   \n",
              "4                  None                   Unlocked                  4G   \n",
              "..                  ...                        ...                 ...   \n",
              "517                None  Unlocked for All Carriers                  4G   \n",
              "518                None                   etisalat                  4G   \n",
              "519               Wi-Fi  Unlocked for All Carriers                  5G   \n",
              "520                None                       None                None   \n",
              "521                None  Unlocked for All Carriers                  5G   \n",
              "\n",
              "                sim count tech_spec_id  \n",
              "0                    None        0-0-0  \n",
              "1                    None        0-1-0  \n",
              "2                    None        1-0-1  \n",
              "3    Drievoudige simkaart        0-1-2  \n",
              "4                    None        2-1-0  \n",
              "..                    ...          ...  \n",
              "517                  None        0-1-0  \n",
              "518                  None       23-1-0  \n",
              "519                  None        0-3-2  \n",
              "520                  None        4-1-4  \n",
              "521                  None        0-1-2  \n",
              "\n",
              "[522 rows x 5 columns]"
            ]
          },
          "execution_count": 15,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "techdim"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
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
      "outputs": [
        {
          "data": {
            "application/vnd.livy.statement-meta+json": {
              "execution_finish_time": "2024-10-17T17:48:49.6082616Z",
              "execution_start_time": "2024-10-17T17:48:49.453146Z",
              "livy_statement_state": "available",
              "normalized_state": "finished",
              "parent_msg_id": "31adb25e-fbca-4442-9708-436ad05aaa02",
              "queued_time": "2024-10-17T17:47:56.2731388Z",
              "session_id": "35",
              "session_start_time": null,
              "spark_jobs": null,
              "spark_pool": "tawfeeqpool",
              "state": "finished",
              "statement_id": 8,
              "statement_ids": [
                8
              ]
            },
            "text/plain": [
              "StatementMeta(tawfeeqpool, 35, 8, Finished, Available, Finished)"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "data": {
            "text/plain": [
              "width resolution     float64\n",
              "height resolution    float64\n",
              "resolution            object\n",
              "screen size          float64\n",
              "resolution_id         object\n",
              "dtype: object"
            ]
          },
          "execution_count": 17,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "resdimm.dtypes\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
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
      "outputs": [
        {
          "data": {
            "application/vnd.livy.statement-meta+json": {
              "execution_finish_time": "2024-10-17T17:48:49.9331049Z",
              "execution_start_time": "2024-10-17T17:48:49.755981Z",
              "livy_statement_state": "available",
              "normalized_state": "finished",
              "parent_msg_id": "e2edfae3-7468-46d4-9398-200a19a8e62b",
              "queued_time": "2024-10-17T17:47:56.274859Z",
              "session_id": "35",
              "session_start_time": null,
              "spark_jobs": null,
              "spark_pool": "tawfeeqpool",
              "state": "finished",
              "statement_id": 9,
              "statement_ids": [
                9
              ]
            },
            "text/plain": [
              "StatementMeta(tawfeeqpool, 35, 9, Finished, Available, Finished)"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "data": {
            "text/plain": [
              "Index(['product_id', 'resolution_id', 'tech_spec_id', 'website_id',\n",
              "       'cellular technology_id', 'wireless technology_id',\n",
              "       'wireless provider_id', 'brand_id', 'os_id', 'model_id', 'cpu_id',\n",
              "       'color_id', 'storage_id', 'screen size_id', 'resolution_id2f', 'price',\n",
              "       'price before promotion', 'rate'],\n",
              "      dtype='object')"
            ]
          },
          "execution_count": 19,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "fact.columns"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
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
      "outputs": [
        {
          "data": {
            "application/vnd.livy.statement-meta+json": {
              "execution_finish_time": "2024-10-17T17:48:50.2254291Z",
              "execution_start_time": "2024-10-17T17:48:50.0646732Z",
              "livy_statement_state": "available",
              "normalized_state": "finished",
              "parent_msg_id": "aa4063b8-efde-4697-b627-9b77cf65d786",
              "queued_time": "2024-10-17T17:47:56.2759388Z",
              "session_id": "35",
              "session_start_time": null,
              "spark_jobs": null,
              "spark_pool": "tawfeeqpool",
              "state": "finished",
              "statement_id": 10,
              "statement_ids": [
                10
              ]
            },
            "text/plain": [
              "StatementMeta(tawfeeqpool, 35, 10, Finished, Available, Finished)"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "data": {
            "text/plain": [
              "product_id                 object\n",
              "resolution_id              object\n",
              "tech_spec_id               object\n",
              "website_id                 object\n",
              "cellular technology_id     object\n",
              "wireless technology_id     object\n",
              "wireless provider_id       object\n",
              "brand_id                   object\n",
              "os_id                      object\n",
              "model_id                   object\n",
              "cpu_id                     object\n",
              "color_id                   object\n",
              "storage_id                 object\n",
              "screen size_id             object\n",
              "resolution_id2f            object\n",
              "price                     float64\n",
              "price before promotion    float64\n",
              "rate                      float64\n",
              "dtype: object"
            ]
          },
          "execution_count": 21,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "fact.dtypes\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
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
      "outputs": [
        {
          "data": {
            "application/vnd.livy.statement-meta+json": {
              "execution_finish_time": "2024-10-17T17:48:50.5473673Z",
              "execution_start_time": "2024-10-17T17:48:50.3884913Z",
              "livy_statement_state": "available",
              "normalized_state": "finished",
              "parent_msg_id": "01278e0e-ac4e-4435-94cb-50f6e1b611f8",
              "queued_time": "2024-10-17T17:47:56.2777105Z",
              "session_id": "35",
              "session_start_time": null,
              "spark_jobs": null,
              "spark_pool": "tawfeeqpool",
              "state": "finished",
              "statement_id": 11,
              "statement_ids": [
                11
              ]
            },
            "text/plain": [
              "StatementMeta(tawfeeqpool, 35, 11, Finished, Available, Finished)"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "fact = fact.astype({'cellular technology_id': 'str', 'wireless technology_id': 'str','wireless provider_id':'str','brand_id':'str','os_id':'str','model_id':'str','cpu_id':'str','color_id':'str','storage_id':'str','screen size_id':'str','resolution_id2f':'str'})\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
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
      "outputs": [
        {
          "data": {
            "application/vnd.livy.statement-meta+json": {
              "execution_finish_time": "2024-10-17T17:48:50.8483659Z",
              "execution_start_time": "2024-10-17T17:48:50.6896973Z",
              "livy_statement_state": "available",
              "normalized_state": "finished",
              "parent_msg_id": "96426053-cb29-4234-bd68-60697ab75bec",
              "queued_time": "2024-10-17T17:47:56.2806654Z",
              "session_id": "35",
              "session_start_time": null,
              "spark_jobs": null,
              "spark_pool": "tawfeeqpool",
              "state": "finished",
              "statement_id": 12,
              "statement_ids": [
                12
              ]
            },
            "text/plain": [
              "StatementMeta(tawfeeqpool, 35, 12, Finished, Available, Finished)"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "data": {
            "text/plain": [
              "url           object\n",
              "reviews       object\n",
              "region        object\n",
              "website       object\n",
              "currancy      object\n",
              "website_id    object\n",
              "dtype: object"
            ]
          },
          "execution_count": 25,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "webdim.dtypes"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
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
      "outputs": [
        {
          "data": {
            "application/vnd.livy.statement-meta+json": {
              "execution_finish_time": "2024-10-17T17:48:51.1754277Z",
              "execution_start_time": "2024-10-17T17:48:51.0079175Z",
              "livy_statement_state": "available",
              "normalized_state": "finished",
              "parent_msg_id": "b37f671c-f5b3-4b13-a7af-e588b62b528e",
              "queued_time": "2024-10-17T17:47:56.2820798Z",
              "session_id": "35",
              "session_start_time": null,
              "spark_jobs": null,
              "spark_pool": "tawfeeqpool",
              "state": "finished",
              "statement_id": 13,
              "statement_ids": [
                13
              ]
            },
            "text/plain": [
              "StatementMeta(tawfeeqpool, 35, 13, Finished, Available, Finished)"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "data": {
            "text/plain": [
              "wireless technology    object\n",
              "wireless provider      object\n",
              "cellular technology    object\n",
              "sim count              object\n",
              "tech_spec_id           object\n",
              "dtype: object"
            ]
          },
          "execution_count": 27,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "techdim.dtypes"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
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
      "outputs": [
        {
          "data": {
            "application/vnd.livy.statement-meta+json": {
              "execution_finish_time": "2024-10-17T17:48:51.4722939Z",
              "execution_start_time": "2024-10-17T17:48:51.3089887Z",
              "livy_statement_state": "available",
              "normalized_state": "finished",
              "parent_msg_id": "17099343-f2e1-411f-a62a-03f250c221d4",
              "queued_time": "2024-10-17T17:47:56.2836795Z",
              "session_id": "35",
              "session_start_time": null,
              "spark_jobs": null,
              "spark_pool": "tawfeeqpool",
              "state": "finished",
              "statement_id": 14,
              "statement_ids": [
                14
              ]
            },
            "text/plain": [
              "StatementMeta(tawfeeqpool, 35, 14, Finished, Available, Finished)"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "data": {
            "text/plain": [
              "width resolution     float64\n",
              "height resolution    float64\n",
              "resolution            object\n",
              "screen size          float64\n",
              "resolution_id         object\n",
              "dtype: object"
            ]
          },
          "execution_count": 29,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "resdimm.dtypes"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
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
      "outputs": [
        {
          "data": {
            "application/vnd.livy.statement-meta+json": {
              "execution_finish_time": "2024-10-17T17:48:51.7792968Z",
              "execution_start_time": "2024-10-17T17:48:51.6146867Z",
              "livy_statement_state": "available",
              "normalized_state": "finished",
              "parent_msg_id": "5926fa16-decd-4cf2-b110-491522e45591",
              "queued_time": "2024-10-17T17:47:56.2853211Z",
              "session_id": "35",
              "session_start_time": null,
              "spark_jobs": null,
              "spark_pool": "tawfeeqpool",
              "state": "finished",
              "statement_id": 15,
              "statement_ids": [
                15
              ]
            },
            "text/plain": [
              "StatementMeta(tawfeeqpool, 35, 15, Finished, Available, Finished)"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "data": {
            "text/plain": [
              "title          object\n",
              "brand          object\n",
              "os             object\n",
              "ram           float64\n",
              "cpu            object\n",
              "storage       float64\n",
              "model          object\n",
              "color          object\n",
              "camera         object\n",
              "img            object\n",
              "product_id     object\n",
              "dtype: object"
            ]
          },
          "execution_count": 31,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "productdim.dtypes"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
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
      "outputs": [
        {
          "data": {
            "application/vnd.livy.statement-meta+json": {
              "execution_finish_time": "2024-10-17T17:48:52.0600512Z",
              "execution_start_time": "2024-10-17T17:48:51.9064373Z",
              "livy_statement_state": "available",
              "normalized_state": "finished",
              "parent_msg_id": "80324a6c-1f29-4ec2-8b30-57ec2a20d8b2",
              "queued_time": "2024-10-17T17:47:56.2874365Z",
              "session_id": "35",
              "session_start_time": null,
              "spark_jobs": null,
              "spark_pool": "tawfeeqpool",
              "state": "finished",
              "statement_id": 16,
              "statement_ids": [
                16
              ]
            },
            "text/plain": [
              "StatementMeta(tawfeeqpool, 35, 16, Finished, Available, Finished)"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "data": {
            "text/plain": [
              "product_id                 object\n",
              "resolution_id              object\n",
              "tech_spec_id               object\n",
              "website_id                 object\n",
              "cellular technology_id     object\n",
              "wireless technology_id     object\n",
              "wireless provider_id       object\n",
              "brand_id                   object\n",
              "os_id                      object\n",
              "model_id                   object\n",
              "cpu_id                     object\n",
              "color_id                   object\n",
              "storage_id                 object\n",
              "screen size_id             object\n",
              "resolution_id2f            object\n",
              "price                     float64\n",
              "price before promotion    float64\n",
              "rate                      float64\n",
              "dtype: object"
            ]
          },
          "execution_count": 33,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "fact.dtypes"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
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
      "outputs": [
        {
          "data": {
            "application/vnd.livy.statement-meta+json": {
              "execution_finish_time": "2024-10-17T17:48:52.4373399Z",
              "execution_start_time": "2024-10-17T17:48:52.2682302Z",
              "livy_statement_state": "available",
              "normalized_state": "finished",
              "parent_msg_id": "cb844c9e-b644-4c16-8a14-b324a6119ad1",
              "queued_time": "2024-10-17T17:47:56.2895055Z",
              "session_id": "35",
              "session_start_time": null,
              "spark_jobs": null,
              "spark_pool": "tawfeeqpool",
              "state": "finished",
              "statement_id": 17,
              "statement_ids": [
                17
              ]
            },
            "text/plain": [
              "StatementMeta(tawfeeqpool, 35, 17, Finished, Available, Finished)"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "data": {
            "text/plain": [
              "width resolution     float64\n",
              "height resolution    float64\n",
              "resolution            object\n",
              "screen size          float64\n",
              "resolution_id         object\n",
              "dtype: object"
            ]
          },
          "execution_count": 35,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "resdimm.dtypes"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 17,
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
      "outputs": [
        {
          "data": {
            "application/vnd.livy.statement-meta+json": {
              "execution_finish_time": "2024-10-17T17:48:52.7346772Z",
              "execution_start_time": "2024-10-17T17:48:52.5744669Z",
              "livy_statement_state": "available",
              "normalized_state": "finished",
              "parent_msg_id": "037da46b-f304-4546-b332-4fe470211ad2",
              "queued_time": "2024-10-17T17:47:57.499679Z",
              "session_id": "35",
              "session_start_time": null,
              "spark_jobs": null,
              "spark_pool": "tawfeeqpool",
              "state": "finished",
              "statement_id": 18,
              "statement_ids": [
                18
              ]
            },
            "text/plain": [
              "StatementMeta(tawfeeqpool, 35, 18, Finished, Available, Finished)"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>width resolution</th>\n",
              "      <th>height resolution</th>\n",
              "      <th>resolution</th>\n",
              "      <th>screen size</th>\n",
              "      <th>resolution_id</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>4.70</td>\n",
              "      <td>0-0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1920.0</td>\n",
              "      <td>1080.0</td>\n",
              "      <td>1920 x 1080</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1-1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1-0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1-0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>128.0</td>\n",
              "      <td>128.0</td>\n",
              "      <td>128x128</td>\n",
              "      <td>2.80</td>\n",
              "      <td>2-2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>517</th>\n",
              "      <td>1080.0</td>\n",
              "      <td>2340.0</td>\n",
              "      <td>1080 x 2340</td>\n",
              "      <td>6.56</td>\n",
              "      <td>26-4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>518</th>\n",
              "      <td>720.0</td>\n",
              "      <td>1612.0</td>\n",
              "      <td>720 x 1612</td>\n",
              "      <td>6.56</td>\n",
              "      <td>26-46</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>519</th>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>6.70</td>\n",
              "      <td>4-0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>520</th>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1-0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>521</th>\n",
              "      <td>1080.0</td>\n",
              "      <td>2400.0</td>\n",
              "      <td>1080 x 2400</td>\n",
              "      <td>6.67</td>\n",
              "      <td>9-5</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>522 rows × 5 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "     width resolution  height resolution   resolution  screen size  \\\n",
              "0                 0.0                0.0          0.0         4.70   \n",
              "1              1920.0             1080.0  1920 x 1080         0.00   \n",
              "2                 0.0                0.0          0.0         0.00   \n",
              "3                 0.0                0.0          0.0         0.00   \n",
              "4               128.0              128.0      128x128         2.80   \n",
              "..                ...                ...          ...          ...   \n",
              "517            1080.0             2340.0  1080 x 2340         6.56   \n",
              "518             720.0             1612.0   720 x 1612         6.56   \n",
              "519               0.0                0.0          0.0         6.70   \n",
              "520               0.0                0.0          0.0         0.00   \n",
              "521            1080.0             2400.0  1080 x 2400         6.67   \n",
              "\n",
              "    resolution_id  \n",
              "0             0-0  \n",
              "1             1-1  \n",
              "2             1-0  \n",
              "3             1-0  \n",
              "4             2-2  \n",
              "..            ...  \n",
              "517          26-4  \n",
              "518         26-46  \n",
              "519           4-0  \n",
              "520           1-0  \n",
              "521           9-5  \n",
              "\n",
              "[522 rows x 5 columns]"
            ]
          },
          "execution_count": 37,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "resdimm"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 18,
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
      "outputs": [
        {
          "data": {
            "application/vnd.livy.statement-meta+json": {
              "execution_finish_time": "2024-10-17T17:48:53.0274632Z",
              "execution_start_time": "2024-10-17T17:48:52.8684724Z",
              "livy_statement_state": "available",
              "normalized_state": "finished",
              "parent_msg_id": "232b3117-5554-4803-9530-9a01ef549269",
              "queued_time": "2024-10-17T17:47:59.8224499Z",
              "session_id": "35",
              "session_start_time": null,
              "spark_jobs": null,
              "spark_pool": "tawfeeqpool",
              "state": "finished",
              "statement_id": 19,
              "statement_ids": [
                19
              ]
            },
            "text/plain": [
              "StatementMeta(tawfeeqpool, 35, 19, Finished, Available, Finished)"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "data": {
            "text/plain": [
              "Index(['product_id', 'resolution_id', 'tech_spec_id', 'website_id',\n",
              "       'cellular_technology_id', 'wireless_technology_id',\n",
              "       'wireless_provider_id', 'brand_id', 'os_id', 'model_id', 'cpu_id',\n",
              "       'color_id', 'storage_id', 'screen_size_id', 'resolution_id2f', 'price',\n",
              "       'price_before_promotion', 'rate'],\n",
              "      dtype='object')"
            ]
          },
          "execution_count": 39,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "fact.columns = fact.columns.str.replace(' ', '_')\n",
        "fact.columns\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 19,
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
      "outputs": [
        {
          "data": {
            "application/vnd.livy.statement-meta+json": {
              "execution_finish_time": "2024-10-17T17:48:53.3304904Z",
              "execution_start_time": "2024-10-17T17:48:53.1638692Z",
              "livy_statement_state": "available",
              "normalized_state": "finished",
              "parent_msg_id": "25df892e-ff40-4191-9fe2-512b7f2d9d99",
              "queued_time": "2024-10-17T17:48:00.2071103Z",
              "session_id": "35",
              "session_start_time": null,
              "spark_jobs": null,
              "spark_pool": "tawfeeqpool",
              "state": "finished",
              "statement_id": 20,
              "statement_ids": [
                20
              ]
            },
            "text/plain": [
              "StatementMeta(tawfeeqpool, 35, 20, Finished, Available, Finished)"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "resdimm.columns = resdimm.columns.str.replace(' ', '_')\n",
        "techdim.columns = techdim.columns.str.replace(' ', '_')\n",
        "webdim.columns = webdim.columns.str.replace(' ', '_')\n",
        "productdim.columns = productdim.columns.str.replace(' ', '_')\n",
        "productdim.columns\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 20,
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
      "outputs": [
        {
          "data": {
            "application/vnd.livy.statement-meta+json": {
              "execution_finish_time": "2024-10-17T17:48:53.9998222Z",
              "execution_start_time": "2024-10-17T17:48:53.4690166Z",
              "livy_statement_state": "available",
              "normalized_state": "finished",
              "parent_msg_id": "b2a1305e-a8ed-4aec-ac6e-2348a9207e4b",
              "queued_time": "2024-10-17T17:48:00.5547622Z",
              "session_id": "35",
              "session_start_time": null,
              "spark_jobs": null,
              "spark_pool": "tawfeeqpool",
              "state": "finished",
              "statement_id": 21,
              "statement_ids": [
                21
              ]
            },
            "text/plain": [
              "StatementMeta(tawfeeqpool, 35, 21, Finished, Available, Finished)"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "\n",
        "productdim.to_parquet(\"###@#####.core.windows.net/Product_Dimsion.parquet\",index=False)\n",
        "#resdimm.to_parquet(\"###@#####.core.windows.net/Resolution_Dimsion.parquet\",index=False)\n",
        "techdim.to_parquet(\"###@#####.core.windows.net/Tech_special_Dimion.parquet\",index=False)\n",
        "webdim.to_parquet(\"###@#####.core.windows.net/Website_Dimsion.parquet\",index=False)\n",
        "fact.to_parquet(\"###@#####.core.windows.net/Fact_Table.parquet\",index=False)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 21,
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
      "outputs": [
        {
          "data": {
            "application/vnd.livy.statement-meta+json": {
              "execution_finish_time": "2024-10-17T17:48:54.3117125Z",
              "execution_start_time": "2024-10-17T17:48:54.1441899Z",
              "livy_statement_state": "available",
              "normalized_state": "finished",
              "parent_msg_id": "ef6ce5de-5b02-4ab8-8acf-7b562d97c2ef",
              "queued_time": "2024-10-17T17:48:00.9410067Z",
              "session_id": "35",
              "session_start_time": null,
              "spark_jobs": null,
              "spark_pool": "tawfeeqpool",
              "state": "finished",
              "statement_id": 22,
              "statement_ids": [
                22
              ]
            },
            "text/plain": [
              "StatementMeta(tawfeeqpool, 35, 22, Finished, Available, Finished)"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Convert any specific columns that may be problematic\n",
        "resdimm['resolution'] = resdimm['resolution'].astype(str)  # if necessary\n",
        "\n",
        "#engine='pyarrow'\n",
        "resdimm.to_parquet(\"abfss://###@#####.dfs.core.windows.net/Resolution_Dimsion.parquet\",index=False)\n"
      ]
    }
  ],
  "metadata": {
    "description": null,
    "kernelspec": {
      "display_name": "python",
      "name": "synapse_pyspark"
    },
    "language_info": {
      "name": "python"
    },
    "save_output": true,
    "synapse_widget": {
      "state": {},
      "version": "0.1"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 2
}
