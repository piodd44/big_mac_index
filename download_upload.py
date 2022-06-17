import AWS
import nasdaq
import pandas as pd

# wczytujemy liste kraj - kod
country_codes_df = pd.read_csv("economist_country_codes.csv")

# tworzymy liste nazw plików które chcemy pobrać
name_list = []
for value in country_codes_df.values:
    country, code = value[0].split("|")
    name_list.append("ECONOMIST/BIGMAC_" + code)

# pobieramy dane i zapisujemy do listy
data_list = nasdaq.download_many_data(name_list)

# zapisujemy dane na dysku
file_path_list = []
for data, name in zip(data_list, name_list):
    csv_data = data.to_csv("bigmac_data/" + name + ".csv")
    file_path_list.append("bigmac_data/" + name + ".csv")

# wysyłamy dane na S3 (uznałem że nazwa pliku na s3 taka sama jak na dysku)
for file_path in file_path_list:
    AWS.upload_file(file_path=file_path, folder_name="ZadanieRekrutacyjne")
