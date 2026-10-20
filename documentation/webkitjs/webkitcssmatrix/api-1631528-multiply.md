# multiply

**Framework**: WebKit JS  
**Kind**: instm  
**Role**: Instance Method

Returns the result of multiplying this matrix by a given matrix that is on the right.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
WebKitCSSMatrix multiply(
    optional WebKitCSSMatrix? secondMatrix
);
```

#### Return Value

A new matrix that is the result of multiplying this matrix by the given matrix.

#### Discussion

The given matrix is on the right of the multiplication. This matrix is not modified by this method.

## Parameters

- `secondMatrix`: The matrix to multiply.

## See Also

### Applying Operations
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
- [skewY](./api-1631022-skewy.md)
  Specifies a skew transformation along the y-axis by the given angle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/webkitcssmatrix/1631528-multiply)*