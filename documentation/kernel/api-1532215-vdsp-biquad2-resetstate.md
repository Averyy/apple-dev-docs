# vDSP_biquad2_ResetState

**Framework**: Kernel  
**Kind**: func

Resets the filter state of a single-precision stereo biquadratic filter object.

**Availability**:
- macOS 10.9+

## Declaration

```swift
void vDSP_biquad2_ResetState(vDSP_biquad_Setup);
```

## Parameters

- `Parameter 0 `: The biquadratic filter object that the function resets.

## See Also

- [vDSP_biquad2](1532195-vdsp_biquad2.md)
  Applies a single-precision stereo biquadratic IIR filter.
- [vDSP_biquad2_CreateSetup](1532224-vdsp_biquad2_createsetup.md)
  Builds a data structure that contains precalculated single-precision data for stereo biquadratic filter functions to use.
- [IIRChannel](iirchannel.md)
  Constants that specify which channels a stereo biquadratic filter operates.
- [vDSP_biquad2_CopyState](1532220-vdsp_biquad2_copystate.md)
  Copies the filter state from one biquadratic filter object to another.
- [vDSP_biquad2_DestroySetup](1532201-vdsp_biquad2_destroysetup.md)
  Destroys a single-precision stereo biquadratic IIR setup object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1532215-vdsp_biquad2_resetstate)*