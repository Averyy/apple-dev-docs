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
func sincospi(_ x: simd_double8) -> (sin: simd_double8, cos: simd_double8)
```

## Return Value

A two-element tuple. The first element contains the sines, and the second element contains the cosines.

## Parameters

- `x`: The source vector.

## See Also

### Trigonometric Functions
- [func acos(simd_double8) -> simd_double8](./acos%28_%29-2141m.md)
  Returns the arccosine of each element in a vector.
- [func asin(simd_double8) -> simd_double8](./asin%28_%29-78d03.md)
  Returns the arcsine of each element in a vector.
- [func atan(simd_double8) -> simd_double8](./atan%28_%29-7b52p.md)
  Returns the arctangent of each element in a vector.
- [func atan2(simd_double8, simd_double8) -> simd_double8](./atan2%28_,_%29-8pfg9.md)
  Returns the arctangent of each pair of corresponding elements in two vectors.
- [func cos(simd_double8) -> simd_double8](./cos%28_%29-7bqey.md)
  Returns the cosine of each element in a vector.
- [func cospi(simd_double8) -> simd_double8](./cospi%28_%29-8d55q.md)
  Returns the cosine of each element in a vector multiplied by pi.
- [func sin(simd_double8) -> simd_double8](./sin%28_%29-1joh9.md)
  Returns the sine of each element in a vector.
- [func sinpi(simd_double8) -> simd_double8](./sinpi%28_%29-9tdix.md)
  Returns the sine of each element in a vector multiplied by pi.
- [func sincos(simd_double8) -> (sin: simd_double8, cos: simd_double8)](./sincos%28_%29-3iwed.md)
  Returns the sine and cosine of each element in a vector.
- [func tan(simd_double8) -> simd_double8](./tan%28_%29-7a2xj.md)
  Returns the tangent of each element in a vector.
- [func tanpi(simd_double8) -> simd_double8](./tanpi%28_%29-3lobh.md)
  Returns the tangent of each element in a vector multiplied by pi.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/sincospi(_:)-5yfry)*