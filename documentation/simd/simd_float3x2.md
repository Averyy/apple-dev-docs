# simd_float3x2

**Framework**: simd  
**Kind**: struct  
**Role**: Structure

A matrix of three columns and two rows that contains single-precision values.

## Declaration

```swift
struct simd_float3x2
```

```c
typedef struct { ... } simd_float3x2;
```

## Topics

### Initializers
- [init()](./simd_float3x2/init%28%29.md)
  Creates a new matrix with uninitialized memory.
- [init(Float)](./simd_float3x2/init%28_%29-8cvcd.md)
  Creates a new matrix with the specified scalar value on the main diagonal.
- [init(diagonal: SIMD2<Float>)](./simd_float3x2/init%28diagonal%29.md)
  Creates a new matrix with the specified vector on the main diagonal.
- [init([SIMD2<Float>])](./simd_float3x2/init%28_%29-7ssoh.md)
  Creates a new matrix from an array.
- [init(SIMD2<Float>, SIMD2<Float>, SIMD2<Float>)](./simd_float3x2/init%28_,_,_%29.md)
  Creates a new matrix with the specified vectors as columns.
- [init(columns: (simd_float2, simd_float2, simd_float2))](./simd_float3x2/init%28columns%29.md)
  Creates a new matrix with the specified columns.
- [init(rows: [SIMD3<Float>])](./simd_float3x2/init%28rows%29.md)
  Creates a new matrix with the specified rows.
### Matrix Properties
- [var transpose: float2x3](./simd_float3x2/transpose.md)
  The transpose of the matrix.
- [var columns: (simd_float2, simd_float2, simd_float2)](./simd_float3x2/columns.md)
  The columns of the matrix.
### Matrix Creation Functions
- [func simd_matrix(simd_float2, simd_float2, simd_float2) -> simd_float3x2](./simd_matrix%28_,_,_%29-2oltj.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_float3, simd_float3) -> simd_float3x2](./simd_matrix_from_rows%28_,_%29-48bjr.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD3<Float>, SIMD3<Float>) -> simd_float3x2](./matrix_from_rows%28_,_%29-47wrn.md)
  Returns a new matrix with the specified rows.
### Element Access
- [subscript(Int) -> SIMD2<Float>](./simd_float3x2/subscript%28_%29.md)
  Accesses the column at the specified position.
- [subscript(Int, Int) -> Float](./simd_float3x2/subscript%28_,_%29.md)
  Accesses the element at the specified position.
### Type Aliases
- [typealias float3x2](./float3x2.md)
  A type alias for a single-precision 3 x 2 matrix.
- [typealias matrix_float3x2](./matrix_float3x2.md)
  A type alias for a single-precision 3 x 2 matrix.
### Deprecated Symbols
- [func matrix_from_columns(SIMD2<Float>, SIMD2<Float>, SIMD2<Float>) -> simd_float3x2](./matrix_from_columns%28_,_,_%29-6ua0c.md)
  Returns a new matrix with the specified columns.
- [func matrix_equal(simd_float3x2, simd_float3x2) -> Bool](./matrix_equal%28_,_%29-1kgro.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_transpose(simd_float3x2) -> float2x3](./matrix_transpose%28_%29-92iqd.md)
  Returns the transpose of a matrix.
- [var cmatrix: simd_float3x2](./simd_float3x2/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.
- [init(simd_float3x2)](./simd_float3x2/init%28_%29-323m3.md)
  Creates a new matrix with the specified matrix.
### Operators
- [static func * (simd_float3x2, float3x3) -> float3x2](./simd_float3x2/star%28_,_%29-2dgpn.md)
- [static func * (simd_float3x2, float2x3) -> float2x2](./simd_float3x2/star%28_,_%29-2raa3.md)
- [static func * (simd_float3x2, float4x3) -> float4x2](./simd_float3x2/star%28_,_%29-5obls.md)
- [static func * (simd_float3x2, Float) -> simd_float3x2](./simd_float3x2/star%28_,_%29-7x4bm.md)
- [static func * (SIMD2<Float>, simd_float3x2) -> SIMD3<Float>](./simd_float3x2/star%28_,_%29-83wp.md)
- [static func * (simd_float3x2, SIMD3<Float>) -> SIMD2<Float>](./simd_float3x2/star%28_,_%29-8l62c.md)
- [static func * (Float, simd_float3x2) -> simd_float3x2](./simd_float3x2/star%28_,_%29-9c2w1.md)
- [static func *= (inout simd_float3x2, float3x3)](./simd_float3x2/stareq%28_,_%29-46fya.md)
- [static func *= (inout simd_float3x2, Float)](./simd_float3x2/stareq%28_,_%29-6ojp8.md)
- [static func + (simd_float3x2, simd_float3x2) -> simd_float3x2](./simd_float3x2/plus%28_,_%29.md)
- [static func += (inout simd_float3x2, simd_float3x2)](./simd_float3x2/pluseq%28_,_%29.md)
- [static func - (simd_float3x2) -> simd_float3x2](./simd_float3x2/minus%28_%29.md)
- [static func - (simd_float3x2, simd_float3x2) -> simd_float3x2](./simd_float3x2/minus%28_,_%29.md)
- [static func -= (inout simd_float3x2, simd_float3x2)](./simd_float3x2/minuseq%28_,_%29.md)
### Math Functions
- [simd_add](./simd_add-2n7i.md)
  Returns the sum of two matrices.
- [simd_sub](./simd_sub-5gv4w.md)
  Returns the difference of two matrices.
- [matrix_scale](./matrix_scale-27p9m.md)
  Returns the product of a scalar value and a matrix.
### Matrix-Scalar Multiplication Functions
- [simd_mul](./simd_mul-63kuc.md)
  Returns the product of a scalar value and a 3 x 2 matrix.
### Matrix-Vector Multiplication Functions
- [matrix_multiply](./matrix_multiply-1e54g.md)
  Returns the product of a two-element vector and a 3 x 2 matrix.
- [simd_mul](./simd_mul-6vmls.md)
  Returns the product of a four-element vector and a 2 x 4 matrix.
- [matrix_multiply](./matrix_multiply-3bktl.md)
  Returns the product of a 3 x 2 matrix and a three-element vector.
- [simd_mul](./simd_mul-3kx08.md)
  Returns the product of a 3 x 2 matrix and a three-element vector.
### Matrix-Matrix Multiplication Functions
- [simd_mul](./simd_mul-5coc0.md)
  Returns the product of a 2 x 2 matrix and a 3 x 2 matrix.
- [matrix_multiply](./matrix_multiply-2syft.md)
  Returns the product of a 2 x 2 matrix and a 3 x 2 matrix.
- [simd_mul](./simd_mul-9m23z.md)
  Returns the product of a 3 x 2 matrix and a 3 x 3 matrix.
- [matrix_multiply](./matrix_multiply-2cyog.md)
  Returns the product of a 3 x 2 matrix and a 3 x 3 matrix.
- [simd_mul](./simd_mul-39sak.md)
  Returns the product of a 4 x 2 matrix and a 3 x 4 matrix.
- [matrix_multiply](./matrix_multiply-4o3v4.md)
  Returns the product of a 4 x 2 matrix and a 3 x 4 matrix.
### Equality Functions
- [simd_equal](./simd_equal-6hbvw.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix.
- [simd_almost_equal_elements](./simd_almost_equal_elements-2osqw.md)
  Returns true if every element in a matrix is within a specified tolerance to the corresponding element in a second matrix.
- [simd_almost_equal_elements_relative](./simd_almost_equal_elements_relative-80z14.md)
  Returns true if every element in a matrix is within a specified single-precision relative tolerance to the corresponding element in a second matrix.
### Linear Combination Function
- [simd_linear_combination](./simd_linear_combination-7mkq9.md)
  Returns the linear combination of two scalar values and two matrices.
### Transpose Function
- [simd_transpose](./simd_transpose-10k3m.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_float3x2)*