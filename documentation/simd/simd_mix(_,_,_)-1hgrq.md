# simd_mix(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns an element-wise linearly interpolated value between two vectors.

## Declaration

```swift
func simd_mix(_ x: simd_float16, _ y: simd_float16, _ t: simd_float16) -> simd_float16
```

```c
static simd_float16 simd_mix(simd_float16 x, simd_float16 y, simd_float16 t);
```

## See Also

### Interpolation Functions
- [func simd_smoothstep(simd_float16, simd_float16, simd_float16) -> simd_float16](./simd_smoothstep%28_,_,_%29-2q68m.md)
  Returns an element-wise smoothly interpolated value between two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_mix(_:_:_:)-1hgrq)*