# simd_muladd(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the multiply-add result for corresponding elements in three vectors.

## Declaration

```swift
func simd_muladd(_ x: simd_double4, _ y: simd_double4, _ z: simd_double4) -> simd_double4
```

```c
static simd_double4 simd_muladd(simd_double4 x, simd_double4 y, simd_double4 z);
```

#### Return Value

The result of `x*y + z`.

## Parameters

- `x`: The *x* in `x*y + z`.
- `y`: The *y* in `x*y + z`.
- `z`: The *z* in `x*y + z`.

## See Also

### Math Functions
- [func cbrt(simd_double4) -> simd_double4](./cbrt%28_%29-7pm3s.md)
  Returns the cube root of each element in a vector.
- [func ceil(SIMD4<Double>) -> SIMD4<Double>](./ceil%28_%29-9s503.md)
  Returns the ceiling of each element in a vector.
- [func erf(simd_double4) -> simd_double4](./erf%28_%29-1yjjk.md)
  Returns the error function for each element in a vector.
- [func erfc(simd_double4) -> simd_double4](./erfc%28_%29-6rgzx.md)
  Returns the complementary error function for each element in a vector.
- [func floor(SIMD4<Double>) -> SIMD4<Double>](./floor%28_%29-3956i.md)
  Returns the floor of each element in a vector.
- [func fma(simd_double4, simd_double4, simd_double4) -> simd_double4](./fma%28_,_,_%29-6mqpv.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func fmod(simd_double4, simd_double4) -> simd_double4](./fmod%28_,_%29-92tjw.md)
  Returns the modulus after dividing each element in a vector by the corresponding element in a second vector.
- [func hypot(simd_double4, simd_double4) -> simd_double4](./hypot%28_,_%29-2exik.md)
  Returns the hypotenuse of a right-angled triangle with the sides that are adjacent to the right angle that two vectors define.
- [func lgamma(simd_double4) -> simd_double4](./lgamma%28_%29-2frmv.md)
  Returns the natural logarithm of the absolute value of the gamma function of each element in a vector.
- [func nextafter(simd_double4, simd_double4) -> simd_double4](./nextafter%28_,_%29-oxq7.md)
  Returns the next representable value of each element in a vector in the direction of the corresponding element in a second vector.
- [func pow(simd_double4, simd_double4) -> simd_double4](./pow%28_,_%29-3jh7o.md)
  Returns each element in a vector raised to the power of the corresponding element in a second vector.
- [func remainder(simd_double4, simd_double4) -> simd_double4](./remainder%28_,_%29-jw8b.md)
  Returns the remainder after dividing each element in an array by the corresponding element in a second array of double-precision values.
- [func round(simd_double4) -> simd_double4](./round%28_%29-5ytc6.md)
  Returns each element in a vector rounded to the nearest integer.
- [func tgamma(simd_double4) -> simd_double4](./tgamma%28_%29-2o8vo.md)
  Returns the gamma function for each element in a vector.
- [func trunc(SIMD4<Double>) -> SIMD4<Double>](./trunc%28_%29-9n2h5.md)
  Returns each element in a vector rounded toward zero to the nearest integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_muladd(_:_:_:)-6kpyx)*