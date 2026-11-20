# ChartCommon

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The properties shared by every kind of chart.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(ChartCommon.area3Dchart | ChartCommon.areaChart | ChartCommon.bar3Dchart | ChartCommon.barChart | ChartCommon.barInteractiveChart | ChartCommon.bubbleChart | ChartCommon.bubbleInteractiveChart | ChartCommon.column3Dchart | ChartCommon.columnChart | ChartCommon.columnInteractiveChart | ChartCommon.donutChart | ChartCommon.genericChartCommon | ChartCommon.line3Dchart | ChartCommon.lineChart | ChartCommon.mixedChart | ChartCommon.pie3Dchart | ChartCommon.pieChart | ChartCommon.radarChart | ChartCommon.scatterChart | ChartCommon.scatterInteractiveChart | ChartCommon.stackedArea3Dchart | ChartCommon.stackedAreaChart | ChartCommon.stackedBar3Dchart | ChartCommon.stackedBarChart | ChartCommon.stackedColumn3Dchart | ChartCommon.stackedColumnChart | ChartCommon.twoAxisChart) ChartCommon
```



**Allowed Types**: `ChartCommon.area3Dchart`, `ChartCommon.areaChart`, `ChartCommon.bar3Dchart`, `ChartCommon.barChart`, `ChartCommon.barInteractiveChart`, `ChartCommon.bubbleChart`, `ChartCommon.bubbleInteractiveChart`, `ChartCommon.column3Dchart`, `ChartCommon.columnChart`, `ChartCommon.columnInteractiveChart`, `ChartCommon.donutChart`, `ChartCommon.genericChartCommon`, `ChartCommon.line3Dchart`, `ChartCommon.lineChart`, `ChartCommon.mixedChart`, `ChartCommon.pie3Dchart`, `ChartCommon.pieChart`, `ChartCommon.radarChart`, `ChartCommon.scatterChart`, `ChartCommon.scatterInteractiveChart`, `ChartCommon.stackedArea3Dchart`, `ChartCommon.stackedAreaChart`, `ChartCommon.stackedBar3Dchart`, `ChartCommon.stackedBarChart`, `ChartCommon.stackedColumn3Dchart`, `ChartCommon.stackedColumnChart`, `ChartCommon.twoAxisChart`

## Discussion

These are the data grid, the styling for each series, the ordered series styles in `chart_colors`, the legend, and the title and caption from `TitleOwning` and `CaptionOwning`. Axes come from `CategoryComparisonChart` or `CorrelationChart` instead. When a chart is read, it takes its style from the theme’s first chart style, and that style supplies any styling the chart doesn’t set. A chart uses the title as its own built-in title and adopts `TitleOwning` alone rather than `PlaceableTitleOwning`, because it lays out that title itself, and the format offers no placement control over it.

This value takes one of the following forms:

- `area3Dchart`: A 3D area chart. 3D appearance settings such as rotation, depth, lighting, and textures aren’t included: rotation and depth take the default for this chart type, and lighting and a textured series’ fill come from the chart’s style.
- `areaChart`: A 2D area chart. Keynote draws each series as a filled region against a shared category axis and value axis.
- `bar3Dchart`: A 3D horizontal bar chart. 3D appearance settings such as rotation, depth, lighting, and textures aren’t included: rotation and depth take the default for this chart type, and lighting and a textured series’ fill come from the chart’s style.
- `barChart`: A 2D bar chart. Keynote draws each series as horizontal bars against a shared category axis and value axis.
- `barInteractiveChart`: An interactive horizontal bar chart, which shows one data set at a time. You can step between the data sets. The interactive control, the position of the data set name, and which data set is shown aren’t included, so they take the default for this chart type.
- `bubbleChart`: A bubble chart. Keynote plots each data point against an X and a Y value axis, and its bubble area comes from a third data value rather than a series setting. See `data.shared_xvalues` for how the grid’s rows or columns map onto each series.
- `bubbleInteractiveChart`: An interactive bubble chart, which shows one data set at a time. You can step between the data sets. Keynote lays out the series as a bubble chart; for more information, see `data.shared_xvalues`. The interactive control, the position of the data set name, and which data set is shown aren’t included, so they take the default for this chart type.
- `column3Dchart`: A 3D vertical column chart. 3D appearance settings such as rotation, depth, lighting, and textures aren’t included: rotation and depth take the default for this chart type, and lighting and a textured series’ fill come from the chart’s style.
- `columnChart`: A 2D column chart. Keynote draws each series as vertical columns against a shared category axis and value axis. A chart whose type this version of the format doesn’t recognize is also written out as a column chart.
- `columnInteractiveChart`: An interactive vertical column chart, which shows one data set at a time. You can step between the data sets. The interactive control, the position of the data set name, and which data set is shown aren’t included, so they take the default for this chart type.
- `donutChart`: A donut chart. Each series contributes one segment of the ring, sized by that series’ first value; Keynote doesn’t show later values in a series. Donut charts have no categories and no axes. The title, when shown, appears in the center of the ring.
- `genericChartCommon`: A stand-in for a chart, when the reader doesn’t recognize its kind. Every set of shared properties has one, to stand in for an object whose kind isn’t recognized. Nothing in the format has the type `ChartCommon`, though, so this object never appears in a document; its properties appear only as part of the types that adopt `ChartCommon`.
- `line3Dchart`: A 3D line chart. 3D appearance settings such as rotation, depth, lighting, and textures aren’t included: rotation and depth take the default for this chart type, and lighting and a textured series’ fill come from the chart’s style.
- `lineChart`: A 2D line chart. Keynote draws each series as a line against a shared category axis and value axis.
- `mixedChart`: A mixed chart, which draws individual series as columns, lines, or areas. The series share a category axis and value axis, and each series picks its shape through its `ChartSeries.mixed_series_type` value.
- `pie3Dchart`: A 3D pie chart. Like the 2D pie chart, it has no axes. 3D appearance settings such as rotation, depth, lighting, and textures aren’t included: rotation and depth take the default for this chart type, and lighting and a textured series’ fill come from the chart’s style.
- `pieChart`: A pie chart. Each series contributes one wedge, sized by that series’ first value; Keynote doesn’t show later values in a series. Pie charts have no categories and no axes.
- `radarChart`: A radar chart. Keynote arranges the categories radially around a center point and plots each series against a shared radial value scale.
- `scatterChart`: A scatter chart. Keynote plots each data point against an X and a Y value axis rather than against a category axis. See `data.shared_xvalues` for how the grid’s rows or columns map onto each series.
- `scatterInteractiveChart`: An interactive scatter chart, which shows one data set at a time. You can step between the data sets. Keynote lays out the series as a scatter chart; for more information, see `data.shared_xvalues`. The interactive control, the position of the data set name, and which data set the reader shows aren’t included, so they take the default for this chart type.
- `stackedArea3Dchart`: A 3D stacked area chart. 3D appearance settings such as rotation, depth, lighting, and textures aren’t included: rotation and depth take the default for this chart type, and lighting and a textured series’ fill come from the chart’s style.
- `stackedAreaChart`: A 2D stacked area chart. Keynote stacks each series’ filled region on top of the one before it against a shared category axis and value axis.
- `stackedBar3Dchart`: A 3D stacked horizontal bar chart. 3D appearance settings such as rotation, depth, lighting, and textures aren’t included: rotation and depth take the default for this chart type, and lighting and a textured series’ fill come from the chart’s style.
- `stackedBarChart`: A 2D stacked bar chart. Each series contributes a segment to a single horizontal bar for each category, which Keynote measures against a shared value axis.
- `stackedColumn3Dchart`: A 3D stacked vertical column chart. 3D appearance settings such as rotation, depth, lighting, and textures aren’t included: rotation and depth take the default for this chart type, and lighting and a textured series’ fill come from the chart’s style.
- `stackedColumnChart`: A 2D stacked column chart. Each series contributes a segment to a single vertical column for each category, which Keynote measures against a shared value axis.
- `twoAxisChart`: A two-axis chart, which is a category chart with two independent value scales. The two scales let Keynote measure different series against different value axes. It’s the only chart type that uses `value_axis_secondary`, and, like the mixed chart, it lets each series pick its shape through its `ChartSeries.mixed_series_type` value.

## Topics

### Objects
- [object ChartCommon.ChartColor](./chartcommon.chartcolor.md)
  One entry in a chart’s series styles.
### Dictionaries
- [object ChartCommon.area3Dchart](./chartcommon/area3dchart.md)
  A 3D area chart.
- [object ChartCommon.areaChart](./chartcommon/areachart.md)
  A 2D area chart.
- [object ChartCommon.bar3Dchart](./chartcommon/bar3dchart.md)
  A 3D horizontal bar chart.
- [object ChartCommon.barChart](./chartcommon/barchart.md)
  A 2D bar chart.
- [object ChartCommon.barInteractiveChart](./chartcommon/barinteractivechart.md)
  An interactive horizontal bar chart, which shows one data set at a time.
- [object ChartCommon.bubbleChart](./chartcommon/bubblechart.md)
  A bubble chart.
- [object ChartCommon.bubbleInteractiveChart](./chartcommon/bubbleinteractivechart.md)
  An interactive bubble chart, which shows one data set at a time.
- [object ChartCommon.column3Dchart](./chartcommon/column3dchart.md)
  A 3D vertical column chart.
- [object ChartCommon.columnChart](./chartcommon/columnchart.md)
  A 2D column chart.
- [object ChartCommon.columnInteractiveChart](./chartcommon/columninteractivechart.md)
  An interactive vertical column chart, which shows one data set at a time.
- [object ChartCommon.donutChart](./chartcommon/donutchart.md)
  A donut chart.
- [object ChartCommon.genericChartCommon](./chartcommon/genericchartcommon.md)
  An object with only the properties of ChartCommon.
- [object ChartCommon.line3Dchart](./chartcommon/line3dchart.md)
  A 3D line chart.
- [object ChartCommon.lineChart](./chartcommon/linechart.md)
  A 2D line chart.
- [object ChartCommon.mixedChart](./chartcommon/mixedchart.md)
  A mixed chart, which draws individual series as columns, lines, or areas.
- [object ChartCommon.pie3Dchart](./chartcommon/pie3dchart.md)
  A 3D pie chart.
- [object ChartCommon.pieChart](./chartcommon/piechart.md)
  A pie chart.
- [object ChartCommon.radarChart](./chartcommon/radarchart.md)
  A radar chart.
- [object ChartCommon.scatterChart](./chartcommon/scatterchart.md)
  A scatter chart.
- [object ChartCommon.scatterInteractiveChart](./chartcommon/scatterinteractivechart.md)
  An interactive scatter chart, which shows one data set at a time.
- [object ChartCommon.stackedArea3Dchart](./chartcommon/stackedarea3dchart.md)
  A 3D stacked area chart.
- [object ChartCommon.stackedAreaChart](./chartcommon/stackedareachart.md)
  A 2D stacked area chart.
- [object ChartCommon.stackedBar3Dchart](./chartcommon/stackedbar3dchart.md)
  A 3D stacked horizontal bar chart.
- [object ChartCommon.stackedBarChart](./chartcommon/stackedbarchart.md)
  A 2D stacked bar chart.
- [object ChartCommon.stackedColumn3Dchart](./chartcommon/stackedcolumn3dchart.md)
  A 3D stacked vertical column chart.
- [object ChartCommon.stackedColumnChart](./chartcommon/stackedcolumnchart.md)
  A 2D stacked column chart.
- [object ChartCommon.twoAxisChart](./chartcommon/twoaxischart.md)
  A two-axis chart, which is a category chart with two independent value scales.

## See Also

### Charts
- [type Chart](./chart.md)
  An object that plots a grid of data in a visual style such as column, pie, or scatter.
- [type ChartAxisCommon](./chartaxiscommon.md)
  The properties every chart axis shares, flattened into both the category axis and the value axis.
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

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chartcommon)*