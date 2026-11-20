# ListLevelType

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

One nesting level of a list style.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ListLevelType
```

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.list-level-type`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `label_indent` (number) *(required)*: The indent, in points, from the paragraph’s leading edge to the list label for this level. Validation: minimum value `0`.

  **Minimum**: `0`
- `text_indent` (number) *(required)*: The additional indent from the list label to the paragraph text for this level, as a multiple of the paragraph’s font size rather than in points. Validation: minimum value `0`.

  **Minimum**: `0`
- `label` (ListLabelType) *(required)*: The kind of bullet or number shown at this level.

## See Also

### Lists
- [object ListProperties](./listproperties.md)
  The properties of a list style.
- [type ListLabelType](./listlabeltype.md)
  The kind of label shown at a list level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/listleveltype)*