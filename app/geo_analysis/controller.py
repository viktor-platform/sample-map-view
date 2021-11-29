"""Copyright (c) 2021 VIKTOR B.V.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

VIKTOR PROVIDES THIS SOFTWARE ON AN "AS IS" BASIS, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from viktor.core import ViktorController
from viktor.views import MapPoint, MapResult, MapView, DataResult, DataItem, DataGroup, DataView
from viktor.views import Summary, MapPolyline, MapPolygon
from .parametrization import ExampleParametrisation
from munch import Munch


class ExampleController(ViktorController):
    """Controller class which acts as interface for the GeoAnalysis entity type.

    Connects the Parametrization (left-side of web UI), with the Views (right-side of web UI.
    """
    label = 'Analysis'
    summary = Summary()
    parametrization = ExampleParametrisation

    @MapView('Map view', duration_guess=1)  # in seconds, if it is larger or equal to 3, the "update" button will appear
    def get_map_view(self, params: Munch, **kwargs) -> MapResult:
        features = []

        if params.location.point:
            marker = params.location.point
            features.append(MapPoint.from_geo_point(marker))

        if params.location.line:
            marker = params.location.line
            features.append(MapPolyline.from_geo_polyline(marker))

        if params.location.polygon:
            marker = params.location.polygon
            features.append(MapPolygon.from_geo_polygon(marker))

        return MapResult(features)
