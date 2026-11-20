# Text

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

A body of text, such as the text of a text box, a table cell, or a slide’s presenter notes.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(Text.paragraphs | Text.string | Text.text_runs) Text
```

## Mentions

- [Understanding Keynote Interchange Format structure](./understanding-keynote-interchange-format-structure.md)



**Allowed Types**: `Text.paragraphs`, `Text.string`, `Text.text_runs`

## Discussion

It’s carried in exactly one of these forms. The text-run form is accepted when supplying text, but Keynote always writes text as paragraphs or a plain string.

This value takes one of the following forms:

- `paragraphs`: An array of paragraphs of text.
- `string`: A string of Unicode text.
- `text_runs`: An array of runs of text.

## Topics

### Dictionaries
- [object Text.paragraphs](./text/paragraphs.md)
  An array of paragraphs of text.
- [object Text.string](./text/string.md)
  A string of Unicode text.
- [object Text.text_runs](./text/text_runs.md)
  An array of runs of text.

## See Also

### Text
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
- [object LayoutProperties](./layoutproperties.md)
  The text layout properties of a shape style or a column of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/text)*