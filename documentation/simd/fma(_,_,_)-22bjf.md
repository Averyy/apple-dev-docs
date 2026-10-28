# fma(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the multiply-add result for corresponding elements in three vectors.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
func fma(_ x: simd_float3, _ y: simd_float3, _ z: simd_float3) -> simd_float3
```

## Return Value

The result of `x*y + z`.

## Parameters

- `x`: The *x* in `x*y + z`.
- `y`: The *y* in `x*y + z`.
- `z`: The *z* in `x*y + z`.

## See Also

### Math Functions
- [func cbrt(simd_float3) -> simd_float3](./cbrt%28_%29-6vcwl.md)
  Returns the cube root of each element in a vector.
- [func ceil(SIMD3<Float>) -> SIMD3<Float>](./ceil%28_%29-580ar.md)
  Returns the ceiling of each element in a vector.
- [func erf(simd_float3) -> simd_float3](./erf%28_%29-2fow4.md)
  Returns the error function for each element in a vector.
- [func erfc(simd_float3) -> simd_float3](./erfc%28_%29-7e6kk.md)
  Returns the complementary error function for each element in a vector.
- [func floor(SIMD3<Float>) -> SIMD3<Float>](./floor%28_%29-50q1o.md)
  Returns the floor of each element in a vector.
- [func fmod(simd_float3, simd_float3) -> simd_float3](./fmod%28_,_%29-3x8lc.md)
  Returns the modulus after dividing each element in a vector by the corresponding element in a second vector.
- [func hypot(simd_float3, simd_float3) -> simd_float3](./hypot%28_,_%29-4xggy.md)
  Returns the hypotenuse of a right-angled triangle with the sides that are adjacent to the right angle that two vectors define.
- [func lgamma(simd_float3) -> simd_float3](./lgamma%28_%29-7kgzo.md)
  Returns the natural logarithm of the absolute value of the gamma function of each element in a vector.
- [func nextafter(simd_float3, simd_float3) -> simd_float3](./nextafter%28_,_%29-ymwd.md)
  Returns the next representable value of each element in a vector in the direction of the corresponding element in a second vector.
- [func pow(simd_float3, simd_float3) -> simd_float3](./pow%28_,_%29-65mb9.md)
  Returns each element in a vector raised to the power of the corresponding element in a second vector.
- [func remainder(simd_float3, simd_float3) -> simd_float3](./remainder%28_,_%29-7ij10.md)
  Returns the remainder after dividing each element in an array by the corresponding element in a second array of double-precision values.
- [func round(simd_float3) -> simd_float3](./round%28_%29-1tl5h.md)
  Returns each element in a vector rounded to the nearest integer.
- [func simd_muladd(simd_float3, simd_float3, simd_float3) -> simd_float3](./simd_muladd%28_,_,_%29-8a66m.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func tgamma(simd_float3) -> simd_float3](./tgamma%28_%29-6difz.md)
  Returns the gamma function for each element in a vector.
- [func trunc(SIMD3<Float>) -> SIMD3<Float>](./trunc%28_%29-9byjt.md)
  Returns each element in a vector rounded toward zero to the nearest integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/fma(_:_:_:)-22bjf)*