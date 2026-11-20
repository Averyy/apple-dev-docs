# ChartCommon.stackedBar3Dchart

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A 3D stacked horizontal bar chart.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ChartCommon.stackedBar3Dchart
```

## Overview

3D appearance settings such as rotation, depth, lighting, and textures aren’t included: rotation and depth take the default for this chart type, and lighting and a textured series’ fill come from the chart’s style.

Written as `{"stackedBar3Dchart": …}`: the `stackedBar3Dchart` form of `ChartCommon`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.chart-common`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `stackedBar3Dchart` (StackedBar3DChart) *(required)*: A 3D stacked horizontal bar chart. 3D appearance settings such as rotation, depth, lighting, and textures aren’t included: rotation and depth take the default for this chart type, and lighting and a textured series’ fill come from the chart’s style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chartcommon/stackedbar3dchart)*