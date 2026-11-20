# SlideObject.PlaceholderInfo.tagged

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A placeholder that has a tag associated with it. It can be an image, a movie, a shape, or a text box.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object SlideObject.PlaceholderInfo.tagged
```

## Overview

Written as `{"tagged": …}`: the `tagged` form of `SlideObject.PlaceholderInfo`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.slide-object.placeholder-info`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `tagged` (string) *(required)*: A placeholder that has a tag associated with it. It can be an image, a movie, a shape, or a text box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/slideobject.placeholderinfo/tagged)*