# vDSP_svs

**Framework**: Kernel  
**Kind**: func

Calculates the sum of signed squares in a single-precision vector.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vDSP_svs(const float *__A, vDSP_Stride __IA, float *__C, vDSP_Length __N);
```

#### Discussion

This function calculates the mean of the signed squares of the first `N` elements of `A` and writes the result to `C`:

![A diagram showing the operation of the vDSP_svs function. There are three rows. The top row represents the input, vector A. The second row represents the summation operation. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the operation and from the operation to the output vector indicating the relationships between the input and output.](https://docs-assets.developer.apple.com/published/82b8352d65/bdbc3d4e-6681-41fe-89c7-a4eb9790588d.png)

The operation is: 

```other
C[0] = sum(A[n] * |A[n]|, 0 <= n < N);
```

The following code shows an example of using [`vDSP_svs`](https://developer.apple.com/documentation/accelerate/vdsp_svs):

```swift
let stride = vDSP_Stride(1)

let a: [Float] = [-1.5, 2.25, 3.6,
                  0.2, -0.1, -4.3]
let n = vDSP_Length(a.count)

var c: Float = .nan

vDSP_svs(a,
         stride,
         &c,
         n)

// Prints "sum of signed squares -2.6875".
print(String(format: "sum of signed squares %.4f", c))
```

## Parameters

- `__A`: The single-precision real input vector  . 
- `__I`: The stride for input vector  . 
- `__C`: The single-precision output scalar. 
- `__N`: The number of elements to process.

## See Also

- [vDSP_rmsqv](1532207-vdsp_rmsqv.md)
  Calculates the root mean square of a single-precision vector.
- [vDSP_svesq](1532179-vdsp_svesq.md)
  Calculates the sum of values and the sum of squares in a single-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1532174-vdsp_svs)*