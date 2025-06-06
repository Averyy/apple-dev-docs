# vDSP_zvabs

**Framework**: Kernel  
**Kind**: func

Complex vector absolute values; single precision.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vDSP_zvabs(const DSPSplitComplex *__A, vDSP_Stride __IA, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This performs the following operation:

![](https://docs-assets.developer.apple.com/published/097ccd4f03/vdsp_98_2x_a8979de2-a708-420c-a093-3b2570865b5e.png)

## Parameters

- `__A`: Single-precision complex input vector.
- `__IA`: Address stride for  .
- `__C`: Single-precision real output vector.
- `__IC`: Address stride for  .
- `__N`: The number of elements to process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1579998-vdsp_zvabs)*