# LayoutProperties

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The text layout properties of a shape style or a column of text.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object LayoutProperties
```

## Overview

An omitted property is inherited from the preset named by `preset_identifier`; otherwise, it’s inherited from the shape or text box style’s preset or, for a column style, from the style named by `parent`. Anything still unset takes the property’s built-in default, and a `null` clears it instead.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.layout-properties`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `columns` ((ColumnMetrics | null)): The number and spacing of the columns. The default is a single column of full width.

  **Allowed Types**: `ColumnMetrics`, `null`
- `continuous` ((boolean | null)): Whether text using this layout continues on the page; if false, it always begins on a new page. It applies only to column layout and has no effect on shapes or text boxes.

  **Allowed Types**: `boolean`, `null`
- `margins` ((Insets | null)): The margins, in points, between the edges of the text container and the column layout inside it. They apply only to column layout; for the inset applied to any text container, see `padding`.

  **Allowed Types**: `Insets`, `null`
- `padding` ((Insets | null)): The space, in points, between the edges of the text container and the text laid out inside it, on all four edges. Unlike `margins`, which position the column layout within the container’s text area, padding insets that whole text area and applies to any text container.

  **Allowed Types**: `Insets`, `null`
- `shrink_to_fit` ((boolean | null)): Whether the text is scaled down to fit inside the container, to as little as 40% of the given font sizes; text that still doesn’t fit at that scale overflows. The container keeps its own size. The default is `false`.

  **Allowed Types**: `boolean`, `null`
- `vertical_alignment` ((VerticalAlignmentType | null)): The vertical alignment of text within a container.

  **Allowed Types**: `VerticalAlignmentType`, `null`
- `vertical_text` ((boolean | null)): Whether the text is vertical.

  **Allowed Types**: `boolean`, `null`
- `writing_direction` ((WritingDirectionType | null)): The writing direction of the text: left to right, right to left, or natural for the content.

  **Allowed Types**: `WritingDirectionType`, `null`

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
- [object LineSpacingType](./linespacingtype.md)
  The spacing between lines of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/layoutproperties)*