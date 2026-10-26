# simd_double2x3

**Framework**: simd  
**Kind**: struct  
**Role**: Structure

A matrix of two columns and three rows that contains double-precision values.

## Declaration

```swift
struct simd_double2x3
```

```c
typedef struct { ... } simd_double2x3;
```

## Topics

### Initializers
- [init()](./simd_double2x3/init%28%29.md)
  Creates a new matrix with uninitialized memory.
- [init(Double)](./simd_double2x3/init%28_%29-6xclm.md)
  Creates a new matrix with the specified scalar value on the main diagonal.
- [init(diagonal: SIMD2<Double>)](./simd_double2x3/init%28diagonal%29.md)
  Creates a new matrix with the specified vector on the main diagonal.
- [init([SIMD3<Double>])](./simd_double2x3/init%28_%29-6n7k.md)
  Creates a new matrix from an array.
- [init(SIMD3<Double>, SIMD3<Double>)](./simd_double2x3/init%28_,_%29.md)
  Creates a new matrix with the specified vectors as columns.
- [init(columns: (simd_double3, simd_double3))](./simd_double2x3/init%28columns%29.md)
  Creates a new matrix with the specified columns.
- [init(rows: [SIMD2<Double>])](./simd_double2x3/init%28rows%29.md)
  Creates a new matrix with the specified rows.
### Matrix Properties
- [var transpose: double3x2](./simd_double2x3/transpose.md)
  The transpose of the matrix.
- [var columns: (simd_double3, simd_double3)](./simd_double2x3/columns.md)
  The columns of the matrix.
### Matrix Creation Functions
- [func simd_matrix(simd_double3, simd_double3) -> simd_double2x3](./simd_matrix%28_,_%29-86soe.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_double2, simd_double2, simd_double2) -> simd_double2x3](./simd_matrix_from_rows%28_,_,_%29-96jbn.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD2<Double>, SIMD2<Double>, SIMD2<Double>) -> simd_double2x3](./matrix_from_rows%28_,_,_%29-2ar1l.md)
  Returns a new matrix with the specified rows.
### Element Access
- [subscript(Int) -> SIMD3<Double>](./simd_double2x3/subscript%28_%29.md)
  Accesses the column at the specified position.
- [subscript(Int, Int) -> Double](./simd_double2x3/subscript%28_,_%29.md)
  Accesses the element at the specified position.
### Type Aliases
- [typealias double2x3](./double2x3.md)
  A type alias for a double-precision 2 x 3 matrix.
- [typealias matrix_double2x3](./matrix_double2x3.md)
  A type alias for a double-precision 2 x 3 matrix.
### Deprecated Symbols
- [func matrix_equal(simd_double2x3, simd_double2x3) -> Bool](./matrix_equal%28_,_%29-52vds.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_from_columns(SIMD3<Double>, SIMD3<Double>) -> simd_double2x3](./matrix_from_columns%28_,_%29-61w2n.md)
  Returns a new matrix with the specified columns.
- [func matrix_transpose(simd_double3x2) -> double2x3](./matrix_transpose%28_%29-97k0o.md)
  Returns the transpose of a matrix.
- [init(simd_double2x3)](./simd_double2x3/init%28_%29-98rcw.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_double2x3](./simd_double2x3/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.
### Operators
- [static func * (simd_double2x3, SIMD2<Double>) -> SIMD3<Double>](./simd_double2x3/star%28_,_%29-26bpe.md)
- [static func * (simd_double2x3, double3x2) -> double3x3](./simd_double2x3/star%28_,_%29-2qo9o.md)
- [static func * (simd_double2x3, Double) -> simd_double2x3](./simd_double2x3/star%28_,_%29-3li3r.md)
- [static func * (simd_double2x3, double2x2) -> double2x3](./simd_double2x3/star%28_,_%29-4bwlw.md)
- [static func * (Double, simd_double2x3) -> simd_double2x3](./simd_double2x3/star%28_,_%29-559m0.md)
- [static func * (SIMD3<Double>, simd_double2x3) -> SIMD2<Double>](./simd_double2x3/star%28_,_%29-8rxeu.md)
- [static func * (simd_double2x3, double4x2) -> double4x3](./simd_double2x3/star%28_,_%29-919bm.md)
- [static func *= (inout simd_double2x3, double2x2)](./simd_double2x3/stareq%28_,_%29-3lbnh.md)
- [static func *= (inout simd_double2x3, Double)](./simd_double2x3/stareq%28_,_%29-9b91z.md)
- [static func + (simd_double2x3, simd_double2x3) -> simd_double2x3](./simd_double2x3/plus%28_,_%29.md)
- [static func += (inout simd_double2x3, simd_double2x3)](./simd_double2x3/pluseq%28_,_%29.md)
- [static func - (simd_double2x3) -> simd_double2x3](./simd_double2x3/minus%28_%29.md)
- [static func - (simd_double2x3, simd_double2x3) -> simd_double2x3](./simd_double2x3/minus%28_,_%29.md)
- [static func -= (inout simd_double2x3, simd_double2x3)](./simd_double2x3/minuseq%28_,_%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_double2x3)*