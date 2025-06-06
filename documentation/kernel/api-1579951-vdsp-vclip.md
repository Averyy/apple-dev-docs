# vDSP_vclip

**Framework**: Kernel  
**Kind**: func

Calculates the elements of a single-precision vector clipped to the specified range using the specified stride.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vDSP_vclip(const float *__A, vDSP_Stride __IA, const float *__B, const float *__C, float *__D, vDSP_Stride __ID, vDSP_Length __N);
```

#### Discussion

This performs the following operation:

```occ
for (n = 0; n < N; ++n) {
    if (A[n*IA] < *B)
        D[n*ID] = *B;
    else if (A[n*IA] > *C)
        D[n*ID] = *C;
    else
        D[n*ID] = A[n*IA];
}
```

Elements of `A` are copied to `D`, while clipping elements that are outside the interval [`*B`, `*C`] to the endpoints of the interval.

## Parameters

- `__A`: Single-precision real input vector
- `__IA`: Stride for 
- `__B`: Pointer to single-precision real input scalar: low clipping threshold
- `__C`: Pointer to single-precision real input scalar: high clipping threshold
- `__D`: Single-precision real output vector
- `__ID`: Stride for 
- `__N`: The number of elements to process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1579951-vdsp_vclip)*