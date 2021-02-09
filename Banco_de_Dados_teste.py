

'''        Código referente ao desenvolvimento de um banco de dados teste 
    para simular a estação eólica/solar da Universidade Federal da Paraíba - Júlia Alves Santos       '''
 

#Bibliotecas Necessárias

import pymysql
import numpy as np
import random
import time

#criando conexão com o servidor
con = pymysql.connect( host = 'localhost', user= 'root', passwd='', database='comunicacao')


#função para criação da tabela
def create_table():
    
    #criando o cursor
    cr = con.cursor()
    cr.execute('CREATE TABLE IF NOT EXISTS tab2teste(Temperatura REAL, Velocidade REAL,Precipitação REAL)')
    con.commit()
    print ('Tabela criada na base de dados')
    cr.close()
    
#criando a tabela
create_table()

#função para gerar dados aletórios de temperatura
def inserir():
   
    for i in range(0,1):
        t = 10*np.random.rand()+10
        t = np.random.randint(23,29)
       
    return (t)

#função para gerar dados aletórios de velocidade
def inserirv():
    for i in range(0,1):
        v = 10*np.random.rand()+10
        v = np.random.randint(2,14)
      
    return (v)


#função para gerar dados aletórios de precipitação
def inserirp():
    for i in range(0,1):
        p = 10*np.random.rand()+10
        p = np.random.randint(30,100)
      
    return (p)

#função para inserir os dados na tabela
def data_entry():

    c = con.cursor()
    va1 = inserir()
    va2= inserirv()
    va3= inserirp()
    print(va1)
    print(va2)
    print(va3)
    # Inserção dos dados
    c.execute('INSERT INTO tab2teste(Temperatura,Velocidade,Precipitação) VALUES (%s,%s,%s)',(va1, va2, va3))
    con.commit()
    print ('Base de dados  atualizada')
    #fechar acesso
    c.close()



# Loop de update de base de dados
i=1
while True:
    # Atualiza banco de dados
    data_entry()
    print(i)
    # Tempo de amostragem
    time.sleep(2)
    if i == 2:
        break
    else:
        i+=1

print ('Base de dados  desconectada')





