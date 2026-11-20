# ChartData.ChartDataRow

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

One row of the chart’s data grid, holding its cells in column order.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ChartData.ChartDataRow
```

## Overview

A row isn’t necessarily a series: `plot_direction` decides whether rows or columns become the chart’s series. Rows need not be the same length, because the grid is padded out to its longest row.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.chart-data.chart-data-row`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `values` ([ChartData.ChartDataValue]) *(required)*: The row’s cells, in column order. Rows need not be the same length: a short row is padded with empty cells to the length of the longest row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chartdata.chartdatarow)*