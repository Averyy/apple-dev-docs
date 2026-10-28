# rotate

**Framework**: WebKit JS  
**Kind**: instm  
**Role**: Instance Method

Rotates the canvas coordinate system.

**Availability**:
- Safari Desktop 3.0+
- Safari Mobile 1.0+

## Declaration

```
void rotate(
    unrestricted float angle
);
```

## Discussion

Changes to the coordinate system affect subsequent drawing operations, but do not affect anything already drawn. Rotation is clockwise around the origin, which by default is the upper-left corner.

## Parameters

- `angle`: The amount of rotation, in radians, clockwise.

## See Also

### Changing the Coordinate System
- [scale](./api-1631799-scale.md)
  Scales the canvas coordinate system horizontally and vertically.
- [setTransform](./api-1630015-settransform.md)
  Sets the transformation matrix.
- [transform](./api-1629911-transform.md)
  Transforms the current transformation matrix using another matrix.
- [translate](./api-1629441-translate.md)
  Moves the origin of the canvas coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1630553-rotate)*