# LineSpacingType

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The spacing between lines of text.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object LineSpacingType
```

## Topics

### Enumerations
- [type LineSpacingType.LineSpacingKindType](./linespacingtype.linespacingkindtype.md)
  A kind of line spacing.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.line-spacing-type`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `kind` (LineSpacingType.LineSpacingKindType): The kind of line spacing, which sets how `value` is interpreted: `relative` treats it as a multiple of the natural line height; `minimum`, `exact`, and `maximum` treat it as a line height in points; and `between` treats it as extra space added between lines. The default is `relative`.
- `value` (number) *(required)*: The amount of line spacing, interpreted according to `kind`: a multiplier for `relative` (1.0 is single-spaced, 2.0 double-spaced), otherwise a measurement in points. A negative value is meaningful only for `between`, where it tightens the space between lines.

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
- [object Paragraph](./paragraph.md)
  A paragraph of text.
- [object ParagraphProperties](./paragraphproperties.md)
  The paragraph-level properties of text.
- [object CharacterProperties](./characterproperties.md)
  The character-level properties of text.
- [type WritingDirectionType](./writingdirectiontype.md)
  The writing direction of the text.
- [type LineEnd](./lineend.md)
  A decoration drawn at the end of a connection line or of a shape’s open path, such as an arrowhead.
- [object LayoutProperties](./layoutproperties.md)
  The text layout properties of a shape style or a column of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/linespacingtype)*