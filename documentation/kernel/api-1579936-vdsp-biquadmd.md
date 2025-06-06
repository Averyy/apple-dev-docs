# vDSP_biquadmD

**Framework**: Kernel  
**Kind**: func

Applies a double-precision multichannel biquad IIR filter.

**Availability**:
- macOS 10.10+

## Declaration

```swift
void vDSP_biquadmD(vDSP_biquadm_SetupD __Setup, const double * _Nonnull *__X, vDSP_Stride __IX, double * _Nonnull *__Y, vDSP_Stride __IY, vDSP_Length __N);
```

#### Discussion

For each channel, this function applies a cascaded biquad filter to the input values specified by the channel’s pointer in `X`. 

The function places the results in the array specified by the corresponding pointer in `Y`.

The function supports interleaved data. In this case, define the stride as the number of channels, and the pointers as consecutive locations in memory.

> **Note**: For the best performance and energy efficiency, specify a stride of `1` for non-interleaved data. Specify a stride equal to the number of channels for interleaved data. 

For the best performance and energy efficiency, specify a stride of `1` for non-interleaved data. Specify a stride equal to the number of channels for interleaved data. 

The function updates the state contained in the `setup` object upon return.

## Parameters

- `__setup`: The   object defining the filter to apply.
- `__X`: An array of pointers, each of which specifies an array of double-precision input data for a single channel.
- `__IX`: Stride for   (see Discussion below).
- `__Y`: An array of pointers, each of which specifies an array of double-precision input data for a single channel. 
- `__IY`: Stride for   (see Discussion below).
- `__N`: The number of elements to filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1579936-vdsp_biquadmd)*