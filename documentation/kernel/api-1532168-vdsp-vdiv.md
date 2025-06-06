# vDSP_vdiv

**Framework**: Kernel  
**Kind**: func

Divides two single-precision vectors.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vDSP_vdiv(const float *__B, vDSP_Stride __IB, const float *__A, vDSP_Stride __IA, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function calculates the first `N` elements of `A` divided by the corresponding element in `B`, writing the result to `C`:

![A diagram showing the operation of the vDSP_vdiv function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://docs-assets.developer.apple.com/published/f46a5a223a/515d83d1-9e17-4a30-857b-fd0b4c849ccb.png)

The operation is:

```other
 for (n = 0; n < N; ++n)
    C[n] = A[n] / B[n];
```

The following code shows an example of using [`vDSP_vdiv`](https://developer.apple.com/documentation/accelerate/vdsp_vdiv):

```swift
let stride = vDSP_Stride(1)

let a: [Float] = [10, 20, 30, 40, 50]
let b: [Float] = [ 1,  2,  3,  4,  5]

let n = vDSP_Length(a.count)

var c = [Float](repeating: 0,
                count: a.count)

vDSP_vdiv(b, stride,
          a, stride,
          &c, stride,
          n)

// Prints "[10, 10, 10, 10, 10]".
print(c)
```

## Parameters

- `__B`: The single-precision real input vector  . 
- `__IB`: The stride for input vector  .
- `__A`: The single-precision real input vector  . 
- `__IA`: The stride for input vector  . 
- `__C`: The single-precision real output vector  .
- `__IC`: The stride for output vector  .
- `__N`: The number of elements to process.

## See Also

- [vDSP_vadd](1532191-vdsp_vadd.md)
  Adds two single-precision vectors.
- [vDSP_vma](1532193-vdsp_vma.md)
  Adds a single-precision vector to the product of two single-precision vectors.
- [vDSP_vsub](1532189-vdsp_vsub.md)
  Subtracts two single-precision vectors.
- [vDSP_vmul](1532206-vdsp_vmul.md)
  Multiplies two single-precision vectors.
- [vDSP_vsmul](1532223-vdsp_vsmul.md)
  Multiplies a single-precision scalar value by a single-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1532168-vdsp_vdiv)*