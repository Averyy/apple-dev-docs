# simd_smoothstep(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns an element-wise smoothly interpolated value between two vectors.

## Declaration

```swift
func simd_smoothstep(_ edge0: simd_float16, _ edge1: simd_float16, _ x: simd_float16) -> simd_float16
```

```c
static simd_float16 simd_smoothstep(simd_float16 edge0, simd_float16 edge1, simd_float16 x);
```

## See Also

### Interpolation Functions
- [func simd_mix(simd_float16, simd_float16, simd_float16) -> simd_float16](./simd_mix%28_,_,_%29-1hgrq.md)
  Returns an element-wise linearly interpolated value between two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_smoothstep(_:_:_:)-2q68m)*