import dash
from dash import html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings

# Load CSV data
df = pd.read_csv('cleaned_data.csv', sep='|')

# Create a scatter_geo plot
fig = px.scatter_geo(
    df,
    lat='latitude',
    lon='longitude',
    projection='natural earth',  # Choose a map projection
    title='Geographic Scatter Plot',
    template='plotly',
)

# Increase the size of the figure
fig.update_layout(height=600, width=800)  # Adjust the height and width as needed

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Global Research Insights Hub"),  # Add the header here
    dcc.Graph(figure=fig)
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
