# SKDocument

**Framework**: Core Services  
**Kind**: tdef

Defines an opaque data type representing a document’s URL.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```swift
typealias SKDocument = CFTypeRef
```

#### Discussion

A document URL object is a generic location specification for a document. It is built from a document scheme, a parent document, and a document name. You can convert back and forth between document URL objects and `CFURL` objects using Search Kit’s [`SKDocumentCreateWithURL(_:)`](1442564-skdocumentcreatewithurl.md) and [`SKDocumentCopyURL(_:)`](1449624-skdocumentcopyurl.md) functions.

To create a Search Kit document URL object, use [`SKDocumentCreateWithURL(_:)`](1442564-skdocumentcreatewithurl.md) when you can provide a complete URL, or use [`SKDocumentCreate(_:_:_:)`](1443212-skdocumentcreate.md) when you want to specify document location indirectly using a parent document URL object. For other operations on documents, see [`Working with Documents and Terms`](search_kit#1655072.md).

If you create document URL objects with indirect locations using the [`SKDocumentCreate(_:_:_:)`](1443212-skdocumentcreate.md) function, you can resolve the locations by assembling them piece by piece, starting with a document URL object and going up step by step, parent to parent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/skdocument)*