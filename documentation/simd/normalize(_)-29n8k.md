# normalize(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector pointing in the same direction of the supplied vector with a length of 1.

## Declaration

```swift
func normalize(_ x: SIMD3<Double>) -> SIMD3<Double>
```

#### Return Value

The normalized vector.

#### Discussion

This function returns an undefined value if the supplied vector has zero length or is poorly scaled such that an intermediate computation overflows or underflows.

## Parameters

- `x`: The vector to normalize.

## See Also

### Geometry Functions
- [func cross(SIMD3<Double>, SIMD3<Double>) -> SIMD3<Double>](./cross%28_,_%29-7sd7t.md)
  Returns the cross product of two vectors.
- [func dot(SIMD3<Double>, SIMD3<Double>) -> Double](./dot%28_,_%29-2sdb.md)
  Returns the dot product of two vectors.
- [func project(SIMD3<Double>, SIMD3<Double>) -> SIMD3<Double>](./project%28_,_%29-9jlig.md)
  Returns the first vector projected onto the second vector.
- [func reflect(SIMD3<Double>, n: SIMD3<Double>) -> SIMD3<Double>](./reflect%28_,n%29-1vw0n.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [func refract(SIMD3<Double>, n: SIMD3<Double>, eta: Double) -> SIMD3<Double>](./refract%28_,n,eta%29-13wsy.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/normalize(_:)-29n8k)*