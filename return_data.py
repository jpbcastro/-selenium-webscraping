import user_data
import pandas as pd
import mysql.connector
import warnings
warnings.filterwarnings("ignore")

mydb = mysql.connector.connect(
    host='localhost',
    user=user_data.user,
    password=user_data.password,
    database='proj_ws'
)

query = "select distinct sigla from p;"
df_x = pd.read_sql(query,mydb)
name = list(df_x['sigla'])

query = "select distinct dia from p;"
df_x = pd.read_sql(query,mydb)
data = list(df_x['dia'])

df = pd.DataFrame(columns=['sigla']+data)

for acao in name:
    query = "select preco from p where sigla='{acao}';".format(acao = acao)
    df_x = pd.read_sql(query,mydb)
    preco = list(df_x['preco'])
    df.loc[len(df)] = [acao]+preco

df = df.set_index('sigla')
mydb.close()

print(df)