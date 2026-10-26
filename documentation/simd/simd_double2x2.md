# simd_double2x2

**Framework**: simd  
**Kind**: struct  
**Role**: Structure

A matrix of two columns and two rows that contains double-precision values.

## Declaration

```swift
struct simd_double2x2
```

```c
typedef struct { ... } simd_double2x2;
```

## Topics

### Initializers
- [init()](./simd_double2x2/init%28%29.md)
  Creates a new matrix with uninitialized memory.
- [init(Double)](./simd_double2x2/init%28_%29-3kbjz.md)
  Creates a new matrix with the specified scalar value on the main diagonal.
- [init(diagonal: SIMD2<Double>)](./simd_double2x2/init%28diagonal%29.md)
  Creates a new matrix with the specified vector on the main diagonal.
- [init([SIMD2<Double>])](./simd_double2x2/init%28_%29-6yq0z.md)
  Creates a new matrix with the specified columns.
- [init(SIMD2<Double>, SIMD2<Double>)](./simd_double2x2/init%28_,_%29.md)
  Creates a new matrix with the specified vectors as columns.
- [init(columns: (simd_double2, simd_double2))](./simd_double2x2/init%28columns%29.md)
  Creates a new matrix with the specified columns.
- [init(rows: [SIMD2<Double>])](./simd_double2x2/init%28rows%29.md)
  Creates a new matrix with the specified rows.
### Matrix Constants
- [let matrix_identity_double2x2: simd_double2x2](./matrix_identity_double2x2.md)
  A 2 x 2 identity matrix.
### Matrix Properties
- [var determinant: Double](./simd_double2x2/determinant.md)
  The determinant of the matrix.
- [var inverse: simd_double2x2](./simd_double2x2/inverse.md)
  The inverse of the matrix.
- [var transpose: double2x2](./simd_double2x2/transpose.md)
  The transpose of the matrix.
- [var columns: (simd_double2, simd_double2)](./simd_double2x2/columns.md)
  The columns of the matrix.
### Matrix Creation Functions
- [func simd_matrix(simd_double2, simd_double2) -> simd_double2x2](./simd_matrix%28_,_%29-938tb.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_double2, simd_double2) -> simd_double2x2](./simd_matrix_from_rows%28_,_%29-368td.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD2<Double>, SIMD2<Double>) -> simd_double2x2](./matrix_from_rows%28_,_%29-1w56v.md)
  Returns a new matrix with the specified vector on the main diagonal.
### Element Access
- [subscript(Int) -> SIMD2<Double>](./simd_double2x2/subscript%28_%29.md)
  Accesses the column at the specified position.
- [subscript(Int, Int) -> Double](./simd_double2x2/subscript%28_,_%29.md)
  Accesses the element at the specified position.
### Type Aliases
- [typealias double2x2](./double2x2.md)
  A type alias for a double-precision 2 x 2 matrix.
- [typealias matrix_double2x2](./matrix_double2x2.md)
  A type alias for a double-precision 2 x 2 matrix.
### Deprecated Symbols
- [func matrix_invert(simd_double2x2) -> simd_double2x2](./matrix_invert%28_%29-nkj5.md)
  Returns the inverse of the specified matrix.
- [func matrix_equal(simd_double2x2, simd_double2x2) -> Bool](./matrix_equal%28_,_%29-4claa.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_from_diagonal(SIMD2<Double>) -> simd_double2x2](./matrix_from_diagonal%28_%29-7i8pm.md)
  Returns a new matrix with the specified vector on the main diagonal.
- [func matrix_determinant(simd_double2x2) -> Double](./matrix_determinant%28_%29-7kglv.md)
  Returns the determinant of the specified matrix.
- [func matrix_from_columns(SIMD2<Double>, SIMD2<Double>) -> simd_double2x2](./matrix_from_columns%28_,_%29-37jug.md)
  Returns a new matrix with the specified columns.
- [func matrix_transpose(simd_double2x2) -> double2x2](./matrix_transpose%28_%29-6qaez.md)
  Returns the transpose of a matrix.
- [init(simd_double2x2)](./simd_double2x2/init%28_%29-9vxjx.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_double2x2](./simd_double2x2/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.
### Operators
- [static func * (simd_double2x2, Double) -> simd_double2x2](./simd_double2x2/star%28_,_%29-34mwe.md)
- [static func * (simd_double2x2, SIMD2<Double>) -> SIMD2<Double>](./simd_double2x2/star%28_,_%29-4srge.md)
- [static func * (simd_double2x2, double2x2) -> double2x2](./simd_double2x2/star%28_,_%29-4x1rs.md)
- [static func * (simd_double2x2, double4x2) -> double4x2](./simd_double2x2/star%28_,_%29-6vah1.md)
- [static func * (simd_double2x2, double3x2) -> double3x2](./simd_double2x2/star%28_,_%29-86p1t.md)
- [static func * (SIMD2<Double>, simd_double2x2) -> SIMD2<Double>](./simd_double2x2/star%28_,_%29-mvy8.md)
- [static func * (Double, simd_double2x2) -> simd_double2x2](./simd_double2x2/star%28_,_%29-xb7z.md)
- [static func *= (inout simd_double2x2, Double)](./simd_double2x2/stareq%28_,_%29-76lel.md)
- [static func *= (inout simd_double2x2, double2x2)](./simd_double2x2/stareq%28_,_%29-99yuu.md)
- [static func + (simd_double2x2, simd_double2x2) -> simd_double2x2](./simd_double2x2/plus%28_,_%29.md)
- [static func += (inout simd_double2x2, simd_double2x2)](./simd_double2x2/pluseq%28_,_%29.md)
- [static func - (simd_double2x2) -> simd_double2x2](./simd_double2x2/minus%28_%29.md)
- [static func - (simd_double2x2, simd_double2x2) -> simd_double2x2](./simd_double2x2/minus%28_,_%29.md)
- [static func -= (inout simd_double2x2, simd_double2x2)](./simd_double2x2/minuseq%28_,_%29.md)

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
- [struct simd_double4x4](./simd_double4x4.md)
  A matrix of four columns and four rows that contains double-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_double2x2)*