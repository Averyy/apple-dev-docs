# ChartLabelFormatting.chartSeries

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The appearance and label formatting of one of a chart’s data series.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ChartLabelFormatting.chartSeries
```

## Overview

It covers the series’ fill, stroke, data symbols, connecting line, and value labels; the plotted values come from the chart’s data grid. Many properties apply only to certain chart types and are ignored on the rest.

Written as `{"chartSeries": …}`: the `chartSeries` form of `ChartLabelFormatting`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.chart-label-formatting`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `chartSeries` (ChartSeries) *(required)*: The appearance and label formatting of one of a chart’s data series. It covers the series’ fill, stroke, data symbols, connecting line, and value labels; the plotted values come from the chart’s data grid. Many properties apply only to certain chart types and are ignored on the rest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chartlabelformatting/chartseries)*