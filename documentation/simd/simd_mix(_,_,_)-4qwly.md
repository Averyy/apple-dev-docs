# simd_mix(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns an element-wise linearly interpolated value between two vectors.

## Declaration

```swift
func simd_mix(_ x: simd_half32, _ y: simd_half32, _ t: simd_half32) -> simd_half32
```

```c
static simd_half32 simd_mix(simd_half32 x, simd_half32 y, simd_half32 t);
```

## See Also

### Interpolation functions
- [func simd_smoothstep(simd_half32, simd_half32, simd_half32) -> simd_half32](./simd_smoothstep%28_,_,_%29-6nnf0.md)
  Returns an element-wise smoothly interpolated value between two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_mix(_:_:_:)-4qwly)*