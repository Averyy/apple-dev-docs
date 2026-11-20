# Chart.two_axis

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A two-axis chart.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Chart.two_axis
```

## Overview

This type of chart plots each series against either the primary or the secondary value axis; for more information about axes, see `ChartSeries.y_axis_selection`. Each series can appear as columns, as a line, or as an area. For more information, see `ChartSeries.mixed_series_type`.

Written as `{"two_axis": …}`: the `two_axis` form of `Chart`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.chart`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `two_axis` (TwoAxisChart) *(required)*: A two-axis chart. This type of chart plots each series against either the primary or the secondary value axis; for more information about axes, see `ChartSeries.y_axis_selection`. Each series can appear as columns, as a line, or as an area. For more information, see `ChartSeries.mixed_series_type`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chart/two_axis)*