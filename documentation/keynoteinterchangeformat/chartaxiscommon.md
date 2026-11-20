# ChartAxisCommon

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The properties every chart axis shares, flattened into both the category axis and the value axis.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(ChartAxisCommon.chartCategoryAxis | ChartAxisCommon.chartValueAxis | ChartAxisCommon.genericChartAxisCommon) ChartAxisCommon
```



**Allowed Types**: `ChartAxisCommon.chartCategoryAxis`, `ChartAxisCommon.chartValueAxis`, `ChartAxisCommon.genericChartAxisCommon`

## Discussion

They cover the axis’s title, its tick labels and their rotation, and its tick marks. What differs by kind of axis is on `ChartCategoryAxis` and `ChartValueAxis` themselves: the axis line and its gridlines, a category axis’s label spacing, and a value axis’s scale and bounds.

This value takes one of the following forms:

- `chartCategoryAxis`: The axis along which a chart’s categories are laid out, on the chart types that have one. Pie, donut, scatter, and bubble charts have no category axis. A category axis describes only its own appearance; the category names themselves come from the data grid’s row or column labels, whichever `ChartData.plot_direction` leaves as the category direction.
- `chartValueAxis`: A numeric axis that a chart’s values are measured against. The same type serves every value axis a chart has, so a property takes effect only where that axis supports it.
- `genericChartAxisCommon`: A stand-in for a chart axis, when the reader doesn’t recognize its kind. Every set of shared properties has one, to stand in for an object whose kind isn’t recognized. Nothing in the format has the type `ChartAxisCommon`, though, so this object never appears in a document; its properties appear only as part of the types that adopt `ChartAxisCommon`.

## Topics

### Enumerations
- [object ChartAxisCommon.AxisLabelOrientation](./chartaxiscommon.axislabelorientation.md)
  The orientation of an axis’s labels relative to the axis.
### Dictionaries
- [object ChartAxisCommon.chartCategoryAxis](./chartaxiscommon/chartcategoryaxis.md)
  The axis along which a chart’s categories are laid out, on the chart types that have one.
- [object ChartAxisCommon.chartValueAxis](./chartaxiscommon/chartvalueaxis.md)
  A numeric axis that a chart’s values are measured against.
- [object ChartAxisCommon.genericChartAxisCommon](./chartaxiscommon/genericchartaxiscommon.md)
  An object with only the properties of ChartAxisCommon.

## See Also

### Charts
- [type Chart](./chart.md)
  An object that plots a grid of data in a visual style such as column, pie, or scatter.
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

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chartaxiscommon)*