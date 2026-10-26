# simd_muladd(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the multiply-add result for corresponding elements in three vectors.

## Declaration

```swift
func simd_muladd(_ x: simd_float2, _ y: simd_float2, _ z: simd_float2) -> simd_float2
```

```c
static simd_float2 simd_muladd(simd_float2 x, simd_float2 y, simd_float2 z);
```

#### Return Value

The result of `x*y + z`.

## Parameters

- `x`: The *x* in `x*y + z`.
- `y`: The *y* in `x*y + z`.
- `z`: The *z* in `x*y + z`.

## See Also

### Math Functions
- [func cbrt(simd_float2) -> simd_float2](./cbrt%28_%29-1t3k.md)
  Returns the cube root of each element in a vector.
- [func ceil(SIMD2<Float>) -> SIMD2<Float>](./ceil%28_%29-8j6zo.md)
  Returns the ceiling of each element in a vector.
- [func erf(simd_float2) -> simd_float2](./erf%28_%29-1unjp.md)
  Returns the error function for each element in a vector.
- [func erfc(simd_float2) -> simd_float2](./erfc%28_%29-1hisg.md)
  Returns the complementary error function for each element in a vector.
- [func floor(SIMD2<Float>) -> SIMD2<Float>](./floor%28_%29-1e9me.md)
  Returns the floor of each element in a vector.
- [func fma(simd_float2, simd_float2, simd_float2) -> simd_float2](./fma%28_,_,_%29-69k8u.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func fmod(simd_float2, simd_float2) -> simd_float2](./fmod%28_,_%29-566aw.md)
  Returns the modulus after dividing each element in a vector by the corresponding element in a second vector.
- [func hypot(simd_float2, simd_float2) -> simd_float2](./hypot%28_,_%29-1zs4i.md)
  Returns the hypotenuse of a right-angled triangle with the sides that are adjacent to the right angle that two vectors define.
- [func lgamma(simd_float2) -> simd_float2](./lgamma%28_%29-1ksbv.md)
  Returns the natural logarithm of the absolute value of the gamma function of each element in a vector.
- [func nextafter(simd_float2, simd_float2) -> simd_float2](./nextafter%28_,_%29-8mat0.md)
  Returns the next representable value of each element in a vector in the direction of the corresponding element in a second vector.
- [func pow(simd_float2, simd_float2) -> simd_float2](./pow%28_,_%29-15e0y.md)
  Returns each element in a vector raised to the power of the corresponding element in a second vector.
- [func remainder(simd_float2, simd_float2) -> simd_float2](./remainder%28_,_%29-37wwd.md)
  Returns the remainder after dividing each element in an array by the corresponding element in a second array of double-precision values.
- [func round(simd_float2) -> simd_float2](./round%28_%29-608of.md)
  Returns each element in a vector rounded to the nearest integer.
- [func tgamma(simd_float2) -> simd_float2](./tgamma%28_%29-2aqvi.md)
  Returns the gamma function for each element in a vector.
- [func trunc(SIMD2<Float>) -> SIMD2<Float>](./trunc%28_%29-6neoe.md)
  Returns each element in a vector rounded toward zero to the nearest integer.
- [cbrt](./cbrt.md)
  Returns the cube root of each element in a vector.
- [copysign](./copysign.md)
  Returns each element of a vector, with the sign of the corresponding element in a second vector.
- [erf](./erf.md)
  Returns the error function for each element in a vector.
- [erfc](./erfc.md)
  Returns the complementary error function for each element in a vector.
- [fabs](./fabs.md)
  Returns the absolute value of each element in a vector.
- [fdim](./fdim.md)
  Returns the positive difference between corresponding elements in two vectors.
- [fma](./fma.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [fmod](./fmod.md)
  Returns the modulus after dividing each element in a vector by the corresponding element in a second vector.
- [hypot](./hypot.md)
  Returns the hypotenuse of a right-angled triangle with the sides that are adjacent to the right angle that two vectors define.
- [nextafter](./nextafter.md)
  Returns the next representable value of each element in a vector in the direction of the corresponding element in a second vector.
- [pow](./pow.md)
  Returns each element in a vector raised to the power of the corresponding element in a second vector.
- [remainder](./remainder.md)
  Returns the remainder after dividing each element in an array by the corresponding element in a second array of double-precision values.
- [rint](./rint.md)
  Returns each element in a vector rounded to the nearest integer in the specified direction.
- [round](./round.md)
  Returns each element in a vector rounded to the nearest integer.
- [sqrt](./sqrt.md)
  Returns the square root of each element in a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_muladd(_:_:_:)-45h2k)*