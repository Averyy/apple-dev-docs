# simd_double3x2

**Framework**: simd  
**Kind**: struct  
**Role**: Structure

A matrix of three columns and two rows that contains double-precision values.

## Declaration

```swift
struct simd_double3x2
```

```c
typedef struct { ... } simd_double3x2;
```

## Topics

### Initializers
- [init()](./simd_double3x2/init%28%29.md)
  Creates a new matrix with uninitialized memory.
- [init(Double)](./simd_double3x2/init%28_%29-6r1mr.md)
  Creates a new matrix with the specified scalar value on the main diagonal.
- [init(diagonal: SIMD2<Double>)](./simd_double3x2/init%28diagonal%29.md)
  Creates a new matrix with the specified vector on the main diagonal.
- [init([SIMD2<Double>])](./simd_double3x2/init%28_%29-9euf0.md)
  Creates a new matrix from an array.
- [init(SIMD2<Double>, SIMD2<Double>, SIMD2<Double>)](./simd_double3x2/init%28_,_,_%29.md)
  Creates a new matrix with the specified vectors as columns.
- [init(columns: (simd_double2, simd_double2, simd_double2))](./simd_double3x2/init%28columns%29.md)
  Creates a new matrix with the specified columns.
- [init(rows: [SIMD3<Double>])](./simd_double3x2/init%28rows%29.md)
  Creates a new matrix with the specified rows.
### Matrix Properties
- [var transpose: double2x3](./simd_double3x2/transpose.md)
  The transpose of the matrix.
- [var columns: (simd_double2, simd_double2, simd_double2)](./simd_double3x2/columns.md)
  The columns of the matrix.
### Matrix Creation Functions
- [func simd_matrix(simd_double2, simd_double2, simd_double2) -> simd_double3x2](./simd_matrix%28_,_,_%29-59y1c.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_double3, simd_double3) -> simd_double3x2](./simd_matrix_from_rows%28_,_%29-7mxf9.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD3<Double>, SIMD3<Double>) -> simd_double3x2](./matrix_from_rows%28_,_%29-630eh.md)
  Returns a new matrix with the specified rows.
### Element Access
- [subscript(Int) -> SIMD2<Double>](./simd_double3x2/subscript%28_%29.md)
  Accesses the column at the specified position.
- [subscript(Int, Int) -> Double](./simd_double3x2/subscript%28_,_%29.md)
  Accesses the element at the specified position.
### Type Aliases
- [typealias double3x2](./double3x2.md)
  A type alias for a double-precision 3 x 2 matrix.
- [typealias matrix_double3x2](./matrix_double3x2.md)
  A type alias for a double-precision 3 x 2 matrix.
### Deprecated Symbols
- [func matrix_equal(simd_double3x2, simd_double3x2) -> Bool](./matrix_equal%28_,_%29-3dnu.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_from_columns(SIMD2<Double>, SIMD2<Double>, SIMD2<Double>) -> simd_double3x2](./matrix_from_columns%28_,_,_%29-9wapk.md)
  Returns a new matrix with the specified columns.
- [func matrix_transpose(simd_double2x3) -> double3x2](./matrix_transpose%28_%29-7ueg2.md)
  Returns the transpose of a matrix.
- [init(simd_double3x2)](./simd_double3x2/init%28_%29-6yyfq.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_double3x2](./simd_double3x2/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.
### Operators
- [static func * (SIMD2<Double>, simd_double3x2) -> SIMD3<Double>](./simd_double3x2/star%28_,_%29-1hwgh.md)
- [static func * (Double, simd_double3x2) -> simd_double3x2](./simd_double3x2/star%28_,_%29-1i31n.md)
- [static func * (simd_double3x2, double3x3) -> double3x2](./simd_double3x2/star%28_,_%29-205gc.md)
- [static func * (simd_double3x2, double2x3) -> double2x2](./simd_double3x2/star%28_,_%29-55cki.md)
- [static func * (simd_double3x2, double4x3) -> double4x2](./simd_double3x2/star%28_,_%29-71omv.md)
- [static func * (simd_double3x2, Double) -> simd_double3x2](./simd_double3x2/star%28_,_%29-8b0gm.md)
- [static func * (simd_double3x2, SIMD3<Double>) -> SIMD2<Double>](./simd_double3x2/star%28_,_%29-8sxw1.md)
- [static func *= (inout simd_double3x2, Double)](./simd_double3x2/stareq%28_,_%29-65soi.md)
- [static func *= (inout simd_double3x2, double3x3)](./simd_double3x2/stareq%28_,_%29-7jk10.md)
- [static func + (simd_double3x2, simd_double3x2) -> simd_double3x2](./simd_double3x2/plus%28_,_%29.md)
- [static func += (inout simd_double3x2, simd_double3x2)](./simd_double3x2/pluseq%28_,_%29.md)
- [static func - (simd_double3x2) -> simd_double3x2](./simd_double3x2/minus%28_%29.md)
- [static func - (simd_double3x2, simd_double3x2) -> simd_double3x2](./simd_double3x2/minus%28_,_%29.md)
- [static func -= (inout simd_double3x2, simd_double3x2)](./simd_double3x2/minuseq%28_,_%29.md)

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
- [struct simd_double3x3](./simd_double3x3.md)
  A matrix of three columns and three rows that contains double-precision values.
- [struct simd_double3x4](./simd_double3x4.md)
  A matrix of three columns and four rows that contains double-precision values.
- [struct simd_double4x2](./simd_double4x2.md)
  A matrix of four columns and two rows that contains double-precision values.
- [struct simd_double4x3](./simd_double4x3.md)
  A matrix of four columns and three rows that contains double-precision values.
- [struct simd_double4x4](./simd_double4x4.md)
  A matrix of four columns and four rows that contains double-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_double3x2)*