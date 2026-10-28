# SKIndexCopyDocumentURLsForDocumentIDs(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Gets document URLs based on document IDs.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SKIndexCopyDocumentURLsForDocumentIDs(_ inIndex: SKIndex!, _ inCount: CFIndex, _ inDocumentIDsArray: UnsafeMutablePointer<SKDocumentID>!, _ outDocumentURLsArray: UnsafeMutablePointer<Unmanaged<CFURL>?>!)
```

```c
void SKIndexCopyDocumentURLsForDocumentIDs(SKIndexRef inIndex, CFIndex inCount, SKDocumentID *inDocumentIDsArray, CFURLRef *outDocumentURLsArray);
```

## Discussion

The [`SKIndexCopyDocumentURLsForDocumentIDs(_:_:_:_:)`](./api-1443501-skindexcopydocumenturlsfordocume.md) function lets you get a batch of document URLs (CFURL objects) in one step, based on a list of document IDs.

If you want to get Search Kit Document URL objects (SKDocumentRefs) instead, use [`SKIndexCopyDocumentRefsForDocumentIDs(_:_:_:_:)`](./api-1445305-skindexcopydocumentrefsfordocume.md).

## Parameters

- `inIndex`: The index containing the document information.
- `inCount`: The number of document IDs in `inDocumentIDsArray`.
- `inDocumentIDsArray`: Points to an array of document IDs corresponding to the document URLs (CFURL objects) you want.
- `outDocumentURLsArray`: On input, a pointer to an array for document URLs (CFURL objects). On output, points to the previously allocated array, which now contains document URLs corresponding to the document IDs in `inDocumentIDArray`.

  When finished with the document URL array, dispose of it by calling [`CFRelease`](../CoreFoundation/cfrelease.md) on each array element.

## See Also

### Working with Documents and Terms
- [func SKDocumentCreateWithURL(CFURL!) -> Unmanaged<SKDocument>!](./api-1442564-skdocumentcreatewithurl.md)
  Creates a document URL object (of type [`SKDocument`](./skdocument.md)) from a [`CFURL`](../CoreFoundation/cfurl.md) object.
- [func SKDocumentCreate(CFString!, SKDocument!, CFString!) -> Unmanaged<SKDocument>!](./api-1443212-skdocumentcreate.md)
  Creates a document URL object (of type [`SKDocument`](./skdocument.md)) based on a scheme, parent, and name.
- [func SKDocumentCopyURL(SKDocument!) -> Unmanaged<CFURL>!](./api-1449624-skdocumentcopyurl.md)
  Builds a [`CFURL`](../CoreFoundation/cfurl.md) object from a document URL object (of type [`SKDocument`](./skdocument.md)).
- [func SKDocumentGetName(SKDocument!) -> Unmanaged<CFString>!](./api-1442657-skdocumentgetname.md)
  Gets the name of a document URL object (of type [`SKDocument`](./skdocument.md)).
- [func SKDocumentGetParent(SKDocument!) -> Unmanaged<SKDocument>!](./api-1444449-skdocumentgetparent.md)
  Gets the parent of a document URL object (of type [`SKDocument`](./skdocument.md)).
- [func SKDocumentGetSchemeName(SKDocument!) -> Unmanaged<CFString>!](./api-1448262-skdocumentgetschemename.md)
  Gets the scheme name for a document URL object (of type [`SKDocument`](./skdocument.md)).
- [func SKDocumentGetTypeID() -> CFTypeID](./api-1448891-skdocumentgettypeid.md)
  Gets the type identifier for Search Kit document URL objects.
- [func SKIndexCopyDocumentForDocumentID(SKIndex!, SKDocumentID) -> Unmanaged<SKDocument>!](./api-1442760-skindexcopydocumentfordocumentid.md)
  Obtains a document URL object (of type [`SKDocument`](./skdocument.md)) from an index.
- [func SKIndexCopyInfoForDocumentIDs(SKIndex!, CFIndex, UnsafeMutablePointer<SKDocumentID>!, UnsafeMutablePointer<Unmanaged<CFString>?>!, UnsafeMutablePointer<SKDocumentID>!)](./api-1445499-skindexcopyinfofordocumentids.md)
  Gets document names and parent IDs based on document IDs.
- [func SKIndexCopyDocumentRefsForDocumentIDs(SKIndex!, CFIndex, UnsafeMutablePointer<SKDocumentID>!, UnsafeMutablePointer<Unmanaged<SKDocument>?>!)](./api-1445305-skindexcopydocumentrefsfordocume.md)
  Gets document URL objects (of type [`SKDocument`](./skdocument.md)) based on document IDs.
- [func SKIndexCopyDocumentIDArrayForTermID(SKIndex!, CFIndex) -> Unmanaged<CFArray>!](./api-1448003-skindexcopydocumentidarrayforter.md)
  Obtains document IDs for documents that contain a given term.
- [func SKIndexCopyTermIDArrayForDocumentID(SKIndex!, SKDocumentID) -> Unmanaged<CFArray>!](./api-1446868-skindexcopytermidarrayfordocumen.md)
  Obtains the IDs for the terms of an indexed document.
- [func SKIndexCopyTermStringForTermID(SKIndex!, CFIndex) -> Unmanaged<CFString>!](./api-1442802-skindexcopytermstringfortermid.md)
  Obtains a term, specified by ID, from an index.
- [func SKIndexGetTermIDForTermString(SKIndex!, CFString!) -> CFIndex](./api-1448558-skindexgettermidfortermstring.md)
  Gets the ID for a term in an index.
- [func SKIndexSetDocumentProperties(SKIndex!, SKDocument!, CFDictionary!)](./api-1444576-skindexsetdocumentproperties.md)
  Sets the application-defined properties of a document URL object (of type [`SKDocument`](./skdocument.md)).
- [func SKIndexCopyDocumentProperties(SKIndex!, SKDocument!) -> Unmanaged<CFDictionary>!](./api-1449500-skindexcopydocumentproperties.md)
  Obtains the application-defined properties of an indexed document.
- [func SKIndexGetDocumentState(SKIndex!, SKDocument!) -> SKDocumentIndexState](./api-1443396-skindexgetdocumentstate.md)
  Gets the current indexing state of a document URL object (of type [`SKDocument`](./skdocument.md)) in an index.
- [func SKIndexGetDocumentTermCount(SKIndex!, SKDocumentID) -> CFIndex](./api-1448341-skindexgetdocumenttermcount.md)
  Gets the number of terms for a document in an index.
- [func SKIndexGetDocumentTermFrequency(SKIndex!, SKDocumentID, CFIndex) -> CFIndex](./api-1447537-skindexgetdocumenttermfrequency.md)
  Gets the number of occurrences of a term in a document.
- [func SKIndexGetTermDocumentCount(SKIndex!, CFIndex) -> CFIndex](./api-1444015-skindexgettermdocumentcount.md)
  Gets the number of documents containing a given term represented in an index.
- [func SKIndexGetDocumentID(SKIndex!, SKDocument!) -> SKDocumentID](./api-1444437-skindexgetdocumentid.md)
  Gets the ID of a document URL object (of type [`SKDocument`](./skdocument.md)) in an index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1443501-skindexcopydocumenturlsfordocume)*