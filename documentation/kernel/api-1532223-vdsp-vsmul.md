# vDSP_vsmul

**Framework**: Kernel  
**Kind**: func

Multiplies a single-precision scalar value by a single-precision vector.

**Availability**:
- macOS 10.0+

## Declaration

```swift
void vDSP_vsmul(const float *__A, vDSP_Stride __IA, const float *__B, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function calculates the products of the first `N` elements of `A` and the scalar value `B`, writing the result to `C`:

![A diagram showing the operation of the vDSP_vsmul function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, scalar B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://docs-assets.developer.apple.com/published/d7ddc4b341/54f65645-cf1f-44c1-bc5d-8a78de1289d4.png)

The operation is:

```other
 for (n = 0; n < N; ++n)
    C[n] = A[n] * B;
```

The following code shows an example of using [`vDSP_vsmul`](https://developer.apple.com/documentation/accelerate/vdsp_vsmul):

```swift
let stride = vDSP_Stride(1)

let a: [Float] = [1, 2, 4, 5]
var b: Float = 2

let n = vDSP_Length(a.count)

var c = [Float](repeating: 0,
                count: a.count)

vDSP_vsmul(a, stride,
           &b,
           &c, stride,
           n)

// Prints "[2.0, 4.0, 8.0, 10.0]".
print(c)
```

## Parameters

- `__A`: The single-precision real input vector  . 
- `__IA`: The stride for input vector  . 
- `__B`: A pointer to the single-precision real input scalar.
- `__C`: The single-precision real output vector. 
- `__IC`: The stride for output vector  . 
- `__N`: The number of elements to multiply.

## See Also

- [vDSP_vadd](1532191-vdsp_vadd.md)
  Adds two single-precision vectors.
- [vDSP_vma](1532193-vdsp_vma.md)
  Adds a single-precision vector to the product of two single-precision vectors.
- [vDSP_vsub](1532189-vdsp_vsub.md)
  Subtracts two single-precision vectors.
- [vDSP_vmul](1532206-vdsp_vmul.md)
  Multiplies two single-precision vectors.
- [vDSP_vdiv](1532168-vdsp_vdiv.md)
  Divides two single-precision vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1532223-vdsp_vsmul)*