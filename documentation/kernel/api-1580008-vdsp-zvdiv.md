# vDSP_zvdiv

**Framework**: Kernel  
**Kind**: func

Complex vector_vector divide; single precision.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vDSP_zvdiv(const DSPSplitComplex *__B, vDSP_Stride __IB, const DSPSplitComplex *__A, vDSP_Stride __IA, const DSPSplitComplex *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function divides the first `N` elements of `A` by corresponding elements of `B`, leaving the result in `C`.

![](https://docs-assets.developer.apple.com/published/097ccd4f03/vdsp_89_2x_abf73575-fde7-41b3-a1a5-cf6b3c3813bd.png)

## Parameters

- `__B`: Single-precision complex input vector. Note that   comes before  !
- `__IB`: Stride for  .
- `__A`: Single-precision complex input vector.
- `__IA`: Stride for  .
- `__C`: Single-precision complex output vector.
- `__IC`: Stride for  .
- `__N`: The number of elements to process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1580008-vdsp_zvdiv)*