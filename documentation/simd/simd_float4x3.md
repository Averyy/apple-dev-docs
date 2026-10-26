# simd_float4x3

**Framework**: simd  
**Kind**: struct  
**Role**: Structure

A matrix of four columns and three rows that contains single-precision values.

## Declaration

```swift
struct simd_float4x3
```

```c
typedef struct { ... } simd_float4x3;
```

## Topics

### Initializers
- [init()](./simd_float4x3/init%28%29.md)
  Creates a new matrix with uninitialized memory.
- [init(Float)](./simd_float4x3/init%28_%29-4h0e8.md)
  Creates a new matrix with the specified scalar value on the main diagonal.
- [init(diagonal: SIMD3<Float>)](./simd_float4x3/init%28diagonal%29.md)
  Creates a new matrix with the specified vector on the main diagonal.
- [init([SIMD3<Float>])](./simd_float4x3/init%28_%29-50uqp.md)
  Creates a new matrix from an array.
- [init(SIMD3<Float>, SIMD3<Float>, SIMD3<Float>, SIMD3<Float>)](./simd_float4x3/init%28_,_,_,_%29.md)
  Creates a new matrix with the specified vectors as columns.
- [init(columns: (simd_float3, simd_float3, simd_float3, simd_float3))](./simd_float4x3/init%28columns%29.md)
  Creates a new matrix with the specified columns.
- [init(rows: [SIMD4<Float>])](./simd_float4x3/init%28rows%29.md)
  Creates a new matrix with the specified rows.
- [init(AffineTransform3D)](./simd_float4x3/init%28_%29-3rlc3.md)
- [init(affineTransform: AffineTransform3D)](./simd_float4x3/init%28affinetransform%29.md)
### Matrix Properties
- [var transpose: float3x4](./simd_float4x3/transpose.md)
  The transpose of the matrix.
- [var columns: (simd_float3, simd_float3, simd_float3, simd_float3)](./simd_float4x3/columns.md)
  The columns of the matrix.
### Matrix Creation Functions
- [func simd_matrix(simd_float3, simd_float3, simd_float3, simd_float3) -> simd_float4x3](./simd_matrix%28_,_,_,_%29-55qff.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_float4, simd_float4, simd_float4) -> simd_float4x3](./simd_matrix_from_rows%28_,_,_%29-81rfz.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD4<Float>, SIMD4<Float>, SIMD4<Float>) -> simd_float4x3](./matrix_from_rows%28_,_,_%29-ld0y.md)
  Returns a new matrix with the specified rows.
### Element Access
- [subscript(Int) -> SIMD3<Float>](./simd_float4x3/subscript%28_%29.md)
  Accesses the column at the specified position.
- [subscript(Int, Int) -> Float](./simd_float4x3/subscript%28_,_%29.md)
  Accesses the element at the specified position.
### Type Aliases
- [typealias float4x3](./float4x3.md)
  A type alias for a single-precision 4 x 3 matrix.
- [typealias matrix_float4x3](./matrix_float4x3.md)
  A type alias for a single-precision 4 x 3 matrix.
### Deprecated Symbols
- [func matrix_equal(simd_float4x3, simd_float4x3) -> Bool](./matrix_equal%28_,_%29-2m44x.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_from_columns(SIMD3<Float>, SIMD3<Float>, SIMD3<Float>, SIMD3<Float>) -> simd_float4x3](./matrix_from_columns%28_,_,_,_%29-7tq9m.md)
  Returns a new matrix with the specified columns.
- [func matrix_transpose(simd_float3x4) -> float4x3](./matrix_transpose%28_%29-2oa75.md)
  Returns the transpose of a matrix.
- [var cmatrix: simd_float4x3](./simd_float4x3/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.
- [init(simd_float4x3)](./simd_float4x3/init%28_%29-6f0m9.md)
  Creates a new matrix with the specified matrix.
### Operators
- [static func * (simd_float4x3, SIMD4<Float>) -> SIMD3<Float>](./simd_float4x3/star%28_,_%29-2x5u4.md)
- [static func * (SIMD3<Float>, simd_float4x3) -> SIMD4<Float>](./simd_float4x3/star%28_,_%29-3hma7.md)
- [static func * (simd_float4x3, float2x4) -> float2x3](./simd_float4x3/star%28_,_%29-3u8eq.md)
- [static func * (simd_float4x3, Float) -> simd_float4x3](./simd_float4x3/star%28_,_%29-3wqpi.md)
- [static func * (simd_float4x3, float4x4) -> float4x3](./simd_float4x3/star%28_,_%29-5if2f.md)
- [static func * (simd_float4x3, float3x4) -> float3x3](./simd_float4x3/star%28_,_%29-6s4w1.md)
- [static func * (Float, simd_float4x3) -> simd_float4x3](./simd_float4x3/star%28_,_%29-6v4mm.md)
- [static func *= (inout simd_float4x3, float4x4)](./simd_float4x3/stareq%28_,_%29-5uxwu.md)
- [static func *= (inout simd_float4x3, Float)](./simd_float4x3/stareq%28_,_%29-9icea.md)
- [static func + (simd_float4x3, simd_float4x3) -> simd_float4x3](./simd_float4x3/plus%28_,_%29.md)
- [static func += (inout simd_float4x3, simd_float4x3)](./simd_float4x3/pluseq%28_,_%29.md)
- [static func - (simd_float4x3) -> simd_float4x3](./simd_float4x3/minus%28_%29.md)
- [static func - (simd_float4x3, simd_float4x3) -> simd_float4x3](./simd_float4x3/minus%28_,_%29.md)
- [static func -= (inout simd_float4x3, simd_float4x3)](./simd_float4x3/minuseq%28_,_%29.md)
### Math Functions
- [simd_add](./simd_add-2mwsl.md)
  Returns the sum of two matrices.
- [simd_sub](./simd_sub-2uvgd.md)
  Returns the difference of two matrices.
- [matrix_scale](./matrix_scale-19677.md)
  Returns the product of a scalar value and a matrix.
### Matrix-Scalar Multiplication Functions
- [simd_mul](./simd_mul-7dh4y.md)
  Returns the product of a scalar value and a 4 x 3 matrix.
### Matrix-Vector Multiplication Functions
- [simd_mul](./simd_mul-9e8z9.md)
  Returns the product of a three-element vector and a 4 x 3 matrix.
- [matrix_multiply](./matrix_multiply-9ikfl.md)
  Returns the product of a three-element vector and a 4 x 3 matrix.
- [matrix_multiply](./matrix_multiply-2zrla.md)
  Returns the product of a 4 x 3 matrix and a four-element vector.
- [simd_mul](./simd_mul-2jbub.md)
  Returns the product of a 4 x 3 matrix and a four-element vector.
### Matrix-Matrix Multiplication Functions
- [simd_mul](./simd_mul-1gyxn.md)
  Returns the product of a 2 x 3 matrix and a 4 x 2 matrix.
- [matrix_multiply](./matrix_multiply-4t7o3.md)
  Returns the product of a 2 x 3 matrix and a 4 x 2 matrix.
- [simd_mul](./simd_mul-99lq6.md)
  Returns the product of a 3 x 3 matrix and a 4 x 3 matrix.
- [matrix_multiply](./matrix_multiply-5sdp5.md)
  Returns the product of a 3 x 3 matrix and a 4 x 3 matrix.
- [simd_mul](./simd_mul-28whi.md)
  Returns the product of a 4 x 3 matrix and a 4 x 4 matrix.
- [matrix_multiply](./matrix_multiply-4emfa.md)
  Returns the product of a 4 x 3 matrix and a 4 x 4 matrix.
### Equality Functions
- [simd_equal](./simd_equal-1da77.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix.
- [simd_almost_equal_elements](./simd_almost_equal_elements-6rxjg.md)
  Returns true if every element in a matrix is within a specified tolerance to the corresponding element in a second matrix.
- [simd_almost_equal_elements_relative](./simd_almost_equal_elements_relative-4tjkf.md)
  Returns true if every element in a matrix is within a specified single-precision relative tolerance to the corresponding element in a second matrix.
### Linear Combination Function
- [simd_linear_combination](./simd_linear_combination-12i0i.md)
  Returns the linear combination of two scalar values and two matrices.
### Transpose Function
- [simd_transpose](./simd_transpose-7h9uh.md)
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
- [struct simd_float2x2](./simd_float2x2.md)
  A matrix of two columns and two rows that contains single-precision values.
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
- [struct simd_float4x4](./simd_float4x4.md)
  A matrix of four columns and four rows that contains single-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_float4x3)*