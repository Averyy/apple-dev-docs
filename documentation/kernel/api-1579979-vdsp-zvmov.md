# vDSP_zvmov

**Framework**: Kernel  
**Kind**: func

Complex vector copy; single precision.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vDSP_zvmov(const DSPSplitComplex *__A, vDSP_Stride __IA, const DSPSplitComplex *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

Copies complex vector `A` to complex vector `C`.

![mathematical formula](https://docs-assets.developer.apple.com/published/097ccd4f03/vdsp_106_2x_226bf0dd-aec4-4fa3-a26c-4a9df225033b.png)

## Parameters

- `__A`: Single-precision complex input vector.
- `__IA`: Address stride for  .
- `__C`: Single-precision complex output vector.
- `__IC`: Address stride for  .
- `__N`: The number of elements to process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1579979-vdsp_zvmov)*