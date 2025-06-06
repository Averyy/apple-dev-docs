# SKIndexAddDocument(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Adds location information for a file-based document, and the document’s textual content, to an index.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SKIndexAddDocument(_ inIndex: SKIndex!, _ inDocument: SKDocument!, _ inMIMETypeHint: CFString!, _ inCanReplace: Bool) -> Bool
```

#### Return_value

A Boolean value of `true` on success, or `false` on failure. Also returns `false` if the document has an entry in the index and `inCanReplace` is set to `false`.

#### Discussion

 The document scheme must be of type “`file`” to use this function. If it’s not, call [`SKIndexAddDocumentWithText(_:_:_:_:)`](1444518-skindexadddocumentwithtext.md) instead. For more information on schemes, see [`http://www.iana.org/assignments/uri-schemes.html`](https://developer.apple.comhttp://www.iana.org/assignments/uri-schemes.html).

This function uses the referenced document and the optional MIME type hint to get the document’s textual content using the Spotlight metadata importers. If you do not supply a MIME type hint, Spotlight’s importers will use filename extensions and type/creator codes to guess file types.

Search Kit indexes any nonexecutable file associated with a document URL object (of type [`SKDocument`](skdocument.md)) that you hand to this function, even nontext files such as images. Your application takes responsibility for ensuring that the document URL objects you pass to `SKIndexAddDocument` are in fact the locations of files you want to index.

If your application did not call [`SKLoadDefaultExtractorPlugIns()`](1447859-skloaddefaultextractorplugins.md), Search Kit indexes the first 10 MB of a document. Otherwise, Search Kit indexes the entire document up to the index file size limit of 4 GB.

Search Kit is thread-safe. You can use separate indexing and searching threads. Your application is responsible for ensuring that no more than one process is open at a time for writing to an index.

A single Search Kit index can hold up to 4 billion document URL objects and their associated textual content.

##### 1817190

In the current implementation of Search Kit, some functions do not provide expected results unless you follow `SKIndexAddDocument` with a call to [`SKIndexFlush(_:)`](1450667-skindexflush.md). The affected functions include [`SKIndexGetDocumentCount(_:)`](1449093-skindexgetdocumentcount.md), [`SKIndexGetDocumentTermCount(_:_:)`](1448341-skindexgetdocumenttermcount.md), [`SKIndexGetDocumentTermFrequency(_:_:_:)`](1447537-skindexgetdocumenttermfrequency.md), and [`SKIndexGetTermDocumentCount(_:_:)`](1444015-skindexgettermdocumentcount.md). However, in typical use this won’t be an issue, because applications call these functions after a search, and you must call `SKIndexFlush` before a search.

## Parameters

- `inIndex`: The index to which you are adding the document URL object ( ).
- `inDocument`: The document URL object (of type  ) , containing a file-based document’s location information, to add to the index. You can release the document URL object immediately after adding it to the index.
- `inMIMETypeHint`: Specify a MIME type hint to help Spotlight determine which of its metadata importers to use when Search Kit is indexing a file-based document. Search Kit uses filename extensions and type/creator codes in attempting to determine file types when indexing files. See  . You can circumvent Search Kit’s file type determination process, or override it, by using a MIME type hint.
- `inCanReplace`: A Boolean value specifying whether Search Kit will overwrite a document’s index entry ( , indicated by   or  ), or retain the entry if it exists ( , indicated by   or  ).

## See Also

- [func SKIndexAddDocumentWithText(SKIndex!, SKDocument!, CFString!, Bool) -> Bool](1444518-skindexadddocumentwithtext.md)
  Adds a document URL ([`SKDocument`](skdocument.md)) object, and the associated document’s textual content, to an index.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444897-skindexadddocument)*