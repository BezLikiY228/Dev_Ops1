import dash
from dash import dcc, html
import plotly.express as px

app = dash.Dash(__name__)

df = px.data.gapminder()
fig = px.scatter(df, x="gdpPercap", y="lifeExp", color="continent", size="pop", hover_name="country")

app.layout = html.Div(children=[
    html.H1(children='Простой дэшборд'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
