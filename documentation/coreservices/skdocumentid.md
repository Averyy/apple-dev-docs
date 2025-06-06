# SKDocumentID

**Framework**: Core Services  
**Kind**: tdef

Defines an opaque data type representing a lightweight document identifier.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```swift
typealias SKDocumentID = CFIndex
```

#### Discussion

Use document IDs rather than document URL objects (SKDocumentRefs) whenever possible. Using document IDs results in faster searching.

You can work with document IDs using a variety of Search Kit functions. See [`SKIndexGetMaximumDocumentID(_:)`](1444628-skindexgetmaximumdocumentid.md), [`SKIndexCopyDocumentForDocumentID(_:_:)`](1442760-skindexcopydocumentfordocumentid.md), [`SKIndexCopyInfoForDocumentIDs(_:_:_:_:_:)`](1445499-skindexcopyinfofordocumentids.md), [`SKIndexCopyDocumentRefsForDocumentIDs(_:_:_:_:)`](1445305-skindexcopydocumentrefsfordocume.md), [`SKIndexCopyDocumentURLsForDocumentIDs(_:_:_:_:)`](1443501-skindexcopydocumenturlsfordocume.md), [`SKIndexCopyDocumentIDArrayForTermID(_:_:)`](1448003-skindexcopydocumentidarrayforter.md), and [`SKIndexCopyTermIDArrayForDocumentID(_:_:)`](1446868-skindexcopytermidarrayfordocumen.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/skdocumentid)*