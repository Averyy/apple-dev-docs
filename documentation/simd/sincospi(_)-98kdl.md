# sincospi(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the sine and cosine of each element in a vector multiplied by pi.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
func sincospi(_ x: simd_float3) -> (sin: simd_float3, cos: simd_float3)
```

#### Return Value

A two-element tuple. The first element contains the sines, and the second element contains the cosines.

## Parameters

- `x`: The source vector.

## See Also

### Trigonometric Functions
- [func acos(simd_float3) -> simd_float3](./acos%28_%29-8bwml.md)
  Returns the arccosine of each element in a vector.
- [func asin(simd_float3) -> simd_float3](./asin%28_%29-5t22r.md)
  Returns the arcsine of each element in a vector.
- [func atan(simd_float3) -> simd_float3](./atan%28_%29-3otbw.md)
  Returns the arctangent of each element in a vector.
- [func atan2(simd_float3, simd_float3) -> simd_float3](./atan2%28_,_%29-40z9.md)
  Returns the arctangent of each pair of corresponding elements in two vectors.
- [func cos(simd_float3) -> simd_float3](./cos%28_%29-2d0cu.md)
  Returns the cosine of each element in a vector.
- [func cospi(simd_float3) -> simd_float3](./cospi%28_%29-1ceix.md)
  Returns the cosine of each element in a vector multiplied by pi.
- [func sin(simd_float3) -> simd_float3](./sin%28_%29-78r0i.md)
  Returns the sine of each element in a vector.
- [func sinpi(simd_float3) -> simd_float3](./sinpi%28_%29-99o27.md)
  Returns the sine of each element in a vector multiplied by pi.
- [func sincos(simd_float3) -> (sin: simd_float3, cos: simd_float3)](./sincos%28_%29-3330.md)
  Returns the sine and cosine of each element in a vector.
- [func tan(simd_float3) -> simd_float3](./tan%28_%29-yv9u.md)
  Returns the tangent of each element in a vector.
- [func tanpi(simd_float3) -> simd_float3](./tanpi%28_%29-3lzzx.md)
  Returns the tangent of each element in a vector multiplied by pi.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/sincospi(_:)-98kdl)*