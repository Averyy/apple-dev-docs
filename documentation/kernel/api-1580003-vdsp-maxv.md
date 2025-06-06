# vDSP_maxv

**Framework**: Kernel  
**Kind**: func

Calculates the maximum value in a single-precision vector.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vDSP_maxv(const float *__A, vDSP_Stride __IA, float *__C, vDSP_Length __N);
```

#### Discussion

This function calculates the maximum value of the first `N` elements of `A` and writes the result to `C`:

![A diagram showing the operation of the vDSP_maxv function. There are three rows. The top row represents the input, vector A. The second row represents the maximum value operation. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the operation and from the operation to the output vector indicating the relationships between the input and output.](https://docs-assets.developer.apple.com/published/6be5f0f9d8/6628cbdf-982b-42ae-a1ae-39c7bc73d461.png)

The operation is: 

```other
*C = -INFINITY;
for (n = 0; n < N; ++n)
    if (*C < A[n*I])
        *C = A[n*I];
```

The following code shows an example of using [`vDSP_maxv`](https://developer.apple.com/documentation/accelerate/vdsp_maxv).

```swift
let stride = vDSP_Stride(1)

let a: [Float] = [-1.5, 2.25, 3.6,
                  0.2, -0.1, -4.3]
let n = vDSP_Length(a.count)

var c: Float = .nan

vDSP_maxv(a,
          stride,
          &c,
          n)

print("max", c) // Prints "max 3.6"
```

## Parameters

- `__A`: Single-precision real input vector.
- `__I`: Stride for  .
- `__C`: Output scalar.
- `__N`: The number of elements to process. If   is zero ( ), this function returns  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1580003-vdsp_maxv)*