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
func sincos(_ x: simd_double2) -> (sin: simd_double2, cos: simd_double2)
```

## Return Value

A two-element tuple. The first element contains the sines, and the second element contains the cosines.

## Parameters

- `x`: The source vector.

## See Also

### Trigonometric Functions
- [func acos(simd_double2) -> simd_double2](./acos%28_%29-1hgv5.md)
  Returns the arccosine of each element in a vector.
- [func asin(simd_double2) -> simd_double2](./asin%28_%29-72orw.md)
  Returns the arcsine of each element in a vector.
- [func atan(simd_double2) -> simd_double2](./atan%28_%29-9onaa.md)
  Returns the arctangent of each element in a vector.
- [func atan2(simd_double2, simd_double2) -> simd_double2](./atan2%28_,_%29-6ogu4.md)
  Returns the arctangent of each pair of corresponding elements in two vectors.
- [func cos(simd_double2) -> simd_double2](./cos%28_%29-3p9ym.md)
  Returns the cosine of each element in a vector.
- [func cospi(simd_double2) -> simd_double2](./cospi%28_%29-57353.md)
  Returns the cosine of each element in a vector multiplied by pi.
- [func sin(simd_double2) -> simd_double2](./sin%28_%29-3p88b.md)
  Returns the sine of each element in a vector.
- [func sinpi(simd_double2) -> simd_double2](./sinpi%28_%29-4lgpo.md)
  Returns the sine of each element in a vector multiplied by pi.
- [func sincospi(simd_double2) -> (sin: simd_double2, cos: simd_double2)](./sincospi%28_%29-3fwbj.md)
  Returns the sine and cosine of each element in a vector multiplied by pi.
- [func tan(simd_double2) -> simd_double2](./tan%28_%29-5czlf.md)
  Returns the tangent of each element in a vector.
- [func tanpi(simd_double2) -> simd_double2](./tanpi%28_%29-9z76.md)
  Returns the tangent of each element in a vector multiplied by pi.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/sincos(_:)-9pa2l)*