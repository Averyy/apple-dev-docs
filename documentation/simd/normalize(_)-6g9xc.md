# normalize(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector pointing in the same direction of the supplied vector with a length of 1.

## Declaration

```swift
func normalize(_ x: SIMD4<Float>) -> SIMD4<Float>
```

#### Return Value

The normalized vector.

#### Discussion

This function returns an undefined value if the supplied vector has zero length or is poorly scaled such that an intermediate computation overflows or underflows.

## Parameters

- `x`: The vector to normalize.

## See Also

### Geometry Functions
- [func dot(SIMD4<Float>, SIMD4<Float>) -> Float](./dot%28_,_%29-47df.md)
  Returns the dot product of two vectors.
- [func project(SIMD4<Float>, SIMD4<Float>) -> SIMD4<Float>](./project%28_,_%29-pdsh.md)
  Returns the first vector projected onto the second vector.
- [func reflect(SIMD4<Float>, n: SIMD4<Float>) -> SIMD4<Float>](./reflect%28_,n%29-8i5cc.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [func refract(SIMD4<Float>, n: SIMD4<Float>, eta: Float) -> SIMD4<Float>](./refract%28_,n,eta%29-8qo9c.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/normalize(_:)-6g9xc)*