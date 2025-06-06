# vDSP_sve_svesq

**Framework**: Kernel  
**Kind**: func

Calculates the sum of values and the sum of squares in a single-precision vector.

**Availability**:
- macOS 10.8+

## Declaration

```swift
void vDSP_sve_svesq(const float *__A, vDSP_Stride __IA, float *__Sum, float *__SumOfSquares, vDSP_Length __N);
```

#### Discussion

This function calculates the sum of values and the sum of squares of the first `N` elements of `A` and writes the result to `Sum` and `SumOfSquares` respectively:

![A diagram showing the operation of the vDSP_sve_svesq function. There are three rows. The top row represents the input, vector A. The second row represents the summation operations. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the operation and from the operation to the output vector indicating the relationships between the input and output.](https://docs-assets.developer.apple.com/published/7d47a62767/76401862-7c25-4288-92ff-4e7b94821c8f.png)

The operation is: 

```other
Sum          = sum(A[n],      0 <= n < N);
SumOfSquares = sum(A[n] ** 2, 0 <= n < N);
```

The following code shows an example of using [`vDSP_sve_svesq`](https://developer.apple.com/documentation/accelerate/vdsp_sve_svesq):

```swift
let stride = vDSP_Stride(1)

let a: [Float] = [-1.5, 2.25, 3.6,
                  0.2, -0.1, -4.3]
let n = vDSP_Length(a.count)

var sum: Float = .nan
var sumOfSquares: Float = .nan

vDSP_sve_svesq(a,
               stride,
               &sum,
               &sumOfSquares,
               n)

// Prints "sum 0.1500 sum of squares 38.8125"
print(String(format: "sum %.4f", sum),
      String(format: "sum of squares %.4f", sumOfSquares))
```

## Parameters

- `__A`: Single-precision input vector.
- `__IA`: Stride for the input vector.
- `__Sum`: Single-precision sum (scalar) of the elements of  .
- `__SumOfSquares`: Single-precision sum (scalar) of the squares of the elements of  .
- `__N`: Number of elements in  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1579989-vdsp_sve_svesq)*