# ChartAxisCommon.AxisLabelOrientation

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The orientation of an axis’s labels relative to the axis.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(object | string("horizontal" | "left_diagonal" | "left_vertical" | "parallel" | "perpendicular" | "right_diagonal" | "right_vertical")) ChartAxisCommon.AxisLabelOrientation
```



**Allowed Types**: `object`, `string("horizontal" | "left_diagonal" | "left_vertical" | "parallel" | "perpendicular" | "right_diagonal" | "right_vertical")`

## Overview

Rotating the labels lets long labels stay legible without widening the chart.

Labels rotated by the given number of degrees, measured counterclockwise. The value is written in the range `0` to `360`; a value outside that range is read as the equivalent angle within it. An angle that matches one of the five named straight-axis orientations is written as that case instead.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.chart-axis-common.axis-label-orientation`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `custom` (number) *(required)*: Labels rotated by the given number of degrees, measured counterclockwise. The value is written in the range `0` to `360`; a value outside that range is read as the equivalent angle within it. An angle that matches one of the five named straight-axis orientations is written as that case instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chartaxiscommon.axislabelorientation)*