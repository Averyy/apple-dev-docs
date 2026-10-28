# lineWidth

**Framework**: WebKit JS  
**Kind**: instp  
**Role**: Instance Property

A floating-point number that controls the width of lines and strokes, in pixels.

**Availability**:
- Safari Desktop 3.0+
- Safari Mobile 1.0+

## Declaration

```
attribute unrestricted float lineWidth;
```

## Discussion

The default line width is 1 pixel. This property specifies not only the width of lines drawn with `lineTo()`, but also the stroke thickness of any `stroke()` operation.

## See Also

### Filling and Stroking Lines and Paths
- [fill](./api-1631011-fill.md)
  Fills the current path using the current fill color, gradient, or pattern.
- [fillStyle](./api-1633959-fillstyle.md)
  A CSS color, a gradient, or a pattern used to fill shapes and text.
- [lineCap](./api-1629505-linecap.md)
  A string specifying the type of end cap to put on lines to be drawn using `lineTo()`.
- [lineJoin](./api-1629229-linejoin.md)
  A string specifying the manner in which line joins are drawn.
- [miterLimit](./api-1631529-miterlimit.md)
  A floating-point number that controls the miter limit ratio for mitered line joins.
- [stroke](./api-1634233-stroke.md)
  Draws the outline of the current path using the current stroke style and line width.
- [strokeStyle](./api-1634470-strokestyle.md)
  A CSS color, a gradient, or a pattern used to stroke lines and shapes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1630379-linewidth)*