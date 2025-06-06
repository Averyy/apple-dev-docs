# tableNum

**Framework**: Core Services  
**Kind**: structp

An array of unsigned 8-bit integers that map modifier bit combinations to table numbers. These values are indexes into the `keyToCharTableOffsets` array in a [`UCKeyToCharTableIndex`](uckeytochartableindex.md)structure; these, in turn, are offsets to the actual key-code-to character tables, which follow the `UCKeyToCharTableIndex` structure in the `'uchr'` resource.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var tableNum: UInt8
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/uckeymodifierstotablenum/1390564-tablenum)*