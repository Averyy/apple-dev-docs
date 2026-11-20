# Image.InstantAlphaPath

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A masking path applied to an image to clip out its background, with only the area it encloses shown.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Image.InstantAlphaPath
```

## Overview

A `path` that comes out empty, encloses no area, or lies outside the image is discarded, and the image keeps its background.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.image.instant-alpha-path`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `path` (string) *(required)*: The outline of the visible area, in the syntax of an SVG `<path>` element’s `d` attribute, with these differences: only the moveto (`M`), lineto (`L`), cubic and quadratic curveto (`C` and `Q`), and closepath (`Z`) commands are read; every segment must have its own command letter; separators must be spaces; and a lowercase command is read as absolute rather than relative. The value must begin with a moveto command. Reading stops at the first token that can’t be read; the outline up to there is kept, including the interrupted segment, with its missing numbers taken as 0.
- `size` (Size): If present, `path` is treated as relative to a rectangle at the origin with this size, and then stretched to cover the natural size of the image. If absent, it’s assumed to equal the natural size of the image.

## See Also

### Objects
- [object Image.Mask](./image.mask.md)
  The crop applied to an image, clipping the resource to a path within the mask’s own geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/image.instantalphapath)*