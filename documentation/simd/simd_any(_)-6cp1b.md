# simd_any(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns true if the high-order bit of any element is set; false otherwise.

## Declaration

```swift
func simd_any(_ x: simd_int4) -> simd_bool
```

```c
static simd_bool simd_any(simd_int4 x);
```

## See Also

### Logic and Bitwise Functions
- [func simd_all(simd_int4) -> simd_bool](./simd_all%28_%29-1jw6t.md)
  Returns true if the high-order bit of every element is set; false otherwise.
- [func simd_bitselect(simd_int4, simd_int4, simd_int4) -> simd_int4](./simd_bitselect%28_,_,_%29-27mh1.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_any(_:)-6cp1b)*