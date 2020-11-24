
'''                                       Código referente a criação de um dashboard teste
                 para aplicação na estação eólica/solar da Universidade Federal da Paraíba - Júlia Alves Santos       '''





#---------------------------------------------------  bibliotecas necessárias   ---------------------------------------------------------#
import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import datetime
import matplotlib.pyplot as plt



#----------------------------------------------------------------------------------------------------------------------------------------#
#Funções para facilitar na construção do layout


# criando o cabeçalho 
def div_topo():
    return html.Div(children=[
        html.H2('Estação Eólica/Solar', style={'font-weight':'bold',}),

                html.H4('Universidade Federal da Paraíba- UFPB')
                ],
                style={
                    'textAlign':'center',
                    'font-weight':'bold',
                    }
    )
# criando um rodapé 
def div_base():
    return html.Div(children=[
           

               html.H6('''Desenvolvimento de sistema  SCADA para estação eólica/solar utilizando Python'''),
               html.H6(''' Júlia Alves Santos, Paraíba - 2020'''),

                ],
                style={
                    'textAlign':'center',
                    'font-weight':'bold',
                   }
    )

#Hora e data da atualização
def hora():
    return html.Div(children=[

            html.H6('''Estação Atualizada em:'''),
            html.H5( 
                datetime.datetime.now().strftime('%d/%m/%Y'),
                 style={
                     'opacity': '1',
                     'color': 'black', 
                     'fontSize': 20
                        }
                    ),

            html.H5( 
                datetime.datetime.now().strftime('%H:%M:%S'),
                 style={
                     'opacity': '1',
                     'color': 'black', 
                     'fontSize': 40
                        }
                    ),
                
                
                ],
                style={
                    'textAlign':'center',
                    'font-weight':'bold',
                    'color':'black'
                    }

        )

#Criando um display pra umidade e outro para pressão
def displays():
    return html.Div(children=[

    daq.LEDDisplay(
                    label="Umidade (%)",
                    value='60',
                    color="#111114"
                  ),

    daq.LEDDisplay(
                     label="Pressão Atmosférica (atm)",
                     value='0.99',
                    color="#111114"
                  )

        ]
    )

#Criando um gráfico para precipitação
def precipitacao():
    return html.Div(

        dcc.Graph(
                id='prec',
                figure = {   
                    'data':[
            
                            {
                            'x':['15/11','16/11','17/11','18/11'],
                            'y':[30,48,61,36],
                            'type': 'bar', 
                         
                                },
   
                        ],
                    'layout':{'title':'Precipitação'}
                    },

                 style={
                    'height':'200%',
                    "width": "90%",
                    'border-color': 'black',  
                    }
                 )
        )

# ----------------------------------------------------------------------------------------------------------------------------------------#

# adicionando um estilo externo

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# criando a aplicação por meio da função Dash do pacote dash e atribuindo a variável app

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets
)

# Um dicionário com as cores definidas
colors = {
    'background':'#F9FBFA ',
    'text':'#11111'
}

#dados do graifico de rosa dos ventos
df = px.data.wind()


#aplicação do layout
app.layout = html.Div([


#---------------------- ---------------------------------------------------------------------------------------------------------------#

    # Cabeçalho = Imagem + Título
    html.Div([

        #Imagem a direita
        html.Div([


         html.Img(src="/assets/UFPB.jpg", width='25%')
         
          ],

                className="three columns",
                style={
                'height':'100px',
                     }
            ),

        #Título
        html.Div([
                    div_topo(),],
                        className="six columns",
                        style={'height':'100px','border-color': 'black'}),

        #horário
        html.Div([
            
                 html.Img(src="/assets/CEAR2.png", width='75%')
                
                 ],
                className="three columns",
                style={'height':'100px','border-color': 'black'}
                ),

            ],   
                style={'height':'100px'}
                
                ),
#------------------------------------------------------------------------------------------------------------------------------------#

    html.Hr(),
    

    html.Div([

        # centro direito
        html.Div([
  
             hora()
                ],

                className='three columns', #  width: 30.6666666667%;
                style={
                    'height':'300px',
                    'border-color': 'black'
                    }
        ),

        # centro centro
        html.Div([

            daq.Gauge(
                    id='vel',
                    color= {
                        "gradient":True,
                        "ranges":{
                            "blue":[0,6],
                            "purple":[6,8],
                            "red":[8,10]
                        }
                    },
                    value=8,
                    label='Velocidade do Vento',
                    max=10,
                    min=0, 
                    scale={
                        'start': 1,
                        'interval': 1,
                        'labelInterval':1
                    },
                    showCurrentValue=True,
                    units="m/s",
                )
            ],
            className='three columns', #  width: 30.6666666667%;

            style={
                'height':'300px',
                'border-color': 'black'}
            ),

        # centro esquerda
        html.Div([

             daq.Thermometer(
                    id='left-top-graph',
                    value=25,
                    label='Temperatura Ambiente',
                    min=0,
                    max=45,
                    color= 'yellow',
                    scale={
                        'start': 0,
                        'interval': 5,
                        'labelInterval':1,
                    },
                    showCurrentValue=True,
                    units="C",
                )
            ],
            className='three columns', #  width: 30.6666666667%;
            style={
                'height':'300px',
                'border-color': 'black' 
                }
        ),

        html.Div([

            displays()
                ],

                className='three columns', #  width: 30.6666666667%;
                style={
                    'height':'300px',
                    'border-color': 'black'
                    }
                )
    
            ],
       style={'height':'300px'}),

    html.Hr(),


# seção que contém os gráficos
   html.Div([

        html.Div([

        #gráfico de radição
            dcc.Graph(
                id='rad',
                figure = {   
                    'data':[
                        #primeiro traço
                        {
                            'x':['8h','9h','10h','11h'],
                            'y':[731.5,880.6,981.0,1023.75],
                            'type': 'line',
                            'name':'GHI (W/m^2)',
                           
                        },
                        #segundo traço
                        {
                            'x':['8h','9h','10h','11h'],
                            'y':[612.45,753.25,848.95,889.9],
                            'type': 'line',
                            'name':'DNI (W/m^2)',
        

                        },
                        #terceiro traço
                        {
                            'x':['8h','9h','10h','11h'],
                            'y':[119.05,127.35,132.05,133.85],
                            'type': 'line',
                            'name':'DHI (W/m^2)',

                        },


                    ],
                    'layout':{'title':'Radiação Diária'}


                },

                style={
                    'height':'100%',
                    "width": "90%",
                    'border-color': 'black'},          
       
                )
            ],

            className='four columns', # width: 48%;
    
            ),


#gráfico de precitação centro
   html.Div([

        precipitacao()

    ],
    className='four columns',
    
    ),
    
     html.Div([

        dcc.Graph(
                id='rosa dos ventos',
              
                figure =px.density_heatmap(px.data.tips(), x="total_bill", y="tip"),
               

                style={
                    'height':'100%',
                    "width": "90%",
                    'border-color': 'black',
                  
                }
                
            )
        ],
    
        className='four columns', # width: 48%;
    ),


    ],
    
    style={'height':'300px'}
),
       
        
  
    
    
html.Hr(),

html.Div([
    #rodapé
    div_base()
    
        ]
    )
    
    
    ],
    #style={'backgroundColor':'black'}
)


if __name__ == '__main__':
    app.run_server(debug=True, port=8124)