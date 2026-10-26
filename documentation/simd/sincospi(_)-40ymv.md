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
func sincospi(_ x: simd_double4) -> (sin: simd_double4, cos: simd_double4)
```

#### Return Value

A two-element tuple. The first element contains the sines, and the second element contains the cosines.

## Parameters

- `x`: The source vector.

## See Also

### Trigonometric Functions
- [func acos(simd_double4) -> simd_double4](./acos%28_%29-9cb48.md)
  Returns the arccosine of each element in a vector.
- [func asin(simd_double4) -> simd_double4](./asin%28_%29-70soc.md)
  Returns the arcsine of each element in a vector.
- [func atan(simd_double4) -> simd_double4](./atan%28_%29-5w6c7.md)
  Returns the arctangent of each element in a vector.
- [func atan2(simd_double4, simd_double4) -> simd_double4](./atan2%28_,_%29-19fnn.md)
  Returns the arctangent of each pair of corresponding elements in two vectors.
- [func cos(simd_double4) -> simd_double4](./cos%28_%29-1leci.md)
  Returns the cosine of each element in a vector.
- [func cospi(simd_double4) -> simd_double4](./cospi%28_%29-8cke2.md)
  Returns the cosine of each element in a vector multiplied by pi.
- [func sin(simd_double4) -> simd_double4](./sin%28_%29-67ulu.md)
  Returns the sine of each element in a vector.
- [func sinpi(simd_double4) -> simd_double4](./sinpi%28_%29-45nf0.md)
  Returns the sine of each element in a vector multiplied by pi.
- [func sincos(simd_double4) -> (sin: simd_double4, cos: simd_double4)](./sincos%28_%29-9olep.md)
  Returns the sine and cosine of each element in a vector.
- [func tan(simd_double4) -> simd_double4](./tan%28_%29-5zsp2.md)
  Returns the tangent of each element in a vector.
- [func tanpi(simd_double4) -> simd_double4](./tanpi%28_%29-54qo6.md)
  Returns the tangent of each element in a vector multiplied by pi.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/sincospi(_:)-40ymv)*