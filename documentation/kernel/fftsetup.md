# FFTSetup

**Framework**: Kernel  
**Kind**: tdef

An opaque type that contains setup information for a given FFT transform.

**Availability**:
- macOS 10.13+

## Declaration

```swift
typedef struct OpaqueFFTSetup *FFTSetup;
```

#### Discussion

A setup object can be allocated with [`vDSP_create_fftsetup`](1580009-vdsp_create_fftsetup.md) and destroyed with [`vDSP_destroy_fftsetup`](1579978-vdsp_destroy_fftsetup.md). The setup object includes, among other things, precomputed tables used in computing an FFT of the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/fftsetup)*