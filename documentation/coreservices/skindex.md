# SKIndex

**Framework**: Core Services  
**Kind**: cl

Defines an opaque data type representing an index.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```swift
class SKIndex
```

#### Overview

A Search Kit index object contains the textual contents of one or more documents, as well as document URL objects (SKDocumentRefs) representing those documents’ locations.

To create a new disk-based Search Kit index object, use [`SKIndexCreateWithURL(_:_:_:_:)`](1446111-skindexcreatewithurl.md). To create a memory-based index, use [`SKIndexCreateWithMutableData(_:_:_:_:)`](1447500-skindexcreatewithmutabledata.md). For other operations on indexes, see [`Creating, Opening, and Closing Indexes`](search_kit#1654608.md) and [`Managing Indexes`](search_kit#1654733.md). Also see[`Fast Asynchronous Searching`](search_kit#1655469.md).

##### 1681550

You cannot use [`CFMakeCollectable`](https://developer.apple.com/documentation/corefoundation/1521163-cfmakecollectable) with SKIndex objects. In a garbage-collected environment, you must use [`SKIndexClose(_:)`](1442401-skindexclose.md) to dispose of an SKIndex object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/skindex)*