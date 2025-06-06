# SKDocumentIndexState

**Framework**: Core Services  
**Kind**: struct

The indexing state of a document.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```swift
struct SKDocumentIndexState
```

## Topics

### Constants
- [var kSKDocumentStateNotIndexed: SKDocumentIndexState](kskdocumentstatenotindexed.md)
  Specifies that the document is not indexed.
- [var kSKDocumentStateIndexed: SKDocumentIndexState](kskdocumentstateindexed.md)
  Specifies that the document is indexed.
- [var kSKDocumentStateAddPending: SKDocumentIndexState](kskdocumentstateaddpending.md)
  Specifies that the document is not in the index but will be added after the index is flushed or closed.
- [var kSKDocumentStateDeletePending: SKDocumentIndexState](kskdocumentstatedeletepending.md)
  Specifies that the document is in the index but will be deleted after the index is flushed or closed.
### Initializers
- [init(UInt32)](skdocumentindexstate/1450037-init.md)
- [init(rawValue: UInt32)](skdocumentindexstate/1441863-init.md)
### Instance Properties
- [var rawValue: UInt32](skdocumentindexstate/1443351-rawvalue.md)

## Relationships

### Conforms To
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/skdocumentindexstate)*