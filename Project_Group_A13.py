{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/nanda1296/Predictive-Analytics-for-Real-Estate/blob/Different_models/Project_Group_A13.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "id": "-yTS4jABSH5V",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "3d8695b2-b2b7-4fa7-948f-872ec637fd8b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "lgGokGmK8isi"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "\n",
        "from sklearn.impute import KNNImputer"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_excel('/content/drive/MyDrive/Colab Notebooks/Dataset/Spring 2023 - AISC - Nest Analytics_Toronto_housing_data_Cleaned.xlsx')\n",
        "df = df.drop(df.columns[0],axis=1)\n",
        "df.head()"
      ],
      "metadata": {
        "id": "WQdGNqbb8szQ",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 507
        },
        "outputId": "04ad0b38-a13d-4b23-9912-0002add2a343"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "            Land Use  Property Address Suite/ RESIDENTIAL CONDO#  Sale Date  \\\n",
              "0  RESIDENTIAL CONDO    1208 3RD AVE S                         8 2013-01-24   \n",
              "1      SINGLE FAMILY   1802 STEWART PL                       NaN 2013-01-11   \n",
              "2      SINGLE FAMILY  2761 ROSEDALE PL                       NaN 2013-01-18   \n",
              "3      SINGLE FAMILY  224 PEACHTREE ST                       NaN 2013-01-18   \n",
              "4      SINGLE FAMILY      316 LUTIE ST                       NaN 2013-01-23   \n",
              "\n",
              "   Sale Price   Legal Reference Sold As Vacant  \\\n",
              "0      132000  20130128-0008725             No   \n",
              "1      191500  20130118-0006337             No   \n",
              "2      202000  20130124-0008033             No   \n",
              "3       32000  20130128-0008863             No   \n",
              "4      102000  20130131-0009929             No   \n",
              "\n",
              "  Multiple Parcels Involved in Sale                     Owner Name  \\\n",
              "0                                No                            NaN   \n",
              "1                                No              STINSON, LAURA M.   \n",
              "2                                No                NUNES, JARED R.   \n",
              "3                                No                WHITFORD, KAREN   \n",
              "4                                No  HENDERSON, JAMES P. & LYNN P.   \n",
              "\n",
              "            Address  ...  Building Value  Total Value Finished Area  \\\n",
              "0               NaN  ...             NaN          NaN           NaN   \n",
              "1   1802 STEWART PL  ...        134400.0     168300.0    1149.00000   \n",
              "2  2761 ROSEDALE PL  ...        157800.0     191800.0    2090.82495   \n",
              "3  224 PEACHTREE ST  ...        243700.0     268700.0    2145.60001   \n",
              "4      316 LUTIE ST  ...        138100.0     164800.0    1969.00000   \n",
              "\n",
              "   Foundation Type  Year Built  Exterior Wall  Grade  Bedrooms Full Bath  \\\n",
              "0              NaN         NaN            NaN    NaN       NaN       NaN   \n",
              "1          PT BSMT      1941.0          BRICK   C          2.0       1.0   \n",
              "2             SLAB      2000.0    BRICK/FRAME   C          3.0       2.0   \n",
              "3        FULL BSMT      1948.0    BRICK/FRAME   B          4.0       2.0   \n",
              "4            CRAWL      1910.0          FRAME   C          2.0       1.0   \n",
              "\n",
              "   Half Bath  \n",
              "0        NaN  \n",
              "1        0.0  \n",
              "2        1.0  \n",
              "3        0.0  \n",
              "4        0.0  \n",
              "\n",
              "[5 rows x 25 columns]"
            ],
            "text/html": [
              "\n",
              "\n",
              "  <div id=\"df-aaf843dc-0c8c-4bd5-a279-16a24b8131c1\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>Land Use</th>\n",
              "      <th>Property Address</th>\n",
              "      <th>Suite/ RESIDENTIAL CONDO#</th>\n",
              "      <th>Sale Date</th>\n",
              "      <th>Sale Price</th>\n",
              "      <th>Legal Reference</th>\n",
              "      <th>Sold As Vacant</th>\n",
              "      <th>Multiple Parcels Involved in Sale</th>\n",
              "      <th>Owner Name</th>\n",
              "      <th>Address</th>\n",
              "      <th>...</th>\n",
              "      <th>Building Value</th>\n",
              "      <th>Total Value</th>\n",
              "      <th>Finished Area</th>\n",
              "      <th>Foundation Type</th>\n",
              "      <th>Year Built</th>\n",
              "      <th>Exterior Wall</th>\n",
              "      <th>Grade</th>\n",
              "      <th>Bedrooms</th>\n",
              "      <th>Full Bath</th>\n",
              "      <th>Half Bath</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>RESIDENTIAL CONDO</td>\n",
              "      <td>1208 3RD AVE S</td>\n",
              "      <td>8</td>\n",
              "      <td>2013-01-24</td>\n",
              "      <td>132000</td>\n",
              "      <td>20130128-0008725</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>SINGLE FAMILY</td>\n",
              "      <td>1802 STEWART PL</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2013-01-11</td>\n",
              "      <td>191500</td>\n",
              "      <td>20130118-0006337</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>STINSON, LAURA M.</td>\n",
              "      <td>1802 STEWART PL</td>\n",
              "      <td>...</td>\n",
              "      <td>134400.0</td>\n",
              "      <td>168300.0</td>\n",
              "      <td>1149.00000</td>\n",
              "      <td>PT BSMT</td>\n",
              "      <td>1941.0</td>\n",
              "      <td>BRICK</td>\n",
              "      <td>C</td>\n",
              "      <td>2.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>SINGLE FAMILY</td>\n",
              "      <td>2761 ROSEDALE PL</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2013-01-18</td>\n",
              "      <td>202000</td>\n",
              "      <td>20130124-0008033</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>NUNES, JARED R.</td>\n",
              "      <td>2761 ROSEDALE PL</td>\n",
              "      <td>...</td>\n",
              "      <td>157800.0</td>\n",
              "      <td>191800.0</td>\n",
              "      <td>2090.82495</td>\n",
              "      <td>SLAB</td>\n",
              "      <td>2000.0</td>\n",
              "      <td>BRICK/FRAME</td>\n",
              "      <td>C</td>\n",
              "      <td>3.0</td>\n",
              "      <td>2.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>SINGLE FAMILY</td>\n",
              "      <td>224 PEACHTREE ST</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2013-01-18</td>\n",
              "      <td>32000</td>\n",
              "      <td>20130128-0008863</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>WHITFORD, KAREN</td>\n",
              "      <td>224 PEACHTREE ST</td>\n",
              "      <td>...</td>\n",
              "      <td>243700.0</td>\n",
              "      <td>268700.0</td>\n",
              "      <td>2145.60001</td>\n",
              "      <td>FULL BSMT</td>\n",
              "      <td>1948.0</td>\n",
              "      <td>BRICK/FRAME</td>\n",
              "      <td>B</td>\n",
              "      <td>4.0</td>\n",
              "      <td>2.0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>SINGLE FAMILY</td>\n",
              "      <td>316 LUTIE ST</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2013-01-23</td>\n",
              "      <td>102000</td>\n",
              "      <td>20130131-0009929</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>HENDERSON, JAMES P. &amp; LYNN P.</td>\n",
              "      <td>316 LUTIE ST</td>\n",
              "      <td>...</td>\n",
              "      <td>138100.0</td>\n",
              "      <td>164800.0</td>\n",
              "      <td>1969.00000</td>\n",
              "      <td>CRAWL</td>\n",
              "      <td>1910.0</td>\n",
              "      <td>FRAME</td>\n",
              "      <td>C</td>\n",
              "      <td>2.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>5 rows × 25 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-aaf843dc-0c8c-4bd5-a279-16a24b8131c1')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "\n",
              "\n",
              "\n",
              "    <div id=\"df-d90af667-a3d2-4ec1-ac56-135b5c726a26\">\n",
              "      <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-d90af667-a3d2-4ec1-ac56-135b5c726a26')\"\n",
              "              title=\"Suggest charts.\"\n",
              "              style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "      </button>\n",
              "    </div>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "    background-color: #E8F0FE;\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: #1967D2;\n",
              "    height: 32px;\n",
              "    padding: 0 0 0 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: #E2EBFA;\n",
              "    box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: #174EA6;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "    background-color: #3B4455;\n",
              "    fill: #D2E3FC;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart:hover {\n",
              "    background-color: #434B5C;\n",
              "    box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "    filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "    fill: #FFFFFF;\n",
              "  }\n",
              "</style>\n",
              "\n",
              "    <script>\n",
              "      async function quickchart(key) {\n",
              "        const containerElement = document.querySelector('#' + key);\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      }\n",
              "    </script>\n",
              "\n",
              "      <script>\n",
              "\n",
              "function displayQuickchartButton(domScope) {\n",
              "  let quickchartButtonEl =\n",
              "    domScope.querySelector('#df-d90af667-a3d2-4ec1-ac56-135b5c726a26 button.colab-df-quickchart');\n",
              "  quickchartButtonEl.style.display =\n",
              "    google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "}\n",
              "\n",
              "        displayQuickchartButton(document);\n",
              "      </script>\n",
              "      <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-aaf843dc-0c8c-4bd5-a279-16a24b8131c1 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-aaf843dc-0c8c-4bd5-a279-16a24b8131c1');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_0Sg1AZ_khAi",
        "outputId": "9d3753d0-6775-43d5-95a0-f8f177ed1423"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(56636, 25)"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#checking the data types of all the features\n",
        "df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_hePhY-3Lhek",
        "outputId": "bb039a78-8218-4ff8-eb30-4d0ce3d3abb9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 56636 entries, 0 to 56635\n",
            "Data columns (total 25 columns):\n",
            " #   Column                                 Non-Null Count  Dtype         \n",
            "---  ------                                 --------------  -----         \n",
            " 0   Land Use                               56636 non-null  object        \n",
            " 1   Property Address                       56477 non-null  object        \n",
            " 2   Suite/ RESIDENTIAL CONDO#              6109 non-null   object        \n",
            " 3   Sale Date                              56636 non-null  datetime64[ns]\n",
            " 4   Sale Price                             56636 non-null  int64         \n",
            " 5   Legal Reference                        56636 non-null  object        \n",
            " 6   Sold As Vacant                         56636 non-null  object        \n",
            " 7   Multiple Parcels Involved in Sale      56636 non-null  object        \n",
            " 8   Owner Name                             25261 non-null  object        \n",
            " 9   Address                                26017 non-null  object        \n",
            " 10  Is (Property Address = Owner Address)  56636 non-null  bool          \n",
            " 11  Acreage                                26017 non-null  float64       \n",
            " 12  Tax District                           26017 non-null  object        \n",
            " 13  Neighborhood                           26017 non-null  float64       \n",
            " 14  Land Value                             26017 non-null  float64       \n",
            " 15  Building Value                         26017 non-null  float64       \n",
            " 16  Total Value                            26017 non-null  float64       \n",
            " 17  Finished Area                          24166 non-null  float64       \n",
            " 18  Foundation Type                        24164 non-null  object        \n",
            " 19  Year Built                             24165 non-null  float64       \n",
            " 20  Exterior Wall                          24165 non-null  object        \n",
            " 21  Grade                                  24165 non-null  object        \n",
            " 22  Bedrooms                               24159 non-null  float64       \n",
            " 23  Full Bath                              24277 non-null  float64       \n",
            " 24  Half Bath                              24146 non-null  float64       \n",
            "dtypes: bool(1), datetime64[ns](1), float64(10), int64(1), object(12)\n",
            "memory usage: 10.4+ MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Checking for null values of each feature\n",
        "df.isnull().sum().sort_values(ascending=False)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "57fcMNFRMSW_",
        "outputId": "5ea87eaf-ca6f-468e-b002-04d040f99845"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Suite/ RESIDENTIAL CONDO#                50527\n",
              "Half Bath                                32490\n",
              "Bedrooms                                 32477\n",
              "Foundation Type                          32472\n",
              "Grade                                    32471\n",
              "Exterior Wall                            32471\n",
              "Year Built                               32471\n",
              "Finished Area                            32470\n",
              "Full Bath                                32359\n",
              "Owner Name                               31375\n",
              "Land Value                               30619\n",
              "Total Value                              30619\n",
              "Building Value                           30619\n",
              "Tax District                             30619\n",
              "Neighborhood                             30619\n",
              "Acreage                                  30619\n",
              "Address                                  30619\n",
              "Property Address                           159\n",
              "Is (Property Address = Owner Address)        0\n",
              "Multiple Parcels Involved in Sale            0\n",
              "Sold As Vacant                               0\n",
              "Legal Reference                              0\n",
              "Sale Price                                   0\n",
              "Sale Date                                    0\n",
              "Land Use                                     0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Checking for unique rows in each feature\n",
        "df.nunique().sort_values(ascending=False)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bidoEPTJesvs",
        "outputId": "9ae3fbf5-5564-42fe-a7a1-12037f5e921c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Legal Reference                          52898\n",
              "Property Address                         43179\n",
              "Address                                  22327\n",
              "Owner Name                               19713\n",
              "Sale Price                                8085\n",
              "Finished Area                             6117\n",
              "Total Value                               5848\n",
              "Building Value                            4406\n",
              "Suite/ RESIDENTIAL CONDO#                 1475\n",
              "Land Value                                1122\n",
              "Sale Date                                 1117\n",
              "Acreage                                    519\n",
              "Neighborhood                               203\n",
              "Year Built                                 126\n",
              "Land Use                                    35\n",
              "Grade                                       20\n",
              "Bedrooms                                    12\n",
              "Full Bath                                   11\n",
              "Exterior Wall                               10\n",
              "Tax District                                 7\n",
              "Foundation Type                              6\n",
              "Half Bath                                    4\n",
              "Is (Property Address = Owner Address)        2\n",
              "Multiple Parcels Involved in Sale            2\n",
              "Sold As Vacant                               2\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.describe()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "id": "2fDHIIfRfTE1",
        "outputId": "b541bc90-3ce5-4322-e488-cae3c8e6ca7c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "         Sale Price       Acreage  Neighborhood    Land Value  Building Value  \\\n",
              "count  5.663600e+04  26017.000000  26017.000000  2.601700e+04    2.601700e+04   \n",
              "mean   3.272111e+05      0.498903   4356.215782  6.907267e+04    1.608025e+05   \n",
              "std    9.287425e+05      1.570396   2170.348270  1.060405e+05    2.068041e+05   \n",
              "min    5.000000e+01      0.010000    107.000000  1.000000e+02    0.000000e+00   \n",
              "25%    1.350000e+05      0.180000   3126.000000  2.100000e+04    7.590000e+04   \n",
              "50%    2.054500e+05      0.270000   3929.000000  2.880000e+04    1.114000e+05   \n",
              "75%    3.290000e+05      0.450000   6228.000000  6.000000e+04    1.807000e+05   \n",
              "max    5.427806e+07    160.060000   9530.000000  2.772000e+06    1.297180e+07   \n",
              "\n",
              "        Total Value  Finished Area    Year Built      Bedrooms     Full Bath  \\\n",
              "count  2.601700e+04   24166.000000  24165.000000  24159.000000  24277.000000   \n",
              "mean   2.323971e+05    1926.954345   1963.749224      3.090029      1.886106   \n",
              "std    2.810703e+05    1687.017313     26.546141      0.852942      0.961572   \n",
              "min    1.000000e+02       0.000000   1799.000000      0.000000      0.000000   \n",
              "25%    1.028000e+05    1239.000000   1948.000000      3.000000      1.000000   \n",
              "50%    1.485000e+05    1632.000000   1960.000000      3.000000      2.000000   \n",
              "75%    2.685000e+05    2212.000000   1983.000000      3.000000      2.000000   \n",
              "max    1.394040e+07  197988.000000   2017.000000     11.000000     10.000000   \n",
              "\n",
              "          Half Bath  \n",
              "count  24146.000000  \n",
              "mean       0.283981  \n",
              "std        0.487905  \n",
              "min        0.000000  \n",
              "25%        0.000000  \n",
              "50%        0.000000  \n",
              "75%        1.000000  \n",
              "max        3.000000  "
            ],
            "text/html": [
              "\n",
              "\n",
              "  <div id=\"df-6a20c1b8-7195-4dc4-93a0-c8b61c9464fe\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>Sale Price</th>\n",
              "      <th>Acreage</th>\n",
              "      <th>Neighborhood</th>\n",
              "      <th>Land Value</th>\n",
              "      <th>Building Value</th>\n",
              "      <th>Total Value</th>\n",
              "      <th>Finished Area</th>\n",
              "      <th>Year Built</th>\n",
              "      <th>Bedrooms</th>\n",
              "      <th>Full Bath</th>\n",
              "      <th>Half Bath</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>5.663600e+04</td>\n",
              "      <td>26017.000000</td>\n",
              "      <td>26017.000000</td>\n",
              "      <td>2.601700e+04</td>\n",
              "      <td>2.601700e+04</td>\n",
              "      <td>2.601700e+04</td>\n",
              "      <td>24166.000000</td>\n",
              "      <td>24165.000000</td>\n",
              "      <td>24159.000000</td>\n",
              "      <td>24277.000000</td>\n",
              "      <td>24146.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>3.272111e+05</td>\n",
              "      <td>0.498903</td>\n",
              "      <td>4356.215782</td>\n",
              "      <td>6.907267e+04</td>\n",
              "      <td>1.608025e+05</td>\n",
              "      <td>2.323971e+05</td>\n",
              "      <td>1926.954345</td>\n",
              "      <td>1963.749224</td>\n",
              "      <td>3.090029</td>\n",
              "      <td>1.886106</td>\n",
              "      <td>0.283981</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>9.287425e+05</td>\n",
              "      <td>1.570396</td>\n",
              "      <td>2170.348270</td>\n",
              "      <td>1.060405e+05</td>\n",
              "      <td>2.068041e+05</td>\n",
              "      <td>2.810703e+05</td>\n",
              "      <td>1687.017313</td>\n",
              "      <td>26.546141</td>\n",
              "      <td>0.852942</td>\n",
              "      <td>0.961572</td>\n",
              "      <td>0.487905</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>5.000000e+01</td>\n",
              "      <td>0.010000</td>\n",
              "      <td>107.000000</td>\n",
              "      <td>1.000000e+02</td>\n",
              "      <td>0.000000e+00</td>\n",
              "      <td>1.000000e+02</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1799.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>1.350000e+05</td>\n",
              "      <td>0.180000</td>\n",
              "      <td>3126.000000</td>\n",
              "      <td>2.100000e+04</td>\n",
              "      <td>7.590000e+04</td>\n",
              "      <td>1.028000e+05</td>\n",
              "      <td>1239.000000</td>\n",
              "      <td>1948.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>2.054500e+05</td>\n",
              "      <td>0.270000</td>\n",
              "      <td>3929.000000</td>\n",
              "      <td>2.880000e+04</td>\n",
              "      <td>1.114000e+05</td>\n",
              "      <td>1.485000e+05</td>\n",
              "      <td>1632.000000</td>\n",
              "      <td>1960.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>3.290000e+05</td>\n",
              "      <td>0.450000</td>\n",
              "      <td>6228.000000</td>\n",
              "      <td>6.000000e+04</td>\n",
              "      <td>1.807000e+05</td>\n",
              "      <td>2.685000e+05</td>\n",
              "      <td>2212.000000</td>\n",
              "      <td>1983.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>5.427806e+07</td>\n",
              "      <td>160.060000</td>\n",
              "      <td>9530.000000</td>\n",
              "      <td>2.772000e+06</td>\n",
              "      <td>1.297180e+07</td>\n",
              "      <td>1.394040e+07</td>\n",
              "      <td>197988.000000</td>\n",
              "      <td>2017.000000</td>\n",
              "      <td>11.000000</td>\n",
              "      <td>10.000000</td>\n",
              "      <td>3.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-6a20c1b8-7195-4dc4-93a0-c8b61c9464fe')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "\n",
              "\n",
              "\n",
              "    <div id=\"df-911acf93-f7aa-4516-ab49-8cd00e8882dc\">\n",
              "      <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-911acf93-f7aa-4516-ab49-8cd00e8882dc')\"\n",
              "              title=\"Suggest charts.\"\n",
              "              style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "      </button>\n",
              "    </div>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "    background-color: #E8F0FE;\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: #1967D2;\n",
              "    height: 32px;\n",
              "    padding: 0 0 0 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: #E2EBFA;\n",
              "    box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: #174EA6;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "    background-color: #3B4455;\n",
              "    fill: #D2E3FC;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart:hover {\n",
              "    background-color: #434B5C;\n",
              "    box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "    filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "    fill: #FFFFFF;\n",
              "  }\n",
              "</style>\n",
              "\n",
              "    <script>\n",
              "      async function quickchart(key) {\n",
              "        const containerElement = document.querySelector('#' + key);\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      }\n",
              "    </script>\n",
              "\n",
              "      <script>\n",
              "\n",
              "function displayQuickchartButton(domScope) {\n",
              "  let quickchartButtonEl =\n",
              "    domScope.querySelector('#df-911acf93-f7aa-4516-ab49-8cd00e8882dc button.colab-df-quickchart');\n",
              "  quickchartButtonEl.style.display =\n",
              "    google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "}\n",
              "\n",
              "        displayQuickchartButton(document);\n",
              "      </script>\n",
              "      <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-6a20c1b8-7195-4dc4-93a0-c8b61c9464fe button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-6a20c1b8-7195-4dc4-93a0-c8b61c9464fe');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Data Exploration"
      ],
      "metadata": {
        "id": "VCTB3VGXfKdi"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=[12,6])\n",
        "sns.heatmap(df.corr(), annot=True, cmap=\"Reds\")\n",
        "plt.title('Correlation Matrix \\n'.center(10))\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 877
        },
        "id": "B2xU6LiYk4Bt",
        "outputId": "ee0986c5-31c8-4955-e742-163d7c2d8b13"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-9-71efaa35b498>:2: FutureWarning: The default value of numeric_only in DataFrame.corr is deprecated. In a future version, it will default to False. Select only valid columns or specify the value of numeric_only to silence this warning.\n",
            "  sns.heatmap(df.corr(), annot=True, cmap=\"Reds\")\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1200x600 with 2 Axes>"
            ],
            "image/png": "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AKDGlDwAJfejH/0o3/72t/P8888XHQUAAKghn2sBlNy73/3uNDU15dSpU+nUqVO6dOly1vMjR44UlAwAAKimDkUHAKC27rvvvqIjAAAA54FNHgAAAIASsMkDUEJvvPHG2363R48eNUwCAACcLzZ5AEqorq4ulUrlbb3b2tpa4zQAAMD5YJMHoITWrl175t//+Mc/Mm/evNx8880ZNWpUkuSZZ57J4sWLM3/+/KIiAgAAVWaTB6Dkxo8fn1mzZmXq1KlnzX/xi1/kwQcfzLp164oJBgAAVJWSB6Dk3vWud2XLli0ZPHjwWfOXXnopH/3oR9PU1FRQMgAAoJrqig4AQG3169cvDz300Dnzhx9+OP369SsgEQAAUAs2eQBKbvXq1ZkyZUouvfTSjBw5MkmycePG/O1vf8vKlSvz+c9/vuCEAABANSh5ANqBPXv2ZOHChdmxY0eSZOjQoZk9e7ZNHgAAKBElDwAAAEAJuEIdoIT++te/vu13P/KRj9QwCQAAcL7Y5AEoobq6ulQqlbS1taVSqZyZ//tH/n/PWltbz3s+AACg+tyuBVBCu3btyssvv5xdu3Zl5cqVGThwYB544IFs3rw5mzdvzgMPPJBBgwZl5cqVRUcFAACqxCYPQMldeeWVueOOO865RWv16tW5/fbb8+c//7mgZAAAQDXZ5AEoua1bt2bgwIHnzAcOHJht27YVkAgAAKgFJQ9AyQ0dOjTz589PS0vLmVlLS0vmz5+foUOHFpgMAACoJp9rAZTcxo0bM3HixLS1tZ25Sevft2+tWrUqV155ZZHxAACAKlHyALQDx48fz7Jly7Jjx44kb233TJs2LV27di04GQAAUC1KHoB2avv27Vm0aFHuvffeoqMAAABV4EwegHbk+PHjWbRoUUaPHp1hw4bl8ccfLzoSAABQJUoegHbg6aefzowZM9KnT5989atfzejRo7Nt27Y8//zzRUcDAACqRMkDUFIHDx7MPffckyFDhuT6669Pz549s27dutTV1WXGjBkZMmRI0REBAIAq6lB0AABqo3///rn++utz//3357Of/Wzq6vT6AABQZn7jByip/v37Z8OGDfnjH/+Yl156qeg4AABAjSl5AEpqx44dWbp0afbt25crrrgil19+eX7yk58kSSqVSsHpAACAanOFOkA7cOzYsfzyl7/MI488kmeffTZXXXVVpk2bluuuuy69evUqOh4AAFAFSh6Admb79u1ZtGhRHnvssRw5ciQnT54sOhIAAFAFSh6AdurUqVP57W9/m8mTJxcdBQAAqAIlDwAAAEAJOHgZAAAAoASUPAAAAAAloOQBAAAAKAElD0DJPfLII2lqaio6BgAAUGMOXgYouT59+qS5uTlf/OIXM3PmzIwePbroSAAAQA3Y5AEoub1792bx4sU5dOhQxo0blyFDhmTBggXZv39/0dEAAIAqsskD0I4cOHAgS5cuzeLFi7Njx45MmDAhM2fOzMSJE1NXp/cHAID/ZX6jB2hH+vTpk09+8pMZNWpU6urqsnXr1kyfPj2DBg3KunXrio4HAAC8A0oegHbgwIEDuffeezNs2LCMGzcub7zxRlatWpVdu3Zl7969ueGGGzJ9+vSiYwIAAO+Az7UASm7ixIlZs2ZNPvCBD2TWrFm56aab8p73vOesdw4ePJiLLroop0+fLiglAADwTnUoOgAAtdW7d++sX78+o0aN+n/f6dWrV3bt2nUeUwEAANXmcy2AkrvqqqvysY997Jx5S0tLlixZkiSpVCrp37//+Y4GAABUkc+1AEruggsuyL59+9K7d++z5ocPH07v3r3T2tpaUDIAAKCabPIAlFxbW1sqlco581deeSUNDQ0FJAIAAGrBmTwAJTVixIhUKpVUKpWMHz8+HTr850d+a2trdu3alQkTJhSYEAAAqCYlD0BJXXfddUmSzZs355prrkm3bt3OPOvUqVMGDBiQKVOmFJQOAACoNmfyAJRYa2trli5dmquvvjoXX3xx0XEAAIAaUvIAlFx9fX22b9+egQMHFh0FAACoIQcvA5Tchz/84bz88stFxwAAAGrMJg9AyT3++OP57ne/mzvvvDOXX355unbtetbzHj16FJQMAACoJiUPQMnV1f1nafO/r1L/99Xqra2tRcQCAACqzO1aACW3du3aoiMAAADngU0eAAAAgBJw8DJAO/CnP/0pN954Y0aPHp29e/cmSR577LFs2LCh4GQAAEC1KHkASm7lypW55ppr0qVLl2zatCknTpxIkrz++uv54Q9/WHA6AACgWpQ8ACV311135ec//3keeuihdOzY8cx8zJgx2bRpU4HJAACAalLyAJTciy++mLFjx54zb2hoyNGjR89/IAAAoCaUPAAld9FFF2Xnzp3nzDds2JD3v//9BSQCAABqQckDUHJf+cpX8o1vfCPPPfdcKpVK/vWvf2XZsmWZO3duvv71rxcdDwAAqJIORQcAoLbmzZuX06dPZ/z48WlqasrYsWPTuXPnzJ07N7feemvR8QAAgCqptLW1tRUdAoDaa2lpyc6dO3Ps2LF86EMfSrdu3YqOBAAAVJFNHoB2olOnTunevXu6d++u4AEAgBJyJg9AyZ06dSq33357GhoaMmDAgAwYMCANDQ257bbbcvLkyaLjAQAAVWKTB6Dkbr311jQ2Nuaee+7JqFGjkiTPPPNM7rjjjhw+fDgLFy4sOCEAAFANzuQBKLmGhoYsX748n/vc586ar169OlOnTs3rr79eUDIAAKCafK4FUHKdO3fOgAEDzpkPHDgwnTp1Ov+BAACAmlDyAJTcLbfckjvvvDMnTpw4Mztx4kTuvvvu3HLLLQUmAwAAqsnnWgAlN2nSpDz11FPp3Llzhg8fniTZsmVLWlpaMn78+LPebWxsLCIiAABQBQ5eBii5nj17ZsqUKWfN+vXrV1AaAACgVmzyAAAAAJSATR6AduLVV1/Niy++mCT54Ac/mF69ehWcCAAAqCYHLwOU3PHjxzNjxoxcfPHFGTt2bMaOHZu+fftm5syZaWpqKjoeAABQJUoegJL75je/mfXr1+d3v/tdjh49mqNHj+Y3v/lN1q9fn29961tFxwMAAKrEmTwAJXfhhRdmxYoVGTdu3FnztWvX5oYbbsirr75aTDAAAKCqbPIAlFxTU1P69Olzzrx3794+1wIAgBKxyQNQcuPHj8973/veLFmyJPX19UmS5ubmTJ8+PUeOHMmTTz5ZcEIAAKAalDwAJbd169ZMmDAhJ06cyPDhw5MkW7ZsSX19fdasWZNhw4YVnBAAAKgGJQ9AO9DU1JRly5Zlx44dSZKhQ4fmy1/+crp06VJwMgAAoFqUPAAldvLkyQwZMiSrVq3K0KFDi44DAADUkIOXAUqsY8eOefPNN4uOAQAAnAdKHoCSmzNnThYsWJBTp04VHQUAAKghn2sBlNykSZPy1FNPpVu3brnsssvStWvXs543NjYWlAwAAKimDkUHAKC2evbsmSlTphQdAwAAqDGbPAAAAAAl4EwegJI6ffp0FixYkDFjxuSKK67IvHnz0tzcXHQsAACgRpQ8ACV1991353vf+166deuWSy65JPfff3/mzJlTdCwAAKBGfK4FUFKDBw/O3Llz87WvfS1J8uSTT+YLX/hCmpubU1en4wcAgLJR8gCUVOfOnbNz587069fvzKy+vj47d+7M+973vgKTAQAAteBPuQAlderUqdTX158169ixY06ePFlQIgAAoJZcoQ5QUm1tbbn55pvTuXPnM7M333wzs2fPTteuXc/MGhsbi4gHAABUmZIHoKSmT59+zuzGG28sIAkAAHA+OJMHAAAAoAScyQMAAABQAkoegBKaPXt2Xnnllbf17q9+9assW7asxokAAIBacyYPQAn16tUrw4YNy5gxYzJx4sR8/OMfT9++fVNfX5/XXnst27Zty4YNG7J8+fL07ds3Dz74YNGRAQCAd8iZPAAldeDAgTz88MNZvnx5tm3bdtaz7t275zOf+UxmzZqVCRMmFJQQAACoJiUPQDvw2muv5Z///Geam5tz4YUXZtCgQalUKkXHAgAAqkjJAwAAAFACDl4GAAAAKAElDwAAAEAJKHkAAAAASkDJAwAAAFACSh6Akmtubk5TU9OZ/+/evTv33XdfnnjiiQJTAQAA1abkASi5a6+9NkuWLEmSHD16NCNHjsyPf/zjXHvttVm4cGHB6QAAgGpR8gCU3KZNm/KpT30qSbJixYr06dMnu3fvzpIlS/LTn/604HQAAEC1KHkASq6pqSndu3dPkjzxxBOZPHly6urq8olPfCK7d+8uOB0AAFAtSh6Akrv00kvz61//Onv27MmaNWty9dVXJ0kOHjyYHj16FJwOAACoFiUPQMl9//vfz9y5czNgwICMHDkyo0aNSvLWVs+IESMKTgcAAFRLpa2tra3oEADU1v79+7Nv374MHz48dXVv9fsbN25Mjx49MmTIkILTAQAA1aDkAQAAACiBDkUHAKA2Jk+e/Lbea2xsrHESAADgfFDyAJRUQ0ND0REAAIDzyOdaAAAAACXgdi0AAACAElDyAAAAAJSAkgcAAACgBJQ8AAAAACWg5AEAAAAoASUPAAAAQAkoeQAAAABKQMkDAAAAUAJKHgAAAIAS+D/tiitNyLx9cQAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df = df.drop(['Property Address','Suite/ RESIDENTIAL CONDO#','Legal Reference','Sale Date','Owner Name','Address'], axis=1)"
      ],
      "metadata": {
        "id": "ykTTL70OkgWd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "col = list(df.columns)\n",
        "categorical_features = []\n",
        "numerical_features = []\n",
        "\n",
        "for i in col:\n",
        "        if df[i].dtype == 'object' or df[i].dtype == 'bool':\n",
        "            categorical_features.append(i)\n",
        "        else:\n",
        "            numerical_features.append(i)\n",
        "\n",
        "print('Categorical_Features: ', categorical_features)\n",
        "print('Numerical_Features: ', numerical_features)\n",
        "\n",
        "print('\\nInference: The Dataset has {} categorical & {} numerical features.'.format(len(categorical_features),len(numerical_features)))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pAojAfiVkHxd",
        "outputId": "d269a27b-b064-4796-9572-39cbbe9a199f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Categorical_Features:  ['Land Use', 'Sold As Vacant', 'Multiple Parcels Involved in Sale', 'Is (Property Address = Owner Address)', 'Tax District', 'Foundation Type', 'Exterior Wall', 'Grade']\n",
            "Numerical_Features:  ['Sale Price', 'Acreage', 'Neighborhood', 'Land Value', 'Building Value', 'Total Value', 'Finished Area', 'Year Built', 'Bedrooms', 'Full Bath', 'Half Bath']\n",
            "\n",
            "Inference: The Dataset has 8 categorical & 11 numerical features.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df[categorical_features] = df[categorical_features].fillna(df[categorical_features].mode().iloc[0])"
      ],
      "metadata": {
        "id": "O72sddX9spPd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "imputer = KNNImputer(n_neighbors=3)\n",
        "imputed = imputer.fit_transform(df[numerical_features])\n",
        "imputed"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j3uFTSczh_Il",
        "outputId": "1f3d980f-5388-4b64-c00b-e1d2bc5d0d73"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[1.32000000e+05, 2.43333333e-01, 4.76266667e+03, ...,\n",
              "        3.33333333e+00, 1.66666667e+00, 0.00000000e+00],\n",
              "       [1.91500000e+05, 1.70000000e-01, 3.12700000e+03, ...,\n",
              "        2.00000000e+00, 1.00000000e+00, 0.00000000e+00],\n",
              "       [2.02000000e+05, 1.10000000e-01, 9.12600000e+03, ...,\n",
              "        3.00000000e+00, 2.00000000e+00, 1.00000000e+00],\n",
              "       ...,\n",
              "       [7.42000000e+05, 9.73333333e-01, 6.42766667e+03, ...,\n",
              "        4.66666667e+00, 4.66666667e+00, 3.33333333e-01],\n",
              "       [3.20000000e+05, 1.86666667e-01, 1.45933333e+03, ...,\n",
              "        2.66666667e+00, 1.33333333e+00, 3.33333333e-01],\n",
              "       [3.30000000e+05, 5.06666667e-01, 3.92666667e+03, ...,\n",
              "        3.66666667e+00, 3.00000000e+00, 3.33333333e-01]])"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data_imputed = pd.DataFrame(imputed, columns=numerical_features)\n",
        "data_imputed.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "QBH0fibzZoOX",
        "outputId": "317bb27d-8387-4bc8-cb82-f938efe135c9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Sale Price   Acreage  Neighborhood    Land Value  Building Value  \\\n",
              "0    132000.0  0.243333   4762.666667  22333.333333    87833.333333   \n",
              "1    191500.0  0.170000   3127.000000  32000.000000   134400.000000   \n",
              "2    202000.0  0.110000   9126.000000  34000.000000   157800.000000   \n",
              "3     32000.0  0.170000   3130.000000  25000.000000   243700.000000   \n",
              "4    102000.0  0.340000   3130.000000  25000.000000   138100.000000   \n",
              "\n",
              "     Total Value  Finished Area  Year Built  Bedrooms  Full Bath  Half Bath  \n",
              "0  113866.666667    1486.973327      1971.0  3.333333   1.666667        0.0  \n",
              "1  168300.000000    1149.000000      1941.0  2.000000   1.000000        0.0  \n",
              "2  191800.000000    2090.824950      2000.0  3.000000   2.000000        1.0  \n",
              "3  268700.000000    2145.600010      1948.0  4.000000   2.000000        0.0  \n",
              "4  164800.000000    1969.000000      1910.0  2.000000   1.000000        0.0  "
            ],
            "text/html": [
              "\n",
              "\n",
              "  <div id=\"df-a2707e66-242b-422a-b2ab-cd04740a2a80\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>Sale Price</th>\n",
              "      <th>Acreage</th>\n",
              "      <th>Neighborhood</th>\n",
              "      <th>Land Value</th>\n",
              "      <th>Building Value</th>\n",
              "      <th>Total Value</th>\n",
              "      <th>Finished Area</th>\n",
              "      <th>Year Built</th>\n",
              "      <th>Bedrooms</th>\n",
              "      <th>Full Bath</th>\n",
              "      <th>Half Bath</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>132000.0</td>\n",
              "      <td>0.243333</td>\n",
              "      <td>4762.666667</td>\n",
              "      <td>22333.333333</td>\n",
              "      <td>87833.333333</td>\n",
              "      <td>113866.666667</td>\n",
              "      <td>1486.973327</td>\n",
              "      <td>1971.0</td>\n",
              "      <td>3.333333</td>\n",
              "      <td>1.666667</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>191500.0</td>\n",
              "      <td>0.170000</td>\n",
              "      <td>3127.000000</td>\n",
              "      <td>32000.000000</td>\n",
              "      <td>134400.000000</td>\n",
              "      <td>168300.000000</td>\n",
              "      <td>1149.000000</td>\n",
              "      <td>1941.0</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>202000.0</td>\n",
              "      <td>0.110000</td>\n",
              "      <td>9126.000000</td>\n",
              "      <td>34000.000000</td>\n",
              "      <td>157800.000000</td>\n",
              "      <td>191800.000000</td>\n",
              "      <td>2090.824950</td>\n",
              "      <td>2000.0</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>32000.0</td>\n",
              "      <td>0.170000</td>\n",
              "      <td>3130.000000</td>\n",
              "      <td>25000.000000</td>\n",
              "      <td>243700.000000</td>\n",
              "      <td>268700.000000</td>\n",
              "      <td>2145.600010</td>\n",
              "      <td>1948.0</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>102000.0</td>\n",
              "      <td>0.340000</td>\n",
              "      <td>3130.000000</td>\n",
              "      <td>25000.000000</td>\n",
              "      <td>138100.000000</td>\n",
              "      <td>164800.000000</td>\n",
              "      <td>1969.000000</td>\n",
              "      <td>1910.0</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-a2707e66-242b-422a-b2ab-cd04740a2a80')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "\n",
              "\n",
              "\n",
              "    <div id=\"df-fa9117c0-62e4-492d-b783-8cf0451392f4\">\n",
              "      <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-fa9117c0-62e4-492d-b783-8cf0451392f4')\"\n",
              "              title=\"Suggest charts.\"\n",
              "              style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "      </button>\n",
              "    </div>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "    background-color: #E8F0FE;\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: #1967D2;\n",
              "    height: 32px;\n",
              "    padding: 0 0 0 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: #E2EBFA;\n",
              "    box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: #174EA6;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "    background-color: #3B4455;\n",
              "    fill: #D2E3FC;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart:hover {\n",
              "    background-color: #434B5C;\n",
              "    box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "    filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "    fill: #FFFFFF;\n",
              "  }\n",
              "</style>\n",
              "\n",
              "    <script>\n",
              "      async function quickchart(key) {\n",
              "        const containerElement = document.querySelector('#' + key);\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      }\n",
              "    </script>\n",
              "\n",
              "      <script>\n",
              "\n",
              "function displayQuickchartButton(domScope) {\n",
              "  let quickchartButtonEl =\n",
              "    domScope.querySelector('#df-fa9117c0-62e4-492d-b783-8cf0451392f4 button.colab-df-quickchart');\n",
              "  quickchartButtonEl.style.display =\n",
              "    google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "}\n",
              "\n",
              "        displayQuickchartButton(document);\n",
              "      </script>\n",
              "      <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-a2707e66-242b-422a-b2ab-cd04740a2a80 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-a2707e66-242b-422a-b2ab-cd04740a2a80');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df2 = df.drop(numerical_features, axis=1)\n",
        "df = pd.concat([df2, data_imputed], axis=1)\n",
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 513
        },
        "id": "y43kXTOeoN8X",
        "outputId": "28bbbd53-6647-48cf-f8d6-a1445751b073"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "            Land Use Sold As Vacant Multiple Parcels Involved in Sale  \\\n",
              "0  RESIDENTIAL CONDO             No                                No   \n",
              "1      SINGLE FAMILY             No                                No   \n",
              "2      SINGLE FAMILY             No                                No   \n",
              "3      SINGLE FAMILY             No                                No   \n",
              "4      SINGLE FAMILY             No                                No   \n",
              "\n",
              "   Is (Property Address = Owner Address)             Tax District  \\\n",
              "0                                  False  URBAN SERVICES DISTRICT   \n",
              "1                                   True  URBAN SERVICES DISTRICT   \n",
              "2                                   True       CITY OF BERRY HILL   \n",
              "3                                   True  URBAN SERVICES DISTRICT   \n",
              "4                                   True  URBAN SERVICES DISTRICT   \n",
              "\n",
              "  Foundation Type Exterior Wall Grade  Sale Price   Acreage  Neighborhood  \\\n",
              "0           CRAWL         BRICK  C       132000.0  0.243333   4762.666667   \n",
              "1         PT BSMT         BRICK  C       191500.0  0.170000   3127.000000   \n",
              "2            SLAB   BRICK/FRAME  C       202000.0  0.110000   9126.000000   \n",
              "3       FULL BSMT   BRICK/FRAME  B        32000.0  0.170000   3130.000000   \n",
              "4           CRAWL         FRAME  C       102000.0  0.340000   3130.000000   \n",
              "\n",
              "     Land Value  Building Value    Total Value  Finished Area  Year Built  \\\n",
              "0  22333.333333    87833.333333  113866.666667    1486.973327      1971.0   \n",
              "1  32000.000000   134400.000000  168300.000000    1149.000000      1941.0   \n",
              "2  34000.000000   157800.000000  191800.000000    2090.824950      2000.0   \n",
              "3  25000.000000   243700.000000  268700.000000    2145.600010      1948.0   \n",
              "4  25000.000000   138100.000000  164800.000000    1969.000000      1910.0   \n",
              "\n",
              "   Bedrooms  Full Bath  Half Bath  \n",
              "0  3.333333   1.666667        0.0  \n",
              "1  2.000000   1.000000        0.0  \n",
              "2  3.000000   2.000000        1.0  \n",
              "3  4.000000   2.000000        0.0  \n",
              "4  2.000000   1.000000        0.0  "
            ],
            "text/html": [
              "\n",
              "\n",
              "  <div id=\"df-7118738f-1e93-4059-bba3-2c881961266b\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>Land Use</th>\n",
              "      <th>Sold As Vacant</th>\n",
              "      <th>Multiple Parcels Involved in Sale</th>\n",
              "      <th>Is (Property Address = Owner Address)</th>\n",
              "      <th>Tax District</th>\n",
              "      <th>Foundation Type</th>\n",
              "      <th>Exterior Wall</th>\n",
              "      <th>Grade</th>\n",
              "      <th>Sale Price</th>\n",
              "      <th>Acreage</th>\n",
              "      <th>Neighborhood</th>\n",
              "      <th>Land Value</th>\n",
              "      <th>Building Value</th>\n",
              "      <th>Total Value</th>\n",
              "      <th>Finished Area</th>\n",
              "      <th>Year Built</th>\n",
              "      <th>Bedrooms</th>\n",
              "      <th>Full Bath</th>\n",
              "      <th>Half Bath</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>RESIDENTIAL CONDO</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>False</td>\n",
              "      <td>URBAN SERVICES DISTRICT</td>\n",
              "      <td>CRAWL</td>\n",
              "      <td>BRICK</td>\n",
              "      <td>C</td>\n",
              "      <td>132000.0</td>\n",
              "      <td>0.243333</td>\n",
              "      <td>4762.666667</td>\n",
              "      <td>22333.333333</td>\n",
              "      <td>87833.333333</td>\n",
              "      <td>113866.666667</td>\n",
              "      <td>1486.973327</td>\n",
              "      <td>1971.0</td>\n",
              "      <td>3.333333</td>\n",
              "      <td>1.666667</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>SINGLE FAMILY</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>True</td>\n",
              "      <td>URBAN SERVICES DISTRICT</td>\n",
              "      <td>PT BSMT</td>\n",
              "      <td>BRICK</td>\n",
              "      <td>C</td>\n",
              "      <td>191500.0</td>\n",
              "      <td>0.170000</td>\n",
              "      <td>3127.000000</td>\n",
              "      <td>32000.000000</td>\n",
              "      <td>134400.000000</td>\n",
              "      <td>168300.000000</td>\n",
              "      <td>1149.000000</td>\n",
              "      <td>1941.0</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>SINGLE FAMILY</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>True</td>\n",
              "      <td>CITY OF BERRY HILL</td>\n",
              "      <td>SLAB</td>\n",
              "      <td>BRICK/FRAME</td>\n",
              "      <td>C</td>\n",
              "      <td>202000.0</td>\n",
              "      <td>0.110000</td>\n",
              "      <td>9126.000000</td>\n",
              "      <td>34000.000000</td>\n",
              "      <td>157800.000000</td>\n",
              "      <td>191800.000000</td>\n",
              "      <td>2090.824950</td>\n",
              "      <td>2000.0</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>SINGLE FAMILY</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>True</td>\n",
              "      <td>URBAN SERVICES DISTRICT</td>\n",
              "      <td>FULL BSMT</td>\n",
              "      <td>BRICK/FRAME</td>\n",
              "      <td>B</td>\n",
              "      <td>32000.0</td>\n",
              "      <td>0.170000</td>\n",
              "      <td>3130.000000</td>\n",
              "      <td>25000.000000</td>\n",
              "      <td>243700.000000</td>\n",
              "      <td>268700.000000</td>\n",
              "      <td>2145.600010</td>\n",
              "      <td>1948.0</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>SINGLE FAMILY</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>True</td>\n",
              "      <td>URBAN SERVICES DISTRICT</td>\n",
              "      <td>CRAWL</td>\n",
              "      <td>FRAME</td>\n",
              "      <td>C</td>\n",
              "      <td>102000.0</td>\n",
              "      <td>0.340000</td>\n",
              "      <td>3130.000000</td>\n",
              "      <td>25000.000000</td>\n",
              "      <td>138100.000000</td>\n",
              "      <td>164800.000000</td>\n",
              "      <td>1969.000000</td>\n",
              "      <td>1910.0</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-7118738f-1e93-4059-bba3-2c881961266b')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "\n",
              "\n",
              "\n",
              "    <div id=\"df-279f8fe3-173b-409c-91b8-f40ada339c46\">\n",
              "      <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-279f8fe3-173b-409c-91b8-f40ada339c46')\"\n",
              "              title=\"Suggest charts.\"\n",
              "              style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "      </button>\n",
              "    </div>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "    background-color: #E8F0FE;\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: #1967D2;\n",
              "    height: 32px;\n",
              "    padding: 0 0 0 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: #E2EBFA;\n",
              "    box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: #174EA6;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "    background-color: #3B4455;\n",
              "    fill: #D2E3FC;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart:hover {\n",
              "    background-color: #434B5C;\n",
              "    box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "    filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "    fill: #FFFFFF;\n",
              "  }\n",
              "</style>\n",
              "\n",
              "    <script>\n",
              "      async function quickchart(key) {\n",
              "        const containerElement = document.querySelector('#' + key);\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      }\n",
              "    </script>\n",
              "\n",
              "      <script>\n",
              "\n",
              "function displayQuickchartButton(domScope) {\n",
              "  let quickchartButtonEl =\n",
              "    domScope.querySelector('#df-279f8fe3-173b-409c-91b8-f40ada339c46 button.colab-df-quickchart');\n",
              "  quickchartButtonEl.style.display =\n",
              "    google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "}\n",
              "\n",
              "        displayQuickchartButton(document);\n",
              "      </script>\n",
              "      <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-7118738f-1e93-4059-bba3-2c881961266b button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-7118738f-1e93-4059-bba3-2c881961266b');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.shape"
      ],
      "metadata": {
        "id": "roBfunTzH4cW",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "abc4ffb3-f82b-47b2-d7d6-095c3346ef6d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(56636, 19)"
            ]
          },
          "metadata": {},
          "execution_count": 37
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "The Datset consists of 19 features and 56636 records after filling the null values"
      ],
      "metadata": {
        "id": "rdMI9WymdoUp"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Checking for null values of each feature after data cleaning\n",
        "df.isnull().sum()"
      ],
      "metadata": {
        "id": "jyLL9Rjlep3G",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "7ce3cdbb-e868-4cc7-cb1d-7d41d350f135"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Land Use                                 0\n",
              "Sold As Vacant                           0\n",
              "Multiple Parcels Involved in Sale        0\n",
              "Is (Property Address = Owner Address)    0\n",
              "Tax District                             0\n",
              "Foundation Type                          0\n",
              "Exterior Wall                            0\n",
              "Grade                                    0\n",
              "Sale Price                               0\n",
              "Acreage                                  0\n",
              "Neighborhood                             0\n",
              "Land Value                               0\n",
              "Building Value                           0\n",
              "Total Value                              0\n",
              "Finished Area                            0\n",
              "Year Built                               0\n",
              "Bedrooms                                 0\n",
              "Full Bath                                0\n",
              "Half Bath                                0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 38
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Exploratory Data Analysis (EDA)"
      ],
      "metadata": {
        "id": "yZgbLOG4sCXT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "sns.set(style='whitegrid')\n",
        "f,ax = plt.subplots(2,2,figsize = (16,12))\n",
        "\n",
        "vis1 = sns.distplot(df['Sale Price'], bins=40, color='red', kde=True, hist_kws=dict(edgecolor='black', linewidth=2),ax= ax[0][0])\n",
        "vis2 = sns.distplot(df['Land Value'], bins=40, color='red', kde=True, hist_kws=dict(edgecolor='black', linewidth=2),ax= ax[0][1])\n",
        "vis3 = sns.distplot(df['Building Value'], bins=40, color='red', kde=True, hist_kws=dict(edgecolor='black', linewidth=2),ax= ax[1][0])\n",
        "vis4 = sns.distplot(df['Total Value'], bins=40, color='red', kde=True, hist_kws=dict(edgecolor='black', linewidth=2),ax= ax[1][1])\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "j9uh2GeIuUCI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def scatter_df():\n",
        "  for feature in numerical_features:\n",
        "    if feature != 'Sale Price':\n",
        "      plot = sns.scatterplot(x=df[feature], y=df['Sale Price'])\n",
        "      plt.title('{} / Sale Price'.format(feature), fontsize = 16)\n",
        "      plt.show()\n",
        "\n",
        "scatter_df()"
      ],
      "metadata": {
        "id": "ABWSBeNodfZC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df['Land Use'].value_counts()"
      ],
      "metadata": {
        "id": "keDoiXrXcrUl",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "31328d7f-1fe4-4a85-e000-b3c72ceb62b6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "SINGLE FAMILY                                 34268\n",
              "RESIDENTIAL CONDO                             14428\n",
              "VACANT RESIDENTIAL LAND                        5164\n",
              "DUPLEX                                         1389\n",
              "ZERO LOT LINE                                  1049\n",
              "TRIPLEX                                          92\n",
              "QUADPLEX                                         39\n",
              "CONDOMINIUM OFC OR OTHER COM CONDO               35\n",
              "CHURCH                                           34\n",
              "MOBILE HOME                                      20\n",
              "DORMITORY/BOARDING HOUSE                         19\n",
              "SPLIT CLASS                                      17\n",
              "VACANT COMMERCIAL LAND                           17\n",
              "PARKING LOT                                      11\n",
              "GREENBELT                                        10\n",
              "FOREST                                           10\n",
              "PARSONAGE                                         6\n",
              "GREENBELT/RES_x000D_\\nGRRENBELT/RES               3\n",
              "DAY CARE CENTER                                   2\n",
              "NON-PROFIT CHARITABLE SERVICE                     2\n",
              "APARTMENT: LOW RISE (BUILT SINCE 1960)            2\n",
              "TERMINAL/DISTRIBUTION WAREHOUSE                   2\n",
              "VACANT ZONED MULTI FAMILY                         2\n",
              "RESTURANT/CAFETERIA                               2\n",
              "OFFICE BLDG (ONE OR TWO STORIES)                  2\n",
              "VACANT RURAL LAND                                 2\n",
              "CLUB/UNION HALL/LODGE                             1\n",
              "LIGHT MANUFACTURING                               1\n",
              "ONE STORY GENERAL RETAIL STORE                    1\n",
              "CONVENIENCE MARKET WITHOUT GAS                    1\n",
              "SMALL SERVICE SHOP                                1\n",
              "STRIP SHOPPING CENTER                             1\n",
              "METRO OTHER THAN OFC, SCHOOL,HOSP, OR PARK        1\n",
              "NIGHTCLUB/LOUNGE                                  1\n",
              "MORTUARY/CEMETERY                                 1\n",
              "Name: Land Use, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 39
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['Tax District'].value_counts()"
      ],
      "metadata": {
        "id": "Jss9XUi-jwWh",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "16a24f51-b201-4101-fb76-7e0520e1b608"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "URBAN SERVICES DISTRICT      50645\n",
              "GENERAL SERVICES DISTRICT     4556\n",
              "CITY OF FOREST HILLS           407\n",
              "CITY OF OAK HILL               393\n",
              "CITY OF GOODLETTSVILLE         379\n",
              "CITY OF BELLE MEADE            235\n",
              "CITY OF BERRY HILL              21\n",
              "Name: Tax District, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 40
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['Foundation Type'].value_counts()"
      ],
      "metadata": {
        "id": "SZy-hfbNX-FL",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a61f0552-5a66-4448-aaf0-c7e0fe831aae"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "CRAWL        47861\n",
              "FULL BSMT     3917\n",
              "PT BSMT       3200\n",
              "SLAB          1581\n",
              "TYPICAL         40\n",
              "PIERS           37\n",
              "Name: Foundation Type, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 41
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['Exterior Wall'].value_counts()"
      ],
      "metadata": {
        "id": "yWNYU-CkYGb8",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "3da6584a-99c9-438b-824b-5db4aff70c9f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "BRICK           44413\n",
              "FRAME            8870\n",
              "BRICK/FRAME      2602\n",
              "STONE             331\n",
              "STUCCO            168\n",
              "CONC BLK          113\n",
              "FRAME/STONE       108\n",
              "LOG                15\n",
              "METAL              15\n",
              "PRECAST CONC        1\n",
              "Name: Exterior Wall, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 42
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['Grade'].value_counts()"
      ],
      "metadata": {
        "id": "TaD20Y9sM6eA",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "979dafa1-777f-4a16-e889-b1fc6ad8a6b5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "C       49733\n",
              "B        3698\n",
              "D        1984\n",
              "A         598\n",
              "X         523\n",
              "E          60\n",
              "TCC        20\n",
              "IDC         3\n",
              "AAB         3\n",
              "AAC         3\n",
              "OFC         2\n",
              "SRC         1\n",
              "SSC         1\n",
              "SRD         1\n",
              "TFC         1\n",
              "TCB         1\n",
              "TAC         1\n",
              "OMB         1\n",
              "OFB         1\n",
              "TCD         1\n",
              "Name: Grade, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 43
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#One-hot encoding the categorical columns\n",
        "\n",
        "from sklearn.preprocessing import OneHotEncoder\n",
        "\n",
        "OH_encoder = OneHotEncoder(sparse=False, handle_unknown='ignore', min_frequency=500)\n",
        "OH_cols = pd.DataFrame(OH_encoder.fit_transform(df[categorical_features]))\n",
        "OH_cols.index = df.index\n",
        "df3 = df.drop(categorical_features, axis=1)\n",
        "df = pd.concat([df3, OH_cols], axis=1)"
      ],
      "metadata": {
        "id": "7DnDn4Mqrgf0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "355b9707-33dc-45c3-c202-07cec4a00a18"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/sklearn/preprocessing/_encoders.py:868: FutureWarning: `sparse` was renamed to `sparse_output` in version 1.2 and will be removed in 1.4. `sparse_output` is ignored unless you leave `sparse` to its default value.\n",
            "  warnings.warn(\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.shape"
      ],
      "metadata": {
        "id": "4iS1Pe-Ij2aS",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6b2d66db-0c33-4cb0-92fa-18a4a92770ae"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(56636, 41)"
            ]
          },
          "metadata": {},
          "execution_count": 45
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.columns"
      ],
      "metadata": {
        "id": "XOm7tsRFcgTM",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "3665f4ef-55f6-483f-bbef-ce1b418fc124"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index([    'Sale Price',        'Acreage',   'Neighborhood',     'Land Value',\n",
              "       'Building Value',    'Total Value',  'Finished Area',     'Year Built',\n",
              "             'Bedrooms',      'Full Bath',      'Half Bath',                0,\n",
              "                      1,                2,                3,                4,\n",
              "                      5,                6,                7,                8,\n",
              "                      9,               10,               11,               12,\n",
              "                     13,               14,               15,               16,\n",
              "                     17,               18,               19,               20,\n",
              "                     21,               22,               23,               24,\n",
              "                     25,               26,               27,               28,\n",
              "                     29],\n",
              "      dtype='object')"
            ]
          },
          "metadata": {},
          "execution_count": 46
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Feature Selection"
      ],
      "metadata": {
        "id": "8SdVaRm17B6c"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "target= 'Sale Price'\n",
        "X = df.drop([target], axis=1)\n",
        "y = df[target]"
      ],
      "metadata": {
        "id": "LS4h_Vjj270I"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X.columns = X.columns.astype(str)"
      ],
      "metadata": {
        "id": "w4X95uCqcK1w"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)\n",
        "\n",
        "print('Original set --> ', X.shape,y.shape, '\\nTraining set --> ', X_train.shape,y_train.shape, '\\nTesting set  --> ', X_test.shape,y_test.shape)"
      ],
      "metadata": {
        "id": "hk8teEAh-ho1",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1fa1e013-b3e4-4f53-c84c-214835bc8192"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Original set -->  (56636, 40) (56636,) \n",
            "Training set -->  (45308, 40) (45308,) \n",
            "Testing set  -->  (11328, 40) (11328,)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Modeling"
      ],
      "metadata": {
        "id": "PtsTL3LW7K4Z"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.linear_model import LinearRegression\n",
        "from sklearn.preprocessing import PolynomialFeatures\n",
        "from sklearn.ensemble import GradientBoostingRegressor\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "from sklearn.metrics import mean_absolute_error\n",
        "\n",
        "from sklearn.linear_model import Ridge\n",
        "from sklearn.linear_model import Lasso\n",
        "from xgboost import XGBRegressor"
      ],
      "metadata": {
        "id": "GcZOr42QzqSR"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Scaling the numerical features using\n",
        "scaler = StandardScaler()\n",
        "X_train_scaled = scaler.fit_transform(X_train.select_dtypes(['int','float']))\n",
        "X_test_scaled = scaler.transform(X_test.select_dtypes(['int', 'float']))"
      ],
      "metadata": {
        "id": "-b40LwQ7VpuW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Linear Regression\n",
        "model1 = LinearRegression()\n",
        "lr = model1.fit(X_train_scaled, y_train)"
      ],
      "metadata": {
        "id": "7gTX_sUyteT7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"LR Train R2 Score: \", lr.score(X_train_scaled, y_train))\n",
        "print(\"LR Test R2 Score: \", lr.score(X_test_scaled, y_test))"
      ],
      "metadata": {
        "id": "EIMuPwYbeSWg",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b371ee1e-c61c-44ec-a029-214561314a36"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "LR Train R2 Score:  0.6846190542353496\n",
            "LR Test R2 Score:  0.7220126545193019\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred_lr = model1.predict(X_test_scaled)"
      ],
      "metadata": {
        "id": "jFHN6jFg9XAv"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "mae = mean_absolute_error(y_test, y_pred_lr)\n",
        "print('Linear Regression MAE: ', mae)"
      ],
      "metadata": {
        "id": "E8hsoDCEpHOs",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "fac0af46-502c-4183-a1c4-b4ed3c5d253d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Linear Regression MAE:  111827.58171140465\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "poly = PolynomialFeatures(degree=2)\n",
        "X_train_poly = poly.fit_transform(X_train_scaled)\n",
        "X_test_poly = poly.transform(X_test_scaled)"
      ],
      "metadata": {
        "id": "bFdUvGI0zqn-"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X_train_poly.shape"
      ],
      "metadata": {
        "id": "VlFePKxU4yLG",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6776936c-03ff-4073-d3a3-395cdefabaf0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(45308, 861)"
            ]
          },
          "metadata": {},
          "execution_count": 58
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X_test_poly.shape"
      ],
      "metadata": {
        "id": "xOn5iH0OWUcM",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0ce8bd59-d90f-4a76-cd4e-0272a39b528e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(11328, 861)"
            ]
          },
          "metadata": {},
          "execution_count": 59
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "polymodel = LinearRegression()\n",
        "pf = polymodel.fit(X_train_poly, y_train)"
      ],
      "metadata": {
        "id": "PR5teiwy_K8O"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"PLR Train R2 Score: \", pf.score(X_train_poly, y_train))\n",
        "print(\"PLR Test R2 Score: \", pf.score(X_test_poly, y_test))"
      ],
      "metadata": {
        "id": "fwHGfO5b0bqq",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "329b989b-71cb-4b24-adeb-30409970d52c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "PLR Train R2 Score:  0.7290179627875752\n",
            "PLR Test R2 Score:  -5030474047949.09\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "ridge = Ridge(alpha=1)\n",
        "rd = ridge.fit(X_train_poly, y_train)"
      ],
      "metadata": {
        "id": "Bmyii2rT4Qb8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"RidgeReg Train R2 Score: \", rd.score(X_train_poly, y_train))\n",
        "print(\"RidgeReg Test R2 Score: \", rd.score(X_test_poly, y_test))"
      ],
      "metadata": {
        "id": "dGTnPq4VFUWH",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6e261bb9-8ae6-488f-8041-c9c9dbd57c95"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "RidgeReg Train R2 Score:  0.7289570785360885\n",
            "RidgeReg Test R2 Score:  0.7274383456545777\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred_rd = ridge.predict(X_test_poly)"
      ],
      "metadata": {
        "id": "DjG9XqSgJs4y"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "mae_rd = mean_absolute_error(y_test, y_pred_rd)\n",
        "print('Ridge Regression MAE: ', mae_rd)"
      ],
      "metadata": {
        "id": "5oeKspE2J0jt",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "14e79832-8657-440f-da2d-3fbe8d6767ef"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ridge Regression MAE:  91322.47267184754\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "lasso = Lasso(alpha=1)\n",
        "ls = lasso.fit(X_train_poly, y_train)"
      ],
      "metadata": {
        "id": "_xbjBJmy2MXp",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "9522460a-db62-4bb0-e1b5-8536a5ded2d5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/sklearn/linear_model/_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 5.560e+15, tolerance: 4.093e+12\n",
            "  model = cd_fast.enet_coordinate_descent(\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Lasso Train R2 Score: \", ls.score(X_train_poly, y_train))\n",
        "print(\"Lasso Test R2 Score: \", ls.score(X_test_poly, y_test))"
      ],
      "metadata": {
        "id": "tZ4hp9Md2nY-",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b70dfa50-c384-4c82-a62b-c5f27516f4b3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Lasso Train R2 Score:  0.7282501799867238\n",
            "Lasso Test R2 Score:  0.737819429668138\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred_ls = lasso.predict(X_test_poly)"
      ],
      "metadata": {
        "id": "n_Q1MaUh8IK5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "mae_ls = mean_absolute_error(y_test, y_pred_ls)\n",
        "print('Lasso Regression MAE: ', mae_ls)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iOIbTDUv8PqA",
        "outputId": "20884fdf-fb85-48a8-ade4-884be1d14b1d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Lasso Regression MAE:  91118.37239831095\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "gbr = GradientBoostingRegressor(n_estimators=2500, learning_rate=0.1, max_depth=2)\n",
        "gbr.fit(X_train_scaled, y_train)"
      ],
      "metadata": {
        "id": "U-E-X0QAqSxh",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 74
        },
        "outputId": "eaad3bf1-eeb2-47d3-ff9c-de102714cb87"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "GradientBoostingRegressor(max_depth=2, n_estimators=2500)"
            ],
            "text/html": [
              "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>GradientBoostingRegressor(max_depth=2, n_estimators=2500)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">GradientBoostingRegressor</label><div class=\"sk-toggleable__content\"><pre>GradientBoostingRegressor(max_depth=2, n_estimators=2500)</pre></div></div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 70
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"GB Train R2 Score: \", gbr.score(X_train_scaled, y_train))\n",
        "print(\"GB Test R2 Score: \", gbr.score(X_test_scaled, y_test))"
      ],
      "metadata": {
        "id": "cV_SkSJABAW8",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "73b136cd-59cd-4186-a7fc-9ec09b55b732"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "GB Train R2 Score:  0.7573072594061377\n",
            "GB Test R2 Score:  0.7731939183095531\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "xgb = XGBRegressor(n_estimators=2500, learning_rate=0.5, n_jobs=5, reg_alpha=5)\n",
        "xgb.fit(X_train_scaled, y_train)"
      ],
      "metadata": {
        "id": "6tCu8rK6k0Wp",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 248
        },
        "outputId": "b3f92094-3b26-4963-f583-eb6564566714"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "XGBRegressor(base_score=None, booster=None, callbacks=None,\n",
              "             colsample_bylevel=None, colsample_bynode=None,\n",
              "             colsample_bytree=None, early_stopping_rounds=None,\n",
              "             enable_categorical=False, eval_metric=None, feature_types=None,\n",
              "             gamma=None, gpu_id=None, grow_policy=None, importance_type=None,\n",
              "             interaction_constraints=None, learning_rate=0.5, max_bin=None,\n",
              "             max_cat_threshold=None, max_cat_to_onehot=None,\n",
              "             max_delta_step=None, max_depth=None, max_leaves=None,\n",
              "             min_child_weight=None, missing=nan, monotone_constraints=None,\n",
              "             n_estimators=2500, n_jobs=5, num_parallel_tree=None,\n",
              "             predictor=None, random_state=None, ...)"
            ],
            "text/html": [
              "<style>#sk-container-id-2 {color: black;background-color: white;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-2\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>XGBRegressor(base_score=None, booster=None, callbacks=None,\n",
              "             colsample_bylevel=None, colsample_bynode=None,\n",
              "             colsample_bytree=None, early_stopping_rounds=None,\n",
              "             enable_categorical=False, eval_metric=None, feature_types=None,\n",
              "             gamma=None, gpu_id=None, grow_policy=None, importance_type=None,\n",
              "             interaction_constraints=None, learning_rate=0.5, max_bin=None,\n",
              "             max_cat_threshold=None, max_cat_to_onehot=None,\n",
              "             max_delta_step=None, max_depth=None, max_leaves=None,\n",
              "             min_child_weight=None, missing=nan, monotone_constraints=None,\n",
              "             n_estimators=2500, n_jobs=5, num_parallel_tree=None,\n",
              "             predictor=None, random_state=None, ...)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-2\" type=\"checkbox\" checked><label for=\"sk-estimator-id-2\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">XGBRegressor</label><div class=\"sk-toggleable__content\"><pre>XGBRegressor(base_score=None, booster=None, callbacks=None,\n",
              "             colsample_bylevel=None, colsample_bynode=None,\n",
              "             colsample_bytree=None, early_stopping_rounds=None,\n",
              "             enable_categorical=False, eval_metric=None, feature_types=None,\n",
              "             gamma=None, gpu_id=None, grow_policy=None, importance_type=None,\n",
              "             interaction_constraints=None, learning_rate=0.5, max_bin=None,\n",
              "             max_cat_threshold=None, max_cat_to_onehot=None,\n",
              "             max_delta_step=None, max_depth=None, max_leaves=None,\n",
              "             min_child_weight=None, missing=nan, monotone_constraints=None,\n",
              "             n_estimators=2500, n_jobs=5, num_parallel_tree=None,\n",
              "             predictor=None, random_state=None, ...)</pre></div></div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 72
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"XGB R^2 Score: \", xgb.score(X_train_scaled, y_train))\n",
        "print(\"XGB Test R^2 Score: \", xgb.score(X_test_scaled, y_test))"
      ],
      "metadata": {
        "id": "ilvpU4GGeDUe",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5be66692-66ad-468d-8d4c-048badb503cf"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "XGB R^2 Score:  0.7666132024008394\n",
            "XGB Test R^2 Score:  0.7778692455817243\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Interpret model predictions with Lime"
      ],
      "metadata": {
        "id": "P7jjVoI34b5U"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "pip install shap"
      ],
      "metadata": {
        "id": "ublEBDFcewaO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import shap"
      ],
      "metadata": {
        "id": "y_nBke5sbLwd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "explainer = shap.Explainer(xgb)\n",
        "shap_values = explainer(X_train_scaled)"
      ],
      "metadata": {
        "id": "YTebwXQflgDt"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "shap.plots.waterfall(shap_values[0])"
      ],
      "metadata": {
        "id": "tU4wNSlhmCDu"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "oSulEe-Lxt48"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}