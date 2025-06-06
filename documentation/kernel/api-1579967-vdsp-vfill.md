# vDSP_vfill

**Framework**: Kernel  
**Kind**: func

Populates a single-precision vector with a specified scalar value.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vDSP_vfill(const float *__A, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

The functions in this group populate a vector with a specified scalar value. 

The following code shows how to clear the array c, setting the value of each element to pi:

```swift
let n = vDSP_Length(10)
let stride = vDSP_Stride(1)

var a = Float.pi

var c = [Float](repeating: .nan,
                count: Int(n))

vDSP_vfill(&a,
           &c,
           stride,
           n)

// Prints "[3.1415925, 3.1415925, 3.1415925,
//          3.1415925, 3.1415925, 3.1415925,
//          3.1415925, 3.1415925, 3.1415925,
//          3.1415925]"
print(c)
```

## Parameters

- `__A`: Pointer to single-precision real input scalar.
- `__C`: Single-precision real output vector.
- `__IC`: Address stride for  .
- `__N`: The number of elements to process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1579967-vdsp_vfill)*