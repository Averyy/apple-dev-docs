# ChartValueAxis

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A numeric axis that a chart’s values are measured against.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ChartValueAxis
```

## Overview

The same type serves every value axis a chart has, so a property takes effect only where that axis supports it.

This type includes the properties of `ChartAxisCommon` and `ChartLabelFormatting`, as does every other type that adopts them.

## Topics

### Enumerations
- [type ChartValueAxis.AxisScale](./chartvalueaxis.axisscale.md)
  How values are spaced along the axis: evenly, or by order of magnitude so that a wide range stays readable.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.chart-value-axis`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `title` (string): The text of the axis title. Whether the title is shown is controlled separately by `show_title`.
- `title_text_style` (ParagraphProperties): The text style of the axis title, such as its font, size, and alignment.
- `label_text_style` (ParagraphProperties): The text style of the axis labels, such as their font, size, and alignment.
- `show_labels` (boolean): Whether the axis’s tick labels are shown.

  **Default**: `true`
- `show_title` (boolean): Whether the axis title is shown.

  **Default**: `false`
- `show_major_tickmarks` (boolean): Whether major tick marks are shown along the axis.

  **Default**: `true`
- `show_minor_tickmarks` (boolean): Whether minor tick marks are shown along the axis.

  **Default**: `true`
- `labels_orientation` (ChartAxisCommon.AxisLabelOrientation): The rotation of the axis’s labels. The five straight-axis orientations correspond to rotations of 0, 45, 90, 270, and 315 degrees, `custom` carries any other rotation, and `parallel` and `perpendicular` apply to radar charts.
- `label_format_type` (Table.CellFormat.FormatType): The kind of formatting applied to the label’s value. It also selects which of `label_number_format`, `label_currency_format`, `label_date_format`, and `label_duration_format` applies. `text`, `boolean`, and `base` have no equivalent for chart labels and behave like `number`, which is also what omitting this property means.
- `label_date_format` (Table.CellFormat.DateTimeFormat): The date and time format of the label, used when `label_format_type` is `date_time`. An empty format string is treated as no format at all and isn’t preserved.
- `label_duration_format` (Table.CellFormat.DurationFormat): The label’s duration format, used when `label_format_type` is `duration`. It covers automatic units, the smallest and largest unit, and the style.
- `label_number_format` (Table.CellFormat.NumberFormat): The decimal places, negative-number style, and thousands separator of the label, used for number, percentage, and scientific labels. A value of 253 for decimal places means automatic. It’s omitted for fraction, base, and custom labels, which have none of these attributes; a prefix or suffix, a fraction accuracy, and a custom format string aren’t preserved. Currency labels use `label_currency_format` instead. On a stacked chart whose value axis has a `ChartValueAxis.scale` of `percent`, the value labels of each series don’t use this format, and their decimal places, negative-number style, and thousands separator aren’t preserved.
- `label_currency_format` (Table.CellFormat.CurrencyFormat): The currency code, accounting style, decimal places, negative-number style, and thousands separator of the label, used when `label_format_type` is `currency`. It takes the place of `label_number_format` for currency labels, and it’s what preserves the currency code; a prefix or suffix and a custom format string aren’t preserved.
- `scale` (ChartValueAxis.AxisScale): The scale of the axis: `linear`, `log` for a logarithmic axis, or `percent`. If it’s omitted, the scale is `linear`.
- `max` (ChartData.ChartDataValue): The upper bound of the axis, which must be above `min`. A date or duration bound takes effect but isn’t written back out, so only a numeric bound is kept when Keynote exports the presentation. If it’s omitted, the axis scales itself to the data.
- `min` (ChartData.ChartDataValue): The lower bound of the axis, which must be below `max`. A date or duration bound takes effect but isn’t written back out, so only a numeric bound is kept when Keynote exports the presentation. If it’s omitted, the axis scales itself to the data.
- `show_axis` (boolean): Whether the value axis line itself is shown.

  **Default**: `false`
- `show_major_gridlines` (boolean): Whether a gridline is shown at each major step of the axis.

  **Default**: `true`
- `show_minimum_label` (boolean): Whether the label for the axis’s lowest value is shown.

  **Default**: `true`
- `number_of_major_gridlines` (integer): The number of major steps the axis is divided into, each marked by a major gridline. Omit it, or set it to 0, to let the chart choose the number of steps automatically.
- `number_of_decades` (integer): The number of powers of ten the axis is divided into, for logarithmic axes only. Omit it, or set it to 0, to let the chart choose the number automatically.
- `number_of_minor_gridlines` (integer): The number of minor steps between each pair of major gridlines. Omit it, or set it to 0, to keep the chart’s own minor spacing.
- `show_minor_gridlines` (boolean): Whether minor gridlines are shown.

  **Default**: `false`

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

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chartvalueaxis)*