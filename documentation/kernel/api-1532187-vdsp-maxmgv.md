# vDSP_maxmgv

**Framework**: Kernel  
**Kind**: func

Calculates the maximum magnitude in a single-precision vector.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vDSP_maxmgv(const float *__A, vDSP_Stride __IA, float *__C, vDSP_Length __N);
```

#### Discussion

This function calculates the maximum magnitude of the first `N` elements of `A` and writes the result to `C`:

![A diagram showing the operation of the vDSP_maxmgv function. There are three rows. The top row represents the input, vector A. The second row represents the maximum magnitude value operation. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the operation and from the operation to the output vector indicating the relationships between the input and output.](https://docs-assets.developer.apple.com/published/bc8c9aceda/9997d1e5-1da8-4603-9168-199bc11da259.png)

The operation is: 

```other
*C = -INFINITY;
for (n = 0; n < N; ++n)
    if (*C < |A[n*I]|)
        *C = |A[n*I]|;
```

The following code shows an example of using [`vDSP_maxmgv`](https://developer.apple.com/documentation/accelerate/vdsp_maxmgv).

```swift
let stride = vDSP_Stride(1)

let a: [Float] = [-1.5, 2.25, 3.6,
                  0.2, -0.1, -4.3]
let n = vDSP_Length(a.count)

var c: Float = .nan

vDSP_maxmgv(a,
            stride,
            &c,
            n)

print("max magnitude", c) // Prints "max magnitude 4.3".
```

## Parameters

- `__A`: The single-precision real input vector  . 
- `__I`: The stride for input vector  . 
- `__C`: The single-precsion output scalar.
- `__N`: The number of elements to process. If   is zero ( ), this function returns  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1532187-vdsp_maxmgv)*