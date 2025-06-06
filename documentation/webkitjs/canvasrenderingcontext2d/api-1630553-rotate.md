# rotate

**Framework**: Webkitjs  
**Kind**: instm

Rotates the canvas coordinate system.

**Availability**:
- Safari Desktop 3.0+
- Safari Mobile 1.0+

## Declaration

```swift
void rotate(
    unrestricted float angle
);
```

#### Discussion

Changes to the coordinate system affect subsequent drawing operations, but do not affect anything already drawn. Rotation is clockwise around the origin, which by default is the upper-left corner.

## Parameters

- `angle`: The amount of rotation, in radians, clockwise.

## See Also

- [scale](canvasrenderingcontext2d/1631799-scale.md)
  Scales the canvas coordinate system horizontally and vertically.
- [setTransform](canvasrenderingcontext2d/1630015-settransform.md)
  Sets the transformation matrix.
- [transform](canvasrenderingcontext2d/1629911-transform.md)
  Transforms the current transformation matrix using another matrix.
- [translate](canvasrenderingcontext2d/1629441-translate.md)
  Moves the origin of the canvas coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1630553-rotate)*