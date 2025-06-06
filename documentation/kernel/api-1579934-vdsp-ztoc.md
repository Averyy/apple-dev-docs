# vDSP_ztoc

**Framework**: Kernel  
**Kind**: func

Copies the contents of a split complex vector `Z` to an interleaved complex vector `C`; single precision.

**Availability**:
- macOS 10.0+

## Declaration

```swift
void vDSP_ztoc(const DSPSplitComplex *__Z, vDSP_Stride __IZ, DSPComplex *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

For best performance, `C`, `Z.realp`, and `Z.imagp` should be 16-byte aligned. 

This performs the following operations:

```occ
for (n = 0; n < N; ++n)
{
  C[n*IC/2].real = Z->realp[n*IZ];
  C[n*IC/2].imag = Z->imagp[n*IZ];
}
```

See also [`vDSP_ctoz`](1579975-vdsp_ctoz.md) and [`vDSP_ctozD`](https://developer.apple.com/documentation/accelerate/vdsp_ctozd).

## Parameters

- `__Z`: Single-precision split-complex input vector.
- `__IZ`: Stride for  .
- `__C`: Single-precision interleaved complex output vector.
- `__IC`: Stride for  . Must be an even number.
- `__N`: The number of elements to process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1579934-vdsp_ztoc)*