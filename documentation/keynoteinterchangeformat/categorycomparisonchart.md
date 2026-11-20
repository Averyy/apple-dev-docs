# CategoryComparisonChart

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The axes shared by every chart type that compares categories against a value scale.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(CategoryComparisonChart.area3Dchart | CategoryComparisonChart.areaChart | CategoryComparisonChart.bar3Dchart | CategoryComparisonChart.barChart | CategoryComparisonChart.barInteractiveChart | CategoryComparisonChart.column3Dchart | CategoryComparisonChart.columnChart | CategoryComparisonChart.columnInteractiveChart | CategoryComparisonChart.genericCategoryComparisonChart | CategoryComparisonChart.line3Dchart | CategoryComparisonChart.lineChart | CategoryComparisonChart.mixedChart | CategoryComparisonChart.radarChart | CategoryComparisonChart.stackedArea3Dchart | CategoryComparisonChart.stackedAreaChart | CategoryComparisonChart.stackedBar3Dchart | CategoryComparisonChart.stackedBarChart | CategoryComparisonChart.stackedColumn3Dchart | CategoryComparisonChart.stackedColumnChart | CategoryComparisonChart.twoAxisChart) CategoryComparisonChart
```



**Allowed Types**: `CategoryComparisonChart.area3Dchart`, `CategoryComparisonChart.areaChart`, `CategoryComparisonChart.bar3Dchart`, `CategoryComparisonChart.barChart`, `CategoryComparisonChart.barInteractiveChart`, `CategoryComparisonChart.column3Dchart`, `CategoryComparisonChart.columnChart`, `CategoryComparisonChart.columnInteractiveChart`, `CategoryComparisonChart.genericCategoryComparisonChart`, `CategoryComparisonChart.line3Dchart`, `CategoryComparisonChart.lineChart`, `CategoryComparisonChart.mixedChart`, `CategoryComparisonChart.radarChart`, `CategoryComparisonChart.stackedArea3Dchart`, `CategoryComparisonChart.stackedAreaChart`, `CategoryComparisonChart.stackedBar3Dchart`, `CategoryComparisonChart.stackedBarChart`, `CategoryComparisonChart.stackedColumn3Dchart`, `CategoryComparisonChart.stackedColumnChart`, `CategoryComparisonChart.twoAxisChart`

## Discussion

These chart types are the column, bar, line, and area charts; their stacked, 3D, and interactive variants; and the mixed, radar, and two-axis charts.

This value takes one of the following forms:

- `area3Dchart`: A 3D area chart. 3D appearance settings such as rotation, depth, lighting, and textures aren’t included: rotation and depth take the default for this chart type, and lighting and a textured series’ fill come from the chart’s style.
- `areaChart`: A 2D area chart. Keynote draws each series as a filled region against a shared category axis and value axis.
- `bar3Dchart`: A 3D horizontal bar chart. 3D appearance settings such as rotation, depth, lighting, and textures aren’t included: rotation and depth take the default for this chart type, and lighting and a textured series’ fill come from the chart’s style.
- `barChart`: A 2D bar chart. Keynote draws each series as horizontal bars against a shared category axis and value axis.
- `barInteractiveChart`: An interactive horizontal bar chart, which shows one data set at a time. You can step between the data sets. The interactive control, the position of the data set name, and which data set is shown aren’t included, so they take the default for this chart type.
- `column3Dchart`: A 3D vertical column chart. 3D appearance settings such as rotation, depth, lighting, and textures aren’t included: rotation and depth take the default for this chart type, and lighting and a textured series’ fill come from the chart’s style.
- `columnChart`: A 2D column chart. Keynote draws each series as vertical columns against a shared category axis and value axis. A chart whose type this version of the format doesn’t recognize is also written out as a column chart.
- `columnInteractiveChart`: An interactive vertical column chart, which shows one data set at a time. You can step between the data sets. The interactive control, the position of the data set name, and which data set is shown aren’t included, so they take the default for this chart type.
- `genericCategoryComparisonChart`: A stand-in for a chart that compares categories against a value scale, when the reader doesn’t recognize its kind. Every set of shared properties has one, to stand in for an object whose kind isn’t recognized. Nothing in the format has the type `CategoryComparisonChart`, though, so this object never appears in a document; its properties appear only as part of the types that adopt `CategoryComparisonChart`.
- `line3Dchart`: A 3D line chart. 3D appearance settings such as rotation, depth, lighting, and textures aren’t included: rotation and depth take the default for this chart type, and lighting and a textured series’ fill come from the chart’s style.
- `lineChart`: A 2D line chart. Keynote draws each series as a line against a shared category axis and value axis.
- `mixedChart`: A mixed chart, which draws individual series as columns, lines, or areas. The series share a category axis and value axis, and each series picks its shape through its `ChartSeries.mixed_series_type` value.
- `radarChart`: A radar chart. Keynote arranges the categories radially around a center point and plots each series against a shared radial value scale.
- `stackedArea3Dchart`: A 3D stacked area chart. 3D appearance settings such as rotation, depth, lighting, and textures aren’t included: rotation and depth take the default for this chart type, and lighting and a textured series’ fill come from the chart’s style.
- `stackedAreaChart`: A 2D stacked area chart. Keynote stacks each series’ filled region on top of the one before it against a shared category axis and value axis.
- `stackedBar3Dchart`: A 3D stacked horizontal bar chart. 3D appearance settings such as rotation, depth, lighting, and textures aren’t included: rotation and depth take the default for this chart type, and lighting and a textured series’ fill come from the chart’s style.
- `stackedBarChart`: A 2D stacked bar chart. Each series contributes a segment to a single horizontal bar for each category, which Keynote measures against a shared value axis.
- `stackedColumn3Dchart`: A 3D stacked vertical column chart. 3D appearance settings such as rotation, depth, lighting, and textures aren’t included: rotation and depth take the default for this chart type, and lighting and a textured series’ fill come from the chart’s style.
- `stackedColumnChart`: A 2D stacked column chart. Each series contributes a segment to a single vertical column for each category, which Keynote measures against a shared value axis.
- `twoAxisChart`: A two-axis chart, which is a category chart with two independent value scales. The two scales let Keynote measure different series against different value axes. It’s the only chart type that uses `value_axis_secondary`, and, like the mixed chart, it lets each series pick its shape through its `ChartSeries.mixed_series_type` value.

## Topics

### Dictionaries
- [object CategoryComparisonChart.area3Dchart](./categorycomparisonchart/area3dchart.md)
  A 3D area chart.
- [object CategoryComparisonChart.areaChart](./categorycomparisonchart/areachart.md)
  A 2D area chart.
- [object CategoryComparisonChart.bar3Dchart](./categorycomparisonchart/bar3dchart.md)
  A 3D horizontal bar chart.
- [object CategoryComparisonChart.barChart](./categorycomparisonchart/barchart.md)
  A 2D bar chart.
- [object CategoryComparisonChart.barInteractiveChart](./categorycomparisonchart/barinteractivechart.md)
  An interactive horizontal bar chart, which shows one data set at a time.
- [object CategoryComparisonChart.column3Dchart](./categorycomparisonchart/column3dchart.md)
  A 3D vertical column chart.
- [object CategoryComparisonChart.columnChart](./categorycomparisonchart/columnchart.md)
  A 2D column chart.
- [object CategoryComparisonChart.columnInteractiveChart](./categorycomparisonchart/columninteractivechart.md)
  An interactive vertical column chart, which shows one data set at a time.
- [object CategoryComparisonChart.genericCategoryComparisonChart](./categorycomparisonchart/genericcategorycomparisonchart.md)
  An object with only the properties of CategoryComparisonChart.
- [object CategoryComparisonChart.line3Dchart](./categorycomparisonchart/line3dchart.md)
  A 3D line chart.
- [object CategoryComparisonChart.lineChart](./categorycomparisonchart/linechart.md)
  A 2D line chart.
- [object CategoryComparisonChart.mixedChart](./categorycomparisonchart/mixedchart.md)
  A mixed chart, which draws individual series as columns, lines, or areas.
- [object CategoryComparisonChart.radarChart](./categorycomparisonchart/radarchart.md)
  A radar chart.
- [object CategoryComparisonChart.stackedArea3Dchart](./categorycomparisonchart/stackedarea3dchart.md)
  A 3D stacked area chart.
- [object CategoryComparisonChart.stackedAreaChart](./categorycomparisonchart/stackedareachart.md)
  A 2D stacked area chart.
- [object CategoryComparisonChart.stackedBar3Dchart](./categorycomparisonchart/stackedbar3dchart.md)
  A 3D stacked horizontal bar chart.
- [object CategoryComparisonChart.stackedBarChart](./categorycomparisonchart/stackedbarchart.md)
  A 2D stacked bar chart.
- [object CategoryComparisonChart.stackedColumn3Dchart](./categorycomparisonchart/stackedcolumn3dchart.md)
  A 3D stacked vertical column chart.
- [object CategoryComparisonChart.stackedColumnChart](./categorycomparisonchart/stackedcolumnchart.md)
  A 2D stacked column chart.
- [object CategoryComparisonChart.twoAxisChart](./categorycomparisonchart/twoaxischart.md)
  A two-axis chart, which is a category chart with two independent value scales.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/categorycomparisonchart)*