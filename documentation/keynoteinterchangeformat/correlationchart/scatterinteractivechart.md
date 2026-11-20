# CorrelationChart.scatterInteractiveChart

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

An interactive scatter chart, which shows one data set at a time.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object CorrelationChart.scatterInteractiveChart
```

## Overview

You can step between the data sets. Keynote lays out the series as a scatter chart; for more information, see `data.shared_xvalues`. The interactive control, the position of the data set name, and which data set the reader shows aren’t included, so they take the default for this chart type.

Written as `{"scatterInteractiveChart": …}`: the `scatterInteractiveChart` form of `CorrelationChart`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.correlation-chart`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `scatterInteractiveChart` (ScatterInteractiveChart) *(required)*: An interactive scatter chart, which shows one data set at a time. You can step between the data sets. Keynote lays out the series as a scatter chart; for more information, see `data.shared_xvalues`. The interactive control, the position of the data set name, and which data set the reader shows aren’t included, so they take the default for this chart type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/correlationchart/scatterinteractivechart)*