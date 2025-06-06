# vDSP_sve

**Framework**: Kernel  
**Kind**: func

Calculates the sum of values in a single-precision vector.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vDSP_sve(const float *__A, vDSP_Stride __I, float *__C, vDSP_Length __N);
```

#### Discussion

This function calculates the sum of the first `N` elements of `A` and writes the result to `C`:

![A diagram showing the operation of the vDSP_sve function. There are three rows. The top row represents the input, vector A. The second row represents the summation operation. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the operation and from the operation to the output vector indicating the relationships between the input and output.](https://docs-assets.developer.apple.com/published/d3fa097403/145b07f5-9718-452e-9ea1-d4619dff6521.png)

The operation is: 

```other
C[0] = sum(A[n], 0 <= n < N);
```

The following code shows an example of using [`vDSP_sve`](https://developer.apple.com/documentation/accelerate/vdsp_sve):

```swift
let stride = vDSP_Stride(1)

let a: [Float] = [-1.5, 2.25, 3.6,
                  0.2, -0.1, -4.3]
let n = vDSP_Length(a.count)

var c: Float = .nan

vDSP_sve(a,
         stride,
         &c,
         n)

// Prints "sum 0.1500"
print(String(format: "sum %.4f", c))
```

## Parameters

- `__A`: Single-precision real input vector.
- `__I`: Stride for  .
- `__C`: Single-precision real output scalar.
- `__N`: The number of elements to process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1579937-vdsp_sve)*