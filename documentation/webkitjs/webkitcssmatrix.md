# WebKitCSSMatrix

**Framework**: Webkitjs  
**Kind**: cl

`WebKitCSSMatrix` objects represent a 4x4 homogeneous matrix for 3D transforms or a vector for 2D transforms. You can use these objects to manipulate matrices in JavaScript. For example, you can multiply, translate, and scale matrices.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 2.0+

## Declaration

```swift
interface WebKitCSSMatrix
```

#### Overview

The values of a 3D matrix can be initialized from the [`matrix3d`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariCSSRef/Articles/Functions.html#//apple_ref/css/func/matrix3d) transform function returned by `window.getComputedStyle(element).webkitTransform()`. To apply the final matrix to an element, construct a string using the [`matrix3d`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariCSSRef/Articles/Functions.html#//apple_ref/css/func/matrix3d) transform function passing the 16 values, and assign it to `element.style.webkitTransform`. Similarly, you can construct a matrix for 2D transforms by setting 6 values, represented by the `a`-`f` properties. 

## Topics

### Accessing Properties
- [a](webkitcssmatrix/1633464-a.md)
  The first 2D vector value.
- [b](webkitcssmatrix/1630954-b.md)
  The second 2D vector value.
- [c](webkitcssmatrix/1629966-c.md)
  The third 2D vector value.
- [d](webkitcssmatrix/1633079-d.md)
  The fourth 2D vector value.
- [e](webkitcssmatrix/1633835-e.md)
  The fifth 2D vector value.
- [f](webkitcssmatrix/1633411-f.md)
  The sixth 2D vector value.
- [m11](webkitcssmatrix/1629449-m11.md)
  The 3D matrix value in the first row and first column.
- [m12](webkitcssmatrix/1629940-m12.md)
  The 3D matrix value in the first row and second column.
- [m13](webkitcssmatrix/1629376-m13.md)
  The 3D matrix value in the first row and third column.
- [m14](webkitcssmatrix/1632308-m14.md)
  The 3D matrix value in the first row and fourth column.
- [m21](webkitcssmatrix/1630988-m21.md)
  The 3D matrix value in the second row and first column.
- [m22](webkitcssmatrix/1632488-m22.md)
  The 3D matrix value in the second row and second column.
- [m23](webkitcssmatrix/1629105-m23.md)
  The 3D matrix value in the second row and third column.
- [m24](webkitcssmatrix/1633956-m24.md)
  The 3D matrix value in the second row and fourth column.
- [m31](webkitcssmatrix/1628844-m31.md)
  The 3D matrix value in the third row and first column.
- [m32](webkitcssmatrix/1633297-m32.md)
  The 3D matrix value in the third row and second column.
- [m33](webkitcssmatrix/1633250-m33.md)
  The 3D matrix value in the third row and third column.
- [m34](webkitcssmatrix/1630077-m34.md)
  The 3D matrix value in the third row and fourth column.
- [m41](webkitcssmatrix/1630945-m41.md)
  The 3D matrix value in the fourth row and first column.
- [m42](webkitcssmatrix/1630663-m42.md)
  The 3D matrix value in the fourth row and second column.
- [m43](webkitcssmatrix/1633644-m43.md)
  The 3D matrix value in the fourth row and third column.
- [m44](webkitcssmatrix/1631430-m44.md)
  The 3D matrix value in the fourth row and fourth column.
### Setting the Matrix
- [setMatrixValue](webkitcssmatrix/1629980-setmatrixvalue.md)
  Sets the matrix values using a string representation.
### Applying Operations
- [multiply](webkitcssmatrix/1631528-multiply.md)
  Returns the result of multiplying this matrix by a given matrix that is on the right.
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
### Converting the Matrix
- [toString](webkitcssmatrix/1630836-tostring.md)
  Returns a string representation of the matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/webkitcssmatrix)*