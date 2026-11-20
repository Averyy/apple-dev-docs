# WritingDirectionType

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The writing direction of the text.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string WritingDirectionType
```

## Discussion

This value takes one of the following forms:

- `left_to_right`: Lay the text out left to right.
- `natural`: Take the writing direction from the surrounding context: the paragraph style first, then the document. A paragraph that defers in this way carries no direction of its own.
- `right_to_left`: Lay the text out right to left.

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
- [type LineEnd](./lineend.md)
  A decoration drawn at the end of a connection line or of a shape’s open path, such as an arrowhead.
- [object LineSpacingType](./linespacingtype.md)
  The spacing between lines of text.
- [object LayoutProperties](./layoutproperties.md)
  The text layout properties of a shape style or a column of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/writingdirectiontype)*