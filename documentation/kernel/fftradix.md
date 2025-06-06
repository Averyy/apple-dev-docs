# FFTRadix

**Framework**: Kernel  
**Kind**: tdef

The size of the FFT decomposition.

**Availability**:
- macOS 10.13+

## Declaration

```swift
typedef int FFTRadix;
```

#### Discussion

An `FFTRadix` value is passed as an argument to [`vDSP_create_fftsetup`](1580009-vdsp_create_fftsetup.md) or [`vDSP_create_fftsetupD`](https://developer.apple.com/documentation/accelerate/vdsp_create_fftsetupd).

## Topics

### Constants
- [kFFTRadix2](../accelerate/kfftradix2.md)
- [kFFTRadix3](../accelerate/kfftradix3.md)
- [kFFTRadix5](1645051-anonymous/kfftradix5.md)
  Specifies a radix of 5.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/fftradix)*