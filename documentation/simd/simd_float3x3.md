# simd_float3x3

**Framework**: simd  
**Kind**: struct  
**Role**: Structure

A matrix of three columns and three rows that contains single-precision values.

## Declaration

```swift
struct simd_float3x3
```

```c
typedef struct { ... } simd_float3x3;
```

## Mentions

- [Working with Matrices](../Accelerate/working-with-matrices.md)

## Topics

### Initializers
- [init()](./simd_float3x3/init%28%29.md)
  Creates a new matrix with uninitialized memory.
- [init(Float)](./simd_float3x3/init%28_%29-43ntv.md)
  Creates a new matrix with the specified scalar value on the main diagonal.
- [init(diagonal: SIMD3<Float>)](./simd_float3x3/init%28diagonal%29.md)
  Creates a new matrix with the specified vector on the main diagonal.
- [init([SIMD3<Float>])](./simd_float3x3/init%28_%29-51tfs.md)
  Creates a new matrix with the specified columns.
- [init(simd_quatf)](./simd_float3x3/init%28_%29-5wkmz.md)
  Creates a new matrix from the specified quarternion.
- [init(SIMD3<Float>, SIMD3<Float>, SIMD3<Float>)](./simd_float3x3/init%28_,_,_%29.md)
  Creates a new matrix with the specified vectors as columns.
- [init(columns: (simd_float3, simd_float3, simd_float3))](./simd_float3x3/init%28columns%29.md)
  Creates a new matrix with the specified columns.
- [init(rows: [SIMD3<Float>])](./simd_float3x3/init%28rows%29.md)
  Creates a new matrix with the specified rows.
### Matrix Constants
- [let matrix_identity_float3x3: simd_float3x3](./matrix_identity_float3x3.md)
  A 3 x 3 identity matrix.
### Matrix Properties
- [var determinant: Float](./simd_float3x3/determinant.md)
  The determinant of the matrix.
- [var inverse: simd_float3x3](./simd_float3x3/inverse.md)
  The inverse of the matrix.
- [var transpose: float3x3](./simd_float3x3/transpose.md)
  The transpose of the matrix.
- [var columns: (simd_float3, simd_float3, simd_float3)](./simd_float3x3/columns.md)
  The columns of the matrix.
### Matrix Creation Functions
- [func simd_matrix(simd_float3, simd_float3, simd_float3) -> simd_float3x3](./simd_matrix%28_,_,_%29-52z0s.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_float3, simd_float3, simd_float3) -> simd_float3x3](./simd_matrix_from_rows%28_,_,_%29-1tn2x.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD3<Float>, SIMD3<Float>, SIMD3<Float>) -> simd_float3x3](./matrix_from_rows%28_,_,_%29-15v2l.md)
  Returns a new matrix with the specified rows.
- [func simd_matrix3x3(simd_quatf) -> simd_float3x3](./simd_matrix3x3%28_%29-60cx9.md)
  Returns a new matrix with the specified quarternion.
- [simd_diagonal_matrix](./simd_diagonal_matrix-2nvn1.md)
  Returns a new matrix with the specified vector on the main diagonal.
### Element Access
- [subscript(Int) -> SIMD3<Float>](./simd_float3x3/subscript%28_%29.md)
  Accesses the column at the specified position.
- [subscript(Int, Int) -> Float](./simd_float3x3/subscript%28_,_%29.md)
  Accesses the element at the specified position.
### Type Aliases
- [typealias float3x3](./float3x3.md)
- [typealias matrix_float3x3](./matrix_float3x3.md)
### Deprecated Symbols
- [func matrix_invert(simd_float3x3) -> simd_float3x3](./matrix_invert%28_%29-15kif.md)
  Returns the inverse of the specified matrix.
- [func matrix_from_diagonal(SIMD3<Float>) -> simd_float3x3](./matrix_from_diagonal%28_%29-61643.md)
  Returns a new matrix with the specified vector on the main diagonal.
- [func matrix_determinant(simd_float3x3) -> Float](./matrix_determinant%28_%29-2m4vm.md)
  Returns the determinant of the specified matrix.
- [func matrix_equal(simd_float3x3, simd_float3x3) -> Bool](./matrix_equal%28_,_%29-14gko.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_from_columns(SIMD3<Float>, SIMD3<Float>, SIMD3<Float>) -> simd_float3x3](./matrix_from_columns%28_,_,_%29-4c7qb.md)
  Returns a new matrix with the specified columns.
- [func matrix_transpose(simd_float3x3) -> float3x3](./matrix_transpose%28_%29-9pl1z.md)
  Returns the transpose of a matrix.
- [init(simd_float3x3)](./simd_float3x3/init%28_%29-7ymye.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_float3x3](./simd_float3x3/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.
### Operators
- [static func * (Float, simd_float3x3) -> simd_float3x3](./simd_float3x3/star%28_,_%29-4x4d0.md)
- [static func * (simd_float3x3, float2x3) -> float2x3](./simd_float3x3/star%28_,_%29-69c2x.md)
- [static func * (SIMD3<Float>, simd_float3x3) -> SIMD3<Float>](./simd_float3x3/star%28_,_%29-6jkru.md)
- [static func * (simd_float3x3, float4x3) -> float4x3](./simd_float3x3/star%28_,_%29-6p68q.md)
- [static func * (simd_float3x3, Float) -> simd_float3x3](./simd_float3x3/star%28_,_%29-81cfn.md)
- [static func * (simd_float3x3, SIMD3<Float>) -> SIMD3<Float>](./simd_float3x3/star%28_,_%29-8sd17.md)
- [static func * (simd_float3x3, float3x3) -> float3x3](./simd_float3x3/star%28_,_%29-9a517.md)
- [static func *= (inout simd_float3x3, Float)](./simd_float3x3/stareq%28_,_%29-1iqf4.md)
- [static func *= (inout simd_float3x3, float3x3)](./simd_float3x3/stareq%28_,_%29-744e6.md)
- [static func + (simd_float3x3, simd_float3x3) -> simd_float3x3](./simd_float3x3/plus%28_,_%29.md)
- [static func += (inout simd_float3x3, simd_float3x3)](./simd_float3x3/pluseq%28_,_%29.md)
- [static func - (simd_float3x3) -> simd_float3x3](./simd_float3x3/minus%28_%29.md)
- [static func - (simd_float3x3, simd_float3x3) -> simd_float3x3](./simd_float3x3/minus%28_,_%29.md)
- [static func -= (inout simd_float3x3, simd_float3x3)](./simd_float3x3/minuseq%28_,_%29.md)
### Math Functions
- [simd_add](./simd_add-2i7sl.md)
  Returns the sum of two matrices.
- [simd_sub](./simd_sub-8o3lk.md)
  Returns the difference of two matrices.
- [matrix_scale](./matrix_scale-27owq.md)
  Returns the product of a scalar value and a matrix.
### Matrix-Scalar Multiplication Functions
- [simd_mul](./simd_mul-63kq0.md)
  Returns the product of a scalar value and a 3 x 3 matrix.
### Matrix-Vector Multiplication Functions
- [simd_mul](./simd_mul-5kjlm.md)
  Returns the product of a three-element vector and a 3 x 3 matrix.
- [matrix_multiply](./matrix_multiply-8trq3.md)
  Returns the product of a three-element vector and a 3 x 3 matrix.
- [simd_mul](./simd_mul-3yvmm.md)
  Returns the product of a 3 x 3 matrix and a three-element vector.
- [matrix_multiply](./matrix_multiply-7b224.md)
  Returns the product of a 3 x 3 matrix and a three-element vector.
### Matrix-Matrix Multiplication Functions
- [simd_mul](./simd_mul-7xeg2.md)
  Returns the product of a 2 x 3 matrix and a 3 x 2 matrix.
- [simd_mul](./simd_mul-7qt0c.md)
  Returns the product of a 3 x 3 matrix and a 3 x 3 matrix.
- [matrix_multiply](./matrix_multiply-3cx53.md)
  Returns the product of a 3 x 3 matrix and a 3 x 3 matrix.
- [simd_mul](./simd_mul-956ho.md)
  Returns the product of a 4 x 3 matrix and a 3 x 4 matrix.
- [matrix_multiply](./matrix_multiply-88ewr.md)
  Returns the product of a 4 x 3 matrix and a 3 x 4 matrix.
### Equality Functions
- [simd_equal](./simd_equal-2up01.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix.
- [simd_almost_equal_elements](./simd_almost_equal_elements-6065x.md)
  Returns true if every element in a matrix is within a specified tolerance to the corresponding element in a second matrix.
- [simd_almost_equal_elements_relative](./simd_almost_equal_elements_relative-edbd.md)
  Returns true if every element in a matrix is within a specified single-precision relative tolerance to the corresponding element in a second matrix.
### Determinant and Inverse Functions
- [simd_determinant](./simd_determinant-43g30.md)
  Returns the determinant of the specified matrix.
- [simd_inverse](./simd_inverse-9xvv5.md)
  Returns the inverse of the specified matrix.
### Linear Combination Function
- [simd_linear_combination](./simd_linear_combination-4dfvx.md)
  Returns the linear combination of two scalar values and two matrices.
### Transpose Function
- [simd_transpose](./simd_transpose-10jte.md)
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
- [struct simd_float3x4](./simd_float3x4.md)
  A matrix of three columns and four rows that contains single-precision values.
- [struct simd_float4x2](./simd_float4x2.md)
  A matrix of four columns and two rows that contains single-precision values.
- [struct simd_float4x3](./simd_float4x3.md)
  A matrix of four columns and three rows that contains single-precision values.
- [struct simd_float4x4](./simd_float4x4.md)
  A matrix of four columns and four rows that contains single-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_float3x3)*