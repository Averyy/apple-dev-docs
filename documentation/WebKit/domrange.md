# DOMRange

**Framework**: WebKit  
**Kind**: class

**Availability**:
- macOS 10.4+

## Declaration

```swift
class DOMRange
```

## Topics

### Instance Properties
- [var collapsed: Bool](domrange/collapsed.md)
- [var commonAncestorContainer: DOMNode!](domrange/commonancestorcontainer.md)
- [var endContainer: DOMNode!](domrange/endcontainer.md)
- [var endOffset: Int32](domrange/endoffset.md)
- [var markupString: String!](domrange/markupstring.md)
  A string in markup format corresponding to the content in the range.
- [var startContainer: DOMNode!](domrange/startcontainer.md)
- [var startOffset: Int32](domrange/startoffset.md)
- [var text: String!](domrange/text.md)
- [var webArchive: WebArchive!](domrange/webarchive.md)
  A web archive of the content in the range.
### Instance Methods
- [func clone() -> DOMRange!](domrange/clone.md)
- [func cloneContents() -> DOMDocumentFragment!](domrange/clonecontents.md)
- [func collapse(Bool)](domrange/collapse(_:).md)
- [func compare(DOMNode!) -> Int16](domrange/compare(_:).md)
- [func compareBoundaryPoints(UInt16, sourceRange: DOMRange!) -> Int16](domrange/compareboundarypoints(_:sourcerange:).md)
- [func comparePoint(DOMNode!, offset: Int32) -> Int16](domrange/comparepoint(_:offset:).md)
- [func createContextualFragment(String!) -> DOMDocumentFragment!](domrange/createcontextualfragment(_:).md)
- [func deleteContents()](domrange/deletecontents.md)
- [func detach()](domrange/detach.md)
- [func extractContents() -> DOMDocumentFragment!](domrange/extractcontents.md)
- [func insert(DOMNode!)](domrange/insert(_:).md)
- [func intersects(DOMNode!) -> Bool](domrange/intersects(_:).md)
- [func isPoint(inRange: DOMNode!, offset: Int32) -> Bool](domrange/ispoint(inrange:offset:).md)
- [func select(DOMNode!)](domrange/select(_:).md)
- [func selectNodeContents(DOMNode!)](domrange/selectnodecontents(_:).md)
- [func setEnd(DOMNode!, offset: Int32)](domrange/setend(_:offset:).md)
- [func setEndAfter(DOMNode!)](domrange/setendafter(_:).md)
- [func setEndBefore(DOMNode!)](domrange/setendbefore(_:).md)
- [func setStart(DOMNode!, offset: Int32)](domrange/setstart(_:offset:).md)
- [func setStartAfter(DOMNode!)](domrange/setstartafter(_:).md)
- [func setStartBefore(DOMNode!)](domrange/setstartbefore(_:).md)
- [func surroundContents(DOMNode!)](domrange/surroundcontents(_:).md)
- [func toString() -> String!](domrange/tostring.md)

## Relationships

### Inherits From
- [DOMObject](domobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class DOMAbstractView](domabstractview.md)
- [class DOMAttr](domattr.md)
- [class DOMBlob](domblob.md)
- [class DOMCDATASection](domcdatasection.md)
- [class DOMCharacterData](domcharacterdata.md)
- [class DOMComment](domcomment.md)
- [class DOMCounter](domcounter.md)
- [class DOMCSSCharsetRule](domcsscharsetrule.md)
- [class DOMCSSFontFaceRule](domcssfontfacerule.md)
- [class DOMCSSImportRule](domcssimportrule.md)
- [class DOMCSSMediaRule](domcssmediarule.md)
- [class DOMCSSPageRule](domcsspagerule.md)
- [class DOMCSSPrimitiveValue](domcssprimitivevalue.md)
- [class DOMCSSRule](domcssrule.md)
- [class DOMCSSRuleList](domcssrulelist.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/domrange)*