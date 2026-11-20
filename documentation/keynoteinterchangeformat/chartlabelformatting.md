# ChartLabelFormatting

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The formatting of a chart element’s numeric labels.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(ChartLabelFormatting.chartCategoryAxis | ChartLabelFormatting.chartSeries | ChartLabelFormatting.chartValueAxis | ChartLabelFormatting.genericChartLabelFormatting) ChartLabelFormatting
```



**Allowed Types**: `ChartLabelFormatting.chartCategoryAxis`, `ChartLabelFormatting.chartSeries`, `ChartLabelFormatting.chartValueAxis`, `ChartLabelFormatting.genericChartLabelFormatting`

## Discussion

It’s flattened into `ChartValueAxis`, `ChartCategoryAxis`, and `ChartSeries`. `label_format_type` selects which of the format properties applies. A prefix or suffix, a fraction accuracy, and a custom format string aren’t preserved.

This value takes one of the following forms:

- `chartCategoryAxis`: The axis along which a chart’s categories are laid out, on the chart types that have one. Pie, donut, scatter, and bubble charts have no category axis. A category axis describes only its own appearance; the category names themselves come from the data grid’s row or column labels, whichever `ChartData.plot_direction` leaves as the category direction.
- `chartSeries`: The appearance and label formatting of one of a chart’s data series. It covers the series’ fill, stroke, data symbols, connecting line, and value labels; the plotted values come from the chart’s data grid. Many properties apply only to certain chart types and are ignored on the rest.
- `chartValueAxis`: A numeric axis that a chart’s values are measured against. The same type serves every value axis a chart has, so a property takes effect only where that axis supports it.
- `genericChartLabelFormatting`: A stand-in for a chart’s numeric label formatting, when the reader doesn’t recognize its kind. Every set of shared properties has one, to stand in for an object whose kind isn’t recognized. Nothing in the format has the type `ChartLabelFormatting`, though, so this object never appears in a document; its properties appear only as part of the types that adopt `ChartLabelFormatting`.

## Topics

### Dictionaries
- [object ChartLabelFormatting.chartCategoryAxis](./chartlabelformatting/chartcategoryaxis.md)
  The axis along which a chart’s categories are laid out, on the chart types that have one.
- [object ChartLabelFormatting.chartSeries](./chartlabelformatting/chartseries.md)
  The appearance and label formatting of one of a chart’s data series.
- [object ChartLabelFormatting.chartValueAxis](./chartlabelformatting/chartvalueaxis.md)
  A numeric axis that a chart’s values are measured against.
- [object ChartLabelFormatting.genericChartLabelFormatting](./chartlabelformatting/genericchartlabelformatting.md)
  An object with only the properties of ChartLabelFormatting.

## See Also

### Charts
- [type Chart](./chart.md)
  An object that plots a grid of data in a visual style such as column, pie, or scatter.
- [type ChartAxisCommon](./chartaxiscommon.md)
  The properties every chart axis shares, flattened into both the category axis and the value axis.
- [type ChartCommon](./chartcommon.md)
  The properties shared by every kind of chart.
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

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chartlabelformatting)*