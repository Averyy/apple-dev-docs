# vDSP_biquad2

**Framework**: Kernel  
**Kind**: func

Applies a single-precision stereo biquadratic IIR filter.

**Availability**:
- macOS 10.9+

## Declaration

```swift
void vDSP_biquad2(const struct vDSP_biquad_SetupStruct *, const float *, float *, size_t);
```

#### Discussion

Use this function to apply a stereo biquadratic IIR filter to the input and write the filtered result to the output. The input and output are interleaved so that even elements correspond to the left channel and odd elements correspond to the right channel.

## Parameters

- `Parameter 0`: The data structure that stores the biquadratic filter state and coefficients.
- `Parameter 1`: A pointer to the single-precision interleaved stereo input data.
- `Parameter 2`: A pointer to the single-precision interleaved stereo output data.
- `Parameter 3`: The number of elements per channel.

## See Also

- [vDSP_biquad2_CreateSetup](1532224-vdsp_biquad2_createsetup.md)
  Builds a data structure that contains precalculated single-precision data for stereo biquadratic filter functions to use.
- [IIRChannel](iirchannel.md)
  Constants that specify which channels a stereo biquadratic filter operates.
- [vDSP_biquad2_CopyState](1532220-vdsp_biquad2_copystate.md)
  Copies the filter state from one biquadratic filter object to another.
- [vDSP_biquad2_ResetState](1532215-vdsp_biquad2_resetstate.md)
  Resets the filter state of a single-precision stereo biquadratic filter object.
- [vDSP_biquad2_DestroySetup](1532201-vdsp_biquad2_destroysetup.md)
  Destroys a single-precision stereo biquadratic IIR setup object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1532195-vdsp_biquad2)*