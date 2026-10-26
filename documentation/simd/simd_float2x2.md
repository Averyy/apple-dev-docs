# simd_float2x2

**Framework**: simd  
**Kind**: struct  
**Role**: Structure

A matrix of two columns and two rows that contains single-precision values.

## Declaration

```swift
struct simd_float2x2
```

```c
typedef struct { ... } simd_float2x2;
```

## Topics

### Initializers
- [init()](./simd_float2x2/init%28%29.md)
  Creates a new matrix with uninitialized memory.
- [init(Float)](./simd_float2x2/init%28_%29-55fda.md)
  Creates a new matrix with the specified scalar value on the main diagonal.
- [init(diagonal: SIMD2<Float>)](./simd_float2x2/init%28diagonal%29.md)
  Creates a new matrix with the specified vector on the main diagonal.
- [init([SIMD2<Float>])](./simd_float2x2/init%28_%29-2mgex.md)
  Creates a new matrix with the specified columns.
- [init(SIMD2<Float>, SIMD2<Float>)](./simd_float2x2/init%28_,_%29.md)
  Creates a new matrix with the specified vectors as columns.
- [init(columns: (simd_float2, simd_float2))](./simd_float2x2/init%28columns%29.md)
  Creates a new matrix with the specified columns.
- [init(rows: [SIMD2<Float>])](./simd_float2x2/init%28rows%29.md)
  Creates a new matrix with the specified rows.
### Matrix Constants
- [let matrix_identity_float2x2: simd_float2x2](./matrix_identity_float2x2.md)
  A 2 x 2 identity matrix.
### Matrix Properties
- [var determinant: Float](./simd_float2x2/determinant.md)
  The determinant of the matrix.
- [var inverse: simd_float2x2](./simd_float2x2/inverse.md)
  The inverse of the matrix.
- [var transpose: float2x2](./simd_float2x2/transpose.md)
  The transpose of the matrix.
- [var columns: (simd_float2, simd_float2)](./simd_float2x2/columns.md)
  The columns of the matrix.
### Matrix Creation Functions
- [func simd_matrix(simd_float2, simd_float2) -> simd_float2x2](./simd_matrix%28_,_%29-1ftcm.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_float2, simd_float2) -> simd_float2x2](./simd_matrix_from_rows%28_,_%29-3mqrr.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD2<Float>, SIMD2<Float>) -> simd_float2x2](./matrix_from_rows%28_,_%29-2pi8i.md)
  Returns a new matrix with the specified rows.
- [simd_diagonal_matrix](./simd_diagonal_matrix-2rboq.md)
  Returns a new matrix with the specified vector on the main diagonal.
### Element Access
- [subscript(Int) -> SIMD2<Float>](./simd_float2x2/subscript%28_%29.md)
  Accesses the column at the specified position.
- [subscript(Int, Int) -> Float](./simd_float2x2/subscript%28_,_%29.md)
  Accesses the element at the specified position.
### Type Aliases
- [typealias float2x2](./float2x2.md)
  A type alias for a single-precision 2 x 2 matrix.
- [typealias matrix_float2x2](./matrix_float2x2.md)
  A type alias for a single-precision 2 x 2 matrix.
### Deprecated Symbols
- [func matrix_invert(simd_float2x2) -> simd_float2x2](./matrix_invert%28_%29-94e37.md)
  Returns the inverse of the specified matrix.
- [func matrix_transpose(simd_float2x2) -> float2x2](./matrix_transpose%28_%29-77v7g.md)
  Returns the transpose of a matrix.
- [func matrix_from_diagonal(SIMD2<Float>) -> simd_float2x2](./matrix_from_diagonal%28_%29-1v0zl.md)
  Returns a new matrix with the specified vector on the main diagonal.
- [func matrix_from_columns(SIMD2<Float>, SIMD2<Float>) -> simd_float2x2](./matrix_from_columns%28_,_%29-5urmx.md)
  Returns a new matrix with the specified columns.
- [func matrix_determinant(simd_float2x2) -> Float](./matrix_determinant%28_%29-30k4n.md)
  Returns the determinant of the specified matrix.
- [func matrix_equal(simd_float2x2, simd_float2x2) -> Bool](./matrix_equal%28_,_%29-88hz9.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [init(simd_float2x2)](./simd_float2x2/init%28_%29-uyy7.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_float2x2](./simd_float2x2/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.
### Operators
- [static func * (simd_float2x2, float2x2) -> float2x2](./simd_float2x2/star%28_,_%29-2jwi9.md)
- [static func * (simd_float2x2, float3x2) -> float3x2](./simd_float2x2/star%28_,_%29-39xxb.md)
- [static func * (simd_float2x2, float4x2) -> float4x2](./simd_float2x2/star%28_,_%29-4h9qy.md)
- [static func * (simd_float2x2, SIMD2<Float>) -> SIMD2<Float>](./simd_float2x2/star%28_,_%29-5fo9p.md)
- [static func * (simd_float2x2, Float) -> simd_float2x2](./simd_float2x2/star%28_,_%29-7begh.md)
- [static func * (Float, simd_float2x2) -> simd_float2x2](./simd_float2x2/star%28_,_%29-92stm.md)
- [static func * (SIMD2<Float>, simd_float2x2) -> SIMD2<Float>](./simd_float2x2/star%28_,_%29-98lyp.md)
- [static func *= (inout simd_float2x2, float2x2)](./simd_float2x2/stareq%28_,_%29-2vg0e.md)
- [static func *= (inout simd_float2x2, Float)](./simd_float2x2/stareq%28_,_%29-obw4.md)
- [static func + (simd_float2x2, simd_float2x2) -> simd_float2x2](./simd_float2x2/plus%28_,_%29.md)
- [static func += (inout simd_float2x2, simd_float2x2)](./simd_float2x2/pluseq%28_,_%29.md)
- [static func - (simd_float2x2) -> simd_float2x2](./simd_float2x2/minus%28_%29.md)
- [static func - (simd_float2x2, simd_float2x2) -> simd_float2x2](./simd_float2x2/minus%28_,_%29.md)
- [static func -= (inout simd_float2x2, simd_float2x2)](./simd_float2x2/minuseq%28_,_%29.md)
### Math Functions
- [simd_add](./simd_add-9bz1e.md)
  Returns the sum of two matrices.
- [simd_sub](./simd_sub-1rmtl.md)
  Returns the difference of two matrices.
- [matrix_scale](./matrix_scale-1ioqq.md)
  Returns the product of a scalar value and a matrix.
### Matrix-Scalar Multiplication Functions
- [simd_mul](./simd_mul-6x19.md)
  Returns the product of a scalar value and a 2 x 2 matrix.
### Matrix-Vector Multiplication Functions
- [simd_mul](./simd_mul-2tj8m.md)
  Returns the product of a two-element vector and a 2 x 2 matrix.
- [matrix_multiply](./matrix_multiply-7aivt.md)
  Returns the product of a two-element vector and a 2 x 2 matrix.
- [simd_mul](./simd_mul-2ymdt.md)
  Returns the product of a 2 x 2 matrix and a two-element vector.
- [matrix_multiply](./matrix_multiply-2mvj0.md)
  Returns the product of a 2 x 2 matrix and a two-element vector.
### Matrix-Matrix Multiplication Functions
- [simd_mul](./simd_mul-4lnzm.md)
  Returns the product of a 2 x 2 matrix and a 2 x 2 matrix.
- [matrix_multiply](./matrix_multiply-906o0.md)
  Returns the product of a 2 x 2 matrix and a 2 x 2 matrix.
- [simd_mul](./simd_mul-5jxwn.md)
  Returns the product of a 3 x 2 matrix and a 2 x 3 matrix.
- [matrix_multiply](./matrix_multiply-89c0b.md)
  Returns the product of a 3 x 2 matrix and a 2 x 3 matrix.
- [simd_mul](./simd_mul-7cznu.md)
  Returns the product of a 4 x 2 matrix and a 2 x 2 matrix.
- [matrix_multiply](./matrix_multiply-8rb5m.md)
  Returns the product of a 4 x 2 matrix and a 2 x 4 matrix.
### Equality Functions
- [simd_equal](./simd_equal-9hy16.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix.
- [simd_almost_equal_elements](./simd_almost_equal_elements-50e42.md)
  Returns true if every element in a matrix is within a specified tolerance to the corresponding element in a second matrix.
- [simd_almost_equal_elements_relative](./simd_almost_equal_elements_relative-6ia0i.md)
  Returns true if every element in a matrix is within a specified single-precision relative tolerance to the corresponding element in a second matrix.
### Determinant and Inverse Functions
- [simd_determinant](./simd_determinant-86nly.md)
  Returns the determinant of the specified matrix.
- [simd_inverse](./simd_inverse-5uob3.md)
  Returns the inverse of the specified matrix.
### Linear Combination Function
- [simd_linear_combination](./simd_linear_combination-6c418.md)
  Returns the linear combination of two scalar values and two matrices.
### Transpose Function
- [simd_transpose](./simd_transpose-53rn8.md)
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
- [struct simd_float2x3](./simd_float2x3.md)
  A matrix of two columns and three rows that contains single-precision values.
- [struct simd_float2x4](./simd_float2x4.md)
  A matrix of two columns and four rows that contains single-precision values.
- [struct simd_float3x2](./simd_float3x2.md)
  A matrix of three columns and two rows that contains single-precision values.
- [struct simd_float3x3](./simd_float3x3.md)
  A matrix of three columns and three rows that contains single-precision values.
- [struct simd_float3x4](./simd_float3x4.md)
  A matrix of three columns and four rows that contains single-precision values.
- [struct simd_float4x2](./simd_float4x2.md)
  A matrix of four columns and two rows that contains single-precision values.
- [struct simd_float4x3](./simd_float4x3.md)
  A matrix of four columns and three rows that contains single-precision values.
- [struct simd_float4x4](./simd_float4x4.md)
  A matrix of four columns and four rows that contains single-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_float2x2)*