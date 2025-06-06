# vDSP_vdbcon

**Framework**: Kernel  
**Kind**: func

Vector convert power or amplitude to decibels; single precision.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vDSP_vdbcon(const float *__A, vDSP_Stride __IA, const float *__B, float *__C, vDSP_Stride __IC, vDSP_Length __N, unsigned int __F);
```

#### Discussion

Performs the following operation. α is 20 if `F` is 1, or 10 if `F` is 0.

![](https://docs-assets.developer.apple.com/published/097ccd4f03/vdsp_87_2x_dd035eff-c1c6-40fa-acbc-49f051a0535b.png)

Converts inputs from vector `A` to their decibel equivalents, calculated  in terms of power or amplitude according to flag `F`. As a relative reference point,  the value of input scalar `*B` is considered to be zero decibels. 

## Parameters

- `__A`: Single-precision real input vector
- `__IA`: Stride for 
- `__B`: Pointer to single-precision real input scalar: zero reference
- `__C`: Single-precision real output vector
- `__IC`: Stride for 
- `__N`: The number of elements to process
- `__F`: Power (0) or amplitude (1) flag


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1580001-vdsp_vdbcon)*