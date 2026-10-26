# reflect(_:n:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the reflection direction of an incident vector and a unit normal vector.

## Declaration

```swift
func reflect(_ x: SIMD2<Float>, n: SIMD2<Float>) -> SIMD2<Float>
```

## See Also

### Geometry Functions
- [func cross(SIMD2<Float>, SIMD2<Float>) -> SIMD3<Float>](./cross%28_,_%29-53xk2.md)
  Returns the cross product of two vectors.
- [func dot(SIMD2<Float>, SIMD2<Float>) -> Float](./dot%28_,_%29-1vb5g.md)
  Returns the dot product of two vectors.
- [func normalize(SIMD2<Float>) -> SIMD2<Float>](./normalize%28_%29-100kb.md)
  Returns a vector pointing in the same direction of the supplied vector with a length of 1.
- [func project(SIMD2<Float>, SIMD2<Float>) -> SIMD2<Float>](./project%28_,_%29-9wt83.md)
  Returns the first vector projected onto the second vector.
- [func refract(SIMD2<Float>, n: SIMD2<Float>, eta: Float) -> SIMD2<Float>](./refract%28_,n,eta%29-5bv79.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/reflect(_:n:)-6w80i)*