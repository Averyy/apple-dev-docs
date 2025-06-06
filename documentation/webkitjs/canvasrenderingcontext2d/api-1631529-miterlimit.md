# miterLimit

**Framework**: Webkitjs  
**Kind**: instp

A floating-point number that controls the miter limit ratio for mitered line joins.

**Availability**:
- Safari Desktop 3.0+
- Safari Mobile 1.0+

## Declaration

```swift
attribute unrestricted float miterLimit;
```

#### Discussion

The `miterLimit` value must be a nonzero positive number. This property affects the appearance of line joins when the `lineJoin` property is set to `miter`.

The miter length is the distance from the point where the join occurs to the intersection of the line edges on the outside of the join. The miter limit ratio is the maximum allowed ratio of the miter length to half the line width. If the miter length would cause the miter limit ratio to be exceeded, the second triangle of the miter join is not rendered, and the join is beveled.

## See Also

- [fill](canvasrenderingcontext2d/1631011-fill.md)
  Fills the current path using the current fill color, gradient, or pattern.
- [fillStyle](canvasrenderingcontext2d/1633959-fillstyle.md)
  A CSS color, a gradient, or a pattern used to fill shapes and text.
- [lineCap](canvasrenderingcontext2d/1629505-linecap.md)
  A string specifying the type of end cap to put on lines to be drawn using `lineTo()`.
- [lineJoin](canvasrenderingcontext2d/1629229-linejoin.md)
  A string specifying the manner in which line joins are drawn.
- [lineWidth](canvasrenderingcontext2d/1630379-linewidth.md)
  A floating-point number that controls the width of lines and strokes, in pixels.
- [stroke](canvasrenderingcontext2d/1634233-stroke.md)
  Draws the outline of the current path using the current stroke style and line width.
- [strokeStyle](canvasrenderingcontext2d/1634470-strokestyle.md)
  A CSS color, a gradient, or a pattern used to stroke lines and shapes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1631529-miterlimit)*