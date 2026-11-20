# CanvasObject.group

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

An ordered set of objects that behave as one when selected, moved, or transformed.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object CanvasObject.group
```

## Overview

The group’s position and size are those of the smallest rectangle enclosing its children, so the reader uses only the rotation and flip from its `geometry`.

Written as `{"group": …}`: the `group` form of `CanvasObject`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.canvas-object`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out. The latest version of `CanvasObject` is 1.2.

  **Default**: `1.2`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `group` (Group) *(required)*: An ordered set of objects that behave as one when selected, moved, or transformed. The group’s position and size are those of the smallest rectangle enclosing its children, so the reader uses only the rotation and flip from its `geometry`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/canvasobject/group)*