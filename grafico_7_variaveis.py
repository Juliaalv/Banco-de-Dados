import pymysql
import pandas as pd
import matplotlib.pyplot as plt


#criando conexão com o servidor
con = pymysql.connect( host = 'localhost', user= 'root', passwd='',database='m1')
#criando o cursor
cr = con.cursor()
#criando o banco de dados
#cr.execute("CREATE DATABASE m1")

#Gravando os dados
#cr.execute('CREATE TABLE base  (dia REAL,mes REAL,ano REAL,hora REAL,minuto REAL,segundo REAL,temperatura REAL)')
#cr.execute('INSERT INTO base (dia,mes,ano,hora,minuto,segundo,temperatura) VALUES (01,10,2020,06,20,53,15),(02,10,2020,06,00,20,20),(03,10,2020,08,10,11,24),(04,10,2020,09,20,43,21),(05,10,2020,08,40,23,28)')
#con.commit()

#criando um Data Frame
query = 'select * from base'
df = pd.read_sql(query, con)

#criando variáveis com cada coluna
va1 = df.iloc[:,0]
va2 = df.iloc[:,1]
va3 = df.iloc[:,2]
va4 = df.iloc[:,3]
va5 = df.iloc[:,4]
va6 = df.iloc[:,5]
va7 = df.iloc[:,6]

#criando uma lista vazia para preencher com as seis primeiras variáveis
l1=[]
#for para selecionar as 6 variáveis em uma lista
for x,y,a,b,c,d in zip(va1,va2,va3,va4,va5,va6):
    z = str(int(x)) + "-"+ str(int(y)) + "-"+ str(int(a)) +" "+ "ás" + " "+ str(int(b))+ ":" +str(int(c))+ ":" + str(int(d))
    l1.append(z)
    
print(l1)

#criando o gráfico
plt.title('CONTROLE DE TEMPERATURA')
plt.bar(l1,df["temperatura"],width=0.25,color='black')
plt.xlabel('DATA') #definindo nome do eixo X
plt.ylabel('TEMPERATURA') #definindo nome do eixo Y
plt.show()

#encerrando a conexão
con.close()
cr.close()


