# simd_quaternion(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

## Declaration

```swift
func simd_quaternion(_ xyzr: UnsafePointer<Float16>!) -> simd_quath
```

```c
static simd_quath simd_quaternion(const _Float16 xyzr[4]);
```

#### Discussion

Constructs a quaternion from an array of four scalars.

Note that the imaginary part of the quaternion comes from array elements 0, 1, and 2, and the real part comes from element 3.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_quaternion(_:)-8kjw1)*