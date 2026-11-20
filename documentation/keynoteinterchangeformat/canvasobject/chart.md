# CanvasObject.chart

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

An object that plots a grid of data in a visual style such as column, pie, or scatter.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object CanvasObject.chart
```

## Overview

Write a chart as an object with a single key, which names its chart type, such as `column` or `pie`, and holds that type’s settings. The chart type decides only how Keynote plots the series: every chart type uses the same chart data, so when you change a chart’s type, that change replots the existing series without rewriting the data.

Written as `{"chart": …}`: the `chart` form of `CanvasObject`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.canvas-object`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out. The latest version of `CanvasObject` is 1.2.

  **Default**: `1.2`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `chart` (Chart) *(required)*: An object that plots a grid of data in a visual style such as column, pie, or scatter. Write a chart as an object with a single key, which names its chart type, such as `column` or `pie`, and holds that type’s settings. The chart type decides only how Keynote plots the series: every chart type uses the same chart data, so when you change a chart’s type, that change replots the existing series without rewriting the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/canvasobject/chart)*