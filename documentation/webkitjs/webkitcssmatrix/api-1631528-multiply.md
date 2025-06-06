# multiply

**Framework**: Webkitjs  
**Kind**: instm

Returns the result of multiplying this matrix by a given matrix that is on the right.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
WebKitCSSMatrix multiply(
    optional WebKitCSSMatrix? secondMatrix
);
```

#### Return_value

A new matrix that is the result of multiplying this matrix by the given matrix.

#### Discussion

The given matrix is on the right of the multiplication. This matrix is not modified by this method.

## Parameters

- `secondMatrix`: The matrix to multiply.

## See Also

- [inverse](webkitcssmatrix/1633805-inverse.md)
  Returns the inverse of this matrix.
- [translate](webkitcssmatrix/1630758-translate.md)
  Returns the result of translating this matrix by a given vector.
- [scale](webkitcssmatrix/1632184-scale.md)
  Returns the result of scaling this matrix by a given vector.
- [rotate](webkitcssmatrix/1629773-rotate.md)
  Returns the result of rotating this matrix by a given vector.
- [rotateAxisAngle](webkitcssmatrix/1632317-rotateaxisangle.md)
  Returns the result of rotating this matrix by a given vector and angle.
- [skewX](webkitcssmatrix/1633353-skewx.md)
  Specifies a skew transformation along the x-axis by the given angle.
- [skewY](webkitcssmatrix/1631022-skewy.md)
  Specifies a skew transformation along the y-axis by the given angle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/webkitcssmatrix/1631528-multiply)*