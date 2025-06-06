# vDSP_biquadm_CopyStateD

**Framework**: Kernel  
**Kind**: func

Copies the filter state from one dopuble-precision multichannel biquad IIR filter object to another.

**Availability**:
- macOS 10.10+

## Declaration

```swift
void vDSP_biquadm_CopyStateD(vDSP_biquadm_SetupD __dest, const struct vDSP_biquadm_SetupStructD *__src);
```

#### Discussion

Both `src` and `dest` objects must be valid single-precision multichannel biquad setup objects created by previous calls to [`vDSP_biquadm_CreateSetupD`](1579944-vdsp_biquadm_createsetupd.md). Both objects must have the same number of channels and sections.

## Parameters

- `__dest`: The   object whose state you wish to overwrite.
- `__src`: The   object whose state you wish to copy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1580000-vdsp_biquadm_copystated)*