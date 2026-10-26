# simd_slerp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

## Declaration

```swift
func simd_slerp(_ q0: simd_quath, _ q1: simd_quath, _ t: Float16) -> simd_quath
```

```c
static simd_quath simd_slerp(simd_quath q0, simd_quath q1, _Float16 t);
```

#### Discussion

Spherical linear interpolation along the shortest arc between quaternions `q0` and `q1`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_slerp(_:_:_:)-7vayy)*