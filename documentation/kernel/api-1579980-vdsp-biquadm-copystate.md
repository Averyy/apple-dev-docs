# vDSP_biquadm_CopyState

**Framework**: Kernel  
**Kind**: func

Copies the filter state from one single-precision multichannel biquad IIR filter object to another.

**Availability**:
- macOS 10.9+

## Declaration

```swift
void vDSP_biquadm_CopyState(vDSP_biquadm_Setup __dest, const struct vDSP_biquadm_SetupStruct *__src);
```

#### Discussion

Both `src` and `dest` objects must be valid single-precision multichannel biquad setup objects created by previous calls to [`vDSP_biquadm_CreateSetup`](1579945-vdsp_biquadm_createsetup.md). Both objects must have the same number of channels and sections.

## Parameters

- `__dest`: The   object whose state you wish to overwrite.
- `__src`: The   object whose state you wish to copy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1579980-vdsp_biquadm_copystate)*