# simd_smoothstep(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns an element-wise smoothly interpolated value between two vectors.

## Declaration

```swift
func simd_smoothstep(_ edge0: simd_double8, _ edge1: simd_double8, _ x: simd_double8) -> simd_double8
```

```c
static simd_double8 simd_smoothstep(simd_double8 edge0, simd_double8 edge1, simd_double8 x);
```

## See Also

### Interpolation Functions
- [func simd_mix(simd_double8, simd_double8, simd_double8) -> simd_double8](./simd_mix%28_,_,_%29-5afwd.md)
  Returns an element-wise linearly interpolated value between two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_smoothstep(_:_:_:)-99l4q)*