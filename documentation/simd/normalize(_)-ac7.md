# normalize(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector pointing in the same direction of the supplied vector with a length of 1.

## Declaration

```swift
func normalize(_ x: SIMD3<Float>) -> SIMD3<Float>
```

#### Return Value

The normalized vector.

#### Discussion

This function returns an undefined value if the supplied vector has zero length or is poorly scaled such that an intermediate computation overflows or underflows.

## Parameters

- `x`: The vector to normalize.

## See Also

### Geometry Functions
- [func cross(SIMD3<Float>, SIMD3<Float>) -> SIMD3<Float>](./cross%28_,_%29-8xu8k.md)
  Returns the cross product of two vectors.
- [func dot(SIMD3<Float>, SIMD3<Float>) -> Float](./dot%28_,_%29-4gb9g.md)
  Returns the dot product of two vectors.
- [func project(SIMD3<Float>, SIMD3<Float>) -> SIMD3<Float>](./project%28_,_%29-9ggyv.md)
  Returns the first vector projected onto the second vector.
- [func reflect(SIMD3<Float>, n: SIMD3<Float>) -> SIMD3<Float>](./reflect%28_,n%29-64cgz.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [func refract(SIMD3<Float>, n: SIMD3<Float>, eta: Float) -> SIMD3<Float>](./refract%28_,n,eta%29-7jv66.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/normalize(_:)-ac7)*