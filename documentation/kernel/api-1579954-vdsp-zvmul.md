# vDSP_zvmul

**Framework**: Kernel  
**Kind**: func

Multiplies two complex vectors, optionally conjugating one of them; single precision.

**Availability**:
- macOS 10.0+

## Declaration

```swift
void vDSP_zvmul(const DSPSplitComplex *__A, vDSP_Stride __IA, const DSPSplitComplex *__B, vDSP_Stride __IB, const DSPSplitComplex *__C, vDSP_Stride __IC, vDSP_Length __N, int __Conjugate);
```

#### Discussion

If `Conjugate` = 1, this function multiplies the first `N` complex elements of `A` by corresponding complex elements of `B`. If `Conjugate` = -1, it multiplies the complex conjugates of the first `N` complex elements of `A` by corresponding complex elements of `B`. In either case, the complex results are left in `C`:

![](https://docs-assets.developer.apple.com/published/097ccd4f03/vdsp_41_2x_1a0245af-fbfc-40df-bf55-f015b974c78e.png)

where  stands for `Conjugate`.

## Parameters

- `__A`: Single-precision complex input vector.
- `__IA`: Stride for  .
- `__B`: Single-precision complex input vector.
- `__IB`: Stride for  .
- `__C`: Single-precision complex output vector.
- `__IC`: Stride for  .
- `__N`: The number of elements to process.
- `__Conjugate`: Set this parameter to   for normal or   for conjugate multiplication, respectively. Results are undefined for other values; represented by   in the discussion


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1579954-vdsp_zvmul)*