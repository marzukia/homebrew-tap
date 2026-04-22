from charted.charts.chart import Chart
from charted.html.element import Circle, G
from charted.utils.themes import Theme
from charted.utils.types import SeriesStyleConfig, Vector, Vector2D


class ScatterChart(Chart):
    def __init__(
        self,
        x_data: Vector | Vector2D,
        y_data: Vector | Vector2D,
        width: float = 500,
        height: float = 500,
        title: str | None = None,
        theme: Theme | None = None,
        series_names: list[str] | None = None,
        series_styles: list[SeriesStyleConfig] | None = None,
    ):
        super().__init__(
            y_data=y_data,
            x_data=x_data,
            width=width,
            height=height,
            title=title,
            theme=theme,
            series_names=series_names,
            chart_type="scatter",
            series_styles=series_styles,
        )

    @property
    def representation(self) -> G:
        g = G(
            opacity=0.8,
            transform=[*self.get_base_transform()],
        )
        for series_idx, (y_values, y_offsets, x_values, color) in enumerate(
            zip(self.y_values, self.y_offsets, self.x_values, self.colors),
        ):
            # Apply style overrides from series_styles
            fill = color
            marker_size = 4  # default
            if self.series_styles and series_idx < len(self.series_styles):
                style = self.series_styles[series_idx] or {}
                if style.get("fill"):
                    fill = style["fill"]
                if style.get("marker_size"):
                    marker_size = style["marker_size"]

            series = G(fill=fill)
            x_offset = self.x_offset

            for x, y, y_offset in zip(x_values, y_values, y_offsets):
                x += x_offset
                y = self._apply_stacking(y, y_offset)
                series.add_child(Circle(cx=x, cy=y, r=marker_size))
            g.add_children(series)

        return g
