# Image.Mask

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The crop applied to an image, clipping the resource to a path within the mask’s own geometry.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Image.Mask
```

## Overview

The part outside the crop is retained in the file rather than trimmed away. A mask whose path encloses no area would hide the image completely, so it’s discarded when it’s read, and the image isn’t cropped.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.image.mask`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `geometry` (Geometry): The geometry of the frame used to crop the image’s resource, in the same coordinate space as the image’s own `geometry`. Either this or `path` must be present.
- `path` (Path): The path used to crop the image’s resource, anchored within `geometry` if present. Either this or `geometry` must be present; if absent and `geometry` is used, the path is assumed to be rectangular.

## See Also

### Objects
- [object Image.InstantAlphaPath](./image.instantalphapath.md)
  A masking path applied to an image to clip out its background, with only the area it encloses shown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/image.mask)*