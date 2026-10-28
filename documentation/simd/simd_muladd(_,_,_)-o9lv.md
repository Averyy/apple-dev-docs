# simd_muladd(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the multiply-add result for corresponding elements in three vectors.

## Declaration

```swift
func simd_muladd(_ x: simd_double2, _ y: simd_double2, _ z: simd_double2) -> simd_double2
```

```c
static simd_double2 simd_muladd(simd_double2 x, simd_double2 y, simd_double2 z);
```

## Return Value

The result of `x*y + z`.

## Parameters

- `x`: The *x* in `x*y + z`.
- `y`: The *y* in `x*y + z`.
- `z`: The *z* in `x*y + z`.

## See Also

### Math Functions
- [func cbrt(simd_double2) -> simd_double2](./cbrt%28_%29-75bqn.md)
  Returns the cube root of each element in a vector.
- [func ceil(SIMD2<Double>) -> SIMD2<Double>](./ceil%28_%29-cu6z.md)
  Returns the ceiling of each element in a vector.
- [func erf(simd_double2) -> simd_double2](./erf%28_%29-7tfrz.md)
  Returns the error function for each element in a vector.
- [func erfc(simd_double2) -> simd_double2](./erfc%28_%29-8i2r6.md)
  Returns the complementary error function for each element in a vector.
- [func floor(SIMD2<Double>) -> SIMD2<Double>](./floor%28_%29-21h1y.md)
- [func fma(simd_double2, simd_double2, simd_double2) -> simd_double2](./fma%28_,_,_%29-4fxau.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func fmod(simd_double2, simd_double2) -> simd_double2](./fmod%28_,_%29-81hr1.md)
  Returns the modulus after dividing each element in a vector by the corresponding element in a second vector.
- [func hypot(simd_double2, simd_double2) -> simd_double2](./hypot%28_,_%29-9ecpz.md)
  Returns the hypotenuse of a right-angled triangle with the sides that are adjacent to the right angle that two vectors define.
- [func lgamma(simd_double2) -> simd_double2](./lgamma%28_%29-697vf.md)
  Returns the natural logarithm of the absolute value of the gamma function of each element in a vector.
- [func nextafter(simd_double2, simd_double2) -> simd_double2](./nextafter%28_,_%29-6qeuz.md)
  Returns the next representable value of each element in a vector in the direction of the corresponding element in a second vector.
- [func pow(simd_double2, simd_double2) -> simd_double2](./pow%28_,_%29-2ov0n.md)
  Returns each element in a vector raised to the power of the corresponding element in a second vector.
- [func remainder(simd_double2, simd_double2) -> simd_double2](./remainder%28_,_%29-1l80m.md)
  Returns the remainder after dividing each element in an array by the corresponding element in a second array of double-precision values.
- [func round(simd_double2) -> simd_double2](./round%28_%29-1ith.md)
  Returns each element in a vector rounded to the nearest integer.
- [func tgamma(simd_double2) -> simd_double2](./tgamma%28_%29-3id8t.md)
  Returns the gamma function for each element in a vector.
- [func trunc(SIMD2<Double>) -> SIMD2<Double>](./trunc%28_%29-1xvcu.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_muladd(_:_:_:)-o9lv)*