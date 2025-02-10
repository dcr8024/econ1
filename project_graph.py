import pandas as pd
import plotly.graph_objects as go

# Read the CSV file
df = pd.read_csv('mishkin_transformed_data.csv')

# Convert date string to datetime
df['observation_date'] = pd.to_datetime(df['observation_date'])

# Create figure
fig = go.Figure()

# Add traces
fig.add_trace(
    go.Scatter(
        x=df['observation_date'],
        y=df['Real_GDP_Growth'],
        name="Real GDP Growth Rate",
        line=dict(color='blue')
    )
)

fig.add_trace(
    go.Scatter(
        x=df['observation_date'],
        y=df['Real_M1_Growth'],
        name="Real M1 Growth Rate",
        line=dict(color='red')
    )
)

# Update layout with fixed y-axis range
fig.update_layout(
    title='Real GDP Growth Rate vs Real M1 Growth Rate (1982-Present)',
    xaxis_title='Time',
    yaxis_title='Growth Rate (%)',
    template='plotly_white',
    hovermode='x unified',
    width=1000,
    height=600,
    yaxis=dict(
        range=[-5, 5],  # Set y-axis range from -5 to 5
        showgrid=True,
        gridwidth=1,
        gridcolor='LightGray'
    ),
    xaxis=dict(
        showgrid=True,
        gridwidth=1,
        gridcolor='LightGray'
    )
)

# Customize x-axis
fig.update_xaxes(
    tickangle=45,
    tickformat="%Y-%m",
    tickmode='auto',
    nticks=20
)

# Save the figure as HTML
fig.write_html("growth_rates_scaled.html")

# Show figure
fig.show()
