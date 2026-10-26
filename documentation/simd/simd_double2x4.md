# simd_double2x4

**Framework**: simd  
**Kind**: struct  
**Role**: Structure

A matrix of two columns and four rows that contains double-precision values.

## Declaration

```swift
struct simd_double2x4
```

```c
typedef struct { ... } simd_double2x4;
```

## Topics

### Initializers
- [init()](./simd_double2x4/init%28%29.md)
  Creates a new matrix with uninitialized memory.
- [init(Double)](./simd_double2x4/init%28_%29-71dee.md)
  Creates a new matrix with the specified scalar value on the main diagonal.
- [init(diagonal: SIMD2<Double>)](./simd_double2x4/init%28diagonal%29.md)
  Creates a new matrix with the specified vector on the main diagonal.
- [init([SIMD4<Double>])](./simd_double2x4/init%28_%29-6lqav.md)
  Creates a new matrix from an array.
- [init(SIMD4<Double>, SIMD4<Double>)](./simd_double2x4/init%28_,_%29.md)
  Creates a new matrix with the specified vectors as columns.
- [init(columns: (simd_double4, simd_double4))](./simd_double2x4/init%28columns%29.md)
  Creates a new matrix with the specified columns.
- [init(rows: [SIMD2<Double>])](./simd_double2x4/init%28rows%29.md)
  Creates a new matrix with the specified rows.
### Matrix Properties
- [var transpose: double4x2](./simd_double2x4/transpose.md)
  The transpose of the matrix.
- [var columns: (simd_double4, simd_double4)](./simd_double2x4/columns.md)
  The columns of the matrix.
### Matrix Creation Functions
- [func simd_matrix(simd_double4, simd_double4) -> simd_double2x4](./simd_matrix%28_,_%29-7hafe.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_double2, simd_double2, simd_double2, simd_double2) -> simd_double2x4](./simd_matrix_from_rows%28_,_,_,_%29-851r7.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD2<Double>, SIMD2<Double>, SIMD2<Double>, SIMD2<Double>) -> simd_double2x4](./matrix_from_rows%28_,_,_,_%29-897qw.md)
  Returns a new matrix with the specified rows.
### Element Access
- [subscript(Int) -> SIMD4<Double>](./simd_double2x4/subscript%28_%29.md)
  Accesses the column at the specified position.
- [subscript(Int, Int) -> Double](./simd_double2x4/subscript%28_,_%29.md)
  Accesses the element at the specified position.
### Type Aliases
- [typealias double2x4](./double2x4.md)
  A type alias for a double-precision 2 x 4 matrix.
- [typealias matrix_double2x4](./matrix_double2x4.md)
  A type alias for a double-precision 2 x 4 matrix.
### Deprecated Symbols
- [func matrix_equal(simd_double2x4, simd_double2x4) -> Bool](./matrix_equal%28_,_%29-1dcgx.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_from_columns(SIMD4<Double>, SIMD4<Double>) -> simd_double2x4](./matrix_from_columns%28_,_%29-9q8xb.md)
  Returns a new matrix with the specified columns.
- [func matrix_transpose(simd_double4x2) -> double2x4](./matrix_transpose%28_%29-bpqg.md)
  Returns the transpose of a matrix.
- [init(simd_double2x4)](./simd_double2x4/init%28_%29-6ssjo.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_double2x4](./simd_double2x4/cmatrix.md)
  Creates a new matrix with the specified matrix.
### Operators
- [static func * (simd_double2x4, double3x2) -> double3x4](./simd_double2x4/star%28_,_%29-2rc47.md)
- [static func * (simd_double2x4, double2x2) -> double2x4](./simd_double2x4/star%28_,_%29-3croh.md)
- [static func * (simd_double2x4, SIMD2<Double>) -> SIMD4<Double>](./simd_double2x4/star%28_,_%29-4f5rx.md)
- [static func * (SIMD4<Double>, simd_double2x4) -> SIMD2<Double>](./simd_double2x4/star%28_,_%29-4iash.md)
- [static func * (simd_double2x4, Double) -> simd_double2x4](./simd_double2x4/star%28_,_%29-59wcu.md)
- [static func * (simd_double2x4, double4x2) -> double4x4](./simd_double2x4/star%28_,_%29-8judh.md)
- [static func * (Double, simd_double2x4) -> simd_double2x4](./simd_double2x4/star%28_,_%29-98679.md)
- [static func *= (inout simd_double2x4, Double)](./simd_double2x4/stareq%28_,_%29-45oag.md)
- [static func *= (inout simd_double2x4, double2x2)](./simd_double2x4/stareq%28_,_%29-57wbl.md)
- [static func + (simd_double2x4, simd_double2x4) -> simd_double2x4](./simd_double2x4/plus%28_,_%29.md)
- [static func += (inout simd_double2x4, simd_double2x4)](./simd_double2x4/pluseq%28_,_%29.md)
- [static func - (simd_double2x4) -> simd_double2x4](./simd_double2x4/minus%28_%29.md)
- [static func - (simd_double2x4, simd_double2x4) -> simd_double2x4](./simd_double2x4/minus%28_,_%29.md)
- [static func -= (inout simd_double2x4, simd_double2x4)](./simd_double2x4/minuseq%28_,_%29.md)
### Math Functions
- [simd_add](./simd_add-1e1xc.md)
  Returns the sum of two matrices.
- [simd_sub](./simd_sub-75iiq.md)
  Returns the difference of two matrices.
- [matrix_scale](./matrix_scale-1fgte.md)
  Returns the product of a scalar value and a matrix.
### Matrix-Scalar Multiplication Functions
- [simd_mul](./simd_mul-7g2eo.md)
  Returns the product of a scalar value and a 2 x 4 matrix.
### Matrix-Vector Multiplication Functions
- [simd_mul](./simd_mul-43dfj.md)
  Returns the product of a four-element vector and a 2 x 4 matrix.
- [matrix_multiply](./matrix_multiply-4dr8s.md)
  Returns the product of a four-element vector and a 2 x 4 matrix.
- [simd_mul](./simd_mul-6ub7w.md)
  Returns the product of a 2 x 4 matrix and a two-element vector.
- [matrix_multiply](./matrix_multiply-7vmen.md)
  Returns the product of a 2 x 4 matrix and a two-element vector.
### Matrix-Matrix Multiplication Functions
- [simd_mul](./simd_mul-3mmg5.md)
  Returns the product of a 2 x 4 matrix and a 2 x 2 matrix.
- [matrix_multiply](./matrix_multiply-1k4mc.md)
  Returns the product of a 2 x 4 matrix and a 2 x 2 matrix.
- [simd_mul](./simd_mul-6qmy5.md)
  Returns the product of a 3 x 4 matrix and a 2 x 3 matrix.
- [matrix_multiply](./matrix_multiply-tcz1.md)
  Returns the product of a 3 x 4 matrix and a 2 x 3 matrix.
- [simd_mul](./simd_mul-63k1v.md)
  Returns the product of a 4 x 4 matrix and a 2 x 4 matrix.
- [matrix_multiply](./matrix_multiply-30ogt.md)
  Returns the product of a 4 x 4 matrix and a 2 x 4 matrix.
### Equality Functions
- [simd_equal](./simd_equal-3xz83.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix.
- [simd_almost_equal_elements](./simd_almost_equal_elements-59py1.md)
  Returns true if every element in a matrix is within a specified tolerance to the corresponding element in a second matrix.
- [simd_almost_equal_elements_relative](./simd_almost_equal_elements_relative-8187e.md)
  Returns true if every element in a matrix is within a specified double-precision relative tolerance to the corresponding element in a second matrix.
### Linear Combination Function
- [simd_linear_combination](./simd_linear_combination-gtsr.md)
### Transpose Function
- [simd_transpose](./simd_transpose-847r1.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_double2x4)*