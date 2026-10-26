# simd_float2x4

**Framework**: simd  
**Kind**: struct  
**Role**: Structure

A matrix of two columns and four rows that contains single-precision values.

## Declaration

```swift
struct simd_float2x4
```

```c
typedef struct { ... } simd_float2x4;
```

## Topics

### Initializers
- [init()](./simd_float2x4/init%28%29.md)
  Creates a new matrix with uninitialized memory.
- [init(Float)](./simd_float2x4/init%28_%29-smdg.md)
  Creates a new matrix with the specified scalar value on the main diagonal.
- [init(diagonal: SIMD2<Float>)](./simd_float2x4/init%28diagonal%29.md)
  Creates a new matrix with the specified vector on the main diagonal.
- [init([SIMD4<Float>])](./simd_float2x4/init%28_%29-hvkr.md)
  Creates a new matrix from an array.
- [init(SIMD4<Float>, SIMD4<Float>)](./simd_float2x4/init%28_,_%29.md)
  Creates a new matrix with the specified vectors as columns.
- [init(columns: (simd_float4, simd_float4))](./simd_float2x4/init%28columns%29.md)
  Creates a new matrix with the specified columns.
- [init(rows: [SIMD2<Float>])](./simd_float2x4/init%28rows%29.md)
  Creates a new matrix with the specified rows.
### Matrix Properties
- [var transpose: float4x2](./simd_float2x4/transpose.md)
  The transpose of the matrix.
- [var columns: (simd_float4, simd_float4)](./simd_float2x4/columns.md)
  The columns of the matrix.
### Matrix Creation Functions
- [func simd_matrix(simd_float4, simd_float4) -> simd_float2x4](./simd_matrix%28_,_%29-7ayva.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_float2, simd_float2, simd_float2, simd_float2) -> simd_float2x4](./simd_matrix_from_rows%28_,_,_,_%29-7s7pv.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD2<Float>, SIMD2<Float>, SIMD2<Float>, SIMD2<Float>) -> simd_float2x4](./matrix_from_rows%28_,_,_,_%29-51dz4.md)
  Returns a new matrix with the specified rows.
### Element Access
- [subscript(Int) -> SIMD4<Float>](./simd_float2x4/subscript%28_%29.md)
  Accesses the column at the specified position.
- [subscript(Int, Int) -> Float](./simd_float2x4/subscript%28_,_%29.md)
  Accesses the element at the specified position.
### Type Aliases
- [typealias float2x4](./float2x4.md)
  A type alias for a single-precision 2 x 4 matrix.
- [typealias matrix_float2x4](./matrix_float2x4.md)
  A type alias for a single-precision 2 x 4 matrix.
### Deprecated Symbols
- [func matrix_from_columns(SIMD4<Float>, SIMD4<Float>) -> simd_float2x4](./matrix_from_columns%28_,_%29-6tvfl.md)
  Returns a new matrix with the specified columns.
- [func matrix_equal(simd_float2x4, simd_float2x4) -> Bool](./matrix_equal%28_,_%29-34fuu.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_transpose(simd_float4x2) -> float2x4](./matrix_transpose%28_%29-5ymlr.md)
  Returns the transpose of a matrix.
- [init(simd_float2x4)](./simd_float2x4/init%28_%29-3teag.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_float2x4](./simd_float2x4/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.
### Operators
- [static func * (SIMD4<Float>, simd_float2x4) -> SIMD2<Float>](./simd_float2x4/star%28_,_%29-10gif.md)
- [static func * (simd_float2x4, float2x2) -> float2x4](./simd_float2x4/star%28_,_%29-239o8.md)
- [static func * (simd_float2x4, float4x2) -> float4x4](./simd_float2x4/star%28_,_%29-35xo4.md)
- [static func * (simd_float2x4, Float) -> simd_float2x4](./simd_float2x4/star%28_,_%29-3x5jg.md)
- [static func * (simd_float2x4, SIMD2<Float>) -> SIMD4<Float>](./simd_float2x4/star%28_,_%29-4clgl.md)
- [static func * (Float, simd_float2x4) -> simd_float2x4](./simd_float2x4/star%28_,_%29-7gnvu.md)
- [static func * (simd_float2x4, float3x2) -> float3x4](./simd_float2x4/star%28_,_%29-7ypgr.md)
- [static func *= (inout simd_float2x4, float2x2)](./simd_float2x4/stareq%28_,_%29-6u2a.md)
- [static func *= (inout simd_float2x4, Float)](./simd_float2x4/stareq%28_,_%29-jfkv.md)
- [static func + (simd_float2x4, simd_float2x4) -> simd_float2x4](./simd_float2x4/plus%28_,_%29.md)
- [static func += (inout simd_float2x4, simd_float2x4)](./simd_float2x4/pluseq%28_,_%29.md)
- [static func - (simd_float2x4) -> simd_float2x4](./simd_float2x4/minus%28_%29.md)
- [static func - (simd_float2x4, simd_float2x4) -> simd_float2x4](./simd_float2x4/minus%28_,_%29.md)
- [static func -= (inout simd_float2x4, simd_float2x4)](./simd_float2x4/minuseq%28_,_%29.md)
### Math Functions
- [simd_add](./simd_add-8r5kq.md)
  Returns the sum of two matrices.
- [simd_sub](./simd_sub-6idm9.md)
  Returns the difference of two matrices.
- [matrix_scale](./matrix_scale-1imr2.md)
  Returns the product of a scalar value and a matrix.
### Matrix-Scalar Multiplication Functions
- [simd_mul](./simd_mul-6xn9.md)
  Returns the product of a scalar value and a 2 x 4 matrix.
### Matrix-Vector Multiplication Functions
- [simd_mul](./simd_mul-5fjl0.md)
  Returns the product of a four-element vector and a 2 x 4 matrix.
- [matrix_multiply](./matrix_multiply-pq7f.md)
  Returns the product of a four-element vector and a 2 x 4 matrix.
- [simd_mul](./simd_mul-9tdcy.md)
  Returns the product of a 2 x 4 matrix and a two-element vector.
- [matrix_multiply](./matrix_multiply-55lia.md)
  Returns the product of a 2 x 4 matrix and a two-element vector.
### Matrix-Matrix Multiplication Functions
- [simd_mul](./simd_mul-65z85.md)
  Returns the product of a 2 x 4 matrix and a 2 x 1 matrix.
- [matrix_multiply](./matrix_multiply-6pu5f.md)
  Returns the product of a 2 x 4 matrix and a 2 x 1 matrix.
- [simd_mul](./simd_mul-9rkxm.md)
  Returns the product of a 3 x 4 matrix and a 2 x 3 matrix.
- [matrix_multiply](./matrix_multiply-5mq06.md)
  Returns the product of a 3 x 4 matrix and a 2 x 3 matrix.
- [simd_mul](./simd_mul-31xd0.md)
  Returns the product of a 4 x 4 matrix and a 2 x 4 matrix.
- [matrix_multiply](./matrix_multiply-20lvz.md)
  Returns the product of a 4 x 4 matrix and a 2 x 4 matrix.
### Equality Functions
- [simd_equal](./simd_equal-6e7pf.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix.
- [simd_almost_equal_elements](./simd_almost_equal_elements-9t9wk.md)
  Returns true if every element in a matrix is within a specified tolerance to the corresponding element in a second matrix.
- [simd_almost_equal_elements_relative](./simd_almost_equal_elements_relative-8geix.md)
  Returns true if every element in a matrix is within a specified single-precision relative tolerance to the corresponding element in a second matrix.
### Linear Combination Function
- [simd_linear_combination](./simd_linear_combination-5m3zf.md)
  Returns the linear combination of two scalar values and two matrices.
### Transpose Function
- [simd_transpose](./simd_transpose-53s98.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_float2x4)*