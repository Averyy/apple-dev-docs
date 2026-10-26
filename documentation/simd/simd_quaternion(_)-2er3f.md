# simd_quaternion(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

## Declaration

```swift
func simd_quaternion(_ matrix: simd_half3x3) -> simd_quath
```

```c
static simd_quath simd_quaternion(simd_half3x3 matrix);
```

#### Discussion

Construct a quaternion from a 3x3 rotation `matrix`.

If `matrix` is not orthogonal with determinant 1, the result is undefined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_quaternion(_:)-2er3f)*