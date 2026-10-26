# project(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the first vector projected onto the second vector.

## Declaration

```swift
func project(_ x: SIMD4<Double>, _ y: SIMD4<Double>) -> SIMD4<Double>
```

## See Also

### Geometry Functions
- [func dot(SIMD4<Double>, SIMD4<Double>) -> Double](./dot%28_,_%29-5ifd.md)
  Returns the dot product of two vectors.
- [func normalize(SIMD4<Double>) -> SIMD4<Double>](./normalize%28_%29-3lhrd.md)
  Returns a vector pointing in the same direction of the supplied vector with a length of 1.
- [func reflect(SIMD4<Double>, n: SIMD4<Double>) -> SIMD4<Double>](./reflect%28_,n%29-1nabs.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [func refract(SIMD4<Double>, n: SIMD4<Double>, eta: Double) -> SIMD4<Double>](./refract%28_,n,eta%29-2macj.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/project(_:_:)-1uuxo)*