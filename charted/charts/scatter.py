from charted.charts.chart import Chart
from charted.html.element import Circle, G, Path, Rect
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
            marker_shape = "circle"  # default
            if self.series_styles and series_idx < len(self.series_styles):
                style = self.series_styles[series_idx] or {}
                if style.get("fill"):
                    fill = style["fill"]
                if style.get("marker_size"):
                    marker_size = style["marker_size"]
                if style.get("marker_shape"):
                    marker_shape = style["marker_shape"]

            series = G(fill=fill)
            x_offset = self.x_offset

            for x, y, y_offset in zip(x_values, y_values, y_offsets):
                x += x_offset
                y = self._apply_stacking(y, y_offset)
                # Render marker based on shape
                if marker_shape == "square":
                    half = marker_size / 2
                    series.add_child(
                        Rect(
                            x=x - half,
                            y=y - half,
                            width=marker_size,
                            height=marker_size,
                        )
                    )
                elif marker_shape == "diamond":
                    points_str = (
                        f"{x},{y - marker_size} "
                        f"{x + marker_size},{y} "
                        f"{x},{y + marker_size} "
                        f"{x - marker_size},{y}"
                    )
                    series.add_child(Path(d=f"M{points_str} Z", fill=fill))
                elif marker_shape != "none":  # circle
                    series.add_child(Circle(cx=x, cy=y, r=marker_size))
            g.add_children(series)

        return g
