# simd_float4x4

**Framework**: simd  
**Kind**: struct  
**Role**: Structure

A matrix of four columns and four rows that contains single-precision values.

## Declaration

```swift
struct simd_float4x4
```

```c
typedef struct { ... } simd_float4x4;
```

## Topics

### Initializers
- [init()](./simd_float4x4/init%28%29.md)
  Creates a new matrix with uninitialized memory.
- [init(Float)](./simd_float4x4/init%28_%29-6pc85.md)
  Creates a new matrix with the specified scalar value on the main diagonal.
- [init(diagonal: SIMD4<Float>)](./simd_float4x4/init%28diagonal%29.md)
  Creates a new matrix with the specified vector on the main diagonal.
- [init([SIMD4<Float>])](./simd_float4x4/init%28_%29-50sjs.md)
  Creates a new matrix with the specified columns.
- [init(simd_quatf)](./simd_float4x4/init%28_%29-7ig5g.md)
  Creates a new matrix from the specified quaternion.
- [init(SCNMatrix4)](./simd_float4x4/init%28_%29-4jrbw.md)
  Creates a new matrix from the specified SceneKit matrix.
- [init(SCNMatrix4)](./simd_float4x4/init%28_%29-q9z6.md)
  Creates a new matrix from the specified SceneKit matrix.
- [init(SIMD4<Float>, SIMD4<Float>, SIMD4<Float>, SIMD4<Float>)](./simd_float4x4/init%28_,_,_,_%29.md)
  Creates a new matrix with the specified vectors as columns.
- [init(columns: (simd_float4, simd_float4, simd_float4, simd_float4))](./simd_float4x4/init%28columns%29.md)
  Creates a new matrix with the specified columns.
- [init(rows: [SIMD4<Float>])](./simd_float4x4/init%28rows%29.md)
  Creates a new matrix with the specified rows.
- [init(AffineTransform3D)](./simd_float4x4/init%28_%29-3op4b.md)
- [init(ProjectiveTransform3D)](./simd_float4x4/init%28_%29-9txnb.md)
- [init(Pose3D)](./simd_float4x4/init%28_%29-77vxr.md)
- [init(affineTransform: AffineTransform3D)](./simd_float4x4/init%28affinetransform%29.md)
- [init(pose: Pose3D)](./simd_float4x4/init%28pose%29.md)
- [init(projectiveTransform: ProjectiveTransform3D)](./simd_float4x4/init%28projectivetransform%29.md)
### Matrix Constants
- [let matrix_identity_float4x4: simd_float4x4](./matrix_identity_float4x4.md)
  A 4 x 4 identity matrix.
### Matrix Properties
- [var determinant: Float](./simd_float4x4/determinant.md)
  The determinant of the matrix.
- [var inverse: simd_float4x4](./simd_float4x4/inverse.md)
  The inverse of the matrix.
- [var transpose: float4x4](./simd_float4x4/transpose.md)
  The transpose of the matrix.
- [var columns: (simd_float4, simd_float4, simd_float4, simd_float4)](./simd_float4x4/columns.md)
  The columns of the matrix.
### Matrix Creation Functions
- [func simd_matrix(simd_float4, simd_float4, simd_float4, simd_float4) -> simd_float4x4](./simd_matrix%28_,_,_,_%29-4p5ox.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_float4, simd_float4, simd_float4, simd_float4) -> simd_float4x4](./simd_matrix_from_rows%28_,_,_,_%29-34hac.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD4<Float>, SIMD4<Float>, SIMD4<Float>, SIMD4<Float>) -> simd_float4x4](./matrix_from_rows%28_,_,_,_%29-18jb3.md)
  Returns a new matrix with the specified rows.
- [func simd_matrix4x4(simd_quatf) -> simd_float4x4](./simd_matrix4x4%28_%29-20lv7.md)
  Returns a new matrix with the specified quarternion.
- [simd_diagonal_matrix](./simd_diagonal_matrix-2l0e4.md)
  Returns a new matrix with the specified vector on the main diagonal.
### Element Access
- [subscript(Int) -> SIMD4<Float>](./simd_float4x4/subscript%28_%29.md)
  Accesses the column at the specified position.
- [subscript(Int, Int) -> Float](./simd_float4x4/subscript%28_,_%29.md)
  Accesses the element at the specified position.
### Type Aliases
- [typealias float4x4](./float4x4.md)
  A type alias for a single-precision 4 x 4 matrix.
- [typealias matrix_float4x4](./matrix_float4x4.md)
  A type alias for a single-precision 4 x 4 matrix.
### Deprecated Symbols
- [func matrix_invert(simd_float4x4) -> simd_float4x4](./matrix_invert%28_%29-7fevy.md)
  Returns the inverse of the specified matrix.
- [func matrix_from_diagonal(SIMD4<Float>) -> simd_float4x4](./matrix_from_diagonal%28_%29-71pds.md)
  Returns a new matrix with the specified vector on the main diagonal.
- [func matrix_determinant(simd_float4x4) -> Float](./matrix_determinant%28_%29-4yqoy.md)
  Returns the determinant of the specified matrix.
- [func matrix_equal(simd_float4x4, simd_float4x4) -> Bool](./matrix_equal%28_,_%29-752xl.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_from_columns(SIMD4<Float>, SIMD4<Float>, SIMD4<Float>, SIMD4<Float>) -> simd_float4x4](./matrix_from_columns%28_,_,_,_%29-5d0yw.md)
  Returns a new matrix with the specified columns.
- [func matrix_transpose(simd_float4x4) -> float4x4](./matrix_transpose%28_%29-8t44c.md)
  Returns the transpose of a matrix.
- [var cmatrix: simd_float4x4](./simd_float4x4/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.
- [init(simd_float4x4)](./simd_float4x4/init%28_%29-2ga0f.md)
  Creates a new matrix with the specified matrix.
### Operators
- [static func * (simd_float4x4, Float) -> simd_float4x4](./simd_float4x4/star%28_,_%29-1qmhs.md)
- [static func * (simd_float4x4, float2x4) -> float2x4](./simd_float4x4/star%28_,_%29-1qwyg.md)
- [static func * (simd_float4x4, float4x4) -> float4x4](./simd_float4x4/star%28_,_%29-6yrrr.md)
- [static func * (SIMD4<Float>, simd_float4x4) -> SIMD4<Float>](./simd_float4x4/star%28_,_%29-973nq.md)
- [static func * (simd_float4x4, float3x4) -> float3x4](./simd_float4x4/star%28_,_%29-97jjs.md)
- [static func * (simd_float4x4, SIMD4<Float>) -> SIMD4<Float>](./simd_float4x4/star%28_,_%29-9bvh7.md)
- [static func * (Float, simd_float4x4) -> simd_float4x4](./simd_float4x4/star%28_,_%29-vr6m.md)
- [static func *= (inout simd_float4x4, float4x4)](./simd_float4x4/stareq%28_,_%29-10057.md)
- [static func *= (inout simd_float4x4, Float)](./simd_float4x4/stareq%28_,_%29-43syc.md)
- [static func + (simd_float4x4, simd_float4x4) -> simd_float4x4](./simd_float4x4/plus%28_,_%29.md)
- [static func += (inout simd_float4x4, simd_float4x4)](./simd_float4x4/pluseq%28_,_%29.md)
- [static func - (simd_float4x4) -> simd_float4x4](./simd_float4x4/minus%28_%29.md)
- [static func - (simd_float4x4, simd_float4x4) -> simd_float4x4](./simd_float4x4/minus%28_,_%29.md)
- [static func -= (inout simd_float4x4, simd_float4x4)](./simd_float4x4/minuseq%28_,_%29.md)
### Math Functions
- [simd_add](./simd_add-8hvd.md)
  Returns the sum of two matrices.
- [simd_sub](./simd_sub-bfqo.md)
  Returns the difference of two matrices.
- [matrix_scale](./matrix_scale-197rd.md)
  Returns the product of a scalar value and a matrix.
### Matrix-Scalar Multiplication Functions
- [simd_mul](./simd_mul-7dgim.md)
  Returns the product of a scalar value and a 4 x 4 matrix.
### Matrix-Vector Multiplication Functions
- [simd_mul](./simd_mul-78xlj.md)
  Returns the product of a four-element vector and a 4 x 4 matrix.
- [matrix_multiply](./matrix_multiply-43zat.md)
  Returns the product of a four-element vector and a 4 x 4 matrix.
- [simd_mul](./simd_mul-781du.md)
  Returns the product of a 4 x 4 matrix and a four-element vector.
- [matrix_multiply](./matrix_multiply-1q25o.md)
  Returns the product of a 4 x 4 matrix and a four-element vector.
### Matrix-Matrix Multiplication Functions
- [simd_mul](./simd_mul-904fl.md)
  Returns the product of a 2 x 4 matrix and a 4 x 2 matrix.
- [matrix_multiply](./matrix_multiply-93c5i.md)
  Returns the product of a 2 x 4 matrix and a 4 x 2 matrix.
- [matrix_multiply](./matrix_multiply-7g81z.md)
  Returns the product of a 3 x 4 matrix and a 4 x 3 matrix.
- [simd_mul](./simd_mul-6xfmy.md)
  Returns the product of a 3 x 4 matrix and a 4 x 3 matrix.
- [matrix_multiply](./matrix_multiply-7hosa.md)
  Returns the product of a 4 x 4 matrix and a 4 x 4 matrix.
- [simd_mul](./simd_mul-1sxjd.md)
  Returns the product of a 4 x 4 matrix and a 4 x 4 matrix.
### Equality Functions
- [simd_equal](./simd_equal-cge0.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix.
- [simd_almost_equal_elements](./simd_almost_equal_elements-9kkrw.md)
  Returns true if every element in a matrix is within a specified tolerance to the corresponding element in a second matrix.
- [simd_almost_equal_elements_relative](./simd_almost_equal_elements_relative-8f55s.md)
  Returns true if every element in a matrix is within a specified single-precision relative tolerance to the corresponding element in a second matrix.
### Determinant and Inverse Functions
- [simd_determinant](./simd_determinant-358zf.md)
  Returns the determinant of the specified matrix.
- [simd_inverse](./simd_inverse-3h6ry.md)
  Returns the inverse of the specified matrix.
### Linear Combination Function
- [simd_linear_combination](./simd_linear_combination-4bbf.md)
  Returns the linear combination of two scalar values and two matrices.
### Transpose Function
- [simd_transpose](./simd_transpose-7h97b.md)
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
- [struct simd_float4x3](./simd_float4x3.md)
  A matrix of four columns and three rows that contains single-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_float4x4)*