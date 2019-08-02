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
                },
                {
                    "name": "LAYER 2",
                    "url": "https://tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png",
                    "attribution": "hejsa",
                },
                {
                    "name": "layer 3",
                    "url": "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
                    "attribution": "HELASF",
                },
            ],
            markers=[{"geom": [[0, 0], [0.1, 0]], "cluster": False, "title": "HELLO", "popup": "hej"}],
            circleMarkers=[{"geom": [[0, 0], [0.1, 0]], "cluster": False, "title": "HELLO1", "popup": ["eh", "ofa"]}],
            mapOptions={"center": [0, 0], "minZoom": 0, "maxZoom": 17},
        )
    ],
    style={"width": "90vw", "height": "100vh"},
)


if __name__ == "__main__":
    app.run_server(debug=True)
