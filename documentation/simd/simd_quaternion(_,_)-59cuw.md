# simd_quaternion(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

## Declaration

```swift
func simd_quaternion(_ from: simd_half3, _ to: simd_half3) -> simd_quath
```

```c
static simd_quath simd_quaternion(simd_half3 from, simd_half3 to);
```

#### Discussion

Construct a quaternion that rotates from one vector to another.

The rotation axis is `simd_cross(from, to)`. If `from` and `to` point in opposite directions (to within machine precision), an arbitrary rotation axis is chosen, and the angle is pi radians.

## Parameters

- `from`: A normalized three-element vector.
- `to`: A normalized three-element vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_quaternion(_:_:)-59cuw)*