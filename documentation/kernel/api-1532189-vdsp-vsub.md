# vDSP_vsub

**Framework**: Kernel  
**Kind**: func

Subtracts two single-precision vectors.

**Availability**:
- macOS 10.0+

## Declaration

```swift
void vDSP_vsub(const float *__B, vDSP_Stride __IB, const float *__A, vDSP_Stride __IA, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function calculates the differences of the first `N` elements of input vectors `A` and `B`, writing the result to output vector `C`:

![A diagram showing the operation of the vDSP_vsub function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://docs-assets.developer.apple.com/published/3222a40bfa/1332be04-5da1-44bf-bdc7-e2f991acef73.png)

The operation is:

```other
 for (n = 0; n < N; ++n)
    C[n] = A[n] - B[n];
```

The following code shows an example of using [`vDSP_vsub`](https://developer.apple.com/documentation/accelerate/vdsp_vsub):

```swift
let stride = vDSP_Stride(1)

let a: [Float] = [1, 2, 3, 4, 5]
let b: [Float] = [10, 20, 30, 40, 50]

let n = vDSP_Length(a.count)

var c = [Float](repeating: 0,
                count: a.count)

vDSP_vsub(b, stride,
          a, stride,
          &c, stride,
          n)

// Prints "[-9.0, -18.0, -27.0, -36.0, -45.0]".
print(c)
```

## Parameters

- `__B`: The single-precision real input vector  . 
- `__IB`: The stride for input vector  .
- `__A`: The single-precision real input vector  . 
- `__IA`: The stride for input vector  . 
- `__C`: The single-precision real output vector. 
- `__IC`: The stride for output vector  . 
- `__N`: Number of elements to subtract.

## See Also

- [vDSP_vadd](1532191-vdsp_vadd.md)
  Adds two single-precision vectors.
- [vDSP_vma](1532193-vdsp_vma.md)
  Adds a single-precision vector to the product of two single-precision vectors.
- [vDSP_vmul](1532206-vdsp_vmul.md)
  Multiplies two single-precision vectors.
- [vDSP_vsmul](1532223-vdsp_vsmul.md)
  Multiplies a single-precision scalar value by a single-precision vector.
- [vDSP_vdiv](1532168-vdsp_vdiv.md)
  Divides two single-precision vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1532189-vdsp_vsub)*