Charts API
==========

This is the complete API reference for all chart types in charted.

Base Chart Class
----------------

.. autoclass:: charted.Chart
   :members:
   :undoc-members:
   :show-inheritance:

   The base ``Chart`` class provides a unified interface for creating any chart type dynamically.

Column Chart
------------

.. autoclass:: charted.ColumnChart
   :members:
   :undoc-members:
   :show-inheritance:

   Vertical bar chart with support for multi-series, stacked layouts, and side-by-side grouping.

   **Key Parameters:**

   - ``data`` — List of lists for multi-series, or single list for one series
   - ``labels`` — X-axis labels
   - ``series_names`` — Names for each data series (used in legend)
   - ``y_stacked`` — If True, stack bars vertically (default for multi-series)
   - ``theme`` — Theme dictionary or theme name string

   **Example:**

   .. code-block:: python

      from charted import ColumnChart

      chart = ColumnChart(
          data=[[120, 180, 210], [80, 95, 110]],
          labels=["Q1", "Q2", "Q3"],
          series_names=["Revenue", "Expenses"],
          title="Quarterly Performance"
      )
      chart.save("column.svg")

Bar Chart
---------

.. autoclass:: charted.BarChart
   :members:
   :undoc-members:
   :show-inheritance:

   Horizontal bar chart with support for single/multi-series and various layouts.

   **Key Parameters:**

   - ``data`` — Single list or list of lists for multi-series
   - ``labels`` — Y-axis labels
   - ``x_stacked`` — If True, stack bars horizontally
   - ``theme`` — Theme dictionary or theme name string

   **Example:**

   .. code-block:: python

      from charted import BarChart

      chart = BarChart(
          data=[120, 180, 210],
          labels=["Q1", "Q2", "Q3"],
          title="Sales by Quarter"
      )
      chart.save("bar.svg")

Line Chart
----------

.. autoclass:: charted.LineChart
   :members:
   :undoc-members:
   :show-inheritance:

   Line chart with support for multi-series and XY mode.

   **Key Parameters:**

   - ``data`` — List of lists for multi-series
   - ``labels`` — X-axis labels (or ``x_data`` for XY mode)
   - ``x_data`` — Custom X-axis values for XY mode
   - ``theme`` — Theme dictionary or theme name string

   **Example:**

   .. code-block:: python

      from charted import LineChart

      chart = LineChart(
          data=[[120, 180, 210], [80, 95, 110]],
          labels=["Q1", "Q2", "Q3"],
          series_names=["Revenue", "Expenses"],
          title="Trend Line"
      )
      chart.save("line.svg")

Scatter Chart
-------------

.. autoclass:: charted.ScatterChart
   :members:
   :undoc-members:
   :show-inheritance:

   Scatter plot with marker customization.

   **Key Parameters:**

   - ``data`` — List of [x, y] pairs or list of lists for multi-series
   - ``labels`` — Series names
   - ``marker_shape`` — "circle", "square", or "diamond"
   - ``theme`` — Theme dictionary or theme name string

   **Example:**

   .. code-block:: python

      from charted import ScatterChart

      chart = ScatterChart(
          data=[[1, 2], [2, 3], [3, 5], [4, 4]],
          labels=["Series 1"],
          marker_shape="square",
          title="Scatter Plot"
      )
      chart.save("scatter.svg")

Pie Chart
---------

.. autoclass:: charted.PieChart
   :members:
   :undoc-members:
   :show-inheritance:

   Pie chart with doughnut mode and per-slice styling.

   **Key Parameters:**

   - ``data`` — Single list of values
   - ``labels`` — Slice labels
   - ``series_names`` — Legend name
   - ``doughnut`` — If True, render as doughnut chart
   - ``inner_radius`` — Inner radius for doughnut mode (0.3-0.7)
   - ``slice_styles`` — Per-slice customization (colors, explosion, labels)
   - ``theme`` — Theme dictionary or theme name string

   **Example:**

   .. code-block:: python

      from charted import PieChart

      chart = PieChart(
          data=[300, 150, 100, 50],
          labels=["Product A", "Product B", "Product C", "Product D"],
          series_names=["Sales"],
          title="Market Share"
      )
      chart.save("pie.svg")

   **Doughnut Mode:**

   .. code-block:: python

      chart = PieChart(
          data=[300, 150, 100],
          labels=["A", "B", "C"],
          doughnut=True,
          inner_radius=0.5
      )

   **Per-Slice Styling:**

   .. code-block:: python

      chart = PieChart(
          data=[300, 150, 100],
          labels=["A", "B", "C"],
          slice_styles={
              0: {"color": "#FF6B6B", "explode": 0.1},
              1: {"color": "#4ECDC4"},
              2: {"color": "#45B7D1", "label_position": "outside"}
          }
      )

Common Methods
--------------

All chart types share these methods:

.. py:method:: to_svg()

   Generate the SVG string representation of the chart.

.. py:method:: save(filepath)

   Save the chart to a file. Supports .svg extension.

.. py:method:: to_markdown(path=None)

   Generate markdown embedding. If path is provided, uses image reference. Otherwise returns inline data URL.

.. py:method:: _repr_html_()

   IPython/Jupyter integration — returns HTML with inline SVG.

Data Loading API
----------------

.. autofunction:: charted.load_csv

   Load data from a CSV file.

   **Parameters:**

   - ``filepath`` — Path to CSV file
   - ``x_col`` — Column name for X-axis/labels
   - ``y_cols`` — Column name(s) for Y-axis data
   - ``delimiter`` — CSV delimiter (default: ",")

   **Returns:** Tuple of (x_values, y_values, column_names)

.. autofunction:: charted.load_json

   Load data from a JSON file. Auto-detects format based on JSON structure.

   **Parameters:**

   - ``filepath`` — Path to JSON file

   **Returns:** Tuple of (x_values, y_values, column_names)

   **Supported JSON Formats:**

   .. code-block:: json

      // Simple array
      [120, 180, 210]

      // Array of objects
      [{"label": "Q1", "value": 120}, {"label": "Q2", "value": 180}]

      // Object with data and labels
      {"data": [120, 180, 210], "labels": ["Q1", "Q2", "Q3"], "title": "Sales"}

CLI API
-------

charted includes a command-line interface for generating charts without writing Python code.

.. code-block:: bash

   # Create a single chart
   python -m charted create <chart_type> <output.svg> --data <input.csv|json>

   # Batch process
   python -m charted batch <input_dir> <output_dir>

Theme API
---------

.. autofunction:: charted.get_theme

   Get a built-in theme by name or return a custom theme dictionary.

   **Parameters:**

   - ``theme_name`` — Theme name string or theme dictionary

   **Returns:** Theme dictionary with chart styling

Built-in themes: ``"dark"``, ``"light"``, ``"high-contrast"``, ``"blue"``, ``"green"``, ``"purple"``, ``"orange"``, ``"red"``, ``"pastel"``, ``"vibrant"``.
