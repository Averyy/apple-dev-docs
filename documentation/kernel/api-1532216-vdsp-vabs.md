# vDSP_vabs

**Framework**: Kernel  
**Kind**: func

Calculates the absolute value of each element in the supplied single-precision vector using the specified stride.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vDSP_vabs(const float *__A, vDSP_Stride __IA, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function performs the following operation to write the absolute values of the input elements to the corresponding output elements:

![mathematical formula](https://docs-assets.developer.apple.com/published/097ccd4f03/vdsp_81_2x_1efdff35-5ea0-405a-b1a9-9d9a4c7eec65.png)

## Parameters

- `__A`: The single-precision real input vector.
- `__IA`: The stride for input vector  .
- `__C`: The single-precision real output vector.
- `__IC`: The stride for output vector  . 
- `__N`: The number of elements to process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1532216-vdsp_vabs)*