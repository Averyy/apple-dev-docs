# dot(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the dot product of two vectors.

## Declaration

```swift
func dot(_ x: SIMD4<Float>, _ y: SIMD4<Float>) -> Float
```

## See Also

### Geometry Functions
- [func normalize(SIMD4<Float>) -> SIMD4<Float>](./normalize%28_%29-6g9xc.md)
  Returns a vector pointing in the same direction of the supplied vector with a length of 1.
- [func project(SIMD4<Float>, SIMD4<Float>) -> SIMD4<Float>](./project%28_,_%29-pdsh.md)
  Returns the first vector projected onto the second vector.
- [func reflect(SIMD4<Float>, n: SIMD4<Float>) -> SIMD4<Float>](./reflect%28_,n%29-8i5cc.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [func refract(SIMD4<Float>, n: SIMD4<Float>, eta: Float) -> SIMD4<Float>](./refract%28_,n,eta%29-8qo9c.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/dot(_:_:)-47df)*