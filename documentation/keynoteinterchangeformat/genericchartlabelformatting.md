# GenericChartLabelFormatting

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

An object with only the properties of ChartLabelFormatting.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object GenericChartLabelFormatting
```

## Overview

Every set of shared properties has one, to stand in for an object whose kind isn’t recognized. Nothing in the format has the type `ChartLabelFormatting`, though, so this object never appears in a document; its properties appear only as part of the types that adopt `ChartLabelFormatting`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.chart-label-formatting-generic`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `label_format_type` (Table.CellFormat.FormatType): The kind of formatting applied to the label’s value. It also selects which of `label_number_format`, `label_currency_format`, `label_date_format`, and `label_duration_format` applies. `text`, `boolean`, and `base` have no equivalent for chart labels and behave like `number`, which is also what omitting this property means.
- `label_date_format` (Table.CellFormat.DateTimeFormat): The date and time format of the label, used when `label_format_type` is `date_time`. An empty format string is treated as no format at all and isn’t preserved.
- `label_duration_format` (Table.CellFormat.DurationFormat): The label’s duration format, used when `label_format_type` is `duration`. It covers automatic units, the smallest and largest unit, and the style.
- `label_number_format` (Table.CellFormat.NumberFormat): The decimal places, negative-number style, and thousands separator of the label, used for number, percentage, and scientific labels. A value of 253 for decimal places means automatic. It’s omitted for fraction, base, and custom labels, which have none of these attributes; a prefix or suffix, a fraction accuracy, and a custom format string aren’t preserved. Currency labels use `label_currency_format` instead. On a stacked chart whose value axis has a `ChartValueAxis.scale` of `percent`, the value labels of each series don’t use this format, and their decimal places, negative-number style, and thousands separator aren’t preserved.
- `label_currency_format` (Table.CellFormat.CurrencyFormat): The currency code, accounting style, decimal places, negative-number style, and thousands separator of the label, used when `label_format_type` is `currency`. It takes the place of `label_number_format` for currency labels, and it’s what preserves the currency code; a prefix or suffix and a custom format string aren’t preserved.

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

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/genericchartlabelformatting)*