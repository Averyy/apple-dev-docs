# vDSP_vsadd

**Framework**: Kernel  
**Kind**: func

Adds a single-precision scalar value to a single-precision vector.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vDSP_vsadd(const float *__A, vDSP_Stride __IA, const float *__B, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function calculates the sums of the first `N` elements of `A` and the scalar value `B`, writing the result to `C`:

![A diagram showing the operation of the vDSP_vsadd function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, scalar B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://docs-assets.developer.apple.com/published/17587280e6/f26f940d-6899-4a11-8dfe-1431d62bc3ec.png)

The operation is:

```swift
 for (n = 0; n < N; ++n)
    C[n] = A[n] + B[0];
```

The following code shows an example of using [`vDSP_vsadd`](https://developer.apple.com/documentation/accelerate/vdsp_vsadd):

```swift
let a: [Float] = [1, 2, 4, 5]
var b: Float = 2

let n = vDSP_Length(a.count)

var c = [Float](repeating: 0,
                count: a.count)

vDSP_vsadd(a, stride,
           &b,
           &c, stride,
           n)

// Prints "[3.0, 4.0, 6.0, 7.0]"
print(c)
```

## Parameters

- `__A`: Single-precision real input vector.
- `__IA`: Stride for 
- `__B`: Pointer to single-precision real input scalar.
- `__C`: Single-precision real output vector.
- `__IC`: Stride for 
- `__N`: The number of elements to process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1579993-vdsp_vsadd)*