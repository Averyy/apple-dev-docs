# SKDocumentIndexState

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

The indexing state of a document.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```swift
struct SKDocumentIndexState
```

```c
typedef enum SKDocumentIndexState : unsigned int {
    ...
} SKDocumentIndexState;
```

## Topics

### Constants
- [var kSKDocumentStateNotIndexed: SKDocumentIndexState](./kskdocumentstatenotindexed.md)
  Specifies that the document is not indexed.
- [var kSKDocumentStateIndexed: SKDocumentIndexState](./kskdocumentstateindexed.md)
  Specifies that the document is indexed.
- [var kSKDocumentStateAddPending: SKDocumentIndexState](./kskdocumentstateaddpending.md)
  Specifies that the document is not in the index but will be added after the index is flushed or closed.
- [var kSKDocumentStateDeletePending: SKDocumentIndexState](./kskdocumentstatedeletepending.md)
  Specifies that the document is in the index but will be deleted after the index is flushed or closed.
- [kSKDocumentStateNotIndexed](./skdocumentindexstate/kskdocumentstatenotindexed.md)
  Specifies that the document is not indexed.
- [kSKDocumentStateIndexed](./skdocumentindexstate/kskdocumentstateindexed.md)
  Specifies that the document is indexed.
- [kSKDocumentStateAddPending](./skdocumentindexstate/kskdocumentstateaddpending.md)
  Specifies that the document is not in the index but will be added after the index is flushed or closed.
- [kSKDocumentStateDeletePending](./skdocumentindexstate/kskdocumentstatedeletepending.md)
  Specifies that the document is in the index but will be deleted after the index is flushed or closed.
### Initializers
- [init(UInt32)](./skdocumentindexstate/api-1450037-init.md)
- [init(rawValue: UInt32)](./skdocumentindexstate/api-1441863-init.md)
### Instance Properties
- [var rawValue: UInt32](./skdocumentindexstate/api-1443351-rawvalue.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/skdocumentindexstate)*