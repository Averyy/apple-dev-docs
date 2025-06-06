# cmGamutResultSpace

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.0+

## Declaration

```swift
var cmGamutResultSpace: Int { get }
```

#### Discussion

A color space for the resulting bitmap pointed to by the `resultBitMap` field of the function [`CWMatchColors`](colorsync_manager/1805108-cwmatchcolors.md). A bitmap never uses this constant alone. Instead, it uses the constant `cmGamutResult1Space`, which combines `cmGamutResultSpace` and `cmOneBitDirectPacking` to define a bitmap that is 1 bit deep.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmgamutresultspace)*