# refract(_:n:eta:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.

## Declaration

```swift
func refract(_ x: SIMD4<Double>, n: SIMD4<Double>, eta: Double) -> SIMD4<Double>
```

## See Also

### Geometry Functions
- [func dot(SIMD4<Double>, SIMD4<Double>) -> Double](./dot%28_,_%29-5ifd.md)
  Returns the dot product of two vectors.
- [func normalize(SIMD4<Double>) -> SIMD4<Double>](./normalize%28_%29-3lhrd.md)
  Returns a vector pointing in the same direction of the supplied vector with a length of 1.
- [func project(SIMD4<Double>, SIMD4<Double>) -> SIMD4<Double>](./project%28_,_%29-1uuxo.md)
  Returns the first vector projected onto the second vector.
- [func reflect(SIMD4<Double>, n: SIMD4<Double>) -> SIMD4<Double>](./reflect%28_,n%29-1nabs.md)
  Returns the reflection direction of an incident vector and a unit normal vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/refract(_:n:eta:)-2macj)*