# simd_half3x4

**Framework**: simd  
**Kind**: struct  
**Role**: Structure

A matrix of three columns and four rows that contains half-precision values.

## Declaration

```swift
struct simd_half3x4
```

```c
typedef struct { ... } simd_half3x4;
```

## Topics

### Initializers
- [init()](./simd_half3x4/init%28%29.md)
  Creates a new matrix with uninitialized memory.
- [init(columns: (simd_half4, simd_half4, simd_half4))](./simd_half3x4/init%28columns%29.md)
  Creates a new matrix with the specified columns.
### Matrix properties
- [var columns: (simd_half4, simd_half4, simd_half4)](./simd_half3x4/columns.md)
  The columns of the matrix.
### Matrix creation functions
- [func simd_matrix(simd_half4, simd_half4, simd_half4) -> simd_half3x4](./simd_matrix%28_,_,_%29-5oh9m.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_half3, simd_half3, simd_half3, simd_half3) -> simd_half3x4](./simd_matrix_from_rows%28_,_,_,_%29-9v9ky.md)
  Returns a new matrix with the specified rows.
### Math functions
- [simd_add](./simd_add-2q17g.md)
  Returns the sum of two matrices.
- [simd_sub](./simd_sub-70bzq.md)
  Returns the difference of two matrices.
### Matrix-scalar multiplication functions
- [matrix_scale](./matrix_scale-7i33a.md)
  Returns the product of a scalar value and a matrix.
### Matrix-vector multiplication functions
- [matrix_multiply](./matrix_multiply-4spt.md)
  Returns the product of a vector and a matrix.
### Equality functions
- [simd_equal](./simd_equal-6408u.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix.
- [simd_almost_equal_elements](./simd_almost_equal_elements-59tjx.md)
  Returns true if every element in a matrix is within a specified tolerance to the corresponding element in a second matrix.
- [simd_almost_equal_elements_relative](./simd_almost_equal_elements_relative-6emsr.md)
  Returns true if every element in a matrix is within a specified single-precision relative tolerance to the corresponding element in a second matrix.
### Linear combination function
- [simd_linear_combination](./simd_linear_combination-5ao3y.md)
  Returns the linear combination of two scalar values and two matrices.
### Transpose function
- [simd_transpose](./simd_transpose-8n66z.md)
  Returns the transpose of a matrix.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Matrix structures
- [struct simd_half2x2](./simd_half2x2.md)
  A matrix of two columns and two rows that contains half-precision values.
- [struct simd_half2x3](./simd_half2x3.md)
  A matrix of two columns and three rows that contains half-precision values.
- [struct simd_half2x4](./simd_half2x4.md)
  A matrix of two columns and four rows that contains half-precision values.
- [struct simd_half3x2](./simd_half3x2.md)
  A matrix of three columns and two rows that contains half-precision values.
- [struct simd_half3x3](./simd_half3x3.md)
  A matrix of three columns and three rows that contains half-precision values.
- [struct simd_half4x2](./simd_half4x2.md)
  A matrix of four columns and two rows that contains half-precision values.
- [struct simd_half4x3](./simd_half4x3.md)
  A matrix of four columns and three rows that contains half-precision values.
- [struct simd_half4x4](./simd_half4x4.md)
  A matrix of four columns and four rows that contains half-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_half3x4)*