# ChartData

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The chart’s data as a grid of cells, together with how that grid maps onto the chart.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ChartData
```

## Overview

`plot_direction` decides whether the grid’s rows or its columns become the series; the labels along the other direction name the categories.

## Topics

### Objects
- [object ChartData.ChartDataRow](./chartdata.chartdatarow.md)
  One row of the chart’s data grid, holding its cells in column order.
### Enumerations
- [type ChartData.ChartDataSource](./chartdata.chartdatasource.md)
  The stated source of a chart’s values.
- [type ChartData.ChartDataValue](./chartdata.chartdatavalue.md)
  A single value in the chart’s data grid.
- [type ChartData.PlotDirection](./chartdata.plotdirection.md)
  The direction in which the data grid is read to produce the chart’s series.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.chart-data`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `plot_direction` (ChartData.PlotDirection): Whether the rows or the columns of the data grid become the chart’s series. When omitted, the direction preferred by the chart type is kept.
- `shared_xvalues` (boolean): Whether the grid’s first row or column holds the X values every series shares. It’s `true` by default; when `false`, each series carries its own X values. Y values, and a bubble series’ size values, follow in either case. Only scatter and bubble charts use it; other chart types ignore it.

  **Default**: `true`
- `chart_data_source` (ChartData.ChartDataSource) *(required)*: The source of the chart’s data. Only `chart_data_grid` is supported: that is the value always written, and any other value is ignored, so the grid in `rows` is used either way.
- `column_labels` ([string]): The names of the grid’s columns. The number of columns comes from the longest row of `rows`, so extra names are dropped and missing names become empty.
- `row_labels` ([string]): The names of the grid’s rows. The number of rows comes from `rows`, so extra names are dropped and missing names become empty.
- `rows` ([ChartData.ChartDataRow]): The grid’s data rows. The grid is made rectangular: it takes the length of the longest row, and shorter rows are padded with empty cells. When `rows` is empty or omitted, the chart keeps the placeholder data it was created with.

## See Also

### Charts
- [type Chart](./chart.md)
  An object that plots a grid of data in a visual style such as column, pie, or scatter.
- [type ChartAxisCommon](./chartaxiscommon.md)
  The properties every chart axis shares, flattened into both the category axis and the value axis.
- [type ChartCommon](./chartcommon.md)
  The properties shared by every kind of chart.
- [type ChartLabelFormatting](./chartlabelformatting.md)
  The formatting of a chart element’s numeric labels.
- [object ChartCategoryAxis](./chartcategoryaxis.md)
  The axis along which a chart’s categories are laid out, on the chart types that have one.
- [object ChartLegend](./chartlegend.md)
  The legend of a chart.
- [object ChartSeries](./chartseries.md)
  The appearance and label formatting of one of a chart’s data series.
- [object ChartValueAxis](./chartvalueaxis.md)
  A numeric axis that a chart’s values are measured against.
- [object AreaChart](./areachart.md)
  A 2D area chart.
- [object Area3DChart](./area3dchart.md)
  A 3D area chart.
- [object StackedAreaChart](./stackedareachart.md)
  A 2D stacked area chart.
- [object StackedArea3DChart](./stackedarea3dchart.md)
  A 3D stacked area chart.
- [object BarChart](./barchart.md)
  A 2D bar chart.
- [object Bar3DChart](./bar3dchart.md)
  A 3D horizontal bar chart.
- [object BarInteractiveChart](./barinteractivechart.md)
  An interactive horizontal bar chart, which shows one data set at a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chartdata)*