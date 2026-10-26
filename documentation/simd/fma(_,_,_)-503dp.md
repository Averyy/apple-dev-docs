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
func fma(_ x: simd_float16, _ y: simd_float16, _ z: simd_float16) -> simd_float16
```

#### Return Value

The result of `x*y + z`.

## Parameters

- `x`: The *x* in `x*y + z`.
- `y`: The *y* in `x*y + z`.
- `z`: The *z* in `x*y + z`.

## See Also

### Math Functions
- [func cbrt(simd_float16) -> simd_float16](./cbrt%28_%29-3cnri.md)
  Returns the cube root of each element in a vector.
- [func erf(simd_float16) -> simd_float16](./erf%28_%29-7wkg3.md)
  Returns the error function for each element in a vector.
- [func erfc(simd_float16) -> simd_float16](./erfc%28_%29-20vsh.md)
  Returns the complementary error function for each element in a vector.
- [func fmod(simd_float16, simd_float16) -> simd_float16](./fmod%28_,_%29-2bys0.md)
  Returns the modulus after dividing each element in a vector by the corresponding element in a second vector.
- [func hypot(simd_float16, simd_float16) -> simd_float16](./hypot%28_,_%29-265pt.md)
  Returns the hypotenuse of a right-angled triangle with the sides that are adjacent to the right angle that two vectors define.
- [func lgamma(simd_float16) -> simd_float16](./lgamma%28_%29-1onkc.md)
  Returns the natural logarithm of the absolute value of the gamma function of each element in a vector.
- [func nextafter(simd_float16, simd_float16) -> simd_float16](./nextafter%28_,_%29-9kvo8.md)
  Returns the next representable value of each element in a vector in the direction of the corresponding element in a second vector.
- [func pow(simd_float16, simd_float16) -> simd_float16](./pow%28_,_%29-7mpyc.md)
  Returns each element in a vector raised to the power of the corresponding element in a second vector.
- [func remainder(simd_float16, simd_float16) -> simd_float16](./remainder%28_,_%29-5dxqm.md)
  Returns the remainder after dividing each element in an array by the corresponding element in a second array of double-precision values.
- [func round(simd_float16) -> simd_float16](./round%28_%29-74w3c.md)
  Returns each element in a vector rounded to the nearest integer.
- [func simd_muladd(simd_float16, simd_float16, simd_float16) -> simd_float16](./simd_muladd%28_,_,_%29-8imv2.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func tgamma(simd_float16) -> simd_float16](./tgamma%28_%29-9r61k.md)
  Returns the gamma function for each element in a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/fma(_:_:_:)-503dp)*