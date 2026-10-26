# simd_mix(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns an element-wise linearly interpolated value between two vectors.

## Declaration

```swift
func simd_mix(_ x: simd_double8, _ y: simd_double8, _ t: simd_double8) -> simd_double8
```

```c
static simd_double8 simd_mix(simd_double8 x, simd_double8 y, simd_double8 t);
```

## See Also

### Interpolation Functions
- [func simd_smoothstep(simd_double8, simd_double8, simd_double8) -> simd_double8](./simd_smoothstep%28_,_,_%29-99l4q.md)
  Returns an element-wise smoothly interpolated value between two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_mix(_:_:_:)-5afwd)*