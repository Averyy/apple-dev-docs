# simd_muladd(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the multiply-add result for corresponding elements in three vectors.

## Declaration

```swift
func simd_muladd(_ x: simd_double3, _ y: simd_double3, _ z: simd_double3) -> simd_double3
```

```c
static simd_double3 simd_muladd(simd_double3 x, simd_double3 y, simd_double3 z);
```

## Return Value

The result of `x*y + z`.

## Parameters

- `x`: The *x* in `x*y + z`.
- `y`: The *y* in `x*y + z`.
- `z`: The *z* in `x*y + z`.

## See Also

### Math Functions
- [func cbrt(simd_double3) -> simd_double3](./cbrt%28_%29-38h14.md)
  Returns the cube root of each element in a vector.
- [func ceil(SIMD3<Double>) -> SIMD3<Double>](./ceil%28_%29-72yci.md)
  Returns the ceiling of each element in a vector.
- [func erf(simd_double3) -> simd_double3](./erf%28_%29-8eer2.md)
  Returns the error function for each element in a vector.
- [func erfc(simd_double3) -> simd_double3](./erfc%28_%29-7ux6y.md)
  Returns the complementary error function for each element in a vector.
- [func floor(SIMD3<Double>) -> SIMD3<Double>](./floor%28_%29-262rp.md)
  Returns the floor of each element in a vector.
- [func fma(simd_double3, simd_double3, simd_double3) -> simd_double3](./fma%28_,_,_%29-6w3jf.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func fmod(simd_double3, simd_double3) -> simd_double3](./fmod%28_,_%29-16oie.md)
  Returns the modulus after dividing each element in a vector by the corresponding element in a second vector.
- [func hypot(simd_double3, simd_double3) -> simd_double3](./hypot%28_,_%29-5z7ry.md)
  Returns the hypotenuse of a right-angled triangle with the sides that are adjacent to the right angle that two vectors define.
- [func lgamma(simd_double3) -> simd_double3](./lgamma%28_%29-4lks7.md)
  Returns the natural logarithm of the absolute value of the gamma function of each element in a vector.
- [func nextafter(simd_double3, simd_double3) -> simd_double3](./nextafter%28_,_%29-7qi1e.md)
  Returns the next representable value of each element in a vector in the direction of the corresponding element in a second vector.
- [func pow(simd_double3, simd_double3) -> simd_double3](./pow%28_,_%29-6hgod.md)
  Returns each element in a vector raised to the power of the corresponding element in a second vector.
- [func remainder(simd_double3, simd_double3) -> simd_double3](./remainder%28_,_%29-28w7v.md)
  Returns the remainder after dividing each element in an array by the corresponding element in a second array of double-precision values.
- [func round(simd_double3) -> simd_double3](./round%28_%29-3e7l9.md)
  Returns each element in a vector rounded to the nearest integer.
- [func tgamma(simd_double3) -> simd_double3](./tgamma%28_%29-98alm.md)
  Returns the gamma function for each element in a vector.
- [func trunc(SIMD3<Double>) -> SIMD3<Double>](./trunc%28_%29-4p8mg.md)
  Returns each element in a vector rounded toward zero to the nearest integer.
- [cbrt](./cbrt.md)
  Returns the cube root of each element in a vector.
- [copysign](./copysign.md)
  Returns each element of a vector, with the sign of the corresponding element in a second vector.
- [erf](./erf.md)
  Returns the error function for each element in a vector.
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
- [tgamma](./tgamma.md)
  Returns the gamma function for each element in a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_muladd(_:_:_:)-74qpk)*