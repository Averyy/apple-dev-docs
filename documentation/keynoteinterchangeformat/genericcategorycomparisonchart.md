# GenericCategoryComparisonChart

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

An object with only the properties of CategoryComparisonChart.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object GenericCategoryComparisonChart
```

## Overview

Every set of shared properties has one, to stand in for an object whose kind isn’t recognized. Nothing in the format has the type `CategoryComparisonChart`, though, so this object never appears in a document; its properties appear only as part of the types that adopt `CategoryComparisonChart`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.category-comparison-chart-generic`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `category_axis` (ChartCategoryAxis): The category axis, along which Keynote lays out the chart’s categories. When omitted, the category axis keeps the appearance it inherits from the chart’s style.
- `value_axis` (ChartValueAxis): The primary value axis, which carries the numeric scale to measure the series against. When omitted, the value axis keeps the appearance it inherits from the chart’s style.
- `value_axis_secondary` (ChartValueAxis): The second value axis, used only by a two-axis chart that actually plots a series against a second value scale. On any other chart type, this value doesn’t have an effect.

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

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/genericcategorycomparisonchart)*