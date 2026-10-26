# simd_mix(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns an element-wise linearly interpolated value between two vectors.

## Declaration

```swift
func simd_mix(_ x: simd_float8, _ y: simd_float8, _ t: simd_float8) -> simd_float8
```

```c
static simd_float8 simd_mix(simd_float8 x, simd_float8 y, simd_float8 t);
```

## See Also

### Interpolation Functions
- [func simd_smoothstep(simd_float8, simd_float8, simd_float8) -> simd_float8](./simd_smoothstep%28_,_,_%29-845yk.md)
  Returns an element-wise smoothly interpolated value between two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_mix(_:_:_:)-4c4kn)*