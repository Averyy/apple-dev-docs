# project(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the first vector projected onto the second vector.

## Declaration

```swift
func project(_ x: SIMD3<Float>, _ y: SIMD3<Float>) -> SIMD3<Float>
```

## See Also

### Geometry Functions
- [func cross(SIMD3<Float>, SIMD3<Float>) -> SIMD3<Float>](./cross%28_,_%29-8xu8k.md)
  Returns the cross product of two vectors.
- [func dot(SIMD3<Float>, SIMD3<Float>) -> Float](./dot%28_,_%29-4gb9g.md)
  Returns the dot product of two vectors.
- [func normalize(SIMD3<Float>) -> SIMD3<Float>](./normalize%28_%29-ac7.md)
  Returns a vector pointing in the same direction of the supplied vector with a length of 1.
- [func reflect(SIMD3<Float>, n: SIMD3<Float>) -> SIMD3<Float>](./reflect%28_,n%29-64cgz.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [func refract(SIMD3<Float>, n: SIMD3<Float>, eta: Float) -> SIMD3<Float>](./refract%28_,n,eta%29-7jv66.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/project(_:_:)-9ggyv)*