# refract(_:n:eta:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.

## Declaration

```swift
func refract(_ x: SIMD4<Float>, n: SIMD4<Float>, eta: Float) -> SIMD4<Float>
```

## See Also

### Geometry Functions
- [func dot(SIMD4<Float>, SIMD4<Float>) -> Float](./dot%28_,_%29-47df.md)
  Returns the dot product of two vectors.
- [func normalize(SIMD4<Float>) -> SIMD4<Float>](./normalize%28_%29-6g9xc.md)
  Returns a vector pointing in the same direction of the supplied vector with a length of 1.
- [func project(SIMD4<Float>, SIMD4<Float>) -> SIMD4<Float>](./project%28_,_%29-pdsh.md)
  Returns the first vector projected onto the second vector.
- [func reflect(SIMD4<Float>, n: SIMD4<Float>) -> SIMD4<Float>](./reflect%28_,n%29-8i5cc.md)
  Returns the reflection direction of an incident vector and a unit normal vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/refract(_:n:eta:)-8qo9c)*