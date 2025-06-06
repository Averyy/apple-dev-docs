# SKIndexAddDocumentWithText(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Adds a document URL ([`SKDocument`](skdocument.md)) object, and the associated document’s textual content, to an index.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SKIndexAddDocumentWithText(_ inIndex: SKIndex!, _ inDocument: SKDocument!, _ inDocumentText: CFString!, _ inCanReplace: Bool) -> Bool
```

#### Return_value

A Boolean value of `true` on success, or `false` on failure. Also returns `false` if the document has an entry in the index and `inCanReplace` is set to `false`.

#### Discussion

Use this function to add the textual contents of arbitrary document types to an index. With this function, your application takes responsibility for getting textual content and handing it to the index as A [`CFString`](https://developer.apple.com/documentation/corefoundation/cfstring) object. Because of this, your application can define what it considers to be a document—a database record, a tagged field in an XML document, an object in memory, a text file, and so on.

Search Kit will index any size text string that you give it, up to its 4 GB index file size limit.

To add the textual content of file-based documents to a Search Kit index, you can use this function or take advantage of Search Kit’s ability to locate and read certain on-disk, file-based document types—see [`SKIndexAddDocument(_:_:_:_:)`](1444897-skindexadddocument.md).

Search Kit is thread-safe. You can use separate indexing and searching threads. Your application is responsible for ensuring that no more than one process is open at a time for writing to an index.

A single Search Kit index file can be up to 4 GB in size.

##### 1680744

In OS X v10.3, some functions do not provide expected results unless you follow a call to `SKIndexAddDocumentWithText` with a call to [`SKIndexFlush(_:)`](1450667-skindexflush.md). The affected functions include [`SKIndexGetDocumentCount(_:)`](1449093-skindexgetdocumentcount.md), [`SKIndexGetDocumentTermCount(_:_:)`](1448341-skindexgetdocumenttermcount.md), [`SKIndexGetDocumentTermFrequency(_:_:_:)`](1447537-skindexgetdocumenttermfrequency.md), and [`SKIndexGetTermDocumentCount(_:_:)`](1444015-skindexgettermdocumentcount.md). However, in typical use this won’t be an issue, because applications call these functions after a search, and you must call `SKIndexFlush` before a search.

## Parameters

- `inIndex`: The index to which you are adding the document URL object ( ) .
- `inDocument`: The document URL ( ) object to add.
- `inDocumentText`: The document text. Can be  .
- `inCanReplace`: A Boolean value specifying whether Search Kit will overwrite a document’s index entry ( , indicated by   or  ), or retain the entry if it exists ( , indicated by   or  ).

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444518-skindexadddocumentwithtext)*