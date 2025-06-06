# vDSP_zmmul

**Framework**: Kernel  
**Kind**: func

Multiplies two matrices of single-precision complex numbers out-of-place.

**Availability**:
- macOS 10.2+

## Declaration

```swift
void vDSP_zmmul(const DSPSplitComplex *__A, vDSP_Stride __IA, const DSPSplitComplex *__B, vDSP_Stride __IB, const DSPSplitComplex *__C, vDSP_Stride __IC, vDSP_Length __M, vDSP_Length __N, vDSP_Length __P);
```

#### Discussion

This function performs an out-of-place complex multiplication of an `M`-by-`P` matrix `A` by a `P`-by-`N` matrix `B` and stores the results in an `M`-by-`N` matrix `C`.

This performs the following operation:

![mathematical formula](https://docs-assets.developer.apple.com/published/097ccd4f03/vdsp_49_2x_fd4ec7e6-5014-43b5-83b1-c606e770ded6.png)

## Parameters

- `__A`: Single-precision complex  -by-  input matrix.
- `__IA`: Stride for  .
- `__B`: Single-precision complex  -by- input matrix.
- `__IB`: Stride for  .
- `__C`: Single-precision complex  -by-  result matrix.
- `__IC`: Stride for  .
- `__M`: The number of rows in matrices   and  .
- `__N`: The number of columns in matrices   and  .
- `__P`: The number of columns in matrix   and the number of rows in matrix  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1579976-vdsp_zmmul)*