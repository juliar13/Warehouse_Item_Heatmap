import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import numpy as np
import pandas as pd

app = dash.Dash(__name__,
  meta_tags=[{"name": "viewport",
              "content": "width=device-width, initial-scale=1"}],
)

server = app.server

app.layout = html.Div(
  id = "app-container",
  children = [
    html.Div(
      id = "heatmap",
      children = [
        html.Div(
          id="output-heatmap",
          children=[
            html.B("volume"),
            html.Hr(),
            dcc.Graph(id="hm_volume"),
          ],
        ),
      ],
    ),
  ],
)

@app.callback(
  Output("hm_volume", "figure"),
  [Input("hm_volume", "clickData"),]
)
def update_heatmap(hm_vol):
  return generate_heatmap()


def generate_heatmap():

  df = pd.read_csv("sample.csv")
  item_list = df["Item Name"].unique()
  warehouse_list = df["Warehouse Name"].unique()

  x_axis = item_list
  y_axis = warehouse_list

  item_list_len = len(item_list)
  warehouse_list_len = len(warehouse_list)

  z = np.zeros((warehouse_list_len, item_list_len))
  annotations = []

  for i, y_val in enumerate(y_axis):
    filtered_df = df[df["Warehouse Name"] == y_val]
    for j, x_val in enumerate(x_axis):
      sum_of_record = filtered_df[filtered_df["Item Name"] == x_val]["Number of Records"].sum()
      z[i][j] = sum_of_record

      annotation_dict = dict(
        showarrow=False,
        text=str(sum_of_record),
        # xref="x",
        # yref="y",
        x=x_val,
        y=y_val,
        # font=dict(family="sans-serif"),
      )
      annotations.append(annotation_dict)

  data = [
    dict(
      x=x_axis,
      y=y_axis,
      z=z,
      type="heatmap",
      name="",
    )
  ]

  layout = dict(
    annotations=annotations,
    x_axis=dict(
      side="top",
    ),
    y_axis=dict(
      side="left",
    ),
  )

  return {"data": data, "layout": layout}

if __name__ == "__main__":
  app.run_server(debug=True)
