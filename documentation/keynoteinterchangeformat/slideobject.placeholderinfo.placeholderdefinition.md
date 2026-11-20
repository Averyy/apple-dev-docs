# SlideObject.PlaceholderInfo.PlaceholderDefinition

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The predefined placeholder an object fills.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object SlideObject.PlaceholderInfo.PlaceholderDefinition
```

## Overview

Only a shape or a text box is accepted, and one with `is_visible` set to `false` is still used as the placeholder, keeping its geometry, style, and text. An object of any other kind leaves the placeholder unfilled: it stays on the slide as ordinary content while `is_visible` is `true`, and is dropped altogether when it’s `false`.

## Topics

### Enumerations
- [type SlideObject.PlaceholderInfo.PlaceholderDefinition.Kind](./slideobject.placeholderinfo.placeholderdefinition.kind.md)
  The predefined placeholders that someone can turn on and off on any slide.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.slide-object.placeholder-info.placeholder-definition`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `kind` (SlideObject.PlaceholderInfo.PlaceholderDefinition.Kind) *(required)*: The predefined placeholder this object fills.
- `is_visible` (boolean): Whether this placeholder is turned on for the slide. The default is `true`. When it’s `false`, the entry is still listed in `Slide.contents`, with its geometry and text, but isn’t shown.

  **Default**: `true`


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/slideobject.placeholderinfo.placeholderdefinition)*