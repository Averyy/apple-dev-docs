# vDSP_biquad2_DestroySetup

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Destroys a single-precision stereo biquadratic IIR setup object.

**Availability**:
- macOS 10.9+

## Declaration

```c
void vDSP_biquad2_DestroySetup(vDSP_biquad_Setup);
```

## Parameters

- `Parameter 0 `: The biquadratic filter object that the function destroys.

## See Also

### Biquadratic Infinite Impulse Response (IIR) Filters
- [vDSP_biquad2](./api-1532195-vdsp_biquad2.md)
  Applies a single-precision stereo biquadratic IIR filter.
- [vDSP_biquad2_CreateSetup](./api-1532224-vdsp_biquad2_createsetup.md)
  Builds a data structure that contains precalculated single-precision data for stereo biquadratic filter functions to use.
- [IIRChannel](./iirchannel.md)
  Constants that specify which channels a stereo biquadratic filter operates.
- [vDSP_biquad2_CopyState](./api-1532220-vdsp_biquad2_copystate.md)
  Copies the filter state from one biquadratic filter object to another.
- [vDSP_biquad2_ResetState](./api-1532215-vdsp_biquad2_resetstate.md)
  Resets the filter state of a single-precision stereo biquadratic filter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1532201-vdsp_biquad2_destroysetup)*