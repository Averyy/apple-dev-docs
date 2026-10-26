# simd_smoothstep(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns an element-wise smoothly interpolated value between two vectors.

## Declaration

```swift
func simd_smoothstep(_ edge0: Float, _ edge1: Float, _ x: Float) -> Float
```

```c
static float simd_smoothstep(float edge0, float edge1, float x);
```

## Mentions

- [Using linear interpolation to construct new data points](../Accelerate/using-linear-interpolation-to-construct-new-data-points.md)

## See Also

### Interpolation Functions
- [func simd_mix(Float, Float, Float) -> Float](./simd_mix%28_,_,_%29-3i6gv.md)
  Returns an element-wise linearly interpolated value between two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_smoothstep(_:_:_:)-993b1)*