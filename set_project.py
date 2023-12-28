import user_data
import mysql.connector

###create database if not exists
mydb = mysql.connector.connect(
    host='localhost',
    user=user_data.user,
    password=user_data.password
)

cursor = mydb.cursor()

sql = "create database if not exists proj_ws;"
cursor.execute(sql)
mydb.commit()

mydb.database='proj_ws'
cursor = mydb.cursor()

###create table if not exists
sql = "create table if not exists n(nome varchar(50) not null, sigla varchar(10) not null,primary key (sigla))default charset = utf8mb4;"
cursor.execute(sql)
mydb.commit()

sql = "create table if not exists p(id int not null auto_increment,sigla varchar(10) not null,dia date,preco decimal(5,2),primary key (id))default charset = utf8mb4;"
cursor.execute(sql)
mydb.commit()