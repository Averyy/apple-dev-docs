# simd_quaternion(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

## Declaration

```swift
func simd_quaternion(_ xyzr: simd_half4) -> simd_quath
```

```c
static simd_quath simd_quaternion(simd_half4 xyzr);
```

## Discussion

Constructs a quaternion from a four-element vector.

Note that the imaginary (vector) part of the quaternion comes from lanes 0, 1, and 2 of the vector, and the real (scalar) part comes from lane 3.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_quaternion(_:)-4565s)*