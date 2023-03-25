import random

import dash
from dash import dcc, html, Input, Output, State
import plotly
import plotly.graph_objects as go


app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
)


def gen_plotly_figure():
    avail_vals = list(range(20))
    x_arr = []
    y_arr = []
    for x in avail_vals:
        for y in avail_vals:
            plot_pts = random.random() > 0.6
            if plot_pts:
                x_arr.append(x)
                y_arr.append(y)

    my_figure = go.Figure(
        data=[
            go.Scatter(
                x=x_arr,
                y=y_arr,
                mode="markers",
                marker=dict(color="#1C1D42"),
                hoverinfo="none",
            ),
        ],
        layout={
            "height": 600,
            "width": 600,
            "plot_bgcolor": "#fafafa",
            "paper_bgcolor": "#fafafa",
            "xaxis": {
                "color": "#f3f3f3",
                "tickfont": {
                    "color": "#666666",
                },
                "gridcolor": "#f3f3f3",
            },
            "yaxis": {
                "color": "#f3f3f3",
                "tickfont": {
                    "color": "#666666",
                },
                "gridcolor": "#f3f3f3",
            },
        },
    )
    return my_figure


graph = dcc.Graph(
    id="my-figure", className="my-figure", figure=gen_plotly_figure()
)

tooltip = dcc.Tooltip(
    id="my-tooltip",
    className="my-tooltip",
    loading_text="",
)


def layout():
    return html.Div(
        [
            graph,
            tooltip,
        ]
    )


app.layout = layout


@app.callback(
    Output("my-tooltip", "bbox"),
    Output("my-tooltip", "children"),
    Input("my-figure", "hoverData"),
)
def update_tooltip(hoverData):
    if not hoverData:
        return dash.no_update, dash.no_update

    pt = hoverData["points"][0]
    bbox = pt["bbox"]

    tooltip_content = html.Div(
        [
            html.P(f"X: {pt['x']}"),
            html.P(f"Y: {pt['y']}"),
        ]
    )
    return bbox, tooltip_content


if __name__ == "__main__":
    app.run_server(debug=True)
