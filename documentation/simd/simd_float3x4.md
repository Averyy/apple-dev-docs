# simd_float3x4

**Framework**: simd  
**Kind**: struct  
**Role**: Structure

A matrix of three columns and four rows that contains single-precision values.

## Declaration

```swift
struct simd_float3x4
```

```c
typedef struct { ... } simd_float3x4;
```

## Topics

### Initializers
- [init()](./simd_float3x4/init%28%29.md)
  Creates a new matrix with uninitialized memory.
- [init(Float)](./simd_float3x4/init%28_%29-2os7r.md)
  Creates a new matrix with the specified scalar value on the main diagonal.
- [init(diagonal: SIMD3<Float>)](./simd_float3x4/init%28diagonal%29.md)
  Creates a new matrix with the specified vector on the main diagonal.
- [init([SIMD4<Float>])](./simd_float3x4/init%28_%29-4w4et.md)
  Creates a new matrix from an array.
- [init(SIMD4<Float>, SIMD4<Float>, SIMD4<Float>)](./simd_float3x4/init%28_,_,_%29.md)
  Creates a new matrix with the specified vectors as columns.
- [init(columns: (simd_float4, simd_float4, simd_float4))](./simd_float3x4/init%28columns%29.md)
  Creates a new matrix with the specified columns.
- [init(rows: [SIMD3<Float>])](./simd_float3x4/init%28rows%29.md)
  Creates a new matrix with the specified rows.
### Matrix Properties
- [var transpose: float4x3](./simd_float3x4/transpose.md)
  The transpose of the matrix.
- [var columns: (simd_float4, simd_float4, simd_float4)](./simd_float3x4/columns.md)
  The columns of the matrix.
### Matrix Creation Functions
- [func simd_matrix(simd_float4, simd_float4, simd_float4) -> simd_float3x4](./simd_matrix%28_,_,_%29-1vwb0.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_float3, simd_float3, simd_float3, simd_float3) -> simd_float3x4](./simd_matrix_from_rows%28_,_,_,_%29-6irzy.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD3<Float>, SIMD3<Float>, SIMD3<Float>, SIMD3<Float>) -> simd_float3x4](./matrix_from_rows%28_,_,_,_%29-4bn2a.md)
  Returns a new matrix with the specified rows.
### Element Access
- [subscript(Int) -> SIMD4<Float>](./simd_float3x4/subscript%28_%29.md)
  Accesses the column at the specified position.
- [subscript(Int, Int) -> Float](./simd_float3x4/subscript%28_,_%29.md)
  Accesses the element at the specified position.
### Type Aliases
- [typealias float3x4](./float3x4.md)
  A type alias for a single-precision 3 x 4 matrix.
- [typealias matrix_float3x4](./matrix_float3x4.md)
  A type alias for a single-precision 3 x 4 matrix.
### Deprecated Symbols
- [func matrix_equal(simd_float3x4, simd_float3x4) -> Bool](./matrix_equal%28_,_%29-6el88.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_from_columns(SIMD4<Float>, SIMD4<Float>, SIMD4<Float>) -> simd_float3x4](./matrix_from_columns%28_,_,_%29-5nhl4.md)
  Returns a new matrix with the specified columns.
- [func matrix_transpose(simd_float4x3) -> float3x4](./matrix_transpose%28_%29-6ygo1.md)
  Returns the transpose of a matrix.
- [init(simd_float3x4)](./simd_float3x4/init%28_%29-8fk31.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_float3x4](./simd_float3x4/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.
### Operators
- [static func * (Float, simd_float3x4) -> simd_float3x4](./simd_float3x4/star%28_,_%29-309ny.md)
- [static func * (simd_float3x4, float2x3) -> float2x4](./simd_float3x4/star%28_,_%29-39co8.md)
- [static func * (simd_float3x4, SIMD3<Float>) -> SIMD4<Float>](./simd_float3x4/star%28_,_%29-5hu83.md)
- [static func * (SIMD4<Float>, simd_float3x4) -> SIMD3<Float>](./simd_float3x4/star%28_,_%29-71y0j.md)
- [static func * (simd_float3x4, Float) -> simd_float3x4](./simd_float3x4/star%28_,_%29-7vkfz.md)
- [static func * (simd_float3x4, float4x3) -> float4x4](./simd_float3x4/star%28_,_%29-8gb9i.md)
- [static func * (simd_float3x4, float3x3) -> float3x4](./simd_float3x4/star%28_,_%29-ehb7.md)
- [static func *= (inout simd_float3x4, Float)](./simd_float3x4/stareq%28_,_%29-4brfc.md)
- [static func *= (inout simd_float3x4, float3x3)](./simd_float3x4/stareq%28_,_%29-8yuww.md)
- [static func + (simd_float3x4, simd_float3x4) -> simd_float3x4](./simd_float3x4/plus%28_,_%29.md)
- [static func += (inout simd_float3x4, simd_float3x4)](./simd_float3x4/pluseq%28_,_%29.md)
- [static func - (simd_float3x4) -> simd_float3x4](./simd_float3x4/minus%28_%29.md)
- [static func - (simd_float3x4, simd_float3x4) -> simd_float3x4](./simd_float3x4/minus%28_,_%29.md)
- [static func -= (inout simd_float3x4, simd_float3x4)](./simd_float3x4/minuseq%28_,_%29.md)
### Equality Functions
- [simd_equal](./simd_equal-8ywka.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix.
- [simd_almost_equal_elements](./simd_almost_equal_elements-7vp0d.md)
  Returns true if every element in a matrix is within a specified tolerance to the corresponding element in a second matrix.
- [simd_almost_equal_elements_relative](./simd_almost_equal_elements_relative-8ea8s.md)
  Returns true if every element in a matrix is within a specified single-precision relative tolerance to the corresponding element in a second matrix.
### Math Functions
- [simd_add](./simd_add-2poit.md)
  Returns the sum of two matrices.
- [simd_sub](./simd_sub-8zkd6.md)
  Returns the difference of two matrices.
- [matrix_scale](./matrix_scale-27nie.md)
  Returns the product of a scalar value and a matrix.
### Matrix-Scalar Multiplication Functions
- [simd_mul](./simd_mul-63lgs.md)
  Returns the product of a scalar value and a 3 x 4 matrix.
### Matrix-Vector Multiplication Functions
- [simd_mul](./simd_mul-11qnx.md)
  Returns the product of a four-element vector and a 3 x 4 matrix.
- [matrix_multiply](./matrix_multiply-4sxh3.md)
  Returns the product of a four-element vector and a 3 x 4 matrix.
- [simd_mul](./simd_mul-9abtt.md)
  Returns the product of a 3 x 4 matrix and a three-element vector.
- [matrix_multiply](./matrix_multiply-5tf39.md)
  Returns the product of a 3 x 4 matrix and a three-element vector.
### Matrix-Matrix Multiplication Functions
- [simd_mul](./simd_mul-22ry5.md)
  Returns the product of a 2 x 4 matrix and a 3 x 2 matrix.
- [matrix_multiply](./matrix_multiply-2mmjb.md)
  Returns the product of a 2 x 4 matrix and a 3 x 2 matrix.
- [simd_mul](./simd_mul-3uxip.md)
  Returns the product of a 3 x 4 matrix and a 3 x 3 matrix.
- [matrix_multiply](./matrix_multiply-1a1tt.md)
  Returns the product of a 3 x 4 matrix and a 3 x 3 matrix.
- [simd_mul](./simd_mul-8ylcd.md)
  Returns the product of a 4 x 4 matrix and a 3 x 4 matrix.
- [matrix_multiply](./matrix_multiply-15ddt.md)
  Returns the product of a 4 x 4 matrix and a 3 x 4 matrix.
### Linear Combination Function
- [simd_linear_combination](./simd_linear_combination-q4rt.md)
  Returns the linear combination of two scalar values and two matrices.
### Transpose Function
- [simd_transpose](./simd_transpose-10krq.md)
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
- [struct simd_float4x2](./simd_float4x2.md)
  A matrix of four columns and two rows that contains single-precision values.
- [struct simd_float4x3](./simd_float4x3.md)
  A matrix of four columns and three rows that contains single-precision values.
- [struct simd_float4x4](./simd_float4x4.md)
  A matrix of four columns and four rows that contains single-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_float3x4)*