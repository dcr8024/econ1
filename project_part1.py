import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Read the data
df = pd.read_csv('mishkin_transformed_data.csv')
df['observation_date'] = pd.to_datetime(df['observation_date'])

# Create two separate figures
fig1 = go.Figure()
fig2 = go.Figure()

# Plot 1: Real GDP Growth
fig1.add_trace(
    go.Scatter(
        x=df['observation_date'],
        y=df['Real_GDP_Growth'],
        name="Real GDP Growth Rate",
        line=dict(color='blue')
    )
)

# Update layout for GDP plot
fig1.update_layout(
    title='Real GDP Growth Rate (1982-Present)',
    xaxis_title='Time',
    yaxis_title='Growth Rate (%)',
    template='plotly_white',
    width=1000,
    height=500,
    yaxis=dict(
        range=[-5, 5],
        showgrid=True,
        gridwidth=1,
        gridcolor='LightGray'
    ),
    showlegend=True
)

# Plot 2: Real M1 Growth
fig2.add_trace(
    go.Scatter(
        x=df['observation_date'],
        y=df['Real_M1_Growth'],
        name="Real M1 Growth Rate",
        line=dict(color='red')
    )
)

# Update layout for M1 plot
fig2.update_layout(
    title='Real M1 Growth Rate (1982-Present)',
    xaxis_title='Time',
    yaxis_title='Growth Rate (%)',
    template='plotly_white',
    width=1000,
    height=500,
    yaxis=dict(
        range=[-5, 5],
        showgrid=True,
        gridwidth=1,
        gridcolor='LightGray'
    ),
    showlegend=True
)

# Add COVID-19 annotation to M1 plot
fig2.add_annotation(
    x=pd.Timestamp('2020-07-01'),
    y=4.5,
    text="COVID-19 Emergency<br>M1 Growth: 247.25%",
    showarrow=True,
    arrowhead=1,
    ax=0,
    ay=-40
)

# Customize x-axes for both plots
for fig in [fig1, fig2]:
    fig.update_xaxes(
        tickangle=45,
        tickformat="%Y-%m",
        tickmode='auto',
        nticks=20
    )

# Save the figures as HTML
fig1.write_html("gdp_growth_rate.html")
fig2.write_html("m1_growth_rate.html")

# Show figures
fig1.show()
fig2.show()
