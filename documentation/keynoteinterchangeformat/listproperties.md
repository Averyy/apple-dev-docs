# ListProperties

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The properties of a list style.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ListProperties
```

## Overview

A `preset_identifier` here is matched against the document stylesheet’s list styles before the presets in `presets.json`, and an identifier that matches neither is silently ignored, so `levels` must be written here for a label to be drawn. An omitted `font_color`, `font_name`, `shadow`, or `writing_direction` follows the paragraph’s text styling, and a `null` clears it instead.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.list-properties`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `font_color` ((Color | null)): The color applied to list labels and numbers.

  **Allowed Types**: `Color`, `null`
- `font_name` ((string | null)): The PostScript name of the font used for list labels and numbers. Only the name is carried, not the font itself, so on a device that doesn’t have the font and can’t download it, the labels and numbers are drawn in a substitute font.

  **Allowed Types**: `string`, `null`
- `writing_direction` ((WritingDirectionType | null)): The writing direction: left to right, right to left, or natural for the content.

  **Allowed Types**: `WritingDirectionType`, `null`
- `shadow` ((Shadow | null)): The shadow applied to the list label or number.

  **Allowed Types**: `Shadow`, `null`
- `levels` (([ListLevelType] | null)): The list definition for each nesting level, with index `0` the top level. At most 9 levels are used: any beyond the ninth are ignored, and if fewer are supplied, the last one is repeated for the remaining levels.

  **Allowed Types**: `[ListLevelType]`, `null`

## See Also

### Lists
- [object ListLevelType](./listleveltype.md)
  One nesting level of a list style.
- [type ListLabelType](./listlabeltype.md)
  The kind of label shown at a list level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/listproperties)*