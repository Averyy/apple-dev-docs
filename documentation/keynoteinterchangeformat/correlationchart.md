# CorrelationChart

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The axes shared by every chart type that plots one value scale against another.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(CorrelationChart.bubbleChart | CorrelationChart.bubbleInteractiveChart | CorrelationChart.genericCorrelationChart | CorrelationChart.scatterChart | CorrelationChart.scatterInteractiveChart) CorrelationChart
```



**Allowed Types**: `CorrelationChart.bubbleChart`, `CorrelationChart.bubbleInteractiveChart`, `CorrelationChart.genericCorrelationChart`, `CorrelationChart.scatterChart`, `CorrelationChart.scatterInteractiveChart`

## Discussion

These chart types are the scatter and bubble charts and their interactive variants. They have an X and a Y value axis and no category axis.

This value takes one of the following forms:

- `bubbleChart`: A bubble chart. Keynote plots each data point against an X and a Y value axis, and its bubble area comes from a third data value rather than a series setting. See `data.shared_xvalues` for how the grid’s rows or columns map onto each series.
- `bubbleInteractiveChart`: An interactive bubble chart, which shows one data set at a time. You can step between the data sets. Keynote lays out the series as a bubble chart; for more information, see `data.shared_xvalues`. The interactive control, the position of the data set name, and which data set is shown aren’t included, so they take the default for this chart type.
- `genericCorrelationChart`: A stand-in for a chart that plots one value scale against another, when the reader doesn’t recognize its kind. Every set of shared properties has one, to stand in for an object whose kind isn’t recognized. Nothing in the format has the type `CorrelationChart`, though, so this object never appears in a document; its properties appear only as part of the types that adopt `CorrelationChart`.
- `scatterChart`: A scatter chart. Keynote plots each data point against an X and a Y value axis rather than against a category axis. See `data.shared_xvalues` for how the grid’s rows or columns map onto each series.
- `scatterInteractiveChart`: An interactive scatter chart, which shows one data set at a time. You can step between the data sets. Keynote lays out the series as a scatter chart; for more information, see `data.shared_xvalues`. The interactive control, the position of the data set name, and which data set the reader shows aren’t included, so they take the default for this chart type.

## Topics

### Dictionaries
- [object CorrelationChart.bubbleChart](./correlationchart/bubblechart.md)
  A bubble chart.
- [object CorrelationChart.bubbleInteractiveChart](./correlationchart/bubbleinteractivechart.md)
  An interactive bubble chart, which shows one data set at a time.
- [object CorrelationChart.genericCorrelationChart](./correlationchart/genericcorrelationchart.md)
  An object with only the properties of CorrelationChart.
- [object CorrelationChart.scatterChart](./correlationchart/scatterchart.md)
  A scatter chart.
- [object CorrelationChart.scatterInteractiveChart](./correlationchart/scatterinteractivechart.md)
  An interactive scatter chart, which shows one data set at a time.

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

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/correlationchart)*