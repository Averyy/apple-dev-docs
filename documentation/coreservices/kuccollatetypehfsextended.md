# kUCCollateTypeHFSExtended

**Framework**: Core Services  
**Kind**: data

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kUCCollateTypeHFSExtended: Int { get }
```

#### Discussion

The `kUCCollateTypeHFSExtended` ordering scheme sorts maximally decomposed Unicode according to the rules used by the HFS Extended volume format for its catalog. When this order is used, other collation options are ignored; this order is always case-insensitive (for decomposed characters) and ignores the Unicode characters 200C-200F, 202A-202E, 206A-206F, FEFF.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/kuccollatetypehfsextended)*