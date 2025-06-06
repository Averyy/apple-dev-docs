# scale

**Framework**: Webkitjs  
**Kind**: instm

Returns the result of scaling this matrix by a given vector.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
WebKitCSSMatrix scale(
    optional unrestricted double scaleX, 
    optional unrestricted double scaleY, 
    optional unrestricted double scaleZ
);
```

#### Return_value

A new matrix that is the result of scaling this matrix.

#### Discussion

This matrix is not modified by this method.

## Parameters

- `scaleX`: The x component in the vector.
- `scaleY`: The y component in the vector. If undefined, the x component is used.
- `scaleZ`: The z component in the vector. If undefined,   is used.

## See Also

- [multiply](webkitcssmatrix/1631528-multiply.md)
  Returns the result of multiplying this matrix by a given matrix that is on the right.
- [inverse](webkitcssmatrix/1633805-inverse.md)
  Returns the inverse of this matrix.
- [translate](webkitcssmatrix/1630758-translate.md)
  Returns the result of translating this matrix by a given vector.
- [rotate](webkitcssmatrix/1629773-rotate.md)
  Returns the result of rotating this matrix by a given vector.
- [rotateAxisAngle](webkitcssmatrix/1632317-rotateaxisangle.md)
  Returns the result of rotating this matrix by a given vector and angle.
- [skewX](webkitcssmatrix/1633353-skewx.md)
  Specifies a skew transformation along the x-axis by the given angle.
- [skewY](webkitcssmatrix/1631022-skewy.md)
  Specifies a skew transformation along the y-axis by the given angle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/webkitcssmatrix/1632184-scale)*