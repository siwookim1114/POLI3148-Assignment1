"""
05_dashboard_figures.py — build the three additional dashboard-quality figures
required by Deliverable C of the data-scientist brief.

Outputs:
  - docs/figs/fig_01b_monthly_animated.html  (animated time-series, year slider)
  - docs/figs/fig_05b_mali_animated.html     (animated geographic scatter, year slider)
  - docs/figs/fig_09_treemap.html            (treemap of event-type composition by country x phase)

Idioms taken from `data dashboard example/dashboard.py` (animated scatter,
animation_frame='year' pattern) and `poli3148 course materials/data
visualization/map_conflict_data_*.ipynb` (instructor's ACLED-mapping pattern).

Run:
    python3 code/05_dashboard_figures.py
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

HERE     = Path(__file__).resolve().parent
PROJECT  = HERE.parent
DATA     = PROJECT / "data"
FIGS     = PROJECT / "docs" / "figs"
FIGS.mkdir(parents=True, exist_ok=True)
STATS    = DATA / "final_stats.json"

aes = pd.read_parquet(DATA / "acled_clean.parquet")
fs  = json.loads(STATS.read_text())

AES_COUNTRIES = ["Mali", "Burkina Faso", "Niger"]
COUP_DATES = {
    "Mali":         pd.Timestamp(fs["mali_first_coup"]),
    "Burkina Faso": pd.Timestamp(fs["bf_first_coup"]),
    "Niger":        pd.Timestamp(fs["niger_first_coup"]),
}
WAGNER_DATES = {
    "Mali":         pd.Timestamp(fs["mali_wagner_arrival"]),
    "Burkina Faso": pd.Timestamp(fs["bf_wagner_arrival"]),
    "Niger":        pd.Timestamp(fs["niger_wagner_arrival"]),
}

# -----------------------------------------------------------------------------
# Figure 01b — animated monthly events by country, year slider
# -----------------------------------------------------------------------------
def build_animated_monthly() -> None:
    monthly = (aes.groupby(["country", "year_month"], as_index=False)
                  .agg(events=("event_id_cnty", "count"),
                       fatalities=("fatalities", "sum")))
    monthly["year"] = monthly["year_month"].dt.year
    monthly["month_label"] = monthly["year_month"].dt.strftime("%b %Y")

    # Cumulative within-year events per (country, year): one bar per month, animated by year
    fig = px.bar(
        monthly,
        x="year_month", y="events", color="country",
        animation_frame="year",
        category_orders={"country": AES_COUNTRIES},
        color_discrete_sequence=["#1B2A4A", "#8B0000", "#2E86AB"],
        labels={"events": "events / month", "year_month": "month"},
        hover_data={"fatalities": ":,", "country": False, "year": False, "year_month": False},
        title="Figure 1b — Monthly conflict events by country (year-by-year, animated)",
    )
    fig.update_traces(
        hovertemplate="<b>%{x|%b %Y}</b><br>events = %{y:,}<br>fatalities = %{customdata[0]:,}<extra></extra>",
    )
    fig.update_layout(
        height=540,
        margin=dict(t=80, l=30, r=20, b=40),
        paper_bgcolor="#FFFFFF", plot_bgcolor="#F4F6F9",
        font=dict(family="Segoe UI, system-ui, sans-serif", size=11),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        bargap=0.05,
    )
    fig.update_xaxes(title_text="month")
    fig.update_yaxes(title_text="events / month")

    # Frame-specific annotations: coup + Wagner vlines for each country, persisted across frames
    # (Plotly's known persistence bug — replicate the dashboard.py idiom of attaching annotations
    #  to every frame so the lines do not disappear during animation.)
    if fig.frames:
        for frame in fig.frames:
            frame_year = int(frame.name) if str(frame.name).isdigit() else None
            shapes = []
            annotations = []
            for c in AES_COUNTRIES:
                cd, wd = COUP_DATES[c], WAGNER_DATES[c]
                if frame_year is None or cd.year == frame_year:
                    shapes.append(dict(type="line", x0=cd, x1=cd, y0=0, y1=1,
                                        yref="paper", line=dict(color="#8B0000", dash="dash", width=1.4)))
                if frame_year is None or wd.year == frame_year:
                    shapes.append(dict(type="line", x0=wd, x1=wd, y0=0, y1=1,
                                        yref="paper", line=dict(color="#2E86AB", dash="dash", width=1.4)))
            frame.layout = go.Layout(shapes=shapes, annotations=annotations)

    fig.write_html(FIGS / "fig_01b_monthly_animated.html",
                   include_plotlyjs="cdn", full_html=True)
    print("saved fig_01b_monthly_animated.html")


# -----------------------------------------------------------------------------
# Figure 05b — animated geographic scatter, civilian-targeted Mali events, year slider
# -----------------------------------------------------------------------------
def build_animated_geo_mali() -> None:
    mali = aes[(aes.country == "Mali") & aes.civilian_targeted].copy()
    mali["year"] = mali["event_date"].dt.year
    # Marker size = log1p(fatalities)
    mali["marker_size"] = np.log1p(mali["fatalities"].clip(lower=0)) + 1.0

    # Use scatter_geo (course-aligned: map_conflict_data_1.ipynb / generate_dashboard.py)
    fig = px.scatter_geo(
        mali,
        lat="latitude", lon="longitude",
        color="actor1_role",
        size="marker_size",
        size_max=22,
        animation_frame="year",
        hover_name="admin1",
        hover_data={
            "event_date": True,
            "actor1": True,
            "fatalities": ":,",
            "admin2": True,
            "marker_size": False,
            "year": False,
        },
        color_discrete_sequence=px.colors.qualitative.Set2,
        opacity=0.75,
        title="Figure 5b — Mali civilian-targeted events by year, sized by fatalities, coloured by perpetrator role",
    )
    fig.update_traces(
        marker=dict(line=dict(width=0.15, color="#FFFFFF")),
        selector=dict(type="scattergeo"),
    )
    fig.update_geos(
        showcountries=True, countrycolor="#A5A5A5",
        showcoastlines=True, coastlinecolor="#A5A5A5",
        showocean=True, oceancolor="#FFFFFF",
        showland=True, landcolor="#F7F7F7",
        showframe=False, bgcolor="#FFFFFF",
        fitbounds="locations",
    )
    fig.update_layout(
        height=620, margin=dict(t=80, l=10, r=10, b=20),
        paper_bgcolor="#FFFFFF",
        font=dict(family="Segoe UI, system-ui, sans-serif", size=11),
        legend=dict(title="actor1_role", orientation="v",
                    yanchor="top", y=0.98, xanchor="left", x=1.02),
    )
    fig.write_html(FIGS / "fig_05b_mali_animated.html",
                   include_plotlyjs="cdn", full_html=True)
    print("saved fig_05b_mali_animated.html")


# -----------------------------------------------------------------------------
# Figure 09 — treemap of event-type composition, country × phase
# -----------------------------------------------------------------------------
def build_treemap() -> None:
    df = aes.copy()
    df["phase"] = np.where(df.post_russian_arrival, "post-Wagner", "pre-Wagner")
    agg = (df.groupby(["phase", "country", "event_type", "sub_event_type"], as_index=False)
             .agg(events=("event_id_cnty", "count"),
                  fatalities=("fatalities", "sum")))

    fig = px.treemap(
        agg,
        path=[px.Constant("AES core"), "phase", "country", "event_type", "sub_event_type"],
        values="events",
        color="fatalities",
        color_continuous_scale="YlOrRd",
        title="Figure 9 — Event-type composition by country and Wagner phase (size = events; colour = fatalities)",
    )
    fig.update_traces(
        hovertemplate="<b>%{label}</b><br>events = %{value:,}<br>fatalities = %{color:,.0f}<extra></extra>",
        root_color="#1B2A4A",
    )
    fig.update_layout(
        height=620, margin=dict(t=80, l=10, r=10, b=10),
        paper_bgcolor="#FFFFFF",
        font=dict(family="Segoe UI, system-ui, sans-serif", size=11),
    )
    fig.write_html(FIGS / "fig_09_treemap.html",
                   include_plotlyjs="cdn", full_html=True)
    print("saved fig_09_treemap.html")


if __name__ == "__main__":
    build_animated_monthly()
    build_animated_geo_mali()
    build_treemap()
    print("all dashboard figures built.")
