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
func sincos(_ x: simd_float4) -> (sin: simd_float4, cos: simd_float4)
```

#### Return Value

A two-element tuple. The first element contains the sines, and the second element contains the cosines.

## Parameters

- `x`: The source vector.

## See Also

### Trigonometric Functions
- [func acos(simd_float4) -> simd_float4](./acos%28_%29-2blze.md)
  Returns the arccosine of each element in a vector.
- [func asin(simd_float4) -> simd_float4](./asin%28_%29-87ban.md)
  Returns the arcsine of each element in a vector.
- [func atan(simd_float4) -> simd_float4](./atan%28_%29-8xa90.md)
  Returns the arctangent of each element in a vector.
- [func atan2(simd_float4, simd_float4) -> simd_float4](./atan2%28_,_%29-63ije.md)
  Returns the arctangent of each pair of corresponding elements in two vectors.
- [func cos(simd_float4) -> simd_float4](./cos%28_%29-8qcj2.md)
  Returns the cosine of each element in a vector.
- [func cospi(simd_float4) -> simd_float4](./cospi%28_%29-5chnf.md)
  Returns the cosine of each element in a vector multiplied by pi.
- [func sin(simd_float4) -> simd_float4](./sin%28_%29-80x4.md)
  Returns the sine of each element in a vector.
- [func sinpi(simd_float4) -> simd_float4](./sinpi%28_%29-71xz.md)
  Returns the sine of each element in a vector multiplied by pi.
- [func sincospi(simd_float4) -> (sin: simd_float4, cos: simd_float4)](./sincospi%28_%29-84wzt.md)
  Returns the sine and cosine of each element in a vector multiplied by pi.
- [func tan(simd_float4) -> simd_float4](./tan%28_%29-7uvy9.md)
  Returns the tangent of each element in a vector.
- [func tanpi(simd_float4) -> simd_float4](./tanpi%28_%29-93eul.md)
  Returns the tangent of each element in a vector multiplied by pi.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/sincos(_:)-8bfn1)*