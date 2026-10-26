# simd_half4x2

**Framework**: simd  
**Kind**: struct  
**Role**: Structure

A matrix of four columns and two rows that contains half-precision values.

## Declaration

```swift
struct simd_half4x2
```

```c
typedef struct { ... } simd_half4x2;
```

## Topics

### Initializers
- [init()](./simd_half4x2/init%28%29.md)
  Creates a new matrix with uninitialized memory.
- [init(columns: (simd_half2, simd_half2, simd_half2, simd_half2))](./simd_half4x2/init%28columns%29.md)
  Creates a new matrix with the specified columns.
### Matrix properties
- [var columns: (simd_half2, simd_half2, simd_half2, simd_half2)](./simd_half4x2/columns.md)
  The columns of the matrix.
### Matrix creation functions
- [func simd_matrix(simd_half2, simd_half2, simd_half2, simd_half2) -> simd_half4x2](./simd_matrix%28_,_,_,_%29-9nj2.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_half4, simd_half4) -> simd_half4x2](./simd_matrix_from_rows%28_,_%29-74k.md)
  Returns a new matrix with the specified rows.

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
- [struct simd_half3x4](./simd_half3x4.md)
  A matrix of three columns and four rows that contains half-precision values.
- [struct simd_half4x3](./simd_half4x3.md)
  A matrix of four columns and three rows that contains half-precision values.
- [struct simd_half4x4](./simd_half4x4.md)
  A matrix of four columns and four rows that contains half-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_half4x2)*