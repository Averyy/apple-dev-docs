# Chart

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

An object that plots a grid of data in a visual style such as column, pie, or scatter.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(Chart.area | Chart.area_3d | Chart.bar | Chart.bar_3d | Chart.bar_interactive | Chart.bubble | Chart.bubble_interactive | Chart.column | Chart.column_3d | Chart.column_interactive | Chart.donut | Chart.line | Chart.line_3d | Chart.mixed | Chart.pie | Chart.pie_3d | Chart.radar | Chart.scatter | Chart.scatter_interactive | Chart.stacked_area | Chart.stacked_area_3d | Chart.stacked_bar | Chart.stacked_bar_3d | Chart.stacked_column | Chart.stacked_column_3d | Chart.two_axis) Chart
```



**Allowed Types**: `Chart.area`, `Chart.area_3d`, `Chart.bar`, `Chart.bar_3d`, `Chart.bar_interactive`, `Chart.bubble`, `Chart.bubble_interactive`, `Chart.column`, `Chart.column_3d`, `Chart.column_interactive`, `Chart.donut`, `Chart.line`, `Chart.line_3d`, `Chart.mixed`, `Chart.pie`, `Chart.pie_3d`, `Chart.radar`, `Chart.scatter`, `Chart.scatter_interactive`, `Chart.stacked_area`, `Chart.stacked_area_3d`, `Chart.stacked_bar`, `Chart.stacked_bar_3d`, `Chart.stacked_column`, `Chart.stacked_column_3d`, `Chart.two_axis`

## Discussion

Write a chart as an object with a single key, which names its chart type, such as `column` or `pie`, and holds that type’s settings. The chart type decides only how Keynote plots the series: every chart type uses the same chart data, so when you change a chart’s type, that change replots the existing series without rewriting the data.

This type includes the properties of `CanvasObject`, as does every other type that adopts it.

This value takes one of the following forms:

- `area`: A line chart with the region between the line and the axis filled, one region for each series.
- `area_3d`: A 3D area chart.
- `bar`: Values as horizontal bars, one bar for each series within each category.
- `bar_3d`: A 3D bar chart.
- `bar_interactive`: An interactive bar chart, which shows one data set at a time.
- `bubble`: A scatter chart whose third value sets the area of each point.
- `bubble_interactive`: An interactive bubble chart, which shows one data set at a time.
- `column`: Values as vertical bars, one bar for each series within each category.
- `column_3d`: A 3D column chart.
- `column_interactive`: An interactive column chart, which shows one data set at a time.
- `donut`: A pie chart that appears as a ring with an open center.
- `line`: Values as points joined by a line, with one line for each series.
- `line_3d`: A 3D line chart.
- `mixed`: A mixed chart. Each series can appear as columns, as a line, or as an area. For more information on mixed charts, see `ChartSeries.mixed_series_type`.
- `pie`: One series as wedges of a circle, with each wedge sized by its share of the total.
- `pie_3d`: A 3D pie chart.
- `radar`: Categories that appear around a circle, with each series appearing as a closed outline through its values.
- `scatter`: Each series appears as a plot of pairs of X and Y values against two value axes, rather than against categories.
- `scatter_interactive`: An interactive scatter chart, which shows one data set at a time.
- `stacked_area`: Filled regions that stack on one another, so the outer edge is the category total.
- `stacked_area_3d`: A 3D stacked area chart.
- `stacked_bar`: Horizontal bars with series that stack end to end, so each bar’s length is the category total.
- `stacked_bar_3d`: A 3D stacked bar chart.
- `stacked_column`: Vertical bars with series that stack end to end, so each column’s height is the category total.
- `stacked_column_3d`: A 3D stacked column chart.
- `two_axis`: A two-axis chart. This type of chart plots each series against either the primary or the secondary value axis; for more information about axes, see `ChartSeries.y_axis_selection`. Each series can appear as columns, as a line, or as an area. For more information, see `ChartSeries.mixed_series_type`.

## Topics

### Dictionaries
- [object Chart.area](./chart/area.md)
  A line chart with the region between the line and the axis filled, one region for each series.
- [object Chart.area_3d](./chart/area_3d.md)
  A 3D area chart.
- [object Chart.bar](./chart/bar.md)
  Values as horizontal bars, one bar for each series within each category.
- [object Chart.bar_3d](./chart/bar_3d.md)
  A 3D bar chart.
- [object Chart.bar_interactive](./chart/bar_interactive.md)
  An interactive bar chart, which shows one data set at a time.
- [object Chart.bubble](./chart/bubble.md)
  A scatter chart whose third value sets the area of each point.
- [object Chart.bubble_interactive](./chart/bubble_interactive.md)
  An interactive bubble chart, which shows one data set at a time.
- [object Chart.column](./chart/column.md)
  Values as vertical bars, one bar for each series within each category.
- [object Chart.column_3d](./chart/column_3d.md)
  A 3D column chart.
- [object Chart.column_interactive](./chart/column_interactive.md)
  An interactive column chart, which shows one data set at a time.
- [object Chart.donut](./chart/donut.md)
  A pie chart that appears as a ring with an open center.
- [object Chart.line](./chart/line.md)
  Values as points joined by a line, with one line for each series.
- [object Chart.line_3d](./chart/line_3d.md)
  A 3D line chart.
- [object Chart.mixed](./chart/mixed.md)
  A mixed chart.
- [object Chart.pie](./chart/pie.md)
  One series as wedges of a circle, with each wedge sized by its share of the total.
- [object Chart.pie_3d](./chart/pie_3d.md)
  A 3D pie chart.
- [object Chart.radar](./chart/radar.md)
  Categories that appear around a circle, with each series appearing as a closed outline through its values.
- [object Chart.scatter](./chart/scatter.md)
  Each series appears as a plot of pairs of X and Y values against two value axes, rather than against categories.
- [object Chart.scatter_interactive](./chart/scatter_interactive.md)
  An interactive scatter chart, which shows one data set at a time.
- [object Chart.stacked_area](./chart/stacked_area.md)
  Filled regions that stack on one another, so the outer edge is the category total.
- [object Chart.stacked_area_3d](./chart/stacked_area_3d.md)
  A 3D stacked area chart.
- [object Chart.stacked_bar](./chart/stacked_bar.md)
  Horizontal bars with series that stack end to end, so each bar’s length is the category total.
- [object Chart.stacked_bar_3d](./chart/stacked_bar_3d.md)
  A 3D stacked bar chart.
- [object Chart.stacked_column](./chart/stacked_column.md)
  Vertical bars with series that stack end to end, so each column’s height is the category total.
- [object Chart.stacked_column_3d](./chart/stacked_column_3d.md)
  A 3D stacked column chart.
- [object Chart.two_axis](./chart/two_axis.md)
  A two-axis chart.

## See Also

### Charts
- [type ChartAxisCommon](./chartaxiscommon.md)
  The properties every chart axis shares, flattened into both the category axis and the value axis.
- [type ChartCommon](./chartcommon.md)
  The properties shared by every kind of chart.
- [type ChartLabelFormatting](./chartlabelformatting.md)
  The formatting of a chart element’s numeric labels.
- [object ChartCategoryAxis](./chartcategoryaxis.md)
  The axis along which a chart’s categories are laid out, on the chart types that have one.
- [object ChartData](./chartdata.md)
  The chart’s data as a grid of cells, together with how that grid maps onto the chart.
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

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chart)*