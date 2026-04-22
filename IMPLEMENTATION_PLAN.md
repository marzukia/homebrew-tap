# Column Chart Side-by-Side Regression Fix — Implementation Plan

## Problem
Commit `b65f769` refactored `ColumnChart` to support `y_stacked` as a runtime parameter, but broke side-by-side rendering:
- Bars for all series overlap vertically instead of being placed side-by-side
- SVG output shows 19 paths instead of 12 (4 quarters × 3 series)
- X-positioning logic doesn't center the bar group within its slot

## Root Cause
In `charted/charts/column.py`, the non-stacked branch (lines 65-77) calculates `bar_x` incorrectly:

```python
slot_x = self.x_offset + x_idx * (self.x_width + self.column_gap * self.x_width)
bar_x = slot_x + series_idx * series_width
```

This places bars sequentially without centering. The old code (commit 84a2718) used:

```python
bar_width = self.x_width / num_series
series_offset = (bar_width * (num_series - 1)) / 2
bar_x = x - series_offset + series_idx * bar_width
```

This centers the group of bars within the slot by offsetting the first bar left by half the group width.

## Fix Plan

### Step 1: Restore correct side-by-side positioning
Replace lines 65-77 in `charted/charts/column.py` with the old centering logic:

```python
else:
    # side-by-side mode
    num_series = len(self.y_values)
    bar_width = self.x_width / num_series if num_series > 0 else self.x_width
    series_offset = (bar_width * (num_series - 1)) / 2 if num_series > 0 else 0

    for series_idx in range(num_series):
        y_values = self.y_values[series_idx]
        x_values = self.x_values[series_idx]
        color = (
            self.colors[series_idx]
            if series_idx < len(self.colors)
            else self.colors[series_idx % len(self.colors)]
        )

        paths = []
        for x_idx, (x, y) in enumerate(zip(x_values, y_values)):
            x += self.x_offset
            # center bar within its slot, offset from group center
            bar_x = x - series_offset + series_idx * bar_width
            paths.append(
                Path.get_path(
                    bar_x, min(0, y), bar_width, max(y, 0) - min(0, y)
                )
            )
        g.add_child(Path(d=paths, fill=color))
```

### Step 2: Regenerate baseline SVGs
```bash
cd /home/andryo/git/charted
python3 -c "
from charted.charts.column import ColumnChart
import os

# Regenerate column_sidebyside.svg
data = [[45, 52, 38, 61], [38, 46, 55, 49], [55, 48, 42, 58]]
labels = ['Q1', 'Q2', 'Q3', 'Q4']
chart = ColumnChart(
    data=data,
    labels=labels,
    y_stacked=False,
    title='Sales Performance by Region',
    width=700,
    height=400
)
with open('docs/examples/column_sidebyside.svg', 'w') as f:
    f.write(chart.html)
"
```

### Step 3: Verify fix
```bash
cd /home/andryo/git/charted
# Check that bars are at different x positions
python3 -c "
import re
with open('docs/examples/column_sidebyside.svg') as f:
    html = f.read()
paths = re.findall(r'M([0-9.]+) [0-9.]+ h([0-9.]+)', html)
x_positions = sorted(set(round(float(p[0]), 2) for p in paths))
print(f'Unique x positions: {x_positions}')
print(f'Expected ~12 unique positions (4 quarters × 3 series with slight overlap in grouping)')
"

# Run existing tests
python3 -m pytest tests/charts/test_column.py -v
```

### Step 4: Commit
```bash
git add charted/charts/column.py docs/examples/column_sidebyside.svg
git commit -m "fix: restore correct side-by-side column positioning"
```

## Adversarial Review

### Potential Issues

1. **Stacked mode regression**: The fix only touches the non-stacked branch. Stacked mode uses `y_offsets` which is computed in the base `Chart` class. Need to verify stacked mode still works.

2. **Negative values**: The old code used `min(0, y)` and `max(y, 0) - min(0, y)` to handle negative values. The new code (before fix) used `zero_y` from `self.y_axis.zero`. Need to verify both approaches handle negatives correctly.

3. **`y_offsets` unused in side-by-side mode**: The `y_offsets` field is computed unconditionally in `Chart.__init__` but ignored in side-by-side mode. This is fine but wasteful. Could be optimized later.

4. **Test coverage**: Current tests only check that SVG contains `<path>`, not that bars are positioned correctly. Should add integration tests that verify x-coordinates.

### Verification Steps

1. Compare regenerated `column_sidebyside.svg` with baseline from commit 84a2718
2. Test with negative values: `ColumnChart(data=[[-10, -20], [15, 25]], labels=['a', 'b'], y_stacked=False)`
3. Test stacked mode: `ColumnChart(data=[[10, 20], [15, 25]], labels=['a', 'b'], y_stacked=True)`
4. Test single series: `ColumnChart(data=[10, 20, 30], labels=['a', 'b', 'c'], y_stacked=False)`

### Rollback Plan

If fix breaks stacked mode:
```bash
git checkout 84a2718 -- charted/charts/column.py
git checkout 84a2718 -- docs/examples/
```

Then re-apply only the side-by-side fix, keeping stacked mode changes.
