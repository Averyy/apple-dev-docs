# vDSP_ctoz

**Framework**: Kernel  
**Kind**: func

Copies the contents of an interleaved complex vector `C` to a split complex vector `Z`; single precision.

**Availability**:
- macOS 10.0+

## Declaration

```swift
void vDSP_ctoz(const DSPComplex *__C, vDSP_Stride __IC, const DSPSplitComplex *__Z, vDSP_Stride __IZ, vDSP_Length __N);
```

#### Discussion

For best performance, `C`, `Z.realp`, and `Z.imagp` should be 16-byte aligned.

This function performs the following operations:

```occ
for (n = 0; n < N; ++n)
{
  Z->realp[n*IZ] = C[n*IC/2].real;
  Z->imagp[n*IZ] = C[n*IC/2].imag;
}
```

 See also functions[`vDSP_ztoc`](1579934-vdsp_ztoc.md) and [`vDSP_ztocD`](https://developer.apple.com/documentation/accelerate/vdsp_ztocd).

## Parameters

- `__C`: Single-precision interleaved complex input vector.
- `__IC`: Stride for  ; must be an even number.
- `__Z`: Single-precision split-complex output vector.
- `__IZ`: Stride for  .
- `__N`: The number of elements to process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1579975-vdsp_ctoz)*