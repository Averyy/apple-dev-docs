# simd_reduce_max(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the maximum value in a vector.

## Declaration

```swift
func simd_reduce_max(_ x: simd_uint4) -> UInt32
```

```c
static unsigned int simd_reduce_max(simd_uint4 x);
```

## See Also

### Reduce Functions
- [func simd_reduce_min(simd_uint4) -> UInt32](./simd_reduce_min%28_%29-4ukuu.md)
  Returns the minimum value in a vector.
- [func reduce_min(SIMD4<UInt32>) -> UInt32](./reduce_min%28_%29-3yrpe.md)
  Returns the minimum value in a vector.
- [func reduce_max(SIMD4<UInt32>) -> UInt32](./reduce_max%28_%29-ko69.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_uint4) -> UInt32](./simd_reduce_add%28_%29-2ylgg.md)
  Returns the sum of all elements in a vector.
- [func reduce_add(SIMD4<UInt32>) -> UInt32](./reduce_add%28_%29-9xs7v.md)
  Returns the sum of all elements in a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_reduce_max(_:)-4qtcm)*