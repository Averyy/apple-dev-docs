# vDSP_biquadm_SetCoefficientsDouble

**Framework**: Kernel  
**Kind**: func

Updates double-precision coefficients within a valid single-precision multichannel biquad IIR filter object.

**Availability**:
- macOS 10.11+

## Declaration

```swift
void vDSP_biquadm_SetCoefficientsDouble(vDSP_biquadm_Setup __setup, const double *__coeffs, vDSP_Length __start_sec, vDSP_Length __start_chn, vDSP_Length __nsec, vDSP_Length __nchn);
```

#### Discussion

Use this function to update sections of coefficient values of a biquad setup structure. This function doesn’t allocate new memory. The range specified by `__start_sec` and `__nsec` must be within the number of sections defined by the create setup function.

## Parameters

- `__setup`: The filter state object whose coefficients you wish to update.
- `__coeffs`: An input array of double-precision coefficients.
- `__start_sec`: First section to update in each channel.
- `__start_chn`: First channel to update.
- `__nsec`: Number of sections to update in each channel.
- `__nchn`: Number of channels to update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1579995-vdsp_biquadm_setcoefficientsdoub)*