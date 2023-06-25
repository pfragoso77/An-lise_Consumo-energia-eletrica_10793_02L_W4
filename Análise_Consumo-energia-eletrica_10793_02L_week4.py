"""
Created on Sun Jun 25 17:12:13 2023

@author: Pedro
"""
# Importação da biblioteca Pandas para a realização de uma análise de dados
import pandas as pd
# tarefa 1 > importar dados da tabela Excel 
dados_analise = pd.read_excel('P_Data_Extract_From_World_Development_Indicators.xlsx', sheet_name='Data')
#print(dados_analise)

# tarefa 2 > limpeza de dados
dados_analise = dados_analise[['Country Name', 'Country Code', '1990 [YR1990]', '2000 [YR2000]']]
print(dados_analise)