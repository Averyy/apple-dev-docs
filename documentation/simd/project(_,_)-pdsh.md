# project(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the first vector projected onto the second vector.

## Declaration

```swift
func project(_ x: SIMD4<Float>, _ y: SIMD4<Float>) -> SIMD4<Float>
```

## See Also

### Geometry Functions
- [func dot(SIMD4<Float>, SIMD4<Float>) -> Float](./dot%28_,_%29-47df.md)
  Returns the dot product of two vectors.
- [func normalize(SIMD4<Float>) -> SIMD4<Float>](./normalize%28_%29-6g9xc.md)
  Returns a vector pointing in the same direction of the supplied vector with a length of 1.
- [func reflect(SIMD4<Float>, n: SIMD4<Float>) -> SIMD4<Float>](./reflect%28_,n%29-8i5cc.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [func refract(SIMD4<Float>, n: SIMD4<Float>, eta: Float) -> SIMD4<Float>](./refract%28_,n,eta%29-8qo9c.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/project(_:_:)-pdsh)*