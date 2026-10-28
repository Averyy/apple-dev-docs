# simd_spline(_:_:_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

## Declaration

```swift
func simd_spline(_ q0: simd_quath, _ q1: simd_quath, _ q2: simd_quath, _ q3: simd_quath, _ t: Float16) -> simd_quath
```

```c
static simd_quath simd_spline(simd_quath q0, simd_quath q1, simd_quath q2, simd_quath q3, _Float16 t);
```

## Discussion

Interpolate between quaternions along a spherical cubic spline.

The function interpolates between q1 and q2. q0 is the left endpoint of the previous interval, and q3 is the right endpoint of the next interval. Use this function to smoothly interpolate between a sequence of rotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_spline(_:_:_:_:_:)-4ojmq)*