# CanvasObject.connectionLine

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A line drawn from its tail end to its head end, each of which can attach to another object.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object CanvasObject.connectionLine
```

## Overview

The route comes from `tail`, `head`, and (for a curved or corner line) the control position carried by `line_type`. Because the line’s position and size follow from the route, `geometry` only transforms the supplied end points and control position, and is omitted when Keynote writes out a connection line.

Written as `{"connectionLine": …}`: the `connectionLine` form of `CanvasObject`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.canvas-object`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out. The latest version of `CanvasObject` is 1.2.

  **Default**: `1.2`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `connectionLine` (ConnectionLine) *(required)*: A line drawn from its tail end to its head end, each of which can attach to another object. The route comes from `tail`, `head`, and (for a curved or corner line) the control position carried by `line_type`. Because the line’s position and size follow from the route, `geometry` only transforms the supplied end points and control position, and is omitted when Keynote writes out a connection line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/canvasobject/connectionline)*