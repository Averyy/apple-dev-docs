# textBaseline

**Framework**: WebKit JS  
**Kind**: instp  
**Role**: Instance Property

A string that specifies how the bounding box aligns vertically relative to the y-coordinate.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
attribute DOMString textBaseline;
```

## Discussion

The y-coordinate of a line of text corresponds to the point on the text glyphs specified by `textBaseline`. Possible values are `top`, `hanging`, `middle`, `alphabetic` (default), `ideographic`, and `bottom`. The position of each value on the text glyphs is illustrated in [Figure 1](./api-1629692-textbaseline.md#1965801).

![](https://docs-assets.developer.apple.com/published/cf294fc724/baselines_2x_5dc481c3-5838-4b65-8e38-df1fedbac7ee.png)

See [textBaseline Constants](./textbaseline_constants.md) for descriptions of the constants.

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
- [textAlign](./api-1631811-textalign.md)
  A string that specifies whether text is left-justified, right-justified, or centered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1629692-textbaseline)*