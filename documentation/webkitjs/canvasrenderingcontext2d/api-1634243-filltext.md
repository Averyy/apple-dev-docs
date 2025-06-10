# fillText

**Framework**: WebKit JS  
**Kind**: instm

Draws a line of text at the specified x,y coordinates, optionally scaled to a specified maximum width.

**Availability**:
- Safari Desktop 4.0+
- Safari Mobile 3.0+

## Declaration

```swift
void fillText(
    DOMString text, 
    unrestricted float x, 
    unrestricted float y, 
    optional unrestricted float maxWidth
);
```

#### Discussion

Text is rendered in the current font, with the current `textBaseline` aligned with the y-coordinate and the current `textAlign` point (left, center, or right) aligned with the x-coordinate.  The `x`, `y`, and `maxWidth` parameter values are in the canvas’s current coordinate system, subject to the current transformation matrix (rotation, scale, and so on).

## Parameters

- `text`: A string containing the text to draw.
- `x`: The x-coordinate of the   point (the left edge, right edge, or center of the text).
- `y`: The y-coordinate of the   point.
- `maxWidth`: The maximum width of the string, in pixels. This parameter is optional. If omitted, the current font size is used and text is clipped if it falls outside the canvas’s clipping region. If a maximum width is specified, the font size is scaled down if necessary to fit the text inside the specified width.

## See Also

- [font](canvasrenderingcontext2d/1632249-font.md)
  A string containing font settings, such as the font family, size, and weight.
- [measureText](canvasrenderingcontext2d/1631690-measuretext.md)
  Determines the width of the bounding box required to render the specified text with the current font settings.
- [strokeText](canvasrenderingcontext2d/1630188-stroketext.md)
  Draws a line of text in outline at the specified x,y coordinates, optionally limited to a specified maximum width.
- [textAlign](canvasrenderingcontext2d/1631811-textalign.md)
  A string that specifies whether text is left-justified, right-justified, or centered.
- [textBaseline](canvasrenderingcontext2d/1629692-textbaseline.md)
  A string that specifies how the bounding box aligns vertically relative to the y-coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1634243-filltext)*