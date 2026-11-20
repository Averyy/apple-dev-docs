# Stylesheet

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A collection of styles to use as presets for various objects in a document.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Stylesheet
```

## Topics

### Objects
- [object Stylesheet.CharacterStyle](./stylesheet.characterstyle.md)
  A preset that the reader applies to a range of text within a paragraph.
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

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.stylesheet`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `line_styles` ([Stylesheet.ShapeStyle]): The preset styles that you can apply to lines and connection lines. If you omit this property, it defaults to the document’s built-in line styles.
- `shape_styles` ([Stylesheet.ShapeStyle]): The preset styles that you can apply to shapes. If you omit this property, it defaults to the document’s built-in shape styles.
- `textbox_styles` ([Stylesheet.ShapeStyle]): The preset styles that you can apply to text boxes. If you omit this property, it defaults to the document’s built-in text box styles.
- `image_styles` ([Stylesheet.MediaStyle]): The preset styles that you can apply to images. If you omit this property, it defaults to the document’s built-in image styles.
- `movie_styles` ([Stylesheet.MediaStyle]): The preset styles that you can apply to movies. If you omit this property, it defaults to the document’s built-in movie styles.
- `table_style_collections` ([Stylesheet.TableStyleCollection]): The preset table styles. Each entry groups the styles that make up one table style preset: the table as a whole, its cell borders, and the cell and text styles that the body, header rows, header columns, and footer rows use.
- `character_styles` ([Stylesheet.CharacterStyle]): The preset character styles that you can apply to a range of text. If you omit this property, it defaults to the document’s built-in character styles.
- `paragraph_styles` ([Stylesheet.ParagraphStyle]): The preset paragraph styles that you can apply to whole paragraphs. If you omit this property, it defaults to the document’s built-in paragraph styles.
- `list_styles` ([Stylesheet.ListStyle]): The preset list styles, which control bullets and numbering. If you omit this property, it defaults to the document’s built-in list styles.

## See Also

### Styling
- [object KeynoteTheme](./keynotetheme.md)
  The Keynote theme a presentation is based on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/stylesheet)*