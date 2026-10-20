# skewY

**Framework**: WebKit JS  
**Kind**: instm  
**Role**: Instance Method

Specifies a skew transformation along the y-axis by the given angle.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
WebKitCSSMatrix skewY(
    optional unrestricted double angle
);
```

#### Return Value

A new matrix that is the result of skewing this matrix by the specified angle along the y-axis.

## Parameters

- `angle`: The angle amount in degrees to skew.

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
- [rotateAxisAngle](./api-1632317-rotateaxisangle.md)
  Returns the result of rotating this matrix by a given vector and angle.
- [skewX](./api-1633353-skewx.md)
  Specifies a skew transformation along the x-axis by the given angle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/webkitcssmatrix/1631022-skewy)*