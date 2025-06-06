# vDSP_vmaxmg

**Framework**: Kernel  
**Kind**: func

Calculates the single-precision maximum magnitude of the corresponding values of two vectors using specified strides.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vDSP_vmaxmg(const float *__A, vDSP_Stride __IA, const float *__B, vDSP_Stride __IB, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function compares the magnitudes (absolute values) of the first `N` elements of `A` with corresponding elements of `B`, leaving the greater (or equal) values as corresponding elements of `C`:

```other
for (n = 0; n < N; ++n)
    C[n] = |B[n]| <= |A[n]| ? |A[n]| : |B[n]|;
```

## Parameters

- `__A`: Single-precision real input vector.
- `__IA`: Stride for  .
- `__B`: Single-precision real input vector.
- `__IB`: Stride for  .
- `__C`: Single-precision real output vector.
- `__IC`: Stride for  .
- `__N`: The number of elements to process


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1579943-vdsp_vmaxmg)*