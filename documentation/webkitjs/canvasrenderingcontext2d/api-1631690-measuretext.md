# measureText

**Framework**: WebKit JS  
**Kind**: instm

Determines the width of the bounding box required to render the specified text with the current font settings.

**Availability**:
- Safari Desktop 4.0+
- Safari Mobile 3.0+

## Declaration

```swift
TextMetrics measureText(
    DOMString text
);
```

#### Return_value

An object whose `width` property contains the width in pixels of the bounding box needed to render the text without clipping.

#### Discussion

Use this method to determine how much space is needed to render a string, or to measure the width of an existing string.

## Parameters

- `text`: A string containing the text to measure.

## See Also

- [fillText](canvasrenderingcontext2d/1634243-filltext.md)
  Draws a line of text at the specified x,y coordinates, optionally scaled to a specified maximum width.
- [font](canvasrenderingcontext2d/1632249-font.md)
  A string containing font settings, such as the font family, size, and weight.
- [strokeText](canvasrenderingcontext2d/1630188-stroketext.md)
  Draws a line of text in outline at the specified x,y coordinates, optionally limited to a specified maximum width.
- [textAlign](canvasrenderingcontext2d/1631811-textalign.md)
  A string that specifies whether text is left-justified, right-justified, or centered.
- [textBaseline](canvasrenderingcontext2d/1629692-textbaseline.md)
  A string that specifies how the bounding box aligns vertically relative to the y-coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1631690-measuretext)*