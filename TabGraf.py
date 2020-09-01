import matplotlib.pyplot as plt
import matplotlib as mpl
import sqlite3

import os
os.remove("temperatura.db") if os.path.exists("temperatura.db") else None
#criando uma conexão
conn = sqlite3.connect('temperatura.db')

#criando um cursor
c = conn.cursor()

#Definindo uma função para criar a tabela
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS est (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Data TXT, Temp REAL)')

#Definindo uma função para inserir os dados
def data_insert():
    c.execute("INSERT INTO est (data,Temp) VALUES  ('2020-07-01', 28),('2020-07-02', 20),('2020-07-03', 25),('2020-07-04', 18),('2020-07-05', 12),('2020-07-06', 9),('2020-07-07', 16),('2020-07-08', 21),('2020-07-09', 27),('2020-07-10', 32)")
    conn.commit()
    
 #Definindo uma funçãoo para criar um gráfico       
def dados_grafico():
    c.execute("SELECT Data, Temp FROM est")
    ids = []
    valores = []
    dados = c.fetchall()
    for linha in dados:
        ids.append(linha[0])
        valores.append(linha[1])
    #configurando o gráfico
    plt.title('CONTROLE DE TEMPERATURA')
    plt.xlabel('DATA') #definindo nome do eixo X
    plt.ylabel('TEMPERATURA') #definindo nome do eixo Y
    plt.bar(ids,valores, width=0.25,color='red') #definindo o tipo de gráfico,expussura e cor
   
    
    plt.show()
    
#Executando
create_table()
data_insert()
dados_grafico()

#Encerrando
c.close()
conn.close()

