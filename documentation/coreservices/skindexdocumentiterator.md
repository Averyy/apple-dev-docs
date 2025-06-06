# SKIndexDocumentIterator

**Framework**: Core Services  
**Kind**: cl

Defines an opaque data type representing an index-based document iterator.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```swift
class SKIndexDocumentIterator
```

#### Overview

A Search Kit document iterator lets your application loop through all the document URL objects owned by a given parent document URL object. To create an iterator, use [`SKIndexDocumentIteratorCreate(_:_:)`](1446189-skindexdocumentiteratorcreate.md). To get a copy of the next document in the set owned by the iterator, use [`SKIndexDocumentIteratorCopyNext(_:)`](1442212-skindexdocumentiteratorcopynext.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/skindexdocumentiterator)*