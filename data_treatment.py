import pandas as pd
import csv

col_names = ['id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','zipcode','lat','long','sqft_living15','sqft_lot15','expensive']
col_cri_names = ['id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','zipcode','lat','long','sqft_living15','sqft_lot15']

dados_totais = pd.read_csv("D:/workspace/chatbot_pe/nossas_casas.csv",sep=',')
criterios = pd.read_csv("D:/workspace/chatbot_pe/criterios.csv",sep=",",header=0,names=col_cri_names)
print(criterios)

dados_interesse = dados_totais[col_names]
dados_interesse = dados_interesse.dropna()
print(dados_interesse)

for j in range(0,len(criterios)):
    id_criteria = int(criterios.iloc[j]["id"])
    date_criteria = int(criterios.iloc[j]["date"])
    price_criteria = int(criterios.iloc[j]["price"])
    bedrooms_criteria = int(criterios.iloc[j]["bedrooms"])
    bathrooms_criteria = int(criterios.iloc[j]["bathrooms"])
    sqft_living_criteria = int(criterios.iloc[j]["sqft_living"])
    sqft_lot_criteria = int(criterios.iloc[j]["sqft_lot"])
    floors_criteria = int(criterios.iloc[j]["floors"])
    waterfront_criteria = int(criterios.iloc[j]["waterfront"])
    view_criteria = int(criterios.iloc[j]["view"])
    condition_criteria = int(criterios.iloc[j]["condition"])
    grade_criteria = int(criterios.iloc[j]["grade"])
    sqft_above_criteria = int(criterios.iloc[j]["sqft_above"])
    sqft_basement_criteria = int(criterios.iloc[j]["sqft_basement"])
    yr_built_criteria = int(criterios.iloc[j]["yr_built"])
    yr_renovated_criteria = int(criterios.iloc[j]["yr_renovated"])
    zipcode_criteria = int(criterios.iloc[j]["zipcode"])
    lat_criteria = int(criterios.iloc[j]["lat"])
    long_criteria = int(criterios.iloc[j]["long"])
    sqft_living15_criteria = int(criterios.iloc[j]["sqft_living15"])
    sqft_lot15_criteria = int(criterios.iloc[j]["sqft_lot15"])



    treated_data = open(str("D:/workspace/chatbot_pe/nossas_casas_tratadas_"+str(j)+".csv"),"w")
    treated_data_writer = csv.writer(treated_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    treated_data_writer.writerow(col_names)
    row = []
    for i in range(0,len(dados_interesse)):
        if int(dados_interesse.iloc[i]["id"])<=id_criteria:
            row.append(1)
        else:
            row.append(0)
        
        year = dados_interesse.iloc[i]["date"]
        if int(year[:4])<=date_criteria:
            row.append(1)
        else:
            row.append(0)

        if int(dados_interesse.iloc[i]["price"]) <=price_criteria:
            row.append(1)
        else:
            row.append(0)

        if int(dados_interesse.iloc[i]["bedrooms"]) <=bedrooms_criteria:
            row.append(1)
        else:
            row.append(0)

        if int(dados_interesse.iloc[i]["bathrooms"]) <=bathrooms_criteria:
            row.append(1)
        else:
            row.append(0)

        if int(dados_interesse.iloc[i]["sqft_living"]) <=sqft_living_criteria:
            row.append(1)
        else:
            row.append(0)

        if int(dados_interesse.iloc[i]["sqft_lot"]) <=sqft_lot_criteria:
            row.append(1)
        else:
            row.append(0)

        if int(dados_interesse.iloc[i]["floors"]) <=floors_criteria:
            row.append(1)
        else:
            row.append(0)

        if int(dados_interesse.iloc[i]["waterfront"]) <=waterfront_criteria:
            row.append(1)
        else:
            row.append(0)

        if int(dados_interesse.iloc[i]["view"]) <=view_criteria:
            row.append(1)
        else:
            row.append(0)

        if int(dados_interesse.iloc[i]["condition"]) <=condition_criteria:
            row.append(1)
        else:
            row.append(0)

        if int(dados_interesse.iloc[i]["grade"]) <=grade_criteria:
            row.append(1)
        else:
            row.append(0)

        if int(dados_interesse.iloc[i]["sqft_above"]) <=sqft_above_criteria:
            row.append(1)
        else:
            row.append(0)

        if int(dados_interesse.iloc[i]["sqft_basement"]) <=sqft_basement_criteria:
            row.append(1)
        else:
            row.append(0)

        if int(dados_interesse.iloc[i]["yr_built"]) <=yr_built_criteria:
            row.append(1)
        else:
            row.append(0)

        if int(dados_interesse.iloc[i]["yr_renovated"]) <=yr_renovated_criteria:
            row.append(1)
        else:
            row.append(0)

        if int(dados_interesse.iloc[i]["zipcode"]) <=zipcode_criteria:
            row.append(1)
        else:
            row.append(0)
        
        if int(dados_interesse.iloc[i]["lat"]) <=lat_criteria:
            row.append(1)
        else:
            row.append(0)

        if int(dados_interesse.iloc[i]["long"]) <=long_criteria:
            row.append(1)
        else:
            row.append(0)

        if int(dados_interesse.iloc[i]["sqft_living15"]) <=sqft_living15_criteria:
            row.append(1)
        else:
            row.append(0)

        if int(dados_interesse.iloc[i]["sqft_lot15"]) <=sqft_lot15_criteria:
            row.append(1)
        else:
            row.append(0)

        if dados_interesse.iloc[i]["expensive"] == True:
            row.append(1)
        elif dados_interesse.iloc[i]["expensive"] == False:
            row.append(0)
        treated_data_writer.writerow(row)
        row = []
    treated_data.close()

