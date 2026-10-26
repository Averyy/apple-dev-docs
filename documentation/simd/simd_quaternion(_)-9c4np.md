# simd_quaternion(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

## Declaration

```swift
func simd_quaternion(_ matrix: simd_half4x4) -> simd_quath
```

```c
static simd_quath simd_quaternion(simd_half4x4 matrix);
```

#### Discussion

Construct a quaternion from a 4x4 rotation `matrix`.

The last row and column of the matrix are ignored. This function is equivalent to calling simd_quaternion with the upper-left 3x3 submatrix                .


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_quaternion(_:)-9c4np)*