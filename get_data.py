import user_data
import pandas as pd
import mysql.connector
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import warnings
warnings.filterwarnings("ignore")

### web scraping
options=Options()
options.add_argument("-headless")
options.profile = FirefoxProfile()
driver = webdriver.Firefox(options=options)
driver.get('https://valorinveste.globo.com/cotacoes/')

elements = driver.find_elements(By.XPATH, "/html/body/main/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/table/tbody/tr")

nome=[]
sigla=[]
data=[]
preco=[]

for acao in elements:
    dados = acao.find_elements(By.TAG_NAME, 'td')
    if dados[4].text!='-':
        nome.append(dados[0].text)
        sigla.append(dados[1].text)
        data.append(date.today())
        preco.append(dados[4].text.replace(',','.'))

driver.quit()

dic_name = {'nome':nome, 'sigla':sigla}
dic_price = {'sigla':sigla, 'data':data, 'preco':preco}
df_n = pd.DataFrame(dic_name)
df_p = pd.DataFrame(dic_price)

### connect to mysql database
mydb = mysql.connector.connect(
    host='localhost',
    user=user_data.user,
    password=user_data.password,
    database='proj_ws'
)

cursor = mydb.cursor()

### save new names on database
for index, row in df_n.iterrows():
    sql = "insert into n values (%s, %s) ON DUPLICATE KEY UPDATE nome = %s, sigla = %s;"
    val = (row['nome'], row['sigla'], row['nome'], row['sigla'])
    cursor.execute(sql, val)
    mydb.commit()

### save new prices on database
query = "select distinct dia from p;"
df_x = pd.read_sql(query,mydb)
data = list(df_x['dia'])

if date.today() not in data:    ###colect just once a day
    for index, row in df_p.iterrows():
        sql = "INSERT INTO  p (sigla, dia, preco) VALUES (%s, %s, %s)"
        val = (row['sigla'], row['data'], row['preco'])
        cursor.execute(sql, val)
        mydb.commit()

print('done')