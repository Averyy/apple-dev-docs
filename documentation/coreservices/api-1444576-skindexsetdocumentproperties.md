# SKIndexSetDocumentProperties(_:_:_:)

**Framework**: Core Services  
**Kind**: func

Sets the application-defined properties of a document URL object (of type [`SKDocument`](skdocument.md)).

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SKIndexSetDocumentProperties(_ inIndex: SKIndex!, _ inDocument: SKDocument!, _ inProperties: CFDictionary!)
```

#### Discussion

Search Kit document URL objects (of type [`SKDocument`](skdocument.md)) can have an optional, application-defined properties dictionary to hold any information you’d like to associate with the document represented by a document URL object—such as timestamp, keywords, and so on.

Use `SKIndexSetDocumentProperties` to persistently set application-defined properties for a document URL object in an index. This function replaces a document URL object’s existing properties dictionary with the new one. To obtain a copy of a document URL object’s properties dictionary, use [`SKIndexCopyDocumentProperties(_:_:)`](1449500-skindexcopydocumentproperties.md).

##### 1681176

You must set any desired properties on a document URL object  adding the document URL object to an index. Adding a document URL object to an index clears the object’s preexisting properties.

## Parameters

- `inIndex`: An index containing the document URL object whose properties you want to set.
- `inDocument`: The document URL object whose properties you want to set.
- `inProperties`: A CFDictionary object containing the properties to apply to the document URL object.

## See Also

- [func SKDocumentCreateWithURL(CFURL!) -> Unmanaged<SKDocument>!](1442564-skdocumentcreatewithurl.md)
  Creates a document URL object (of type [`SKDocument`](skdocument.md)) from a [`CFURL`](https://developer.apple.com/documentation/corefoundation/cfurl) object.
- [func SKDocumentCreate(CFString!, SKDocument!, CFString!) -> Unmanaged<SKDocument>!](1443212-skdocumentcreate.md)
  Creates a document URL object (of type [`SKDocument`](skdocument.md)) based on a scheme, parent, and name.
- [func SKDocumentCopyURL(SKDocument!) -> Unmanaged<CFURL>!](1449624-skdocumentcopyurl.md)
  Builds a [`CFURL`](https://developer.apple.com/documentation/corefoundation/cfurl) object from a document URL object (of type [`SKDocument`](skdocument.md)).
- [func SKDocumentGetName(SKDocument!) -> Unmanaged<CFString>!](1442657-skdocumentgetname.md)
  Gets the name of a document URL object (of type [`SKDocument`](skdocument.md)).
- [func SKDocumentGetParent(SKDocument!) -> Unmanaged<SKDocument>!](1444449-skdocumentgetparent.md)
  Gets the parent of a document URL object (of type [`SKDocument`](skdocument.md)).
- [func SKDocumentGetSchemeName(SKDocument!) -> Unmanaged<CFString>!](1448262-skdocumentgetschemename.md)
  Gets the scheme name for a document URL object (of type [`SKDocument`](skdocument.md)).
- [func SKDocumentGetTypeID() -> CFTypeID](1448891-skdocumentgettypeid.md)
  Gets the type identifier for Search Kit document URL objects.
- [func SKIndexCopyDocumentForDocumentID(SKIndex!, SKDocumentID) -> Unmanaged<SKDocument>!](1442760-skindexcopydocumentfordocumentid.md)
  Obtains a document URL object (of type [`SKDocument`](skdocument.md)) from an index.
- [func SKIndexCopyInfoForDocumentIDs(SKIndex!, CFIndex, UnsafeMutablePointer<SKDocumentID>!, UnsafeMutablePointer<Unmanaged<CFString>?>!, UnsafeMutablePointer<SKDocumentID>!)](1445499-skindexcopyinfofordocumentids.md)
  Gets document names and parent IDs based on document IDs.
- [func SKIndexCopyDocumentRefsForDocumentIDs(SKIndex!, CFIndex, UnsafeMutablePointer<SKDocumentID>!, UnsafeMutablePointer<Unmanaged<SKDocument>?>!)](1445305-skindexcopydocumentrefsfordocume.md)
  Gets document URL objects (of type [`SKDocument`](skdocument.md)) based on document IDs.
- [func SKIndexCopyDocumentURLsForDocumentIDs(SKIndex!, CFIndex, UnsafeMutablePointer<SKDocumentID>!, UnsafeMutablePointer<Unmanaged<CFURL>?>!)](1443501-skindexcopydocumenturlsfordocume.md)
  Gets document URLs based on document IDs.
- [func SKIndexCopyDocumentIDArrayForTermID(SKIndex!, CFIndex) -> Unmanaged<CFArray>!](1448003-skindexcopydocumentidarrayforter.md)
  Obtains document IDs for documents that contain a given term.
- [func SKIndexCopyTermIDArrayForDocumentID(SKIndex!, SKDocumentID) -> Unmanaged<CFArray>!](1446868-skindexcopytermidarrayfordocumen.md)
  Obtains the IDs for the terms of an indexed document.
- [func SKIndexCopyTermStringForTermID(SKIndex!, CFIndex) -> Unmanaged<CFString>!](1442802-skindexcopytermstringfortermid.md)
  Obtains a term, specified by ID, from an index.
- [func SKIndexGetTermIDForTermString(SKIndex!, CFString!) -> CFIndex](1448558-skindexgettermidfortermstring.md)
  Gets the ID for a term in an index.
- [func SKIndexCopyDocumentProperties(SKIndex!, SKDocument!) -> Unmanaged<CFDictionary>!](1449500-skindexcopydocumentproperties.md)
  Obtains the application-defined properties of an indexed document.
- [func SKIndexGetDocumentState(SKIndex!, SKDocument!) -> SKDocumentIndexState](1443396-skindexgetdocumentstate.md)
  Gets the current indexing state of a document URL object (of type [`SKDocument`](skdocument.md)) in an index.
- [func SKIndexGetDocumentTermCount(SKIndex!, SKDocumentID) -> CFIndex](1448341-skindexgetdocumenttermcount.md)
  Gets the number of terms for a document in an index.
- [func SKIndexGetDocumentTermFrequency(SKIndex!, SKDocumentID, CFIndex) -> CFIndex](1447537-skindexgetdocumenttermfrequency.md)
  Gets the number of occurrences of a term in a document.
- [func SKIndexGetTermDocumentCount(SKIndex!, CFIndex) -> CFIndex](1444015-skindexgettermdocumentcount.md)
  Gets the number of documents containing a given term represented in an index.
- [func SKIndexGetDocumentID(SKIndex!, SKDocument!) -> SKDocumentID](1444437-skindexgetdocumentid.md)
  Gets the ID of a document URL object (of type [`SKDocument`](skdocument.md)) in an index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444576-skindexsetdocumentproperties)*