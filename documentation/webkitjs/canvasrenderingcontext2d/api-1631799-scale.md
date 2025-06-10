# scale

**Framework**: WebKit JS  
**Kind**: instm

Scales the canvas coordinate system horizontally and vertically.

**Availability**:
- Safari Desktop 3.0+
- Safari Mobile 1.0+

## Declaration

```swift
void scale(
    unrestricted float sx, 
    unrestricted float sy
);
```

#### Discussion

Drawing operations can be scaled up or down by setting the scale. All drawing operation x and y coordinates, widths and heights are multiplied by the scalars. The scalars must be nonzero, but may be negative (which reverses the sign of subsequent x and y coordinates.

## Parameters

- `sx`: The horizontal scalar.
- `sy`: The vertical scalar.

## See Also

- [rotate](canvasrenderingcontext2d/1630553-rotate.md)
  Rotates the canvas coordinate system.
- [setTransform](canvasrenderingcontext2d/1630015-settransform.md)
  Sets the transformation matrix.
- [transform](canvasrenderingcontext2d/1629911-transform.md)
  Transforms the current transformation matrix using another matrix.
- [translate](canvasrenderingcontext2d/1629441-translate.md)
  Moves the origin of the canvas coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1631799-scale)*