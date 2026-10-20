# vDSP_vadd

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Adds two single-precision vectors.

**Availability**:
- macOS 10.0+

## Declaration

```c
void vDSP_vadd(const float *__A, vDSP_Stride __IA, const float *__B, vDSP_Stride __IB, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function calculates the sums of the first `N` elements of input vectors `A` and `B`, writing the result to output vector `C`:

![A diagram showing the operation of the vDSP_vadd function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://docs-assets.developer.apple.com/published/952f6afa1b/103cfef0-b034-412d-87c3-18e5be92f15b.png)

The operation is:

```other
 for (n = 0; n < N; ++n)
    C[n] = A[n] + B[n];
```

The following code shows an example of using [`vDSP_vadd`](../Accelerate/vdsp_vadd.md):

```swift
let stride = vDSP_Stride(1)

let a: [Float] = [1, 2, 3, 4, 5]
let b: [Float] = [10, 20, 30, 40, 50]

let n = vDSP_Length(a.count)

var c = [Float](repeating: 0,
                count: a.count)

vDSP_vadd(a, stride,
          b, stride,
          &c, stride,
          n)

// Prints "[11.0, 22.0, 33.0, 44.0, 55.0]".
print(c)
```

## Parameters

- `__A`: The single-precision real input vector `A`. 
- `__IA`: The stride for input vector `A`. 
- `__B`: The single-precision real input vector `B`.
- `__IB`: The stride for input vector `B`. 
- `__C`: The single-precision real output vector.
- `__IC`: The stride for output vector `C`. 
- `__N`: The number of elements to add.

## See Also

### Vector Arithmetic Functions
- [vDSP_vma](./api-1532193-vdsp_vma.md)
  Adds a single-precision vector to the product of two single-precision vectors.
- [vDSP_vsub](./api-1532189-vdsp_vsub.md)
  Subtracts two single-precision vectors.
- [vDSP_vmul](./api-1532206-vdsp_vmul.md)
  Multiplies two single-precision vectors.
- [vDSP_vsmul](./api-1532223-vdsp_vsmul.md)
  Multiplies a single-precision scalar value by a single-precision vector.
- [vDSP_vdiv](./api-1532168-vdsp_vdiv.md)
  Divides two single-precision vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1532191-vdsp_vadd)*