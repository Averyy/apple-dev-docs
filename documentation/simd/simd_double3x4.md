# simd_double3x4

**Framework**: simd  
**Kind**: struct  
**Role**: Structure

A matrix of three columns and four rows that contains double-precision values.

## Declaration

```swift
struct simd_double3x4
```

```c
typedef struct { ... } simd_double3x4;
```

## Topics

### Initializers
- [init()](./simd_double3x4/init%28%29.md)
  Creates a new matrix with uninitialized memory.
- [init(Double)](./simd_double3x4/init%28_%29-11lc1.md)
  Creates a new matrix with the specified scalar value on the main diagonal.
- [init(diagonal: SIMD3<Double>)](./simd_double3x4/init%28diagonal%29.md)
  Creates a new matrix with the specified vector on the main diagonal.
- [init([SIMD4<Double>])](./simd_double3x4/init%28_%29-74wu4.md)
  Creates a new matrix from an array.
- [init(SIMD4<Double>, SIMD4<Double>, SIMD4<Double>)](./simd_double3x4/init%28_,_,_%29.md)
  Creates a new matrix with the specified vectors as columns.
- [init(columns: (simd_double4, simd_double4, simd_double4))](./simd_double3x4/init%28columns%29.md)
  Creates a new matrix with the specified columns.
- [init(rows: [SIMD3<Double>])](./simd_double3x4/init%28rows%29.md)
  Creates a new matrix with the specified rows.
### Matrix Properties
- [var transpose: double4x3](./simd_double3x4/transpose.md)
  The transpose of the matrix.
- [var columns: (simd_double4, simd_double4, simd_double4)](./simd_double3x4/columns.md)
  The columns of the matrix.
### Matrix Creation Functions
- [func simd_matrix(simd_double4, simd_double4, simd_double4) -> simd_double3x4](./simd_matrix%28_,_,_%29-4o4n5.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_double3, simd_double3, simd_double3, simd_double3) -> simd_double3x4](./simd_matrix_from_rows%28_,_,_,_%29-7j052.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD3<Double>, SIMD3<Double>, SIMD3<Double>, SIMD3<Double>) -> simd_double3x4](./matrix_from_rows%28_,_,_,_%29-69xld.md)
  Returns a new matrix with the specified rows.
### Element Access
- [subscript(Int) -> SIMD4<Double>](./simd_double3x4/subscript%28_%29.md)
  Accesses the column at the specified position.
- [subscript(Int, Int) -> Double](./simd_double3x4/subscript%28_,_%29.md)
  Accesses the element at the specified position.
### Type Aliases
- [typealias double3x4](./double3x4.md)
  A type alias for a double-precision 3 x 4 matrix.
- [typealias matrix_double3x4](./matrix_double3x4.md)
  A type alias for a double-precision 3 x 4 matrix.
### Deprecated Symbols
- [func matrix_equal(simd_double3x4, simd_double3x4) -> Bool](./matrix_equal%28_,_%29-4qog1.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_from_columns(SIMD4<Double>, SIMD4<Double>, SIMD4<Double>) -> simd_double3x4](./matrix_from_columns%28_,_,_%29-4no1k.md)
  Returns a new matrix with the specified columns.
- [func matrix_transpose(simd_double4x3) -> double3x4](./matrix_transpose%28_%29-8am0o.md)
  Returns the transpose of a matrix.
- [init(simd_double3x4)](./simd_double3x4/init%28_%29-2qvpe.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_double3x4](./simd_double3x4/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.
### Operators
- [static func * (simd_double3x4, double2x3) -> double2x4](./simd_double3x4/star%28_,_%29-15q5b.md)
- [static func * (Double, simd_double3x4) -> simd_double3x4](./simd_double3x4/star%28_,_%29-2qxoj.md)
- [static func * (SIMD4<Double>, simd_double3x4) -> SIMD3<Double>](./simd_double3x4/star%28_,_%29-3xyct.md)
- [static func * (simd_double3x4, SIMD3<Double>) -> SIMD4<Double>](./simd_double3x4/star%28_,_%29-4g9jd.md)
- [static func * (simd_double3x4, Double) -> simd_double3x4](./simd_double3x4/star%28_,_%29-4qzww.md)
- [static func * (simd_double3x4, double3x3) -> double3x4](./simd_double3x4/star%28_,_%29-6qa2j.md)
- [static func * (simd_double3x4, double4x3) -> double4x4](./simd_double3x4/star%28_,_%29-962p4.md)
- [static func *= (inout simd_double3x4, Double)](./simd_double3x4/stareq%28_,_%29-62fjm.md)
- [static func *= (inout simd_double3x4, double3x3)](./simd_double3x4/stareq%28_,_%29-sjb5.md)
- [static func + (simd_double3x4, simd_double3x4) -> simd_double3x4](./simd_double3x4/plus%28_,_%29.md)
- [static func += (inout simd_double3x4, simd_double3x4)](./simd_double3x4/pluseq%28_,_%29.md)
- [static func - (simd_double3x4) -> simd_double3x4](./simd_double3x4/minus%28_%29.md)
- [static func - (simd_double3x4, simd_double3x4) -> simd_double3x4](./simd_double3x4/minus%28_,_%29.md)
- [static func -= (inout simd_double3x4, simd_double3x4)](./simd_double3x4/minuseq%28_,_%29.md)
### Equality Functions
- [simd_equal](./simd_equal-4m10u.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix.
- [simd_almost_equal_elements](./simd_almost_equal_elements-h72t.md)
  Returns true if every element in a matrix is within a specified tolerance to the corresponding element in a second matrix.
- [simd_almost_equal_elements_relative](./simd_almost_equal_elements_relative-9q7od.md)
  Returns true if every element in a matrix is within a specified double-precision relative tolerance to the corresponding element in a second matrix.
### Math Functions
- [simd_add](./simd_add-53ag9.md)
  Returns the sum of two matrices.
- [simd_sub](./simd_sub-6yn8w.md)
  Returns the difference of two matrices.
- [matrix_scale](./matrix_scale-5ie6g.md)
  Returns the product of a scalar value and a matrix.
### Matrix-Scalar Multiplication Functions
- [simd_mul](./simd_mul-6r1po.md)
  Returns the product of a scalar value and a 3 x 4 matrix.
### Matrix-Vector Multiplication Functions
- [simd_mul](./simd_mul-5zv.md)
  Returns the product of a four-element vector and a 3 x 4 matrix.
- [matrix_multiply](./matrix_multiply-8rk6t.md)
  Returns the product of a four-element vector and a 3 x 4 matrix.
- [simd_mul](./simd_mul-3kj8k.md)
  Returns the product of a 3 x 4 matrix and a three-element vector.
- [matrix_multiply](./matrix_multiply-f05e.md)
  Returns the product of a 3 x 4 matrix and a three-element vector.
### Matrix-Matrix Multiplication Functions
- [simd_mul](./simd_mul-9jaek.md)
  Returns the product of a 2 x 4 matrix and a 3 x 2 matrix.
- [matrix_multiply](./matrix_multiply-5wjn1.md)
  Returns the product of a 2 x 4 matrix and a 3 x 2 matrix.
- [simd_mul](./simd_mul-tzji.md)
  Returns the product of a 3 x 4 matrix and a 3 x 3 matrix.
- [matrix_multiply](./matrix_multiply-6ga2h.md)
  Returns the product of a 3 x 4 matrix and a 3 x 3 matrix.
- [simd_mul](./simd_mul-hhfz.md)
  Returns the product of a 4 x 4 matrix and a 3 x 4 matrix.
- [matrix_multiply](./matrix_multiply-8xc78.md)
  Returns the product of a 4 x 4 matrix and a 3 x 4 matrix.
### Linear Combination Function
- [simd_linear_combination](./simd_linear_combination-2oumb.md)
  Returns the linear combination of two scalar values and two matrices.
### Transpose Function
- [simd_transpose](./simd_transpose-26pwk.md)
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
- [struct simd_double4x2](./simd_double4x2.md)
  A matrix of four columns and two rows that contains double-precision values.
- [struct simd_double4x3](./simd_double4x3.md)
  A matrix of four columns and three rows that contains double-precision values.
- [struct simd_double4x4](./simd_double4x4.md)
  A matrix of four columns and four rows that contains double-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_double3x4)*