# DashLeaflet

DashLeaflet is a Dash component library.

The code is primarily written by [chschoenenberger](https://github.com/chschoenenberger). 

## Installation

To get started run the following code to install the package

```bash
pip install git+https://github.com/elben10/dash_leaflet
```

## Working example

Create a file named `app.py` with the following content

```python
import dash_leaflet
import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

app.layout = html.Div(
    [
        dash_leaflet.DashLeaflet(
            baselayer=[
                {
                    "name": "LAYER 1 abc",
                    "url": "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                    "attribution": '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
                }
            ],
            markers=[{"geom": [[0,0], [0.1, 0]], "cluster": True, "title": "HELLO"}]
        )
    ],
    style={"width": "90vw", "height": "100vh"},
)


if __name__ == "__main__":
    app.run_server(debug=True)
```

Run the following command `python app.py` in the directory where you have put your `app.py` file.

Go to http://localhost:8050.