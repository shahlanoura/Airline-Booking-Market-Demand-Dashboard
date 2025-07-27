from flask import Flask, render_template, request
import pandas as pd
from utils import fetch_flight_data, get_top_countries, get_summary_chart

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    df = fetch_flight_data()
    countries = df['origin_country'].dropna().unique()
    selected = request.form.get("country") or "Australia"

    filtered_df = df[df['origin_country'] == selected]
    top_countries = get_top_countries(df)
    chart_div = get_summary_chart(filtered_df)

    return render_template(
        "index.html",
        total=len(df),
        countries=sorted(countries),
        selected=selected,
        top_routes=top_countries.to_dict(),
        chart_div=chart_div
    )

if __name__ == "__main__":
    app.run(debug=True)
