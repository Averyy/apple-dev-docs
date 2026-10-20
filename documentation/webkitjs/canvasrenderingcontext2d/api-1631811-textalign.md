# textAlign

**Framework**: WebKit JS  
**Kind**: instp  
**Role**: Instance Property

A string that specifies whether text is left-justified, right-justified, or centered.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
attribute DOMString textAlign;
```

#### Discussion

Possible values are `start` (default), `end`, `left`, `right`, and `center`. The values `start` and `end` are equivalent to either `left` or `right`, depending on the text direction.

## See Also

### Drawing Text
- [fillText](./api-1634243-filltext.md)
  Draws a line of text at the specified x,y coordinates, optionally scaled to a specified maximum width.
- [font](./api-1632249-font.md)
  A string containing font settings, such as the font family, size, and weight.
- [measureText](./api-1631690-measuretext.md)
  Determines the width of the bounding box required to render the specified text with the current font settings.
- [strokeText](./api-1630188-stroketext.md)
  Draws a line of text in outline at the specified x,y coordinates, optionally limited to a specified maximum width.
- [textBaseline](./api-1629692-textbaseline.md)
  A string that specifies how the bounding box aligns vertically relative to the y-coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1631811-textalign)*