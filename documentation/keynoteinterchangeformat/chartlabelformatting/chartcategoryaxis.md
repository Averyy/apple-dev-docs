# ChartLabelFormatting.chartCategoryAxis

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The axis along which a chart’s categories are laid out, on the chart types that have one.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ChartLabelFormatting.chartCategoryAxis
```

## Overview

Pie, donut, scatter, and bubble charts have no category axis. A category axis describes only its own appearance; the category names themselves come from the data grid’s row or column labels, whichever `ChartData.plot_direction` leaves as the category direction.

Written as `{"chartCategoryAxis": …}`: the `chartCategoryAxis` form of `ChartLabelFormatting`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.chart-label-formatting`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `chartCategoryAxis` (ChartCategoryAxis) *(required)*: The axis along which a chart’s categories are laid out, on the chart types that have one. Pie, donut, scatter, and bubble charts have no category axis. A category axis describes only its own appearance; the category names themselves come from the data grid’s row or column labels, whichever `ChartData.plot_direction` leaves as the category direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chartlabelformatting/chartcategoryaxis)*