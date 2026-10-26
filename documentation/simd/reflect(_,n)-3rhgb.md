# reflect(_:n:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the reflection direction of an incident vector and a unit normal vector.

## Declaration

```swift
func reflect(_ x: SIMD2<Double>, n: SIMD2<Double>) -> SIMD2<Double>
```

## See Also

### Geometry Functions
- [func cross(SIMD2<Double>, SIMD2<Double>) -> SIMD3<Double>](./cross%28_,_%29-916aw.md)
  Returns the cross product of two vectors.
- [func dot(SIMD2<Double>, SIMD2<Double>) -> Double](./dot%28_,_%29-6ayky.md)
  Returns the dot product of two vectors.
- [func normalize(SIMD2<Double>) -> SIMD2<Double>](./normalize%28_%29-5mqhk.md)
  Returns a vector pointing in the same direction of the supplied vector with a length of 1.
- [func project(SIMD2<Double>, SIMD2<Double>) -> SIMD2<Double>](./project%28_,_%29-kai1.md)
  Returns the first vector projected onto the second vector.
- [func refract(SIMD2<Double>, n: SIMD2<Double>, eta: Double) -> SIMD2<Double>](./refract%28_,n,eta%29-1ghae.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/reflect(_:n:)-3rhgb)*