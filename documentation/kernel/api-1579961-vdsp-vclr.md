# vDSP_vclr

**Framework**: Kernel  
**Kind**: func

Populates a single-precision vector with zeros.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vDSP_vclr(float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

The [`vDSP_vclr`](https://developer.apple.com/documentation/accelerate/vdsp_vclr) and [`vDSP_vclrD`](https://developer.apple.com/documentation/accelerate/vdsp_vclrd) functions populate a vector with zeros. 

The following code shows how to clear the array c, setting the value of each element to zero:

```swift
let n = vDSP_Length(10)
let stride = vDSP_Stride(1)

var c = [Float](repeating: .nan,
                count: Int(n))

vDSP_vclr(&c,
          stride,
          n)

// Prints "[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]"
print(c)
```

## Parameters

- `__C`: Single-precision real output vector. 
- `__IC`: Address stride for  .
- `__N`: The number of elements to process. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1579961-vdsp_vclr)*