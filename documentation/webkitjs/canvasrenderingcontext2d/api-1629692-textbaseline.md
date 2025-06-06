# textBaseline

**Framework**: Webkitjs  
**Kind**: instp

A string that specifies how the bounding box aligns vertically relative to the y-coordinate.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
attribute DOMString textBaseline;
```

#### Discussion

The y-coordinate of a line of text corresponds to the point on the text glyphs specified by `textBaseline`. Possible values are `top`, `hanging`, `middle`, `alphabetic` (default), `ideographic`, and `bottom`. The position of each value on the text glyphs is illustrated in [`Figure 1`](canvasrenderingcontext2d/1629692-textbaseline#1965801.md).

![](https://docs-assets.developer.apple.com/published/cf294fc724/baselines_2x_5dc481c3-5838-4b65-8e38-df1fedbac7ee.png)

See [`textBaseline Constants`](canvasrenderingcontext2d/textbaseline_constants.md) for descriptions of the constants.

## See Also

- [fillText](canvasrenderingcontext2d/1634243-filltext.md)
  Draws a line of text at the specified x,y coordinates, optionally scaled to a specified maximum width.
- [font](canvasrenderingcontext2d/1632249-font.md)
  A string containing font settings, such as the font family, size, and weight.
- [measureText](canvasrenderingcontext2d/1631690-measuretext.md)
  Determines the width of the bounding box required to render the specified text with the current font settings.
- [strokeText](canvasrenderingcontext2d/1630188-stroketext.md)
  Draws a line of text in outline at the specified x,y coordinates, optionally limited to a specified maximum width.
- [textAlign](canvasrenderingcontext2d/1631811-textalign.md)
  A string that specifies whether text is left-justified, right-justified, or centered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1629692-textbaseline)*