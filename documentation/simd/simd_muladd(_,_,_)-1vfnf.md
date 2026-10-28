# simd_muladd(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the multiply-add result for corresponding elements in three vectors.

## Declaration

```swift
func simd_muladd(_ x: simd_half8, _ y: simd_half8, _ z: simd_half8) -> simd_half8
```

```c
static simd_half8 simd_muladd(simd_half8 x, simd_half8 y, simd_half8 z);
```

## Return Value

The result of `x*y + z`.

## Parameters

- `x`: The *x* in `x*y + z`.
- `y`: The *y* in `x*y + z`.
- `z`: The *z* in `x*y + z`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_muladd(_:_:_:)-1vfnf)*