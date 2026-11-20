# CanvasObject.shape

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A path with a fill and a stroke.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object CanvasObject.shape
```

## Overview

When `geometry` is absent, the geometry defaults to the smallest rectangle that encloses the path. Shapes can have an open or a closed path; a path is *open* when it has a single subpath, no `closepath` command, and ends that don’t meet. Open shapes can have endpoints, `head` and `tail`. Keynote reads a `path` that is a single, straight, open segment as a line and takes its styling from the line presets. A shape with either `Geometry.width_valid` or `Geometry.height_valid` set to `false` becomes an auto-sizing text box. Paths that aren’t straight lines can contain text that appears inside the shape.

Written as `{"shape": …}`: the `shape` form of `CanvasObject`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.canvas-object`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out. The latest version of `CanvasObject` is 1.2.

  **Default**: `1.2`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `shape` (Shape) *(required)*: A path with a fill and a stroke. When `geometry` is absent, the geometry defaults to the smallest rectangle that encloses the path. Shapes can have an open or a closed path; a path is *open* when it has a single subpath, no `closepath` command, and ends that don’t meet. Open shapes can have endpoints, `head` and `tail`. Keynote reads a `path` that is a single, straight, open segment as a line and takes its styling from the line presets. A shape with either `Geometry.width_valid` or `Geometry.height_valid` set to `false` becomes an auto-sizing text box. Paths that aren’t straight lines can contain text that appears inside the shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/canvasobject/shape)*