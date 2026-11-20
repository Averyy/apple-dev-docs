# ChartAxisCommon.chartValueAxis

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A numeric axis that a chart’s values are measured against.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ChartAxisCommon.chartValueAxis
```

## Overview

The same type serves every value axis a chart has, so a property takes effect only where that axis supports it.

Written as `{"chartValueAxis": …}`: the `chartValueAxis` form of `ChartAxisCommon`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.chart-axis-common`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `chartValueAxis` (ChartValueAxis) *(required)*: A numeric axis that a chart’s values are measured against. The same type serves every value axis a chart has, so a property takes effect only where that axis supports it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chartaxiscommon/chartvalueaxis)*