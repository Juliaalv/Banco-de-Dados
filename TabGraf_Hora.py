import matplotlib.pyplot as plt
import matplotlib as mpl
import sqlite3

import os
os.remove("temphora.db") if os.path.exists("temphora.db") else None
#criando uma conexão    
conn = sqlite3.connect('tempehora.db')

#criando um cursor
c = conn.cursor()

#Definindo uma função para criar a tabela
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS med (Hora TXT, Temp REAL)')

#Definindo uma função para inserir os dados
def data_insert():
    c.execute("INSERT INTO med (Hora,Temp) VALUES  ('06:05:36', 12),('09:00:50', 15),('13:08:32', 26),('15:07:47', 28),('18:00:23', 25),('20:04:31', 20),('22:00:35', 15),('00:03:45', 13),('03:07:09', 09),('06:00:50', 11)")
    conn.commit()
    
 #Definindo uma funçãoo para criar um gráfico       
def dados_grafico():
    c.execute("SELECT Hora, Temp FROM med")
    ids = []
    valores = []
    dados = c.fetchall()
    for linha in dados:
        ids.append(linha[0])
        valores.append(linha[1])
    #configurando o gráfico
    plt.title('CONTROLE DE TEMPERATURA')
    plt.xlabel('HORA') #definindo nome do eixo X
    plt.ylabel('TEMPERATURA') #definindo nome do eixo Y
    plt.bar(ids,valores, width=0.25,color='black') #definindo o tipo de gráfico,expussura e cor
   
    
    plt.show()
    
#Executando
create_table()
data_insert()
dados_grafico()

#Encerrando
c.close()
conn.close()

