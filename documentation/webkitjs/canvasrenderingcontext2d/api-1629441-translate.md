# translate

**Framework**: WebKit JS  
**Kind**: instm  
**Role**: Instance Method

Moves the origin of the canvas coordinate system.

**Availability**:
- Safari Desktop 3.0+
- Safari Mobile 1.0+

## Declaration

```
void translate(
    unrestricted float tx, 
    unrestricted float ty
);
```

#### Discussion

The specified point x,y in the canvas coordinate system becomes the point 0,0 and the entire coordinate system is translated accordingly.

## Parameters

- `tx`: The x-coordinate in the current canvas coordinate system to be made the new origin.
- `ty`: The y-coordinate in the current canvas coordinate system to be made the new origin.

## See Also

### Changing the Coordinate System
- [rotate](./api-1630553-rotate.md)
  Rotates the canvas coordinate system.
- [scale](./api-1631799-scale.md)
  Scales the canvas coordinate system horizontally and vertically.
- [setTransform](./api-1630015-settransform.md)
  Sets the transformation matrix.
- [transform](./api-1629911-transform.md)
  Transforms the current transformation matrix using another matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1629441-translate)*