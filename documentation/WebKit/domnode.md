# DOMNode

**Framework**: WebKit  
**Kind**: class  
**Role**: Class

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```swift
class DOMNode
```

```objc
@interface DOMNode : DOMObject
```

## Topics

### Instance Properties
- [var attributes: DOMNamedNodeMap!](./domnode/attributes.md)
- [var baseURI: String!](./domnode/baseuri.md)
- [var childNodes: DOMNodeList!](./domnode/childnodes.md)
- [var firstChild: DOMNode!](./domnode/firstchild.md)
- [var isContentEditable: Bool](./domnode/iscontenteditable.md)
- [var lastChild: DOMNode!](./domnode/lastchild.md)
- [var localName: String!](./domnode/localname.md)
- [var namespaceURI: String!](./domnode/namespaceuri.md)
- [var nextSibling: DOMNode!](./domnode/nextsibling.md)
- [var nodeName: String!](./domnode/nodename.md)
- [var nodeType: UInt16](./domnode/nodetype.md)
- [var nodeValue: String!](./domnode/nodevalue.md)
- [var ownerDocument: DOMDocument!](./domnode/ownerdocument.md)
- [var parent: DOMNode!](./domnode/parent.md)
- [var parentElement: DOMElement!](./domnode/parentelement.md)
- [var prefix: String!](./domnode/prefix.md)
- [var previousSibling: DOMNode!](./domnode/previoussibling.md)
- [var textContent: String!](./domnode/textcontent.md)
- [var webArchive: WebArchive!](./domnode/webarchive.md)
  A web archive of the content of the node and its children.
### Instance Methods
- [func appendChild(DOMNode!) -> DOMNode!](./domnode/appendchild%28_%29.md)
- [func boundingBox() -> NSRect](./domnode/boundingbox%28%29.md)
  Returns a rectangle that bounds the onscreen rendering of the node.
- [func cloneNode(Bool) -> DOMNode!](./domnode/clonenode%28_%29.md)
- [func compareDocumentPosition(DOMNode!) -> UInt16](./domnode/comparedocumentposition%28_%29.md)
- [func contains(DOMNode!) -> Bool](./domnode/contains%28_%29.md)
- [func hasAttributes() -> Bool](./domnode/hasattributes%28%29.md)
- [func hasChildNodes() -> Bool](./domnode/haschildnodes%28%29.md)
- [func insert(before: DOMNode!, refChild: DOMNode!) -> DOMNode!](./domnode/insert%28before,refchild%29.md)
- [func isDefaultNamespace(String!) -> Bool](./domnode/isdefaultnamespace%28_%29.md)
- [func isEqualNode(DOMNode!) -> Bool](./domnode/isequalnode%28_%29.md)
- [func isSameNode(DOMNode!) -> Bool](./domnode/issamenode%28_%29.md)
- [func isSupported(String!, version: String!) -> Bool](./domnode/issupported%28_,version%29.md)
- [func lineBoxRects() -> [Any]!](./domnode/lineboxrects%28%29.md)
  Returns the rectangles that bound each line of text in the node.
- [func lookupNamespaceURI(String!) -> String!](./domnode/lookupnamespaceuri%28_%29.md)
- [func lookupPrefix(String!) -> String!](./domnode/lookupprefix%28_%29.md)
- [func normalize()](./domnode/normalize%28%29.md)
- [func removeChild(DOMNode!) -> DOMNode!](./domnode/removechild%28_%29.md)
- [func replaceChild(DOMNode!, oldChild: DOMNode!) -> DOMNode!](./domnode/replacechild%28_,oldchild%29.md)
- [- insertBefore::](./domnode/insertbefore__.md)
- [- isSupported::](./domnode/issupported__.md)
- [- replaceChild::](./domnode/replacechild__.md)

## Relationships

### Inherits From
- [DOMObject](./domobject.md)
### Inherited By
- [DOMAttr](./domattr.md)
- [DOMCharacterData](./domcharacterdata.md)
- [DOMDocument](./domdocument.md)
- [DOMDocumentFragment](./domdocumentfragment.md)
- [DOMDocumentType](./domdocumenttype.md)
- [DOMElement](./domelement.md)
- [DOMEntity](./domentity.md)
- [DOMEntityReference](./domentityreference.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [DOMEventTarget](./domeventtarget.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/domnode)*