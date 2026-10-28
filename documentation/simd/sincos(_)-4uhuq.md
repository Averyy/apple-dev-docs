# sincos(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the sine and cosine of each element in a vector.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
func sincos(_ x: simd_float2) -> (sin: simd_float2, cos: simd_float2)
```

## Return Value

A two-element tuple. The first element contains the sines, and the second element contains the cosines.

## Parameters

- `x`: The source vector.

## See Also

### Trigonometric Functions
- [func acos(simd_float2) -> simd_float2](./acos%28_%29-1ya4v.md)
  Returns the arccosine of each element in a vector.
- [func asin(simd_float2) -> simd_float2](./asin%28_%29-4tbvj.md)
  Returns the arcsine of each element in a vector.
- [func atan(simd_float2) -> simd_float2](./atan%28_%29-5v3x.md)
  Returns the arctangent of each element in a vector.
- [func atan2(simd_float2, simd_float2) -> simd_float2](./atan2%28_,_%29-4dpoz.md)
  Returns the arctangent of each pair of corresponding elements in two vectors.
- [func cos(simd_float2) -> simd_float2](./cos%28_%29-59waa.md)
  Returns the cosine of each element in a vector.
- [func cospi(simd_float2) -> simd_float2](./cospi%28_%29-2cd9u.md)
  Returns the cosine of each element in a vector multiplied by pi.
- [func sin(simd_float2) -> simd_float2](./sin%28_%29-5k8vo.md)
  Returns the sine of each element in a vector.
- [func sinpi(simd_float2) -> simd_float2](./sinpi%28_%29-524r6.md)
  Returns the sine of each element in a vector multiplied by pi.
- [func sincospi(simd_float2) -> (sin: simd_float2, cos: simd_float2)](./sincospi%28_%29-11sii.md)
  Returns the sine and cosine of each element in a vector multiplied by pi.
- [func tan(simd_float2) -> simd_float2](./tan%28_%29-4rx9f.md)
  Returns the tangent of each element in a vector.
- [func tanpi(simd_float2) -> simd_float2](./tanpi%28_%29-3a1w1.md)
  Returns the tangent of each element in a vector multiplied by pi.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/sincos(_:)-4uhuq)*