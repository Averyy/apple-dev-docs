# simd_float1

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of one 32-bit floating-point element.

## Declaration

```swift
typealias simd_float1 = Float
```

```c
typedef float simd_float1;
```

## Topics

### Common Functions
- [func step(Float, edge: Float) -> Float](./step%28_,edge%29-7md5f.md)
  Returns zero for each element in a vector less than a specified edge; one otherwise.
- [func simd_step(Float, Float) -> Float](./simd_step%28_,_%29-7127e.md)
  Returns zero for each element in a vector less than a specified edge; one otherwise.
- [func simd_clamp(Float, Float, Float) -> Float](./simd_clamp%28_,_,_%29-8f4ck.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_fract(Float) -> Float](./simd_fract%28_%29-1ws2w.md)
  Returns the fractional part of each element in a vector.
- [func sign(Float) -> Float](./sign%28_%29-iw0p.md)
  Returns the sign of each element in a vector.
- [func simd_sign(Float) -> Float](./simd_sign%28_%29-9380i.md)
  Returns the sign of each element in a vector.
### Interpolation Functions
- [func simd_mix(Float, Float, Float) -> Float](./simd_mix%28_,_,_%29-3i6gv.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func simd_smoothstep(Float, Float, Float) -> Float](./simd_smoothstep%28_,_,_%29-993b1.md)
  Returns an element-wise smoothly interpolated value between two vectors.
### Extrema Functions
- [func simd_min(Float, Float) -> Float](./simd_min%28_,_%29-8o17r.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(Float, Float) -> Float](./simd_max%28_,_%29-7wj2s.md)
  Returns the maximum value of each element in a vector.
### Reciprocal and Reciprocal Square Root Functions
- [func recip(Float) -> Float](./recip%28_%29-8b743.md)
  Returns the reciprocal of each element in a vector.
- [func simd_recip(Float) -> Float](./simd_recip%28_%29-7ylar.md)
  Returns the reciprocal of each element in a vector.
- [func simd_fast_recip(Float) -> Float](./simd_fast_recip%28_%29-1hpi.md)
  Returns the fast reciprocal of each element in a vector.
- [func simd_precise_recip(Float) -> Float](./simd_precise_recip%28_%29-6qbmp.md)
  Returns the precise reciprocal of each element in a vector.
- [func rsqrt(Float) -> Float](./rsqrt%28_%29-7h1cq.md)
  Returns the reciprocal square root of each element in a vector.
- [func simd_rsqrt(Float) -> Float](./simd_rsqrt%28_%29-4yg08.md)
  Returns the reciprocal square root of each element in a vector.
- [func simd_fast_rsqrt(Float) -> Float](./simd_fast_rsqrt%28_%29-43uag.md)
  Returns the fast reciprocal square root of each element in a vector.
- [func simd_precise_rsqrt(Float) -> Float](./simd_precise_rsqrt%28_%29-5flt4.md)
  Returns the precise reciprocal square root of each element in a vector.
### Math Functions
- [func simd_muladd(Float, Float, Float) -> Float](./simd_muladd%28_,_,_%29-2pepd.md)
  Returns the multiply-add result for corresponding elements in three vectors.

## See Also

### Vector data types
- [typealias simd_float2](./simd_float2.md)
  A vector of two 32-bit floating-point elements.
- [typealias simd_float3](./simd_float3.md)
  A vector of three 32-bit floating-point elements.
- [typealias simd_float4](./simd_float4.md)
  A vector of four 32-bit floating-point elements.
- [typealias simd_float8](./simd_float8.md)
  A vector of eight 32-bit floating-point elements.
- [typealias simd_float16](./simd_float16.md)
  A vector of sixteen 32-bit floating-point elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_float1)*