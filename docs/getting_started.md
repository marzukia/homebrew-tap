# Getting Started with Charted

A 5-minute guide to creating beautiful SVG charts with zero dependencies.

## Installation

```bash
pip install charted
```

## Quick Start

Create your first chart in under 30 seconds:

```python
from charted import BarChart

# Simple bar chart
chart = BarChart(data=[120, 180, 210], labels=["Q1", "Q2", "Q3"])
chart.save("sales.svg")
```

That's it! You now have a `sales.svg` file ready to use in presentations, websites, or documentation.

## Chart Types

Charted supports 5 chart types:

- **BarChart** - Horizontal bars (comparing categories)
- **ColumnChart** - Vertical bars (time series, distributions)
- **LineChart** - Line graphs (trends over time)
- **ScatterChart** - Scatter plots (correlations, distributions)
- **PieChart** - Pie/doughnut charts (proportions)

## Basic Usage

### Single Series

```python
from charted import BarChart, ColumnChart, LineChart, PieChart

# Bar chart
bar = BarChart(
    data=[120, 180, 210, 150],
    labels=["Q1", "Q2", "Q3", "Q4"],
    title="Sales by Quarter"
)
bar.save("bar.svg")

# Column chart
column = ColumnChart(
    data=[120, 180, 210, 150],
    labels=["Q1", "Q2", "Q3", "Q4"],
    title="Sales by Quarter"
)
column.save("column.svg")

# Line chart
line = LineChart(
    data=[120, 180, 210, 150],
    labels=["Q1", "Q2", "Q3", "Q4"],
    title="Sales Trend"
)
line.save("line.svg")

# Pie chart
pie = PieChart(
    data=[120, 180, 210, 150],
    labels=["Q1", "Q2", "Q3", "Q4"],
    title="Sales Distribution"
)
pie.save("pie.svg")
```

### Multi-Series

```python
from charted import BarChart, ColumnChart

# Multiple data series
data = [
    [120, 180, 210, 150],  # 2023
    [130, 190, 220, 160],  # 2024
]

bar = BarChart(
    data=data,
    labels=["Q1", "Q2", "Q3", "Q4"],
    title="Sales Comparison",
    series_names=["2023", "2024"]
)
bar.save("multi_bar.svg")

column = ColumnChart(
    data=data,
    labels=["Q1", "Q2", "Q3", "Q4"],
    title="Sales Comparison",
    series_names=["2023", "2024"]
)
column.save("multi_column.svg")
```

### Stacked Charts

```python
from charted import BarChart, ColumnChart

# Stacked bar chart
stacked_bar = BarChart(
    data=[[30, 50, 40], [90, 130, 170]],
    labels=["Q1", "Q2", "Q3"],
    title="Sales by Region",
    series_names=["North", "South"],
    x_stacked=True
)
stacked_bar.save("stacked_bar.svg")

# Stacked column chart
stacked_column = ColumnChart(
    data=[[30, 50, 40], [90, 130, 170]],
    labels=["Q1", "Q2", "Q3"],
    title="Sales by Region",
    series_names=["North", "South"],
    y_stacked=True
)
stacked_column.save("stacked_column.svg")
```

## Loading Data from Files

### CSV/TSV Files

```python
from charted import BarChart, load_csv

# Load data from CSV
x, y, labels = load_csv("sales.csv", x_col="Quarter", y_col="Revenue")

# Create chart
chart = BarChart(data=y, labels=x, title=labels[0])
chart.save("sales.svg")
```

**CSV Format Example:**
```csv
Quarter,Revenue
Q1,120
Q2,180
Q3,210
Q4,150
```

### JSON Files

```python
from charted import BarChart, load_json

# Load data from JSON
x, y, labels = load_json("sales.json")

# Create chart
chart = BarChart(data=y, labels=x, title=labels[0])
chart.save("sales.svg")
```

**JSON Format Examples:**

Simple array:
```json
[120, 180, 210, 150]
```

Array of objects:
```json
[
  {"label": "Q1", "value": 120},
  {"label": "Q2", "value": 180},
  {"label": "Q3", "value": 210},
  {"label": "Q4", "value": 150}
]
```

Object with data and labels:
```json
{
  "data": [120, 180, 210, 150],
  "labels": ["Q1", "Q2", "Q3", "Q4"],
  "title": "Sales by Quarter"
}
```

## Jupyter Notebook Integration

Charts display inline automatically:

```python
from charted import BarChart

# In Jupyter, this renders inline
chart = BarChart(
    data=[120, 180, 210, 150],
    labels=["Q1", "Q2", "Q3", "Q4"],
    title="Sales by Quarter"
)
chart  # Last expression renders the chart
```

## Markdown Integration

Embed charts in documentation:

```python
from charted import BarChart, chart_to_markdown

# Create and save chart
chart = BarChart(data=[120, 180, 210], labels=["Q1", "Q2", "Q3"])
chart.save("docs/examples/sales.svg")

# Generate markdown
md = chart_to_markdown("docs/examples/sales.svg", title="Sales Chart", width="600px")
print(md)
# Output: ![Sales Chart](docs/examples/sales.svg){width=600px}
```

Or use data URLs for inline embedding:

```python
from charted import BarChart, chart_to_data_url

# Generate data URL
url = chart_to_data_url("chart.svg")
md = f"![chart]({url})"
```

### Using Chart Methods

The new `Chart` class methods provide a more convenient API:

```python
from charted import BarChart

# Create chart
chart = BarChart(data=[120, 180, 210], labels=["Q1", "Q2", "Q3"], title="Sales")

# Get markdown with data URL (inline embedding)
md = chart.to_markdown()
print(md)
# Output: ![Sales](data:image/svg+xml,{encoded_svg})

# Get markdown with file path
chart.save("docs/examples/sales.svg")
md = chart.to_markdown(path="docs/examples/sales.svg")
print(md)
# Output: ![Sales](docs/examples/sales.svg)

# Get raw SVG
svg = chart.to_svg()
print(svg[:50])
# Output: <svg xmlns="http://www.w3.org/2000/svg" ...

# HTML representation (for Jupyter/web frameworks)
html = chart._repr_html_()
```


## Customization

### Themes

```python
from charted import BarChart
from charted.utils.themes import Theme

# Use built-in theme
chart = BarChart(
    data=[120, 180, 210],
    labels=["Q1", "Q2", "Q3"],
    theme=Theme.DARK  # or Theme.LIGHT, Theme.COLORFUL
)
chart.save("dark_theme.svg")

# Custom theme
custom_theme = Theme(
    background_color="#ffffff",
    text_color="#333333",
    grid_color="#eeeeee",
    primary_color="#3498db",
    secondary_color="#2ecc71"
)
chart = BarChart(
    data=[120, 180, 210],
    labels=["Q1", "Q2", "Q3"],
    theme=custom_theme
)
chart.save("custom_theme.svg")
```

### Dimensions

```python
from charted import BarChart

# Custom size
chart = BarChart(
    data=[120, 180, 210],
    labels=["Q1", "Q2", "Q3"],
    width=800,
    height=400
)
chart.save("wide_chart.svg")
```

### Colors

```python
from charted import BarChart

# Custom colors
chart = BarChart(
    data=[120, 180, 210],
    labels=["Q1", "Q2", "Q3"],
    theme=Theme(
        primary_color="#e74c3c",
        secondary_color="#f39c12"
    )
)
chart.save("custom_colors.svg")
```

## CLI Usage

Charted also has a command-line interface:

```bash
# Create a single chart
charted create bar --data 120,180,210 --labels Q1,Q2,Q3 --title "Sales" --output sales.svg

# Batch generate charts
charted batch config.toml
```

**CLI Example:**
```bash
# Bar chart
charted create bar \
  --data 120,180,210,150 \
  --labels Q1,Q2,Q3,Q4 \
  --title "Quarterly Sales" \
  --width 800 \
  --height 400 \
  --output sales.svg

# Column chart (stacked)
charted create column \
  --data 30,50,40 \
  --data 90,130,170 \
  --labels Q1,Q2,Q3 \
  --series-names North,South \
  --stacked \
  --output stacked.svg
```

## Next Steps

- **API Reference** - Complete documentation for all chart classes
- **Themes** - Learn about theme customization
- **CLI Guide** - Command-line usage examples
- **Examples** - See real-world chart configurations

## Common Patterns

### Percentages (Pie Chart)

```python
from charted import PieChart

# Proportions that sum to 100%
pie = PieChart(
    data=[40, 35, 15, 10],
    labels=["Product A", "Product B", "Product C", "Product D"],
    title="Market Share"
)
pie.save("market_share.svg")
```

### Time Series (Line Chart)

```python
from charted import LineChart

# Time-based data
line = LineChart(
    data=[120, 135, 150, 165, 180, 195],
    labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    title="Monthly Growth"
)
line.save("growth.svg")
```

### Comparison (Column Chart)

```python
from charted import ColumnChart

# Side-by-side comparison
data = [
    [120, 180, 210],  # 2023
    [130, 190, 220],  # 2024
]

column = ColumnChart(
    data=data,
    labels=["Q1", "Q2", "Q3"],
    title="Year-over-Year Comparison",
    series_names=["2023", "2024"]
)
column.save("comparison.svg")
```

## Troubleshooting

### No data error

```python
# ❌ Wrong - empty data
chart = BarChart(data=[], labels=[])

# ✅ Right - provide data
chart = BarChart(data=[1, 2, 3], labels=["A", "B", "C"])
```

### Invalid CSV columns

```python
# ❌ Wrong - column doesn't exist
x, y, labels = load_csv("data.csv", x_col="quarter", y_col="revenue")

# ✅ Right - use exact column names
x, y, labels = load_csv("data.csv", x_col="Quarter", y_col="Revenue")
```

### Chart doesn't display in Jupyter

```python
# ✅ Make sure charted is installed
pip install charted

# ✅ Use the chart object as the last line
chart = BarChart(data=[1, 2, 3], labels=["A", "B", "C"])
chart  # This renders inline
```

## Support

- **Documentation**: https://charted.readthedocs.io
- **GitHub**: https://github.com/peepecat/charted
- **Issues**: https://github.com/peepecat/charted/issues
