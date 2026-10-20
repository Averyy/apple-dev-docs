# rotateAxisAngle

**Framework**: WebKit JS  
**Kind**: instm  
**Role**: Instance Method

Returns the result of rotating this matrix by a given vector and angle.

**Availability**:
- Safari Desktop 4.0+
- Safari Mobile 2.0+

## Declaration

```
WebKitCSSMatrix rotateAxisAngle(
    optional unrestricted double x, 
    optional unrestricted double y, 
    optional unrestricted double z, 
    optional unrestricted double angle
);
```

#### Return Value

A new matrix that is the result of rotating this matrix by each of the three rotation matrices about the major axes and angle. The right-hand rule is used to determine the direction of rotation.

#### Discussion

This matrix is not modified by this method.

## Parameters

- `x`: The x component in the vector, in degrees.
- `y`: The y component in the vector, in degrees. If undefined, the x component is used.
- `z`: The z component in the vector, in degrees. If undefined, the x component is used.
- `angle`: The angle of rotation about the axis vector, in degrees.

## See Also

### Applying Operations
- [multiply](./api-1631528-multiply.md)
  Returns the result of multiplying this matrix by a given matrix that is on the right.
- [inverse](./api-1633805-inverse.md)
  Returns the inverse of this matrix.
- [translate](./api-1630758-translate.md)
  Returns the result of translating this matrix by a given vector.
- [scale](./api-1632184-scale.md)
  Returns the result of scaling this matrix by a given vector.
- [rotate](./api-1629773-rotate.md)
  Returns the result of rotating this matrix by a given vector.
- [skewX](./api-1633353-skewx.md)
  Specifies a skew transformation along the x-axis by the given angle.
- [skewY](./api-1631022-skewy.md)
  Specifies a skew transformation along the y-axis by the given angle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/webkitcssmatrix/1632317-rotateaxisangle)*