# simd_double4x4

**Framework**: simd  
**Kind**: struct  
**Role**: Structure

A matrix of four columns and four rows that contains double-precision values.

## Declaration

```swift
struct simd_double4x4
```

```c
typedef struct { ... } simd_double4x4;
```

## Topics

### Initializers
- [init()](./simd_double4x4/init%28%29.md)
  Creates a new matrix with uninitialized memory.
- [init(Double)](./simd_double4x4/init%28_%29-184ad.md)
  Creates a new matrix with the specified scalar value on the main diagonal.
- [init(diagonal: SIMD4<Double>)](./simd_double4x4/init%28diagonal%29.md)
  Creates a new matrix with the specified vector on the main diagonal.
- [init([SIMD4<Double>])](./simd_double4x4/init%28_%29-ahnn.md)
  Creates a new matrix with the specified columns.
- [init(simd_quatd)](./simd_double4x4/init%28_%29-43z8y.md)
  Creates a new matrix from the specified quaternion.
- [init(SCNMatrix4)](./simd_double4x4/init%28_%29-45usb.md)
  Creates a new matrix from the specified SceneKit matrix.
- [init(SCNMatrix4)](./simd_double4x4/init%28_%29-vm0p.md)
  Creates a new matrix from the specified SceneKit matrix.
- [init(SIMD4<Double>, SIMD4<Double>, SIMD4<Double>, SIMD4<Double>)](./simd_double4x4/init%28_,_,_,_%29.md)
  Creates a new matrix with the specified vectors as columns.
- [init(columns: (simd_double4, simd_double4, simd_double4, simd_double4))](./simd_double4x4/init%28columns%29.md)
  Creates a new matrix with the specified columns.
- [init(rows: [SIMD4<Double>])](./simd_double4x4/init%28rows%29.md)
  Creates a new matrix with the specified rows.
- [init(AffineTransform3DFloat)](./simd_double4x4/init%28_%29-1ara7.md)
  Returns a new 4 x 4 double-precision matrix from a Spatial affine transform.
- [init(Pose3DFloat)](./simd_double4x4/init%28_%29-818zf.md)
  Returns a new 4 x 4 double-precision matrix from a Spatial pose.
- [init(ProjectiveTransform3DFloat)](./simd_double4x4/init%28_%29-98553.md)
  Returns a new 4 x 4 double-precision matrix from a Spatial projective transform.
### Matrix Constants
- [let matrix_identity_double4x4: simd_double4x4](./matrix_identity_double4x4.md)
  A 4 x 4 identity matrix.
### Matrix Properties
- [var determinant: Double](./simd_double4x4/determinant.md)
  The determinant of the matrix.
- [var inverse: simd_double4x4](./simd_double4x4/inverse.md)
  The inverse of the matrix.
- [var transpose: double4x4](./simd_double4x4/transpose.md)
  The transpose of the matrix.
- [var columns: (simd_double4, simd_double4, simd_double4, simd_double4)](./simd_double4x4/columns.md)
  The columns of the matrix.
### Matrix Creation Functions
- [func simd_matrix(simd_double4, simd_double4, simd_double4, simd_double4) -> simd_double4x4](./simd_matrix%28_,_,_,_%29-28at0.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_double4, simd_double4, simd_double4, simd_double4) -> simd_double4x4](./simd_matrix_from_rows%28_,_,_,_%29-898tw.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD4<Double>, SIMD4<Double>, SIMD4<Double>, SIMD4<Double>) -> simd_double4x4](./matrix_from_rows%28_,_,_,_%29-37t0w.md)
  Returns a new matrix with the specified rows.
- [func simd_matrix4x4(simd_quatd) -> simd_double4x4](./simd_matrix4x4%28_%29-20mdz.md)
  Returns a new matrix with the specified quarternion.
### Element Access
- [subscript(Int) -> SIMD4<Double>](./simd_double4x4/subscript%28_%29.md)
  Accesses the column at the specified position.
- [subscript(Int, Int) -> Double](./simd_double4x4/subscript%28_,_%29.md)
  Accesses the element at the specified position.
### Type Aliases
- [typealias double4x4](./double4x4.md)
  A type alias for a double-precision 4 x 4 matrix.
- [typealias matrix_double4x4](./matrix_double4x4.md)
  A type alias for a double-precision 4 x 4 matrix.
### Deprecated Symbols
- [func matrix_invert(simd_double4x4) -> simd_double4x4](./matrix_invert%28_%29-84fxh.md)
  Returns the inverse of the specified matrix.
- [func matrix_from_columns(SIMD4<Double>, SIMD4<Double>, SIMD4<Double>, SIMD4<Double>) -> simd_double4x4](./matrix_from_columns%28_,_,_,_%29-61q4l.md)
  Returns a new matrix with the specified columns.
- [func matrix_from_diagonal(SIMD4<Double>) -> simd_double4x4](./matrix_from_diagonal%28_%29-2r6tr.md)
  Returns a new matrix with the specified vector on the main diagonal.
- [func matrix_determinant(simd_double4x4) -> Double](./matrix_determinant%28_%29-2n34p.md)
  Returns the determinant of the specified matrix.
- [func matrix_equal(simd_double4x4, simd_double4x4) -> Bool](./matrix_equal%28_,_%29-3jmfe.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_transpose(simd_double4x4) -> double4x4](./matrix_transpose%28_%29-66ecl.md)
  Returns the transpose of a matrix.
- [init(simd_double4x4)](./simd_double4x4/init%28_%29-4fie3.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_double4x4](./simd_double4x4/cmatrix.md)
  Creates a new matrix with the specified matrix.
### Operators
- [static func * (simd_double4x4, double2x4) -> double2x4](./simd_double4x4/star%28_,_%29-17puk.md)
- [static func * (simd_double4x4, double4x4) -> double4x4](./simd_double4x4/star%28_,_%29-2wqm8.md)
- [static func * (simd_double4x4, SIMD4<Double>) -> SIMD4<Double>](./simd_double4x4/star%28_,_%29-3jd3c.md)
- [static func * (Double, simd_double4x4) -> simd_double4x4](./simd_double4x4/star%28_,_%29-5459y.md)
- [static func * (simd_double4x4, double3x4) -> double3x4](./simd_double4x4/star%28_,_%29-5i8yr.md)
- [static func * (SIMD4<Double>, simd_double4x4) -> SIMD4<Double>](./simd_double4x4/star%28_,_%29-7cb0c.md)
- [static func * (simd_double4x4, Double) -> simd_double4x4](./simd_double4x4/star%28_,_%29-p402.md)
- [static func *= (inout simd_double4x4, double4x4)](./simd_double4x4/stareq%28_,_%29-12w8l.md)
- [static func *= (inout simd_double4x4, Double)](./simd_double4x4/stareq%28_,_%29-9llx.md)
- [static func + (simd_double4x4, simd_double4x4) -> simd_double4x4](./simd_double4x4/plus%28_,_%29.md)
- [static func += (inout simd_double4x4, simd_double4x4)](./simd_double4x4/pluseq%28_,_%29.md)
- [static func - (simd_double4x4) -> simd_double4x4](./simd_double4x4/minus%28_%29.md)
- [static func - (simd_double4x4, simd_double4x4) -> simd_double4x4](./simd_double4x4/minus%28_,_%29.md)
- [static func -= (inout simd_double4x4, simd_double4x4)](./simd_double4x4/minuseq%28_,_%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Matrix structures
- [struct simd_double2x2](./simd_double2x2.md)
  A matrix of two columns and two rows that contains double-precision values.
- [struct simd_double2x3](./simd_double2x3.md)
  A matrix of two columns and three rows that contains double-precision values.
- [struct simd_double2x4](./simd_double2x4.md)
  A matrix of two columns and four rows that contains double-precision values.
- [struct simd_double3x2](./simd_double3x2.md)
  A matrix of three columns and two rows that contains double-precision values.
- [struct simd_double3x3](./simd_double3x3.md)
  A matrix of three columns and three rows that contains double-precision values.
- [struct simd_double3x4](./simd_double3x4.md)
  A matrix of three columns and four rows that contains double-precision values.
- [struct simd_double4x2](./simd_double4x2.md)
  A matrix of four columns and two rows that contains double-precision values.
- [struct simd_double4x3](./simd_double4x3.md)
  A matrix of four columns and three rows that contains double-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_double4x4)*