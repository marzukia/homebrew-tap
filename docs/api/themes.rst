Themes API
==========

charted includes a comprehensive theme system with 10 built-in themes and full custom theme support.

Built-in Themes
---------------

The following themes are available out of the box:

- ``"default"`` — Clean, professional default with neutral grays and vibrant accents
- ``"dark"`` — Dark background with high-contrast light colors
- ``"pastel"`` — Soft, muted pastel colors for gentle visuals
- ``"vibrant"`` — Bold, saturated colors for eye-catching charts
- ``"minimal"`` — Ultra-clean with minimal decoration
- ``"corporate"`` — Professional business colors (blues, grays)
- ``"nature"`` — Earth tones and natural greens
- ``"monochrome"`` — Black/white/gray only
- ``"warm"`` — Warm color palette (oranges, reds, yellows)
- ``"cool"`` — Cool color palette (blues, purples, teals)

Using Themes
------------

Apply themes by name or dictionary:

.. code-block:: python

   from charted import BarChart

   # Use built-in theme by name
   chart = BarChart(
       data=[120, 180, 210],
       labels=["Q1", "Q2", "Q3"],
       theme="dark"
   )

   # Override specific properties
   chart = BarChart(
       data=[120, 180, 210],
       labels=["Q1", "Q2", "Q3"],
       theme={
           "colors": {
               "palette": ["#FF6B6B", "#4ECDC4", "#45B7D1"]
           }
       }
   )

   # Merge built-in with custom overrides
   chart = BarChart(
       data=[120, 180, 210],
       labels=["Q1", "Q2", "Q3"],
       theme="pastel"  # Start with pastel theme
   )
   chart.apply_theme({
       "title": {
           "font_size": 24,
           "font_weight": "bold"
       }
   })

Theme Dictionary Structure
--------------------------

Complete theme configuration dictionary:

.. code-block:: python

   {
       # Title configuration
       "title": {
           "text": str,              # Title text
           "font_family": str,       # Font family (default: "Arial")
           "font_size": int,         # Font size in pixels (default: 18)
           "font_weight": str,       # "normal", "bold", "lighter" (default: "bold")
           "color": str,             # Text color (default: "#333333")
           "alignment": str,         # "left", "center", "right" (default: "center")
       },

       # Subtitle configuration
       "subtitle": {
           "text": str,              # Subtitle text
           "font_family": str,
           "font_size": int,         # Default: 14
           "font_weight": str,       # Default: "normal"
           "color": str,             # Default: "#666666"
           "alignment": str,
       },

       # Axis configuration
       "axis": {
           "line_color": str,        # Axis line color (default: "#CCCCCC")
           "line_width": float,      # Line width (default: 1.0)
           "tick_color": str,        # Tick mark color (default: "#CCCCCC")
           "tick_length": float,     # Tick length in pixels (default: 5.0)
           "tick_width": float,      # Tick width (default: 1.0)
           "show_grid": bool,        # Show grid lines (default: True)
           "grid_color": str,        # Grid line color (default: "#EEEEEE")
           "grid_width": float,      # Grid line width (default: 0.5)
           "grid_style": str,        # "solid", "dashed", "dotted" (default: "solid")
       },

       # Label configuration
       "label": {
           "font_family": str,       # Font family (default: "Arial")
           "font_size": int,         # Font size (default: 12)
           "font_weight": str,       # Font weight (default: "normal")
           "color": str,             # Text color (default: "#666666")
           "rotation": float,        # Rotation angle in degrees (default: 0)
           "alignment": str,         # "auto", "left", "center", "right" (default: "auto")
       },

       # Legend configuration
       "legend": {
           "show": bool,             # Show legend (default: True)
           "position": str,          # "top", "bottom", "left", "right" (default: "top")
           "font_family": str,
           "font_size": int,         # Default: 12
           "font_weight": str,       # Default: "normal"
           "color": str,             # Default: "#333333"
           "background_color": str,  # Default: "transparent"
           "border_color": str,      # Default: "transparent"
           "border_width": float,    # Default: 0
           "spacing": float,         # Item spacing (default: 15)
       },

       # Colors configuration
       "colors": {
           "palette": list,          # List of hex colors for data series
           "negative_color": str,    # Color for negative values (default: "#FF6B6B")
           "zero_color": str,        # Color for zero values (default: "#95A5A6")
       },

       # Padding configuration
       "padding": {
           "v_padding": float,       # Vertical padding ratio (default: 0.1)
           "h_padding": float,       # Horizontal padding ratio (default: 0.1)
       },

       # Bar-specific configuration
       "bar": {
           "gap": float,             # Gap between bars (default: 0.2)
           "group_gap": float,       # Gap between groups (default: 0.3)
           "border_color": str,      # Bar border color (default: same as fill)
           "border_width": float,    # Bar border width (default: 0)
       },

       # Column-specific configuration
       "column": {
           "gap": float,             # Gap between columns (default: 0.2)
           "group_gap": float,       # Gap between column groups (default: 0.3)
           "border_color": str,
           "border_width": float,
       },

       # Line-specific configuration
       "line": {
           "width": float,           # Line width (default: 2.0)
           "style": str,             # "solid", "dashed", "dotted" (default: "solid")
           "marker": str,            # "circle", "square", "diamond", "none" (default: "circle")
           "marker_size": float,     # Marker size (default: 4.0)
           "marker_border_width": float,  # Marker border width (default: 1.0)
           "smooth": bool,           # Smooth curves (default: False)
       },

       # Scatter-specific configuration
       "scatter": {
           "marker": str,            # "circle", "square", "diamond" (default: "circle")
           "marker_size": float,     # Marker size (default: 6.0)
           "marker_border_width": float,
           "marker_border_color": str,
       },

       # Pie-specific configuration
       "pie": {
           "inner_radius": float,    # For doughnut mode (default: 0)
           "outer_radius": float,    # Outer radius ratio (default: 0.8)
           "label_position": str,    # "inside", "outside", "auto" (default: "auto")
           "label_line_color": str,  # Default: "#CCCCCC"
           "label_line_width": float, # Default: 1.0
           "explode": float,         # Default explode amount (default: 0)
           "border_color": str,      # Slice border color (default: "#FFFFFF")
           "border_width": float,    # Slice border width (default: 2.0)
       },

       # Font configuration
       "font": {
           "family": str,            # Default font family (default: "Arial")
           "size": int,              # Default font size (default: 12)
           "weight": str,            # Default font weight (default: "normal")
       },
   }

Creating Custom Themes
----------------------

Create custom themes by extending built-in themes:

.. code-block:: python

   from charted import BarChart

   # Start with a built-in theme and override
   custom_theme = {
       "colors": {
           "palette": ["#FF6B6B", "#4ECDC4", "#45B7D1", "#FFA07A"]
       },
       "title": {
           "font_size": 24,
           "font_weight": "bold",
           "color": "#2C3E50"
       },
       "axis": {
           "show_grid": False
       }
   }

   chart = BarChart(
       data=[120, 180, 210],
       labels=["Q1", "Q2", "Q3"],
       theme=custom_theme
   )

Theme Validation
----------------

charted validates theme dictionaries and provides helpful errors for invalid values:

- Color values must be valid hex colors (e.g., "#FF6B6B")
- Numeric values must be within acceptable ranges
- String values must be from allowed options (e.g., alignment: "left"/"center"/"right")

Invalid themes will raise a ``ValueError`` with details about what went wrong.

Debugging Themes
----------------

To inspect the final theme applied to a chart:

.. code-block:: python

   chart = BarChart(data=[120, 180], labels=["A", "B"], theme="dark")
   print(chart.theme)  # Shows the complete merged theme dictionary

Best Practices
--------------

1. **Start with built-in themes** — Use ``"default"``, ``"dark"``, ``"pastel"`` as a base
2. **Override minimally** — Change only what you need, don't redefine the entire theme
3. **Maintain contrast** — Ensure text is readable against backgrounds
4. **Consistent palettes** — Use 4-8 colors in your palette for multi-series charts
5. **Test dark/light modes** — If supporting both, test readability in each
