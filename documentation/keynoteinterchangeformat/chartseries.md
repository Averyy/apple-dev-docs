# ChartSeries

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The appearance and label formatting of one of a chart’s data series.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ChartSeries
```

## Overview

It covers the series’ fill, stroke, data symbols, connecting line, and value labels; the plotted values come from the chart’s data grid. Many properties apply only to certain chart types and are ignored on the rest.

This type includes the properties of `ChartLabelFormatting`, as does every other type that adopts it.

## Topics

### Enumerations
- [type ChartSeries.ConnectionLineType](./chartseries.connectionlinetype.md)
  The style of the line drawn through a series’ data points.
- [type ChartSeries.FillReuseRule](./chartseries.fillreuserule.md)
  A rule that reuses one of a series’ own colors in place of an explicit fill.
- [type ChartSeries.MixedSeriesType](./chartseries.mixedseriestype.md)
  The shape a single series takes on a mixed or two-axis chart.
- [type ChartSeries.SeriesSymbolType](./chartseries.seriessymboltype.md)
  The shape of the data symbol drawn at each of a series’ data points.
- [type ChartSeries.SeriesValueLabelPosition](./chartseries.seriesvaluelabelposition.md)
  The position of a data point’s value label, for a series that shows value labels.
- [type ChartSeries.ValueLabelsSelection](./chartseries.valuelabelsselection.md)
  The values of a data point that appear in its value label.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.chart-series`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `label_format_type` (Table.CellFormat.FormatType): The kind of formatting applied to the label’s value. It also selects which of `label_number_format`, `label_currency_format`, `label_date_format`, and `label_duration_format` applies. `text`, `boolean`, and `base` have no equivalent for chart labels and behave like `number`, which is also what omitting this property means.
- `label_date_format` (Table.CellFormat.DateTimeFormat): The date and time format of the label, used when `label_format_type` is `date_time`. An empty format string is treated as no format at all and isn’t preserved.
- `label_duration_format` (Table.CellFormat.DurationFormat): The label’s duration format, used when `label_format_type` is `duration`. It covers automatic units, the smallest and largest unit, and the style.
- `label_number_format` (Table.CellFormat.NumberFormat): The decimal places, negative-number style, and thousands separator of the label, used for number, percentage, and scientific labels. A value of 253 for decimal places means automatic. It’s omitted for fraction, base, and custom labels, which have none of these attributes; a prefix or suffix, a fraction accuracy, and a custom format string aren’t preserved. Currency labels use `label_currency_format` instead. On a stacked chart whose value axis has a `ChartValueAxis.scale` of `percent`, the value labels of each series don’t use this format, and their decimal places, negative-number style, and thousands separator aren’t preserved.
- `label_currency_format` (Table.CellFormat.CurrencyFormat): The currency code, accounting style, decimal places, negative-number style, and thousands separator of the label, used when `label_format_type` is `currency`. It takes the place of `label_number_format` for currency labels, and it’s what preserves the currency code; a prefix or suffix and a custom format string aren’t preserved.
- `series_index` (integer): The zero-based index of the data series this entry applies to. If it’s omitted, the entry’s own position in the series array is used; an entry whose index is negative or past the last series in the data is ignored rather than treated as an error.
- `show_value_labels` (boolean): Whether each data point in this series is labeled with its value.

  **Default**: `false`
- `value_label_position` (ChartSeries.SeriesValueLabelPosition): The position of a data point’s value label relative to the point. Not every chart type offers every position, and a position that isn’t one of the values listed here isn’t preserved.
- `value_label_text_style` (ParagraphProperties): The text style of value labels drawn inside the series element.
- `value_label_outside_text_style` (ParagraphProperties): The text style of value labels drawn outside the series element.
- `fill` ((Fill | null)): The fill of the series’ bars, columns, wedges, or area. `null` clears the fill; omitting the key inherits it from the chart’s style. It’s ignored when `fill_reuse_rules` derives the fill from another color instead.

  **Allowed Types**: `Fill`, `null`
- `stroke` (Stroke): The stroke of the series’ line, or of the border of its bars, columns, or wedges. Bubble series have no such stroke (see `symbol_stroke` instead): a stroke supplied for one is ignored and isn’t preserved.
- `symbol_type` (ChartSeries.SeriesSymbolType): The shape of the data symbol drawn at each data point, or `none` for no data symbol. Data symbols exist only on 2D line, area, scatter, radar, and mixed line or area series, not on bubble or 3D series. Setting any shape other than `none` also turns data symbols on.
- `symbol_stroke` (Stroke): The stroke of the data symbols drawn at each data point. It applies only to series that draw data symbols, which for this purpose include bubbles.
- `symbol_fill` ((Fill | null)): The fill of the data symbols drawn at each data point. `null` clears the fill; omitting the key inherits it from the chart’s style. It applies only to series that draw data symbols, which for this purpose include bubbles.

  **Allowed Types**: `Fill`, `null`
- `symbol_size` (number): The size of the data symbols drawn at each data point, in points. Bubble series have no data symbol size, because a bubble is sized from its data value; a size of `0` is treated as unset and isn’t preserved.
- `fill_reuse_rules` ([ChartSeries.FillReuseRule]): The rules that derive the data symbol or series fill from another of the series’ colors instead of an explicit fill.
- `fill_use_series_stroke_alpha_multiplier` (number): The alpha applied to the series stroke color to derive the series fill when `fill_reuse_rules` contains `series_fill_use_series_stroke`. It’s ignored otherwise.
- `connection_line_type` (ChartSeries.ConnectionLineType): The style of the line joining this series’ data points: `none`, `straight`, or `curved`. It applies only to series that draw a joining line, such as line, scatter, bubble, and radar series.
- `value_labels_selection` (ChartSeries.ValueLabelsSelection): The values of a data point that appear in its value label on a bubble or scatter chart. It’s ignored by other chart types; combinations other than the ones listed here aren’t preserved.
- `show_negative_data` (boolean): Whether a bubble chart shows a bubble for a negative value, sized from the value’s magnitude. When it’s `false`, negative values aren’t plotted. It’s ignored by other chart types.

  **Default**: `false`
- `mixed_series_type` (ChartSeries.MixedSeriesType): The shape of this series on a mixed or two-axis chart: columns, a line, or an area. It’s ignored by other chart types.
- `y_axis_selection` (integer): The value axis this series is plotted against on a two-axis chart: `0` for the primary axis and `1` for the secondary axis. It’s ignored by other chart types. It’s always written for a two-axis chart, including 0, because omitting the key leaves the series on its default axis, which is the secondary axis for every series after the first.

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

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chartseries)*