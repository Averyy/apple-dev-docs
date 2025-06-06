# FFTSetupD

**Framework**: Kernel  
**Kind**: tdef

An opaque type that contains setup information for a given double-precision FFT transform.

**Availability**:
- macOS 10.13+

## Declaration

```swift
typedef struct OpaqueFFTSetupD *FFTSetupD;
```

#### Discussion

A setup object can be allocated with [`vDSP_create_fftsetupD`](https://developer.apple.com/documentation/accelerate/vdsp_create_fftsetupd) and destroyed with [`vDSP_destroy_fftsetupD`](https://developer.apple.com/documentation/accelerate/vdsp_destroy_fftsetupd). The setup object includes, among other things, precomputed tables used in computing an FFT of the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/fftsetupd)*