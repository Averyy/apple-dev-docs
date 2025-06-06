# vDSP_deq22

**Framework**: Kernel  
**Kind**: func

Performs two-pole, two-zero recursive filtering on a single-precision vector.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vDSP_deq22(const float *__A, vDSP_Stride __IA, const float *__B, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function creates `N` new values in output vector `C`, beginning at the third element. The function performs two-pole, two-zero recursive filtering on input vector `A`, which must contain at least `N` + 2 values; `C` must also contain at least `N` + 2 values.  Since the computation is recursive, prior to calling this function, initialize the first two elements in `C`. 

You can only implement this function out of place — that is, the input and output memory must not overlap.

This function performs the following operation:

```swift
or (n = 2; n < N+2; ++n) 
    C[n] =
        + A[n-0]*B[0]
        + A[n-1]*B[1]
        + A[n-2]*B[2]
        - C[n-1]*B[3]
        - C[n-2]*B[4];
```

## Parameters

- `__A`: The single-precision real input vector.
- `__IA`: The stride for input vector  .
- `__B`: Five single-precision input filter coefficients, with a stride of one.
- `__C`: The single-precision real output vector.
- `__IC`: The stride for output vector  .
- `__N`: The number of new output elements to produce.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1532225-vdsp_deq22)*