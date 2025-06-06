# vDSP_vma

**Framework**: Kernel  
**Kind**: func

Adds a single-precision vector to the product of two single-precision vectors.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vDSP_vma(const float *__A, vDSP_Stride __IA, const float *__B, vDSP_Stride __IB, const float *__C, vDSP_Stride __IC, float *__D, vDSP_Stride __ID, vDSP_Length __N);
```

#### Discussion

This function calculates the products of the first `N` elements of `A` and `B`, adds each product to the corresponding value in `C`, and writes the result to `D`:

![A diagram showing the operation of the vDSP_vma function. There are five rows. The top two rows represents the first two inputs, vector A and vector B. The third row represents the intermediate result of the first two inputs. The forth row represents the third input, vector C. The bottom row represents the output, vector D. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://docs-assets.developer.apple.com/published/6deaee1edc/966d3cc0-7e33-45ba-a1ec-2e4032171852.png)

The operation is:

```other
 for (n = 0; n < N; ++n)
    D[n] = A[n] * B[n] + C[n];
```

The following code shows an example of using [`vDSP_vma`](https://developer.apple.com/documentation/accelerate/vdsp_vma):

```swift
let stride = vDSP_Stride(1)

let a: [Float] = [10, 20, 30, 40, 50]
let b: [Float] = [ 1,  2,  3,  4,  5]

let c: [Float] = [1, 2, 3, 4, 5]

let n = vDSP_Length(a.count)

var d = [Float](repeating: 0,
                count: a.count)

vDSP_vma(a, stride,
         b, stride,
         c, stride,
         &d, stride,
         n)

// Prints "[11.0, 42.0, 93.0, 164.0, 255.0]".
print(d)
```

## Parameters

- `__A`: The single-precision real input vector  . 
- `__IA`: The stride for input vector  . 
- `__B`: The single-precision real input vector  .
- `__IB`: The stride for input vector  . 
- `__C`: The single-precision real input vector  . 
- `__IC`: The stride for input vector  .
- `__D`: The single-precision real output vector.
- `__ID`: The stride for output vector  . 
- `__N`: The number of elements to process.

## See Also

- [vDSP_vadd](1532191-vdsp_vadd.md)
  Adds two single-precision vectors.
- [vDSP_vsub](1532189-vdsp_vsub.md)
  Subtracts two single-precision vectors.
- [vDSP_vmul](1532206-vdsp_vmul.md)
  Multiplies two single-precision vectors.
- [vDSP_vsmul](1532223-vdsp_vsmul.md)
  Multiplies a single-precision scalar value by a single-precision vector.
- [vDSP_vdiv](1532168-vdsp_vdiv.md)
  Divides two single-precision vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1532193-vdsp_vma)*