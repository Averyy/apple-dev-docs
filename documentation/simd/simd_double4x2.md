# simd_double4x2

**Framework**: simd  
**Kind**: struct  
**Role**: Structure

A matrix of four columns and two rows that contains double-precision values.

## Declaration

```swift
struct simd_double4x2
```

```c
typedef struct { ... } simd_double4x2;
```

## Mentions

- [Working with Matrices](../Accelerate/working-with-matrices.md)

## Topics

### Initializers
- [init()](./simd_double4x2/init%28%29.md)
  Creates a new matrix with uninitialized memory.
- [init(Double)](./simd_double4x2/init%28_%29-3i3he.md)
  Creates a new matrix with the specified scalar value on the main diagonal.
- [init(diagonal: SIMD2<Double>)](./simd_double4x2/init%28diagonal%29.md)
  Creates a new matrix with the specified vector on the main diagonal.
- [init([SIMD2<Double>])](./simd_double4x2/init%28_%29-9pvdm.md)
  Creates a new matrix from an array.
- [init(SIMD2<Double>, SIMD2<Double>, SIMD2<Double>, SIMD2<Double>)](./simd_double4x2/init%28_,_,_,_%29.md)
  Creates a new matrix with the specified vectors as columns.
- [init(columns: (simd_double2, simd_double2, simd_double2, simd_double2))](./simd_double4x2/init%28columns%29.md)
  Creates a new matrix with the specified columns.
- [init(rows: [SIMD4<Double>])](./simd_double4x2/init%28rows%29.md)
  Creates a new matrix with the specified rows.
### Matrix Properties
- [var transpose: double2x4](./simd_double4x2/transpose.md)
  The transpose of the matrix.
- [var columns: (simd_double2, simd_double2, simd_double2, simd_double2)](./simd_double4x2/columns.md)
  The columns of the matrix.
### Matrix Creation Functions
- [func simd_matrix(simd_double2, simd_double2, simd_double2, simd_double2) -> simd_double4x2](./simd_matrix%28_,_,_,_%29-6cze4.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_double4, simd_double4) -> simd_double4x2](./simd_matrix_from_rows%28_,_%29-5xq2d.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD4<Double>, SIMD4<Double>) -> simd_double4x2](./matrix_from_rows%28_,_%29-2rxkt.md)
  Returns a new matrix with the specified rows.
### Element Access
- [subscript(Int) -> SIMD2<Double>](./simd_double4x2/subscript%28_%29.md)
  Accesses the column at the specified position.
- [subscript(Int, Int) -> Double](./simd_double4x2/subscript%28_,_%29.md)
  Accesses the element at the specified position.
### Type Aliases
- [typealias double4x2](./double4x2.md)
  A type alias for a double-precision 4 x 2 matrix.
- [typealias matrix_double4x2](./matrix_double4x2.md)
  A type alias for a double-precision 4 x 2 matrix.
### Deprecated Symbols
- [func matrix_from_columns(SIMD2<Double>, SIMD2<Double>, SIMD2<Double>, SIMD2<Double>) -> simd_double4x2](./matrix_from_columns%28_,_,_,_%29-6tb78.md)
  Returns a new matrix with the specified columns.
- [func matrix_equal(simd_double4x2, simd_double4x2) -> Bool](./matrix_equal%28_,_%29-5v8g0.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_transpose(simd_double2x4) -> double4x2](./matrix_transpose%28_%29-7ttoe.md)
  Returns the transpose of a matrix.
- [init(simd_double4x2)](./simd_double4x2/init%28_%29-hovz.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_double4x2](./simd_double4x2/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.
### Operators
- [static func * (simd_double4x2, Double) -> simd_double4x2](./simd_double4x2/star%28_,_%29-5166x.md)
- [static func * (SIMD2<Double>, simd_double4x2) -> SIMD4<Double>](./simd_double4x2/star%28_,_%29-64ht9.md)
- [static func * (simd_double4x2, SIMD4<Double>) -> SIMD2<Double>](./simd_double4x2/star%28_,_%29-73ixh.md)
- [static func * (Double, simd_double4x2) -> simd_double4x2](./simd_double4x2/star%28_,_%29-7fz5.md)
- [static func * (simd_double4x2, double4x4) -> double4x2](./simd_double4x2/star%28_,_%29-8tpc2.md)
- [static func * (simd_double4x2, double3x4) -> double3x2](./simd_double4x2/star%28_,_%29-mlrw.md)
- [static func * (simd_double4x2, double2x4) -> double2x2](./simd_double4x2/star%28_,_%29-qtns.md)
- [static func *= (inout simd_double4x2, double4x4)](./simd_double4x2/stareq%28_,_%29-2s2r4.md)
- [static func *= (inout simd_double4x2, Double)](./simd_double4x2/stareq%28_,_%29-9qlax.md)
- [static func + (simd_double4x2, simd_double4x2) -> simd_double4x2](./simd_double4x2/plus%28_,_%29.md)
- [static func += (inout simd_double4x2, simd_double4x2)](./simd_double4x2/pluseq%28_,_%29.md)
- [static func - (simd_double4x2) -> simd_double4x2](./simd_double4x2/minus%28_%29.md)
- [static func - (simd_double4x2, simd_double4x2) -> simd_double4x2](./simd_double4x2/minus%28_,_%29.md)
- [static func -= (inout simd_double4x2, simd_double4x2)](./simd_double4x2/minuseq%28_,_%29.md)
### Math Functions
- [simd_add](./simd_add-6z107.md)
  Returns the sum of two matrices.
- [simd_sub](./simd_sub-7ngxq.md)
  Returns the difference of two matrices.
- [matrix_scale](./matrix_scale-4to50.md)
  Returns the product of a scalar value and a matrix.
### Matrix-Scalar Multiplication Functions
- [simd_mul](./simd_mul-9tjwx.md)
  Returns the product of a scalar value and a 4 x 2 matrix.
### Matrix-Vector Multiplication Functions
- [simd_mul](./simd_mul-9tg9k.md)
  Returns the product of a two-element vector and a 4 x 2 matrix.
- [matrix_multiply](./matrix_multiply-6y1xx.md)
  Returns the product of a two-element vector and a 4 x 2 matrix.
- [simd_mul](./simd_mul-9xo9x.md)
  Returns the product of a 4 x 2 matrix and a four-element vector.
- [matrix_multiply](./matrix_multiply-9ly4k.md)
  Returns the product of a 4 x 2 matrix and a four-element vector.
### Matrix-Matrix Multiplication Functions
- [simd_mul](./simd_mul-193a1.md)
  Returns the product of a 2 x 2 matrix and a 4 x 2 matrix.
- [matrix_multiply](./matrix_multiply-7erm8.md)
  Returns the product of a 2 x 2 matrix and a 4 x 2 matrix.
- [simd_mul](./simd_mul-2ijzp.md)
  Returns the product of a 3 x 2 matrix and a 4 x 3 matrix.
- [matrix_multiply](./matrix_multiply-2dc11.md)
  Returns the product of a 3 x 2 matrix and a 4 x 3 matrix.
- [simd_mul](./simd_mul-jjeg.md)
  Returns the product of a 4 x 2 matrix and a 4 x 4 matrix.
- [matrix_multiply](./matrix_multiply-4um5g.md)
  Returns the product of a 4 x 2 matrix and a 4 x 4 matrix.
### Equality Functions
- [simd_equal](./simd_equal-6rpnx.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix.
- [simd_almost_equal_elements](./simd_almost_equal_elements-3r4i6.md)
  Returns true if every element in a matrix is within a specified tolerance to the corresponding element in a second matrix.
- [simd_almost_equal_elements_relative](./simd_almost_equal_elements_relative-7b8lm.md)
  Returns true if every element in a matrix is within a specified double-precision relative tolerance to the corresponding element in a second matrix.
### Linear Combination Function
- [simd_linear_combination](./simd_linear_combination-9yjju.md)
  Returns the linear combination of two scalar values and two matrices.
### Transpose Function
- [simd_transpose](./simd_transpose-xobi.md)
  Returns the transpose of a matrix.

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
- [struct simd_double4x3](./simd_double4x3.md)
  A matrix of four columns and three rows that contains double-precision values.
- [struct simd_double4x4](./simd_double4x4.md)
  A matrix of four columns and four rows that contains double-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_double4x2)*