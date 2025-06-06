# vDSP_vsmfixu24

**Framework**: Kernel  
**Kind**: func

Scales and converts single-precision floating-point values to unsigned 24-bit integer values.

**Availability**:
- macOS 10.9+

## Declaration

```swift
void vDSP_vsmfixu24(const float vDSP_input1[], ptrdiff_t vDSP_stride1, const float vDSP_input2[], vDSP_uint24 *vDSP_input3, ptrdiff_t vDSP_stride2, size_t vDSP_size);
```

#### Discussion

This function scales vector `A` by the scalar `*B` and converts each resulting value to an unsigned 24-bit integer, placing the results in `C`. After scaling, the function clamps values that are outside the range that unsigned 24-bit integers can represent to the largest or smallest representable values.

This function performs the following operations:

```occ
    for (n = 0; n < N; ++n)
    {
        if     (A[n*IA] * *B < 0)
            C[n*IC] = 0
        else if (A[n*IA] * *B > UINT24_MAX)
            C[n*IC] = UINT24_MAX
        else
            C[n*IC] = (uint24)(A[n*IA] * *B);
    }
```

In this pseudocode, `UINT24_MAX` is equal to `2^24 - 1`.

## Parameters

- `__A`: The single-precision floating-point input vector.
- `__IA`: The stride for input vector  . 
- `__B`: A pointer to a floating-point scaling factor.
- `__C`: The 24-bit integer output vector. 
- `__IC`: The stride for output vector  . 
- `__N`: The number of values to convert.

## See Also

- [vDSP_vsmfix24](1532200-vdsp_vsmfix24.md)
  Scales and converts single-precision floating-point values to signed 24-bit integer values.
- [vDSP_vfix16](1532172-vdsp_vfix16.md)
  Converts an array of single-precision floating-point values to signed 16-bit integer values, rounding toward zero.
- [vDSP_vfix32](1532198-vdsp_vfix32.md)
  Converts an array of single-precision floating-point values to signed 32-bit integer values, rounding toward zero.
- [vDSP_vflt16](1532204-vdsp_vflt16.md)
  Converts an array of signed 16-bit integers to single-precision floating-point values.
- [vDSP_vflt24](1532208-vdsp_vflt24.md)
  Converts signed 24-bit integer values to single-precision floating-point values.
- [vDSP_vflt32](1532181-vdsp_vflt32.md)
  Converts an array of signed 32-bit integers to single-precision floating-point values.
- [vDSP_vfltu24](1532185-vdsp_vfltu24.md)
  Converts unsigned 24-bit integer values to single-precision floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1532178-vdsp_vsmfixu24)*