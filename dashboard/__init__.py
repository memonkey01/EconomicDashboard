import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('/var/www/FlaskApp/FlaskApp/data.csv')

colors = {'bg':'#000000'}

app = dash.Dash()

app.layout = html.Div([
						html.Div([
							html.H2('Analisis de Portafolios',
					                style={'display': 'inline',
					                       'float': 'right',
					                       'font-size': '2.65em',
					                       'margin-left': '7px',
					                       'font-weight': 'bolder',
					                       'font-family': 'Product Sans',
					                       'color': 'black',
					                       'margin-top': '20px',
					                       'margin-right': '50px',
					                       'margin-bottom': '0'
					                       }
					                       ),
					        html.Img(src="https:www.quantconsulting.com.mx/Quant_Consulting.png",
					                style={
					                    'height': '90px',
					                    'margin-top': '20px',
					                    'margin-left': '50px'
					                    #'float': 'right'
					                },
					        )]),


						dcc.Graph(id = 'Precios de Acciones',
							figure={'data': [
											go.Scatter(x = df['Date'],
													   y = df['Adj Close'],
													   mode = 'lines'
												)],
									'layout':go.Layout(
										title = 'Valor del IPC',
										xaxis = {'title':'Dia'},
										yaxis = {'title':'Valor'},
										plot_bgcolor= colors['bg']
									)
									})
						])




server = app.server

if __name__ == '__main__':
	app.run_server(debug=True)
