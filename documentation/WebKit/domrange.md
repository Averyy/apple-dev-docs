# DOMRange

**Framework**: WebKit  
**Kind**: class  
**Role**: Class

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```swift
class DOMRange
```

```objc
@interface DOMRange : DOMObject
```

## Topics

### Instance Properties
- [var collapsed: Bool](./domrange/collapsed.md)
- [var commonAncestorContainer: DOMNode!](./domrange/commonancestorcontainer.md)
- [var endContainer: DOMNode!](./domrange/endcontainer.md)
- [var endOffset: Int32](./domrange/endoffset.md)
- [var markupString: String!](./domrange/markupstring.md)
  A string in markup format corresponding to the content in the range.
- [var startContainer: DOMNode!](./domrange/startcontainer.md)
- [var startOffset: Int32](./domrange/startoffset.md)
- [var text: String!](./domrange/text.md)
- [var webArchive: WebArchive!](./domrange/webarchive.md)
  A web archive of the content in the range.
### Instance Methods
- [func clone() -> DOMRange!](./domrange/clone%28%29.md)
- [func cloneContents() -> DOMDocumentFragment!](./domrange/clonecontents%28%29.md)
- [func collapse(Bool)](./domrange/collapse%28_%29.md)
- [func compare(DOMNode!) -> Int16](./domrange/compare%28_%29.md)
- [func compareBoundaryPoints(UInt16, sourceRange: DOMRange!) -> Int16](./domrange/compareboundarypoints%28_,sourcerange%29.md)
- [func comparePoint(DOMNode!, offset: Int32) -> Int16](./domrange/comparepoint%28_,offset%29.md)
- [func createContextualFragment(String!) -> DOMDocumentFragment!](./domrange/createcontextualfragment%28_%29.md)
- [func deleteContents()](./domrange/deletecontents%28%29.md)
- [func detach()](./domrange/detach%28%29.md)
- [func extractContents() -> DOMDocumentFragment!](./domrange/extractcontents%28%29.md)
- [func insert(DOMNode!)](./domrange/insert%28_%29.md)
- [func intersects(DOMNode!) -> Bool](./domrange/intersects%28_%29.md)
- [func isPoint(inRange: DOMNode!, offset: Int32) -> Bool](./domrange/ispoint%28inrange,offset%29.md)
- [func select(DOMNode!)](./domrange/select%28_%29.md)
- [func selectNodeContents(DOMNode!)](./domrange/selectnodecontents%28_%29.md)
- [func setEnd(DOMNode!, offset: Int32)](./domrange/setend%28_,offset%29.md)
- [func setEndAfter(DOMNode!)](./domrange/setendafter%28_%29.md)
- [func setEndBefore(DOMNode!)](./domrange/setendbefore%28_%29.md)
- [func setStart(DOMNode!, offset: Int32)](./domrange/setstart%28_,offset%29.md)
- [func setStartAfter(DOMNode!)](./domrange/setstartafter%28_%29.md)
- [func setStartBefore(DOMNode!)](./domrange/setstartbefore%28_%29.md)
- [func surroundContents(DOMNode!)](./domrange/surroundcontents%28_%29.md)
- [func toString() -> String!](./domrange/tostring%28%29.md)
- [- compareBoundaryPoints::](./domrange/compareboundarypoints__.md)
- [- setEnd::](./domrange/setend__.md)
- [- setStart::](./domrange/setstart__.md)

## Relationships

### Inherits From
- [DOMObject](./domobject.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Document Object Model (DOM) APIs
- [class DOMAbstractView](./domabstractview.md)
- [class DOMAttr](./domattr.md)
- [class DOMBlob](./domblob.md)
- [class DOMCDATASection](./domcdatasection.md)
- [class DOMCharacterData](./domcharacterdata.md)
- [class DOMComment](./domcomment.md)
- [class DOMCounter](./domcounter.md)
- [class DOMCSSCharsetRule](./domcsscharsetrule.md)
- [class DOMCSSFontFaceRule](./domcssfontfacerule.md)
- [class DOMCSSImportRule](./domcssimportrule.md)
- [class DOMCSSMediaRule](./domcssmediarule.md)
- [class DOMCSSPageRule](./domcsspagerule.md)
- [class DOMCSSPrimitiveValue](./domcssprimitivevalue.md)
- [class DOMCSSRule](./domcssrule.md)
- [class DOMCSSRuleList](./domcssrulelist.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/domrange)*