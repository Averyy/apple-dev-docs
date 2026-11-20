# ChartCommon.scatterChart

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A scatter chart.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ChartCommon.scatterChart
```

## Overview

Keynote plots each data point against an X and a Y value axis rather than against a category axis. See `data.shared_xvalues` for how the grid’s rows or columns map onto each series.

Written as `{"scatterChart": …}`: the `scatterChart` form of `ChartCommon`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.chart-common`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `scatterChart` (ScatterChart) *(required)*: A scatter chart. Keynote plots each data point against an X and a Y value axis rather than against a category axis. See `data.shared_xvalues` for how the grid’s rows or columns map onto each series.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chartcommon/scatterchart)*