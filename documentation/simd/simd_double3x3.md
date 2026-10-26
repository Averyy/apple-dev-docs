# simd_double3x3

**Framework**: simd  
**Kind**: struct  
**Role**: Structure

A matrix of three columns and three rows that contains double-precision values.

## Declaration

```swift
struct simd_double3x3
```

```c
typedef struct { ... } simd_double3x3;
```

## Topics

### Initializers
- [init()](./simd_double3x3/init%28%29.md)
  Creates a new matrix with uninitialized memory.
- [init(Double)](./simd_double3x3/init%28_%29-6qq5k.md)
  Creates a new matrix with the specified scalar value on the main diagonal.
- [init(diagonal: SIMD3<Double>)](./simd_double3x3/init%28diagonal%29.md)
  Creates a new matrix with the specified vector on the main diagonal.
- [init([SIMD3<Double>])](./simd_double3x3/init%28_%29-6kw2p.md)
  Creates a new matrix with the specified columns.
- [init(simd_quatd)](./simd_double3x3/init%28_%29-9wyb6.md)
  Creates a new matrix from the specified quarternion.
- [init(SIMD3<Double>, SIMD3<Double>, SIMD3<Double>)](./simd_double3x3/init%28_,_,_%29.md)
  Creates a new matrix with the specified vectors as columns.
- [init(columns: (simd_double3, simd_double3, simd_double3))](./simd_double3x3/init%28columns%29.md)
  Creates a new matrix with the specified columns.
- [init(rows: [SIMD3<Double>])](./simd_double3x3/init%28rows%29.md)
  Creates a new matrix with the specified rows.
### Matrix Constants
- [let matrix_identity_double3x3: simd_double3x3](./matrix_identity_double3x3.md)
  A 3 x 3 identity matrix.
### Matrix Properties
- [var determinant: Double](./simd_double3x3/determinant.md)
  The determinant of the matrix.
- [var inverse: simd_double3x3](./simd_double3x3/inverse.md)
  The inverse of the matrix.
- [var transpose: double3x3](./simd_double3x3/transpose.md)
  The transpose of the matrix.
- [var columns: (simd_double3, simd_double3, simd_double3)](./simd_double3x3/columns.md)
  The columns of the matrix.
### Matrix Creation Functions
- [func simd_matrix(simd_double3, simd_double3, simd_double3) -> simd_double3x3](./simd_matrix%28_,_,_%29-5h0nl.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_double3, simd_double3, simd_double3) -> simd_double3x3](./simd_matrix_from_rows%28_,_,_%29-48v9h.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD3<Double>, SIMD3<Double>, SIMD3<Double>) -> simd_double3x3](./matrix_from_rows%28_,_,_%29-7a60t.md)
  Returns a new matrix with the specified rows.
- [func simd_matrix3x3(simd_quatd) -> simd_double3x3](./simd_matrix3x3%28_%29-60dhx.md)
  Returns a new matrix with the specified quarternion.
- [simd_diagonal_matrix](./simd_diagonal_matrix-2nuo5.md)
  Returns a new matrix with the specified vector on the main diagonal.
### Element Access
- [subscript(Int) -> SIMD3<Double>](./simd_double3x3/subscript%28_%29.md)
  Accesses the column at the specified position.
- [subscript(Int, Int) -> Double](./simd_double3x3/subscript%28_,_%29.md)
  Accesses the element at the specified position.
### Type Aliases
- [typealias double3x3](./double3x3.md)
  A type alias for a double-precision 3 x 3 matrix.
- [typealias matrix_double3x3](./matrix_double3x3.md)
  A type alias for a double-precision 3 x 3 matrix.
### Deprecated Symbols
- [func matrix_invert(simd_double3x3) -> simd_double3x3](./matrix_invert%28_%29-2lv98.md)
  Returns the inverse of the specified matrix.
- [func matrix_from_columns(SIMD3<Double>, SIMD3<Double>, SIMD3<Double>) -> simd_double3x3](./matrix_from_columns%28_,_,_%29-4bc62.md)
  Returns a new matrix with the specified columns.
- [func matrix_from_diagonal(SIMD3<Double>) -> simd_double3x3](./matrix_from_diagonal%28_%29-3jtgg.md)
  Returns a new matrix with the specified vector on the main diagonal.
- [func matrix_determinant(simd_double3x3) -> Double](./matrix_determinant%28_%29-4bxkm.md)
  Returns the determinant of the specified matrix.
- [func matrix_equal(simd_double3x3, simd_double3x3) -> Bool](./matrix_equal%28_,_%29-9tdua.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_transpose(simd_double3x3) -> double3x3](./matrix_transpose%28_%29-3ectl.md)
  Returns the transpose of a matrix.
- [init(simd_double3x3)](./simd_double3x3/init%28_%29-2o4jh.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_double3x3](./simd_double3x3/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.
### Operators
- [static func * (simd_double3x3, SIMD3<Double>) -> SIMD3<Double>](./simd_double3x3/star%28_,_%29-11ff2.md)
- [static func * (Double, simd_double3x3) -> simd_double3x3](./simd_double3x3/star%28_,_%29-23oic.md)
- [static func * (simd_double3x3, double4x3) -> double4x3](./simd_double3x3/star%28_,_%29-2hizn.md)
- [static func * (simd_double3x3, double3x3) -> double3x3](./simd_double3x3/star%28_,_%29-2oy7n.md)
- [static func * (SIMD3<Double>, simd_double3x3) -> SIMD3<Double>](./simd_double3x3/star%28_,_%29-2yrlv.md)
- [static func * (simd_double3x3, double2x3) -> double2x3](./simd_double3x3/star%28_,_%29-38zoj.md)
- [static func * (simd_double3x3, Double) -> simd_double3x3](./simd_double3x3/star%28_,_%29-8r8se.md)
- [static func *= (inout simd_double3x3, double3x3)](./simd_double3x3/stareq%28_,_%29-4dl51.md)
- [static func *= (inout simd_double3x3, Double)](./simd_double3x3/stareq%28_,_%29-7vz3h.md)
- [static func + (simd_double3x3, simd_double3x3) -> simd_double3x3](./simd_double3x3/plus%28_,_%29.md)
- [static func += (inout simd_double3x3, simd_double3x3)](./simd_double3x3/pluseq%28_,_%29.md)
- [static func - (simd_double3x3) -> simd_double3x3](./simd_double3x3/minus%28_%29.md)
- [static func - (simd_double3x3, simd_double3x3) -> simd_double3x3](./simd_double3x3/minus%28_,_%29.md)
- [static func -= (inout simd_double3x3, simd_double3x3)](./simd_double3x3/minuseq%28_,_%29.md)
### Math Functions
- [simd_add](./simd_add-3e048.md)
  Returns the sum of two matrices.
- [simd_sub](./simd_sub-1bye8.md)
  Returns the difference of two matrices.
- [matrix_scale](./matrix_scale-5igd0.md)
  Returns the product of a scalar value and a matrix.
### Matrix-Scalar Multiplication Functions
- [simd_mul](./simd_mul-6r1mg.md)
  Returns the product of a scalar value and a 3 x 3 matrix.
### Matrix-Vector Multiplication Functions
- [simd_mul](./simd_mul-8vafd.md)
  Returns the product of a three-element vector and a 3 x 3 matrix.
- [matrix_multiply](./matrix_multiply-rhpr.md)
  Returns the product of a three-element vector and a 3 x 3 matrix.
- [simd_mul](./simd_mul-ulvl.md)
  Returns the product of a 3 x 2 matrix and a three-element vector.
- [matrix_multiply](./matrix_multiply-5o7k9.md)
  Returns the product of a 3 x 3 matrix and a three-element vector.
### Matrix-Matrix Multiplication Functions
- [simd_mul](./simd_mul-6war0.md)
  Returns the product of a 2 x 3 matrix and a 3 x 2 matrix.
- [matrix_multiply](./matrix_multiply-9q6cz.md)
  Returns the product of a 2 x 3 matrix and a 3 x 2 matrix.
- [simd_mul](./simd_mul-4t2wx.md)
  Returns the product of a 3 x 3 matrix and a 3 x 3 matrix.
- [matrix_multiply](./matrix_multiply-7h3v.md)
  Returns the product of a 3 x 3 matrix and a 3 x 3 matrix.
- [simd_mul](./simd_mul-7a0d0.md)
  Returns the product of a 4 x 3 matrix and a 3 x 4 matrix.
- [matrix_multiply](./matrix_multiply-8gt1r.md)
  Returns the product of a 4 x 3 matrix and a 3 x 4 matrix.
### Equality Functions
- [simd_equal](./simd_equal-77o8z.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix.
- [simd_almost_equal_elements](./simd_almost_equal_elements-590ch.md)
  Returns true if every element in a matrix is within a specified tolerance to the corresponding element in a second matrix.
- [simd_almost_equal_elements_relative](./simd_almost_equal_elements_relative-1gaj5.md)
  Returns true if every element in a matrix is within a specified double-precision relative tolerance to the corresponding element in a second matrix.
### Determinant and Inverse Functions
- [simd_determinant](./simd_determinant-3a4ma.md)
  Returns the determinant of the specified matrix.
- [simd_inverse](./simd_inverse-3q4en.md)
  Returns the inverse of the specified matrix.
### Linear Combination Function
- [simd_linear_combination](./simd_linear_combination-4hhnj.md)
  Returns the linear combination of two scalar values and two matrices.
### Transpose Function
- [simd_transpose](./simd_transpose-26qy0.md)
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
- [struct simd_double3x4](./simd_double3x4.md)
  A matrix of three columns and four rows that contains double-precision values.
- [struct simd_double4x2](./simd_double4x2.md)
  A matrix of four columns and two rows that contains double-precision values.
- [struct simd_double4x3](./simd_double4x3.md)
  A matrix of four columns and three rows that contains double-precision values.
- [struct simd_double4x4](./simd_double4x4.md)
  A matrix of four columns and four rows that contains double-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_double3x3)*