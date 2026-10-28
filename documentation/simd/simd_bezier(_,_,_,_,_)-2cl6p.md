# simd_bezier(_:_:_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

## Declaration

```swift
func simd_bezier(_ q0: simd_quath, _ q1: simd_quath, _ q2: simd_quath, _ q3: simd_quath, _ t: Float16) -> simd_quath
```

```c
static simd_quath simd_bezier(simd_quath q0, simd_quath q1, simd_quath q2, simd_quath q3, _Float16 t);
```

## Discussion

Spherical cubic Bezier interpolation between quaternions.

The function treats q0 … q3 as control points and uses slerp in place of lerp in the De Castlejeau algorithm. The endpoints of interpolation are thus q0 and q3, and the curve will not generally pass through q1 or q2. Note that the convex hull property of “standard” Bezier curve does not hold on the sphere.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bezier(_:_:_:_:_:)-2cl6p)*