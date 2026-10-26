# project(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the first vector projected onto the second vector.

## Declaration

```swift
func project(_ x: SIMD3<Double>, _ y: SIMD3<Double>) -> SIMD3<Double>
```

## See Also

### Geometry Functions
- [func cross(SIMD3<Double>, SIMD3<Double>) -> SIMD3<Double>](./cross%28_,_%29-7sd7t.md)
  Returns the cross product of two vectors.
- [func dot(SIMD3<Double>, SIMD3<Double>) -> Double](./dot%28_,_%29-2sdb.md)
  Returns the dot product of two vectors.
- [func normalize(SIMD3<Double>) -> SIMD3<Double>](./normalize%28_%29-29n8k.md)
  Returns a vector pointing in the same direction of the supplied vector with a length of 1.
- [func reflect(SIMD3<Double>, n: SIMD3<Double>) -> SIMD3<Double>](./reflect%28_,n%29-1vw0n.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [func refract(SIMD3<Double>, n: SIMD3<Double>, eta: Double) -> SIMD3<Double>](./refract%28_,n,eta%29-13wsy.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/project(_:_:)-9jlig)*