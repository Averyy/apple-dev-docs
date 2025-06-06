# SKIndexCompact(_:)

**Framework**: Core Services  
**Kind**: func

Invokes all pending updates associated with an index, compacts the index if compaction is needed, and commits all changes to backing store.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SKIndexCompact(_ inIndex: SKIndex!) -> Bool
```

#### Return_value

A Boolean value of `true` on success, or `false` on failure.

#### Discussion

Over time, as document URL objects (of type [`SKDocument`](skdocument.md)) and associated contents get added to and removed from an index, the index’s disk or memory footprint may grow due to fragmentation.

Compacting can take a significant amount of time. Do not call [`SKIndexCompact(_:)`](1443628-skindexcompact.md) on the main thread in an application with a user interface. Call it only if the index is significantly fragmented and according to the needs of your application.

Calling [`SKIndexCompact(_:)`](1443628-skindexcompact.md) changes the block allocation for an index’s backing store. Close all clients of an index before calling this function.

## Parameters

- `inIndex`: The index you want to compact.

## See Also

- [func SKIndexAddDocumentWithText(SKIndex!, SKDocument!, CFString!, Bool) -> Bool](1444518-skindexadddocumentwithtext.md)
  Adds a document URL ([`SKDocument`](skdocument.md)) object, and the associated document’s textual content, to an index.
- [func SKIndexAddDocument(SKIndex!, SKDocument!, CFString!, Bool) -> Bool](1444897-skindexadddocument.md)
  Adds location information for a file-based document, and the document’s textual content, to an index.
- [func SKIndexFlush(SKIndex!) -> Bool](1450667-skindexflush.md)
  Invokes all pending updates associated with an index and commits them to backing store.
- [func SKIndexGetDocumentCount(SKIndex!) -> CFIndex](1449093-skindexgetdocumentcount.md)
  Gets the total number of documents represented in an index.
- [func SKIndexGetMaximumDocumentID(SKIndex!) -> SKDocumentID](1444628-skindexgetmaximumdocumentid.md)
  Gets the highest-numbered document ID in an index.
- [func SKIndexGetMaximumTermID(SKIndex!) -> CFIndex](1444278-skindexgetmaximumtermid.md)
  Gets the highest-numbered term ID in an index.
- [func SKIndexDocumentIteratorCreate(SKIndex!, SKDocument!) -> Unmanaged<SKIndexDocumentIterator>!](1446189-skindexdocumentiteratorcreate.md)
  Creates an index-based iterator for document URL objects (of type [`SKDocument`](skdocument.md)) owned by a parent document URL object.
- [func SKIndexDocumentIteratorCopyNext(SKIndexDocumentIterator!) -> Unmanaged<SKDocument>!](1442212-skindexdocumentiteratorcopynext.md)
  Obtains the next document URL object (of type [`SKDocument`](skdocument.md)) from an index using a document iterator.
- [func SKIndexDocumentIteratorGetTypeID() -> CFTypeID](1443022-skindexdocumentiteratorgettypeid.md)
  Gets the type identifier for Search Kit document iterators.
- [func SKIndexGetAnalysisProperties(SKIndex!) -> Unmanaged<CFDictionary>!](1443461-skindexgetanalysisproperties.md)
  Gets the text analysis properties of an index.
- [func SKIndexMoveDocument(SKIndex!, SKDocument!, SKDocument!) -> Bool](1449899-skindexmovedocument.md)
  Changes the parent of a document URL object (of type [`SKDocument`](skdocument.md)) in an index.
- [func SKIndexRemoveDocument(SKIndex!, SKDocument!) -> Bool](1444375-skindexremovedocument.md)
  Removes a document URL object (of type [`SKDocument`](skdocument.md)) and its children, if any, from an index.
- [func SKIndexRenameDocument(SKIndex!, SKDocument!, CFString!) -> Bool](1448935-skindexrenamedocument.md)
  Changes the name of a document URL object (of type [`SKDocument`](skdocument.md)) in an index.
- [func SKIndexSetMaximumBytesBeforeFlush(SKIndex!, CFIndex)](1448696-skindexsetmaximumbytesbeforeflus.md)
  Not recommended. Sets the memory size limit for updates to an index, measured in bytes. 
- [func SKIndexGetMaximumBytesBeforeFlush(SKIndex!) -> CFIndex](1445329-skindexgetmaximumbytesbeforeflus.md)
  Not recommended. Gets the memory size limit for updates to an index, measured in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1443628-skindexcompact)*