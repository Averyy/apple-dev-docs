# kSKProximityIndexing

**Framework**: Core Services  
**Kind**: data

**Availability**:
- macOS 10.4+

## Declaration

```swift
let kSKProximityIndexing: CFString!
```

#### Discussion

A Boolean flag indicating whether or not Search Kit should use proximity indexing. The flag can be a `0` or `kCFBoolenFalse` value (for false) or a `1` or `kCFBooleanTrue` value (for true). Proximity indexing is available only for inverted indexes—that is, indexes of type [`kSKIndexInverted`](kskindexinverted.md).

Use proximity indexing to support phrase searching. If this key is not present in an index’s text analysis properties dictionary, Search Kit defaults to not adding proximity information to the index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/kskproximityindexing)*