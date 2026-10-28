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
func sincos(_ x: simd_double3) -> (sin: simd_double3, cos: simd_double3)
```

## Return Value

A two-element tuple. The first element contains the sines, and the second element contains the cosines.

## Parameters

- `x`: The source vector.

## See Also

### Trigonometric Functions
- [func acos(simd_double3) -> simd_double3](./acos%28_%29-76i0e.md)
  Returns the arccosine of each element in a vector.
- [func asin(simd_double3) -> simd_double3](./asin%28_%29-g6mp.md)
  Returns the arcsine of each element in a vector.
- [func atan(simd_double3) -> simd_double3](./atan%28_%29-2h77h.md)
  Returns the arctangent of each element in a vector.
- [func atan2(simd_double3, simd_double3) -> simd_double3](./atan2%28_,_%29-1zx4a.md)
  Returns the arctangent of each pair of corresponding elements in two vectors.
- [func cos(simd_double3) -> simd_double3](./cos%28_%29-9hw4a.md)
  Returns the cosine of each element in a vector.
- [func cospi(simd_double3) -> simd_double3](./cospi%28_%29-471sg.md)
  Returns the cosine of each element in a vector multiplied by pi.
- [func sin(simd_double3) -> simd_double3](./sin%28_%29-5dnnn.md)
  Returns the sine of each element in a vector.
- [func sinpi(simd_double3) -> simd_double3](./sinpi%28_%29-291vx.md)
  Returns the sine of each element in a vector multiplied by pi.
- [func sincospi(simd_double3) -> (sin: simd_double3, cos: simd_double3)](./sincospi%28_%29-2t5q7.md)
  Returns the sine and cosine of each element in a vector multiplied by pi.
- [func tan(simd_double3) -> simd_double3](./tan%28_%29-2tvur.md)
  Returns the tangent of each element in a vector.
- [func tanpi(simd_double3) -> simd_double3](./tanpi%28_%29-42odv.md)
  Returns the tangent of each element in a vector multiplied by pi.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/sincos(_:)-6572x)*