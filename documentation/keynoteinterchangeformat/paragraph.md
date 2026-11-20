# Paragraph

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A paragraph of text.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Paragraph
```

## Topics

### Objects
- [object Paragraph.HyperlinkField](./paragraph.hyperlinkfield.md)
  A link with styled display text.
### Enumerations
- [type Paragraph.BreakType](./paragraph.breaktype.md)
  The break that ends a paragraph.
- [type Paragraph.Constituent](./paragraph.constituent.md)
  An element of a paragraph’s contents.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.paragraph`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `style` (ParagraphProperties): The paragraph properties for this paragraph. When `preset_identifier` is set, the paragraph inherits from a stylesheet paragraph style; otherwise, the properties are given here.
- `list_style` (ListProperties): The list properties for this paragraph. When `preset_identifier` is set, the paragraph inherits from a stylesheet list style; otherwise, the properties are given here. If `list_style` is absent, the paragraph keeps the list style already in effect (the preceding paragraph’s, or the one the containing text starts with), so ending a list takes an explicit list style whose levels carry no label.
- `list_start` (integer): The number at which list numbering restarts for this paragraph. If it’s omitted or 0, numbering continues from the preceding list item. Values above 4294967295 are clamped.
- `list_level` (integer): The zero-based list level of the paragraph, where `0` is the top level; if it’s absent, the level is 0. The level selects which entry of the list style’s `ListProperties.levels` supplies the indent and the label. Levels outside the range `0` through 8 are adjusted to the nearest supported level rather than rejected.
- `writing_direction` (WritingDirectionType): The writing direction of the paragraph, used only when the paragraph style leaves the direction natural. A direction on the paragraph style takes precedence, and the document’s direction applies when neither sets one.
- `contents` ([Paragraph.Constituent]): The ordered contents of the paragraph: text runs, inline objects, and links. The break that ends the paragraph isn’t included, and the property is omitted for an empty paragraph.
- `break_type` (Paragraph.BreakType): The break that ends the paragraph. By default, paragraphs are separated by a normal paragraph break.

## See Also

### Text
- [type Text](./text.md)
  A body of text, such as the text of a text box, a table cell, or a slide’s presenter notes.
- [object TextRun](./textrun.md)
  A run of text with a single character style.
- [object TextStroke](./textstroke.md)
  A stroke for text, or a special value for no stroke.
- [object Textbox](./textbox.md)
  A container for text that someone places directly on a slide or slide layout.
- [object ParagraphProperties](./paragraphproperties.md)
  The paragraph-level properties of text.
- [object CharacterProperties](./characterproperties.md)
  The character-level properties of text.
- [type WritingDirectionType](./writingdirectiontype.md)
  The writing direction of the text.
- [type LineEnd](./lineend.md)
  A decoration drawn at the end of a connection line or of a shape’s open path, such as an arrowhead.
- [object LineSpacingType](./linespacingtype.md)
  The spacing between lines of text.
- [object LayoutProperties](./layoutproperties.md)
  The text layout properties of a shape style or a column of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/paragraph)*