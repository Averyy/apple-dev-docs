# Label

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

Styled text that the reader uses as a title or caption on an object.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Label
```

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.label`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `layout_properties` (LayoutProperties): The layout overrides, such as insets and columns, for the label’s text. If it’s absent, the theme’s text layout settings are used.
- `paragraph_properties` (ParagraphProperties): The paragraph-level style, such as alignment and spacing, for the label’s text. If it’s absent, the theme’s paragraph style is used.
- `text` (Text): The text of the title or caption.
- `is_visible` (boolean): Whether the title or caption is visible. Defaults to `true`; when `false`, the title or caption is hidden but its text and styling are preserved.

  **Default**: `true`

## See Also

### Common types
- [object Group](./group.md)
  An ordered set of objects that behave as one when selected, moved, or transformed.
- [object Size](./size.md)
  A width and height in whichever coordinate space the property using it defines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/label)*