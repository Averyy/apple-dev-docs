# Size

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A width and height in whichever coordinate space the property using it defines.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Size
```

## Overview

A size is always unrotated; `Geometry` covers how an object’s size relates to its rotation and its position.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.size`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `width` (number) *(required)*: The width, in points.
- `height` (number) *(required)*: The height, in points.

## See Also

### Common types
- [object Group](./group.md)
  An ordered set of objects that behave as one when selected, moved, or transformed.
- [object Label](./label.md)
  Styled text that the reader uses as a title or caption on an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/size)*