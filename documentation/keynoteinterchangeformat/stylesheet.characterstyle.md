# Stylesheet.CharacterStyle

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A preset that the reader applies to a range of text within a paragraph.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Stylesheet.CharacterStyle
```

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.stylesheet.character-style`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `name` (string): The name of the style as shown in Keynote. It’s absent for styles that have no name.
- `properties` (CharacterProperties) *(required)*: The properties that make up the style. When a `preset_identifier` is present, the entry is only a reference and carries no property values; otherwise, this is the style’s complete set of resolved properties.

## See Also

### Objects
- [object Stylesheet.ListStyle](./stylesheet.liststyle.md)
  A preset for bullets and numbering.
- [object Stylesheet.MediaStyle](./stylesheet.mediastyle.md)
  A preset for images and movies.
- [object Stylesheet.ParagraphStyle](./stylesheet.paragraphstyle.md)
  A preset that the reader applies to whole paragraphs, such as a title or body style.
- [object Stylesheet.ShapeStyle](./stylesheet.shapestyle.md)
  A preset for shapes, text boxes, lines, and connection lines.
- [object Stylesheet.TableStyleCollection](./stylesheet.tablestylecollection.md)
  The styles that make up one table style preset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/stylesheet.characterstyle)*