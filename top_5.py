import pandas as pd

country_codes_df = pd.read_csv("economist_country_codes.csv")

name_list = []
for value in country_codes_df.values:
    country, code = value[0].split("|")
    name_list.append("bigmac_data/ECONOMIST/BIGMAC_" + code + ".csv")

date_to_check = "2020-07-31"

date_list = [pd.read_csv(name) for name in name_list]

mac_index_list = []
code_list = []
for data, name in zip(date_list, name_list):
    to_show = data[data["Date"] == date_to_check]
    code = name.split("/")[-1].split("_")[-1]
    code_list.append(code)
    if len(to_show['dollar_ppp'].values) > 0:
        mac_index_list.append(to_show['dollar_ppp'].values[0])
    else:
        mac_index_list.append(-1)

df_country_index = pd.DataFrame(columns=["code", "big_mac_index"], data=zip(code_list, mac_index_list))
df_country_index = df_country_index.sort_values(by="big_mac_index", ascending=False)

print(df_country_index.head(5))
