# setTransform

**Framework**: WebKit JS  
**Kind**: instm

Sets the transformation matrix.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
void setTransform(
    unrestricted float m11, 
    unrestricted float m12, 
    unrestricted float m21, 
    unrestricted float m22, 
    unrestricted float dx, 
    unrestricted float dy
);
```

#### Discussion

Replaces the current transformation matrix with the matrix shown in [`Figure 1`](canvasrenderingcontext2d/1630015-settransform#1965802.md). Each point in the canvas coordinate system is multiplied by the transformation matrix.

![](https://docs-assets.developer.apple.com/published/cf294fc724/matrix_2x_ba813c25-875c-47a3-b3b3-992285a1f6fd.png)

## Parameters

- `m11`: Column 1 row 1 matrix value (a).
- `m12`: Column 1 row 2 matrix value (b).
- `m21`: Column 2 row 1 matrix value (c).
- `m22`: Column 2 row 2 matrix value (d).
- `dx`: X scalar value (e).
- `dy`: Y scalar value (f).

## See Also

- [rotate](canvasrenderingcontext2d/1630553-rotate.md)
  Rotates the canvas coordinate system.
- [scale](canvasrenderingcontext2d/1631799-scale.md)
  Scales the canvas coordinate system horizontally and vertically.
- [transform](canvasrenderingcontext2d/1629911-transform.md)
  Transforms the current transformation matrix using another matrix.
- [translate](canvasrenderingcontext2d/1629441-translate.md)
  Moves the origin of the canvas coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1630015-settransform)*