# vDSP_vflt16

**Framework**: Kernel  
**Kind**: func

Converts an array of signed 16-bit integers to single-precision floating-point values.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vDSP_vflt16(const int16_t *vDSP_input1, ptrdiff_t vDSP_stride1, float *vDSP_input2, ptrdiff_t vDSP_stride2, size_t vDSP_size);
```

## Parameters

- `++A`: The single-precision floating-point input vector.
- `__IA`: The stride for input vector  . 
- `__C`: The single-precision floating-point output vector. 
- `__IC`: The stride for output vector  . 
- `__N`: The number of values to convert.

## See Also

- [vDSP_vsmfix24](1532200-vdsp_vsmfix24.md)
  Scales and converts single-precision floating-point values to signed 24-bit integer values.
- [vDSP_vsmfixu24](1532178-vdsp_vsmfixu24.md)
  Scales and converts single-precision floating-point values to unsigned 24-bit integer values.
- [vDSP_vfix16](1532172-vdsp_vfix16.md)
  Converts an array of single-precision floating-point values to signed 16-bit integer values, rounding toward zero.
- [vDSP_vfix32](1532198-vdsp_vfix32.md)
  Converts an array of single-precision floating-point values to signed 32-bit integer values, rounding toward zero.
- [vDSP_vflt24](1532208-vdsp_vflt24.md)
  Converts signed 24-bit integer values to single-precision floating-point values.
- [vDSP_vflt32](1532181-vdsp_vflt32.md)
  Converts an array of signed 32-bit integers to single-precision floating-point values.
- [vDSP_vfltu24](1532185-vdsp_vfltu24.md)
  Converts unsigned 24-bit integer values to single-precision floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1532204-vdsp_vflt16)*