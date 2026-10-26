# simd_half2x2

**Framework**: simd  
**Kind**: struct  
**Role**: Structure

A matrix of two columns and two rows that contains half-precision values.

## Declaration

```swift
struct simd_half2x2
```

```c
typedef struct { ... } simd_half2x2;
```

## Topics

### Initializers
- [init()](./simd_half2x2/init%28%29.md)
  Creates a new matrix with uninitialized memory.
- [init(columns: (simd_half2, simd_half2))](./simd_half2x2/init%28columns%29.md)
  Creates a new matrix with the specified columns.
### Matrix properties
- [var columns: (simd_half2, simd_half2)](./simd_half2x2/columns.md)
  The columns of the matrix.
### Matrix constants
- [let matrix_identity_half2x2: simd_half2x2](./matrix_identity_half2x2.md)
  A 2 x 2 identity matrix.
### Matrix creation functions
- [func simd_matrix(simd_half2, simd_half2) -> simd_half2x2](./simd_matrix%28_,_%29-1w6b0.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_half2, simd_half2) -> simd_half2x2](./simd_matrix_from_rows%28_,_%29-9lrpr.md)
  Returns a new matrix with the specified rows.
- [simd_diagonal_matrix](./simd_diagonal_matrix-2rg1i.md)
  Returns a new matrix with the specified vector on the main diagonal.
### Math functions
- [simd_add](./simd_add-392vg.md)
  Returns the sum of two matrices.
- [simd_sub](./simd_sub-2a3t7.md)
  Returns the difference of two matrices.
### Matrix-scalar multiplication functions
- [matrix_scale](./matrix_scale-3fz4k.md)
  Returns the product of a scalar value and a matrix.
### Matrix-vector multiplication functions
- [matrix_multiply](./matrix_multiply-5xdmi.md)
  Returns the product of a vector and a matrix.
### Equality functions
- [simd_equal](./simd_equal-1nw3v.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix.
- [simd_almost_equal_elements](./simd_almost_equal_elements-5wyt4.md)
  Returns true if every element in a matrix is within a specified tolerance to the corresponding element in a second matrix.
- [simd_almost_equal_elements_relative](./simd_almost_equal_elements_relative-5ll99.md)
  Returns true if every element in a matrix is within a specified single-precision relative tolerance to the corresponding element in a second matrix.
### Determinant and inverse functions
- [simd_determinant](./simd_determinant-1zkub.md)
  Returns the determinant of the specified matrix.
- [simd_inverse](./simd_inverse-1kqte.md)
  Returns the inverse of the specified matrix.
### Linear combination function
- [simd_linear_combination](./simd_linear_combination-2w3c6.md)
  Returns the linear combination of two scalar values and two matrices.
### Transpose function
- [simd_transpose](./simd_transpose-2zxzv.md)
  Returns the transpose of a matrix.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Matrix structures
- [struct simd_half2x3](./simd_half2x3.md)
  A matrix of two columns and three rows that contains half-precision values.
- [struct simd_half2x4](./simd_half2x4.md)
  A matrix of two columns and four rows that contains half-precision values.
- [struct simd_half3x2](./simd_half3x2.md)
  A matrix of three columns and two rows that contains half-precision values.
- [struct simd_half3x3](./simd_half3x3.md)
  A matrix of three columns and three rows that contains half-precision values.
- [struct simd_half3x4](./simd_half3x4.md)
  A matrix of three columns and four rows that contains half-precision values.
- [struct simd_half4x2](./simd_half4x2.md)
  A matrix of four columns and two rows that contains half-precision values.
- [struct simd_half4x3](./simd_half4x3.md)
  A matrix of four columns and three rows that contains half-precision values.
- [struct simd_half4x4](./simd_half4x4.md)
  A matrix of four columns and four rows that contains half-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_half2x2)*