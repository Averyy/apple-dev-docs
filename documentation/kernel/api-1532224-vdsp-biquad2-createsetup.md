# vDSP_biquad2_CreateSetup

**Framework**: Kernel  
**Kind**: func

Builds a data structure that contains precalculated single-precision data for stereo biquadratic filter functions to use.

**Availability**:
- macOS 10.9+

## Declaration

```swift
vDSP_biquad_Setup vDSP_biquad2_CreateSetup(const double *, const size_t, const IIRChannel);
```

#### Discussion

If the channel parameter is [`vDSP_IIRMonoLeft`](1645949-anonymous/vdsp_iirmonoleft.md) or [`vDSP_IIRMonoRight`](1645949-anonymous/vdsp_iirmonoright.md), the number of elements in the coefficients array must be five times the number of sections. The filter applies pass-through coefficients to the other channel.

If the channel parameter is [`vDSP_IIRStereo`](1645949-anonymous/vdsp_iirstereo.md), the number of elements in the coefficients array must be ten times the number of sections. Specify five left-channel coefficients followed by five right-channel coefficients.

## Parameters

- `Parameter 0`: A pointer to the double-precision filter coefficients. 
- `Parameter 1`: The number of sections in the biquadratic filter.
- `Parameter 2`: An enumeration that specifies the channel.

## See Also

- [vDSP_biquad2](1532195-vdsp_biquad2.md)
  Applies a single-precision stereo biquadratic IIR filter.
- [IIRChannel](iirchannel.md)
  Constants that specify which channels a stereo biquadratic filter operates.
- [vDSP_biquad2_CopyState](1532220-vdsp_biquad2_copystate.md)
  Copies the filter state from one biquadratic filter object to another.
- [vDSP_biquad2_ResetState](1532215-vdsp_biquad2_resetstate.md)
  Resets the filter state of a single-precision stereo biquadratic filter object.
- [vDSP_biquad2_DestroySetup](1532201-vdsp_biquad2_destroysetup.md)
  Destroys a single-precision stereo biquadratic IIR setup object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1532224-vdsp_biquad2_createsetup)*