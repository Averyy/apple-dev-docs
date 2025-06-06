# vDSP_destroy_fftsetup

**Framework**: Kernel  
**Kind**: func

Deallocates an existing single-precision FFT setup structure.

**Availability**:
- macOS 10.0+

## Declaration

```swift
void vDSP_destroy_fftsetup(FFTSetup __setup);
```

#### Discussion

`vDSP_destroy_fftsetup` frees existing setup data and releases any allocated memory.

## Parameters

- `__setup`: The setup structure to deallocate, previously created by  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1579978-vdsp_destroy_fftsetup)*