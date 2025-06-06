# SKIndexDocumentIteratorGetTypeID()

**Framework**: Core Services  
**Kind**: func

Gets the type identifier for Search Kit document iterators.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SKIndexDocumentIteratorGetTypeID() -> CFTypeID
```

#### Return_value

A CFTypeID object containing the type identifier for the SKIndexDocumentIterator opaque type.

#### Discussion

Search Kit represents document iterators with the [`SKIndexDocumentIterator`](skindexdocumentiterator.md) opaque type. If your code needs to determine whether a particular data type is a document iterator, you can use this function along with the [`CFGetTypeID(_:)`](https://developer.apple.com/documentation/corefoundation/cfgettypeid(_:)) function and perform a comparison.

Search Kit is thread-safe. You can use separate indexing and searching threads. Your application is responsible for ensuring that no more than one process is open at a time for writing to an index.

Never hard-code the document iterator type ID because it can change from one release of macOS to another.

## See Also

- [func SKIndexAddDocumentWithText(SKIndex!, SKDocument!, CFString!, Bool) -> Bool](1444518-skindexadddocumentwithtext.md)
  Adds a document URL ([`SKDocument`](skdocument.md)) object, and the associated document’s textual content, to an index.
- [func SKIndexAddDocument(SKIndex!, SKDocument!, CFString!, Bool) -> Bool](1444897-skindexadddocument.md)
  Adds location information for a file-based document, and the document’s textual content, to an index.
- [func SKIndexFlush(SKIndex!) -> Bool](1450667-skindexflush.md)
  Invokes all pending updates associated with an index and commits them to backing store.
- [func SKIndexCompact(SKIndex!) -> Bool](1443628-skindexcompact.md)
  Invokes all pending updates associated with an index, compacts the index if compaction is needed, and commits all changes to backing store.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1443022-skindexdocumentiteratorgettypeid)*