# cmGamutResult1Space

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.0+

## Declaration

```swift
var cmGamutResult1Space: Int { get }
```

#### Discussion

A gamut result color space for the resulting bitmap pointed to by the `resultBitMap` field of the function [`CWMatchColors`](colorsync_manager/1805108-cwmatchcolors.md), with 1-bit direct packing. A pixel in the returned bitmap with value 1 (displayed as black) indicates an out-of-gamut color, while a pixel value of 0 (white) indicates a color that is in gamut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmgamutresult1space)*