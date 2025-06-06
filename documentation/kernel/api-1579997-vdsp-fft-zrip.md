# vDSP_fft_zrip

**Framework**: Kernel  
**Kind**: func

Computes a forward or inverse in-place, single-precision real FFT.

**Availability**:
- macOS 10.0+

## Declaration

```swift
void vDSP_fft_zrip(FFTSetup __Setup, const DSPSplitComplex *__C, vDSP_Stride __IC, vDSP_Length __Log2N, FFTDirection __Direction);
```

#### Discussion

Forward transforms read real input and write packed complex output. Inverse transforms read packed complex input and write real output. As a result of packing the frequency-domain data, time-domain data and its equivalent frequency-domain data have the same storage requirements. You can find more details on the packing format in Data Packing for Real FFTs in vDSP Programming Guide.

![](https://docs-assets.developer.apple.com/published/097ccd4f03/vdsp_23_2x_56158015-f6d8-403d-8a82-7e093c4374e9.png)

where F is `Direction`, C is `C`, and N is two raised to the power of `Log2N`.

See also functions [`vDSP_create_fftsetup`](1580009-vdsp_create_fftsetup.md) and [`vDSP_destroy_fftsetup`](1579978-vdsp_destroy_fftsetup.md).

## Parameters

- `__Setup`: The FFT setup structure for this transform. The setup’s structure   must be greater than or equal to this function’s  .
- `__C`: A pointer to the input-output data.
- `__IC`: The stride between the elements in  , set to 1 for best performance.
- `__Log2N`: The base 2 exponent of the number of elements to process. For example, to process 1024 elements, specify 10 for parameter  .
- `__Direction`: A flag that specifies the transform direction. Pass   to transform from the time domain to the frequency domain. Pass   to transform from the frequency domain to the time domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1579997-vdsp_fft_zrip)*