# Color

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A color that the reader uses as part of a displayed object, in one of the forms the format supports.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Color
```

## Overview

Every form resolves to a color that can be displayed, so a reader never has to handle one that can’t be.

A color given as red, green, blue, and alpha components in a named RGB color space, together with an HDR headroom value.

## Topics

### Objects
- [object Color.RGBA](./color.rgba.md)
  A color in an RGB-component color space, together with its alpha and an HDR headroom value.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.color`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `rgba` (Color.RGBA) *(required)*: A color given as red, green, blue, and alpha components in a named RGB color space, together with an HDR headroom value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/color)*