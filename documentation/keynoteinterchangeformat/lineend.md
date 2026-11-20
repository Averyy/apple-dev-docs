# LineEnd

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

A decoration drawn at the end of a connection line or of a shape’s open path, such as an arrowhead.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string LineEnd
```

## Discussion

Decorations that can’t be represented by one of these cases are written as `simple_arrow`.

This value takes one of the following forms:

- `filled_arrow`: A filled arrowhead, with a notched base. Shown in Keynote as “Filled arrow.”
- `filled_circle`: A filled circle. Shown in Keynote as “Filled circle.”
- `filled_diamond`: A filled diamond. Shown in Keynote as “Filled diamond.”
- `filled_square`: A filled square. Shown in Keynote as “Filled square.”
- `inverted_arrow`: A triangular arrowhead that points toward the center of the line instead of away from it. Shown in Keynote as “Inverted arrow.”
- `line`: A straight line across the end of the line, perpendicular to it. Shown in Keynote as Line.
- `none`: No decoration at this end of the line. Shown in Keynote as None.
- `open_arrow`: An open arrowhead. Shown in Keynote as “Open arrow.”
- `open_circle`: An open circle. Shown in Keynote as “Open circle.”
- `open_square`: An open square. Shown in Keynote as “Open square.”
- `simple_arrow`: A simple arrowhead. Shown in Keynote as “Simple arrow.”

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
- [object LineSpacingType](./linespacingtype.md)
  The spacing between lines of text.
- [object LayoutProperties](./layoutproperties.md)
  The text layout properties of a shape style or a column of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/lineend)*