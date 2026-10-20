# SKIndex

**Framework**: Core Services  
**Kind**: cl  
**Role**: Class

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

To create a new disk-based Search Kit index object, use [`SKIndexCreateWithURL(_:_:_:_:)`](./api-1446111-skindexcreatewithurl.md). To create a memory-based index, use [`SKIndexCreateWithMutableData(_:_:_:_:)`](./api-1447500-skindexcreatewithmutabledata.md). For other operations on indexes, see [Creating, Opening, and Closing Indexes](./search_kit.md#1654608) and [Managing Indexes](./search_kit.md#1654733). Also see[Fast Asynchronous Searching](./search_kit.md#1655469).

##### Special Considerations

You cannot use [`CFMakeCollectable`](../CoreFoundation/cfmakecollectable.md) with SKIndex objects. In a garbage-collected environment, you must use [`SKIndexClose(_:)`](./api-1442401-skindexclose.md) to dispose of an SKIndex object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/skindex)*