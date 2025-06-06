# UCTextBreakType

**Framework**: Core Services  
**Kind**: tdef

Specifies kinds of text boundaries.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias UCTextBreakType = UInt32
```

## Topics

### Constants
- [var kUCTextBreakCharMask: Int](kuctextbreakcharmask.md)
  If the bit specified by this mask is set, boundaries of characters may be located (with surrogate pairs treated as a single character).
- [var kUCTextBreakClusterMask: Int](kuctextbreakclustermask.md)
- [var kUCTextBreakWordMask: Int](kuctextbreakwordmask.md)
  If the bit specified by this mask is set, boundaries of words may be located. This can be used to determine what to highlight as the result of a double-click.
- [var kUCTextBreakLineMask: Int](kuctextbreaklinemask.md)
  If the bit specified by this mask is set, potential line breaks may be located.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/uctextbreaktype)*