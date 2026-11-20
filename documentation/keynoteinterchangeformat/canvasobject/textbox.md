# CanvasObject.textbox

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A container for text that someone places directly on a slide or slide layout.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object CanvasObject.textbox
```

## Overview

It takes its typography and background from the text-box presets rather than the shape presets. A `shape` can hold text too.

Written as `{"textbox": …}`: the `textbox` form of `CanvasObject`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.canvas-object`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out. The latest version of `CanvasObject` is 1.2.

  **Default**: `1.2`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `textbox` (Textbox) *(required)*: A container for text that someone places directly on a slide or slide layout. It takes its typography and background from the text-box presets rather than the shape presets. A `shape` can hold text too.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/canvasobject/textbox)*