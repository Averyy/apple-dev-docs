# CanvasObject.movie

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A movie or animated image defined by a resource with optional styling.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object CanvasObject.movie
```

## Overview

When `geometry` is omitted, the object takes the resource’s natural size, falling back to 640 × 480 points when the reader cannot measure that size. Placed inline in the text of a text box or shape, an unplayable movie removes that whole text box or shape, including all of its text; in a slide’s presenter notes, it stops the document from loading.

Written as `{"movie": …}`: the `movie` form of `CanvasObject`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.canvas-object`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out. The latest version of `CanvasObject` is 1.2.

  **Default**: `1.2`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `movie` (Movie) *(required)*: A movie or animated image defined by a resource with optional styling. When `geometry` is omitted, the object takes the resource’s natural size, falling back to 640 × 480 points when the reader cannot measure that size. Placed inline in the text of a text box or shape, an unplayable movie removes that whole text box or shape, including all of its text; in a slide’s presenter notes, it stops the document from loading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/canvasobject/movie)*