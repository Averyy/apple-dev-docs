# vDSP_create_fftsetup

**Framework**: Kernel  
**Kind**: func

Returns a setup structure that contains precalculated data for single-precision FFT functions.

**Availability**:
- macOS 10.0+

## Declaration

```swift
FFTSetup vDSP_create_fftsetup(vDSP_Length __Log2n, FFTRadix __Radix);
```

#### Return_value

Returns an [`FFTSetup`](fftsetup.md) structure for use with FFT functions. Returns `0` on error.

#### Discussion

Use this function to create a weights array of complex exponential values that the vDSP FFT functions use for forward transforms. Precalculating these values during, for example, your app’s initialization, boosts FFT performance. You can use the same setup structure to perform transforms on vectors that contain up to `2` elements.

For 2D transforms, specify `Log2n` as the greater of the number of rows and the number of columns.

Call [`vDSP_destroy_fftsetup`](1579978-vdsp_destroy_fftsetup.md) to deallocate the setup structure.

## Parameters

- `__Log2n`: The base-two logarithm of the maximum number of elements the setup structure transforms. Subsequent calls to FFT functions using the resulting setup may transform this length or less.
- `__Radix`: Specifies radix options. This function only supports radix-2; other radices are deprecated. Use the   for radix-3, and radix-5.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1580009-vdsp_create_fftsetup)*