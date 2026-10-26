# simd_mix(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns an element-wise linearly interpolated value between two vectors.

## Declaration

```swift
func simd_mix(_ x: simd_half16, _ y: simd_half16, _ t: simd_half16) -> simd_half16
```

```c
static simd_half16 simd_mix(simd_half16 x, simd_half16 y, simd_half16 t);
```

## See Also

### Interpolation functions
- [func simd_smoothstep(simd_half16, simd_half16, simd_half16) -> simd_half16](./simd_smoothstep%28_,_,_%29-4twuq.md)
  Returns an element-wise smoothly interpolated value between two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_mix(_:_:_:)-7hbla)*