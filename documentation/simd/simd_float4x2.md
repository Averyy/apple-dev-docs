# simd_float4x2

**Framework**: simd  
**Kind**: struct  
**Role**: Structure

A matrix of four columns and two rows that contains single-precision values.

## Declaration

```swift
struct simd_float4x2
```

```c
typedef struct { ... } simd_float4x2;
```

## Topics

### Initializers
- [init()](./simd_float4x2/init%28%29.md)
  Creates a new matrix with uninitialized memory.
- [init(Float)](./simd_float4x2/init%28_%29-4xu3o.md)
  Creates a new matrix with the specified scalar value on the main diagonal.
- [init(diagonal: SIMD2<Float>)](./simd_float4x2/init%28diagonal%29.md)
  Creates a new matrix with the specified vector on the main diagonal.
- [init([SIMD2<Float>])](./simd_float4x2/init%28_%29-5k3p5.md)
  Creates a new matrix from an array.
- [init(SIMD2<Float>, SIMD2<Float>, SIMD2<Float>, SIMD2<Float>)](./simd_float4x2/init%28_,_,_,_%29.md)
  Creates a new matrix with the specified vectors as columns.
- [init(columns: (simd_float2, simd_float2, simd_float2, simd_float2))](./simd_float4x2/init%28columns%29.md)
  Creates a new matrix with the specified columns.
- [init(rows: [SIMD4<Float>])](./simd_float4x2/init%28rows%29.md)
  Creates a new matrix with the specified rows.
### Matrix Properties
- [var transpose: float2x4](./simd_float4x2/transpose.md)
  The transpose of the matrix.
- [var columns: (simd_float2, simd_float2, simd_float2, simd_float2)](./simd_float4x2/columns.md)
  The columns of the matrix.
### Matrix Creation Functions
- [func simd_matrix(simd_float2, simd_float2, simd_float2, simd_float2) -> simd_float4x2](./simd_matrix%28_,_,_,_%29-xobw.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_float4, simd_float4) -> simd_float4x2](./simd_matrix_from_rows%28_,_%29-4lzrf.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD4<Float>, SIMD4<Float>) -> simd_float4x2](./matrix_from_rows%28_,_%29-2ip8.md)
  Returns a new matrix with the specified rows.
### Element Access
- [subscript(Int) -> SIMD2<Float>](./simd_float4x2/subscript%28_%29.md)
  Accesses the column at the specified position.
- [subscript(Int, Int) -> Float](./simd_float4x2/subscript%28_,_%29.md)
  Accesses the element at the specified position.
### Type Aliases
- [typealias float4x2](./float4x2.md)
  A type alias for a single-precision 4 x 2 matrix.
- [typealias matrix_float4x2](./matrix_float4x2.md)
  A type alias for a single-precision 4 x 2 matrix.
### Deprecated Symbols
- [func matrix_equal(simd_float4x2, simd_float4x2) -> Bool](./matrix_equal%28_,_%29-1izln.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_from_columns(SIMD2<Float>, SIMD2<Float>, SIMD2<Float>, SIMD2<Float>) -> simd_float4x2](./matrix_from_columns%28_,_,_,_%29-2u92u.md)
  Returns a new matrix with the specified columns.
- [func matrix_transpose(simd_float2x4) -> float4x2](./matrix_transpose%28_%29-260wn.md)
  Returns the transpose of a matrix.
- [var cmatrix: simd_float4x2](./simd_float4x2/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.
- [init(simd_float4x2)](./simd_float4x2/init%28_%29-2e140.md)
  Creates a new matrix with the specified matrix.
### Operators
- [static func * (simd_float4x2, Float) -> simd_float4x2](./simd_float4x2/star%28_,_%29-3xkqa.md)
- [static func * (simd_float4x2, float3x4) -> float3x2](./simd_float4x2/star%28_,_%29-5f1f2.md)
- [static func * (simd_float4x2, float2x4) -> float2x2](./simd_float4x2/star%28_,_%29-85wgv.md)
- [static func * (simd_float4x2, float4x4) -> float4x2](./simd_float4x2/star%28_,_%29-93u9t.md)
- [static func * (Float, simd_float4x2) -> simd_float4x2](./simd_float4x2/star%28_,_%29-9kthx.md)
- [static func * (simd_float4x2, SIMD4<Float>) -> SIMD2<Float>](./simd_float4x2/star%28_,_%29-9wwew.md)
- [static func * (SIMD2<Float>, simd_float4x2) -> SIMD4<Float>](./simd_float4x2/star%28_,_%29-jxxr.md)
- [static func *= (inout simd_float4x2, Float)](./simd_float4x2/stareq%28_,_%29-24lqw.md)
- [static func *= (inout simd_float4x2, float4x4)](./simd_float4x2/stareq%28_,_%29-39csh.md)
- [static func + (simd_float4x2, simd_float4x2) -> simd_float4x2](./simd_float4x2/plus%28_,_%29.md)
- [static func += (inout simd_float4x2, simd_float4x2)](./simd_float4x2/pluseq%28_,_%29.md)
- [static func - (simd_float4x2) -> simd_float4x2](./simd_float4x2/minus%28_%29.md)
- [static func - (simd_float4x2, simd_float4x2) -> simd_float4x2](./simd_float4x2/minus%28_,_%29.md)
- [static func -= (inout simd_float4x2, simd_float4x2)](./simd_float4x2/minuseq%28_,_%29.md)

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
- [struct simd_float4x3](./simd_float4x3.md)
  A matrix of four columns and three rows that contains single-precision values.
- [struct simd_float4x4](./simd_float4x4.md)
  A matrix of four columns and four rows that contains single-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_float4x2)*