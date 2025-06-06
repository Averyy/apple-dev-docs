# vDSP_rmsqv

**Framework**: Kernel  
**Kind**: func

Calculates the root mean square of a single-precision vector.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vDSP_rmsqv(const float *__A, vDSP_Stride __IA, float *__C, vDSP_Length __N);
```

#### Discussion

This function calculates the root mean square of the first `N` elements of `A` and writes the result to `C`:

![A diagram showing the operation of the vDSP_rmsqv function. There are three rows. The top row represents the input, vector A. The second row represents the averaging operation. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the operation and from the operation to the output vector indicating the relationships between the input and output.](https://docs-assets.developer.apple.com/published/16683a60b3/6d79907e-7f0d-4e24-8a83-4d633c6b8791.png)

The operation is: 

```other
C = sqrt(sum(A[n] ** 2, 0 <= n < N) / N);
```

The following code shows an example of using [`vDSP_rmsqv`](https://developer.apple.com/documentation/accelerate/vdsp_rmsqv):

```swift
let stride = vDSP_Stride(1)

let a: [Float] = [-1.5, 2.25, 3.6,
                  0.2, -0.1, -4.3]
let n = vDSP_Length(a.count)

var c: Float = .nan

vDSP_rmsqv(a,
           stride,
           &c,
           n)

print(String(format: "RMS %.4f", c)) // Prints "RMS 2.5434".
```

## Parameters

- `__A`: The single-precision real input vector  . 
- `__I`: The stride for input vector  . 
- `__C`: The single-precision output scalar. 
- `__N`: The number of elements to process. If   is zero ( ), this function returns  .

## See Also

- [vDSP_svesq](1532179-vdsp_svesq.md)
  Calculates the sum of values and the sum of squares in a single-precision vector.
- [vDSP_svs](1532174-vdsp_svs.md)
  Calculates the sum of signed squares in a single-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1532207-vdsp_rmsqv)*