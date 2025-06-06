# IIRChannel

**Framework**: Kernel  
**Kind**: tdef

Constants that specify which channels a stereo biquadratic filter operates.

**Availability**:
- macOS 10.9+

## Declaration

```swift
typedef int IIRChannel;
```

#### Discussion

Pass an [`IIRChannel`](iirchannel.md) constant to [`vDSP_biquad2_CreateSetup`](1532224-vdsp_biquad2_createsetup.md) to specify which channels the function applies filtering to.

## See Also

- [vDSP_biquad2](1532195-vdsp_biquad2.md)
  Applies a single-precision stereo biquadratic IIR filter.
- [vDSP_biquad2_CreateSetup](1532224-vdsp_biquad2_createsetup.md)
  Builds a data structure that contains precalculated single-precision data for stereo biquadratic filter functions to use.
- [vDSP_biquad2_CopyState](1532220-vdsp_biquad2_copystate.md)
  Copies the filter state from one biquadratic filter object to another.
- [vDSP_biquad2_ResetState](1532215-vdsp_biquad2_resetstate.md)
  Resets the filter state of a single-precision stereo biquadratic filter object.
- [vDSP_biquad2_DestroySetup](1532201-vdsp_biquad2_destroysetup.md)
  Destroys a single-precision stereo biquadratic IIR setup object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iirchannel)*