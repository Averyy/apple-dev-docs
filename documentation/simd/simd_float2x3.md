# simd_float2x3

**Framework**: simd  
**Kind**: struct  
**Role**: Structure

A matrix of two columns and three rows that contains single-precision values.

## Declaration

```swift
struct simd_float2x3
```

```c
typedef struct { ... } simd_float2x3;
```

## Topics

### Initializers
- [init()](./simd_float2x3/init%28%29.md)
  Creates a new matrix with uninitialized memory.
- [init(Float)](./simd_float2x3/init%28_%29-9lk1g.md)
  Creates a new matrix with the specified scalar value on the main diagonal.
- [init(diagonal: SIMD2<Float>)](./simd_float2x3/init%28diagonal%29.md)
  Creates a new matrix with the specified vector on the main diagonal.
- [init([SIMD3<Float>])](./simd_float2x3/init%28_%29-757nf.md)
  Creates a new matrix from an array.
- [init(SIMD3<Float>, SIMD3<Float>)](./simd_float2x3/init%28_,_%29.md)
  Creates a new matrix with the specified vectors as columns.
- [init(columns: (simd_float3, simd_float3))](./simd_float2x3/init%28columns%29.md)
  Creates a new matrix with the specified columns.
- [init(rows: [SIMD2<Float>])](./simd_float2x3/init%28rows%29.md)
  Creates a new matrix with the specified rows.
### Matrix Properties
- [var transpose: float3x2](./simd_float2x3/transpose.md)
  The transpose of the matrix.
- [var columns: (simd_float3, simd_float3)](./simd_float2x3/columns.md)
  The columns of the matrix.
### Matrix Creation Functions
- [func simd_matrix(simd_float3, simd_float3) -> simd_float2x3](./simd_matrix%28_,_%29-7qavs.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_float2, simd_float2, simd_float2) -> simd_float2x3](./simd_matrix_from_rows%28_,_,_%29-9kksc.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD2<Float>, SIMD2<Float>, SIMD2<Float>) -> simd_float2x3](./matrix_from_rows%28_,_,_%29-m0hw.md)
  Returns a new matrix with the specified rows.
### Element Access
- [subscript(Int) -> SIMD3<Float>](./simd_float2x3/subscript%28_%29.md)
  Accesses the column at the specified position.
- [subscript(Int, Int) -> Float](./simd_float2x3/subscript%28_,_%29.md)
  Accesses the element at the specified position.
### Type Aliases
- [typealias float2x3](./float2x3.md)
  A type alias for a single-precision 2 x 3 matrix.
- [typealias matrix_float2x3](./matrix_float2x3.md)
  A type alias for a single-precision 2 x 3 matrix.
### Deprecated Symbols
- [func matrix_from_columns(SIMD3<Float>, SIMD3<Float>) -> simd_float2x3](./matrix_from_columns%28_,_%29-8tygq.md)
  Returns a new matrix with the specified columns.
- [func matrix_equal(simd_float2x3, simd_float2x3) -> Bool](./matrix_equal%28_,_%29-he2l.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_transpose(simd_float2x3) -> float3x2](./matrix_transpose%28_%29-71xii.md)
  Returns the transpose of a matrix.
- [init(simd_float2x3)](./simd_float2x3/init%28_%29-55t2w.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_float2x3](./simd_float2x3/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.
### Operators
- [static func * (simd_float2x3, Float) -> simd_float2x3](./simd_float2x3/star%28_,_%29-2hkqa.md)
- [static func * (simd_float2x3, float2x2) -> float2x3](./simd_float2x3/star%28_,_%29-4hssh.md)
- [static func * (Float, simd_float2x3) -> simd_float2x3](./simd_float2x3/star%28_,_%29-4pre4.md)
- [static func * (simd_float2x3, float4x2) -> float4x3](./simd_float2x3/star%28_,_%29-7vzog.md)
- [static func * (SIMD3<Float>, simd_float2x3) -> SIMD2<Float>](./simd_float2x3/star%28_,_%29-82e85.md)
- [static func * (simd_float2x3, float3x2) -> float3x3](./simd_float2x3/star%28_,_%29-84qqs.md)
- [static func * (simd_float2x3, SIMD2<Float>) -> SIMD3<Float>](./simd_float2x3/star%28_,_%29-955tc.md)
- [static func *= (inout simd_float2x3, Float)](./simd_float2x3/stareq%28_,_%29-6hcqy.md)
- [static func *= (inout simd_float2x3, float2x2)](./simd_float2x3/stareq%28_,_%29-7ohft.md)
- [static func + (simd_float2x3, simd_float2x3) -> simd_float2x3](./simd_float2x3/plus%28_,_%29.md)
- [static func += (inout simd_float2x3, simd_float2x3)](./simd_float2x3/pluseq%28_,_%29.md)
- [static func - (simd_float2x3) -> simd_float2x3](./simd_float2x3/minus%28_%29.md)
- [static func - (simd_float2x3, simd_float2x3) -> simd_float2x3](./simd_float2x3/minus%28_,_%29.md)
- [static func -= (inout simd_float2x3, simd_float2x3)](./simd_float2x3/minuseq%28_,_%29.md)
### Math Functions
- [simd_add](./simd_add-9wpew.md)
  Returns the sum of two matrices.
- [simd_sub](./simd_sub-964zd.md)
  Returns the difference of two matrices.
- [matrix_scale](./matrix_scale-1iouq.md)
  Returns the product of a scalar value and a matrix.
### Matrix-Scalar Multiplication Functions
- [simd_mul](./simd_mul-6xb7.md)
  Returns the product of a scalar value and a 2 x 3 matrix.
### Matrix-Vector Multiplication Functions
- [matrix_multiply](./matrix_multiply-4h3hg.md)
  Returns the product of a three-element vector and a 2 x 3 matrix.
- [simd_mul](./simd_mul-9nrvk.md)
  Returns the product of a three-element vector and a 2 x 3 matrix.
- [matrix_multiply](./matrix_multiply-46tk7.md)
  Returns the product of a 2 x 2 matrix and a two-element vector.
- [simd_mul](./simd_mul-5urnv.md)
  Returns the product of a 2 x 2 matrix and a two-element vector.
### Matrix-Matrix Multiplication Functions
- [simd_mul](./simd_mul-3uh3s.md)
  Returns the product of a 2 x 3 matrix and a 2 x 2 matrix.
- [matrix_multiply](./matrix_multiply-1f27l.md)
  Returns the product of a 2 x 3 matrix and a 2 x 2 matrix.
- [matrix_multiply](./matrix_multiply-q1lr.md)
  Returns the product of a 2 x 3 matrix and a 3 x 2 matrix.
- [simd_mul](./simd_mul-4cl38.md)
  Returns the product of a 3 x 3 matrix and a 2 x 3 matrix.
- [matrix_multiply](./matrix_multiply-5hr72.md)
  Returns the product of a 3 x 3 matrix and a 2 x 3 matrix.
- [simd_mul](./simd_mul-532ye.md)
  Returns the product of a 4 x 3 matrix and a 2 x 4 matrix.
- [matrix_multiply](./matrix_multiply-2l8mv.md)
  Returns the product of a 4 x 3 matrix and a 2 x 4 matrix.
### Equality Functions
- [simd_equal](./simd_equal-2flog.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix.
- [simd_almost_equal_elements](./simd_almost_equal_elements-jjiy.md)
  Returns true if every element in a matrix is within a specified tolerance to the corresponding element in a second matrix.
- [simd_almost_equal_elements_relative](./simd_almost_equal_elements_relative-8togh.md)
  Returns true if every element in a matrix is within a specified single-precision relative tolerance to the corresponding element in a second matrix.
### Linear Combination Function
- [simd_linear_combination](./simd_linear_combination-4qv3c.md)
  Returns the linear combination of two scalar values and two matrices.
### Transpose Function
- [simd_transpose](./simd_transpose-53rrs.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_float2x3)*