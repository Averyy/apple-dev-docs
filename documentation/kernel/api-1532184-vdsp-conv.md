# vDSP_conv

**Framework**: Kernel  
**Kind**: func

Performs either correlation or convolution on two real single-precision vectors.

**Availability**:
- macOS 10.0+

## Declaration

```swift
void vDSP_conv(const float *__A, vDSP_Stride __IA, const float *__F, vDSP_Stride __IF, float *__C, vDSP_Stride __IC, vDSP_Length __N, vDSP_Length __P);
```

#### Discussion

Use this function to compute either the convolution or the correlation of an input signal and a filter vector. Both operations compute the sliding dot product of the filter and the section of the input signal that the filter is over. Specify a positive stride through the filter to perform correlation and a negative stride through the filter to perform convolution. When you perform convolution, the `__F` parameter must point to the last element in the filter.

The function can run in place, but `C` can’t be in place with `F`. For example, the following code defines an input signal, a filter, and the number of output elements:

```swift
let signal: [Float] = [1, 2, 3, 4, 5, 6, 7, 8]

let filter: [Float] = [10, 20, 30]

let outputCount = signal.count - filter.count + 1
```

## Parameters

- `__A`: The real single-precision input signal vector. The length of this vector must be at least  .
- `__IA`: The stride through the input signal vector,  .
- `__F`: The real single-precision filter vector.
- `__IF`: The stride through the filter vector,  .
- `__C`: The real single-precision output signal vector.
- `__IC`: The stride through the output signal vector,  .
- `__N`: The number of elements in the output signal vector,  . 
- `__P`: The number of elements in the filter vector,  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1532184-vdsp_conv)*