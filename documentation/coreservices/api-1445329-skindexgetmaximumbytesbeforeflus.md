# SKIndexGetMaximumBytesBeforeFlush(_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Not recommended. Gets the memory size limit for updates to an index, measured in bytes.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SKIndexGetMaximumBytesBeforeFlush(_ inIndex: SKIndex!) -> CFIndex
```

```c
CFIndex SKIndexGetMaximumBytesBeforeFlush(SKIndexRef inIndex);
```

#### Discussion

This function is rarely needed and is likely to be deprecated. Apple recommends using the [`SKIndexFlush(_:)`](./api-1450667-skindexflush.md) function along with the default memory size limit for index updates. Refer to the [`SKIndexSetMaximumBytesBeforeFlush(_:_:)`](./api-1448696-skindexsetmaximumbytesbeforeflus.md) function for more information.

## See Also

### Managing Indexes
- [func SKIndexAddDocumentWithText(SKIndex!, SKDocument!, CFString!, Bool) -> Bool](./api-1444518-skindexadddocumentwithtext.md)
  Adds a document URL ([`SKDocument`](./skdocument.md)) object, and the associated document’s textual content, to an index.
- [func SKIndexAddDocument(SKIndex!, SKDocument!, CFString!, Bool) -> Bool](./api-1444897-skindexadddocument.md)
  Adds location information for a file-based document, and the document’s textual content, to an index.
- [func SKIndexFlush(SKIndex!) -> Bool](./api-1450667-skindexflush.md)
  Invokes all pending updates associated with an index and commits them to backing store.
- [func SKIndexCompact(SKIndex!) -> Bool](./api-1443628-skindexcompact.md)
  Invokes all pending updates associated with an index, compacts the index if compaction is needed, and commits all changes to backing store.
- [func SKIndexGetDocumentCount(SKIndex!) -> CFIndex](./api-1449093-skindexgetdocumentcount.md)
  Gets the total number of documents represented in an index.
- [func SKIndexGetMaximumDocumentID(SKIndex!) -> SKDocumentID](./api-1444628-skindexgetmaximumdocumentid.md)
  Gets the highest-numbered document ID in an index.
- [func SKIndexGetMaximumTermID(SKIndex!) -> CFIndex](./api-1444278-skindexgetmaximumtermid.md)
  Gets the highest-numbered term ID in an index.
- [func SKIndexDocumentIteratorCreate(SKIndex!, SKDocument!) -> Unmanaged<SKIndexDocumentIterator>!](./api-1446189-skindexdocumentiteratorcreate.md)
  Creates an index-based iterator for document URL objects (of type [`SKDocument`](./skdocument.md)) owned by a parent document URL object.
- [func SKIndexDocumentIteratorCopyNext(SKIndexDocumentIterator!) -> Unmanaged<SKDocument>!](./api-1442212-skindexdocumentiteratorcopynext.md)
  Obtains the next document URL object (of type [`SKDocument`](./skdocument.md)) from an index using a document iterator.
- [func SKIndexDocumentIteratorGetTypeID() -> CFTypeID](./api-1443022-skindexdocumentiteratorgettypeid.md)
  Gets the type identifier for Search Kit document iterators.
- [func SKIndexGetAnalysisProperties(SKIndex!) -> Unmanaged<CFDictionary>!](./api-1443461-skindexgetanalysisproperties.md)
  Gets the text analysis properties of an index.
- [func SKIndexMoveDocument(SKIndex!, SKDocument!, SKDocument!) -> Bool](./api-1449899-skindexmovedocument.md)
  Changes the parent of a document URL object (of type [`SKDocument`](./skdocument.md)) in an index.
- [func SKIndexRemoveDocument(SKIndex!, SKDocument!) -> Bool](./api-1444375-skindexremovedocument.md)
  Removes a document URL object (of type [`SKDocument`](./skdocument.md)) and its children, if any, from an index.
- [func SKIndexRenameDocument(SKIndex!, SKDocument!, CFString!) -> Bool](./api-1448935-skindexrenamedocument.md)
  Changes the name of a document URL object (of type [`SKDocument`](./skdocument.md)) in an index.
- [func SKIndexSetMaximumBytesBeforeFlush(SKIndex!, CFIndex)](./api-1448696-skindexsetmaximumbytesbeforeflus.md)
  Not recommended. Sets the memory size limit for updates to an index, measured in bytes. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1445329-skindexgetmaximumbytesbeforeflus)*