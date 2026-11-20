# RadarChart

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A radar chart.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object RadarChart
```

## Overview

Keynote arranges the categories radially around a center point and plots each series against a shared radial value scale.

This type includes the properties of `CanvasObject`, `CategoryComparisonChart`, and `ChartCommon`, as does every other type that adopts them.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.radar-chart`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `title` (Label): The object’s title.
- `caption` (Label): The object’s caption, which Keynote always places below the object. If a caption is off, you still write it out with `Label.is_visible` set to `false`, so having a value doesn’t mean the caption shows.
- `data` (ChartData): The chart’s data grid, together with its plot direction and data-source mode. This data replaces the placeholder data a new chart starts with; when omitted, that placeholder data remains.
- `show_legend` (boolean): A Boolean value that indicates whether the chart’s legend appears. This value is independent of the `legend` property, which sets the legend’s placement and text style rather than its visibility.

  **Default**: `true`
- `legend` (ChartLegend): The placement and label text style of the chart’s legend. This value doesn’t control whether the legend appears (see `show_legend`), and it only applies to a chart that has a legend.
- `series` ([ChartSeries]): The styling and label formatting for individual data series. Each entry applies to the series named by its `ChartSeries.series_index`, or to the series at the same position when `ChartSeries.series_index` is omitted; entries that don’t correspond to a series in the data don’t have an effect.
- `chart_colors` ([ChartCommon.ChartColor]): The chart’s ordered series styles. A series takes the entry at its own position, and the chart’s style supplies any position without an entry or with an empty one, so the list doesn’t wrap. Entries past the last series also remain. Keynote reads one entry for each series style in the chart’s style and ignores any further entries.
- `category_axis` (ChartCategoryAxis): The category axis, along which Keynote lays out the chart’s categories. When omitted, the category axis keeps the appearance it inherits from the chart’s style.
- `value_axis` (ChartValueAxis): The primary value axis, which carries the numeric scale to measure the series against. When omitted, the value axis keeps the appearance it inherits from the chart’s style.
- `value_axis_secondary` (ChartValueAxis): The second value axis, used only by a two-axis chart that actually plots a series against a second value scale. On any other chart type, this value doesn’t have an effect.
- `identifier` (string): An identifier for this object that other objects use to refer to it. This identifier must be unique across the whole document.
- `geometry` (Geometry): The object’s position and size. If this value is absent, Keynote places the object automatically, with a default position and size for its kind.
- `aspect_ratio_locked` (boolean): A Boolean value that indicates whether the object’s width-to-height ratio is locked when the object resizes. The lock doesn’t constrain the `geometry` property. If this property is absent, images, movies, and groups default to `true`, and other objects to `false`.

  **Default**: `false`
- `description` (string): The accessibility description for the object, read aloud by assistive technologies such as VoiceOver.

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

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/radarchart)*