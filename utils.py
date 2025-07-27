import requests
import pandas as pd
import plotly.express as px

def fetch_flight_data():
    url = "https://opensky-network.org/api/states/all"
    res = requests.get(url)
    data = res.json()
    flights = data.get('states', [])

    df = pd.DataFrame(flights, columns=[
        "icao24", "callsign", "origin_country", "time_position", "last_contact",
        "longitude", "latitude", "baro_altitude", "on_ground", "velocity",
        "true_track", "vertical_rate", "sensors", "geo_altitude", "squawk",
        "spi", "position_source"
    ])
    return df.dropna(subset=["origin_country", "longitude", "latitude"])

def get_top_countries(df):
    return df["origin_country"].value_counts().head(10)

def get_summary_chart(df):
    if df.empty:
        return "<p>No data available for this country.</p>"
    fig = px.scatter_geo(df, lat="latitude", lon="longitude", color="velocity",
                         title="Flight Positions and Speed", projection="natural earth")
    return fig.to_html(full_html=False)
