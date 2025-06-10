# DOMNode

**Framework**: WebKit  
**Kind**: class

**Availability**:
- macOS 10.4+

## Declaration

```swift
class DOMNode
```

## Topics

### Instance Properties
- [var attributes: DOMNamedNodeMap!](domnode/attributes.md)
- [var baseURI: String!](domnode/baseuri.md)
- [var childNodes: DOMNodeList!](domnode/childnodes.md)
- [var firstChild: DOMNode!](domnode/firstchild.md)
- [var isContentEditable: Bool](domnode/iscontenteditable.md)
- [var lastChild: DOMNode!](domnode/lastchild.md)
- [var localName: String!](domnode/localname.md)
- [var namespaceURI: String!](domnode/namespaceuri.md)
- [var nextSibling: DOMNode!](domnode/nextsibling.md)
- [var nodeName: String!](domnode/nodename.md)
- [var nodeType: UInt16](domnode/nodetype.md)
- [var nodeValue: String!](domnode/nodevalue.md)
- [var ownerDocument: DOMDocument!](domnode/ownerdocument.md)
- [var parent: DOMNode!](domnode/parent.md)
- [var parentElement: DOMElement!](domnode/parentelement.md)
- [var prefix: String!](domnode/prefix.md)
- [var previousSibling: DOMNode!](domnode/previoussibling.md)
- [var textContent: String!](domnode/textcontent.md)
- [var webArchive: WebArchive!](domnode/webarchive.md)
  A web archive of the content of the node and its children.
### Instance Methods
- [func appendChild(DOMNode!) -> DOMNode!](domnode/appendchild(_:).md)
- [func boundingBox() -> NSRect](domnode/boundingbox.md)
  Returns a rectangle that bounds the onscreen rendering of the node.
- [func cloneNode(Bool) -> DOMNode!](domnode/clonenode(_:).md)
- [func compareDocumentPosition(DOMNode!) -> UInt16](domnode/comparedocumentposition(_:).md)
- [func contains(DOMNode!) -> Bool](domnode/contains(_:).md)
- [func hasAttributes() -> Bool](domnode/hasattributes.md)
- [func hasChildNodes() -> Bool](domnode/haschildnodes.md)
- [func insert(before: DOMNode!, refChild: DOMNode!) -> DOMNode!](domnode/insert(before:refchild:).md)
- [func isDefaultNamespace(String!) -> Bool](domnode/isdefaultnamespace(_:).md)
- [func isEqualNode(DOMNode!) -> Bool](domnode/isequalnode(_:).md)
- [func isSameNode(DOMNode!) -> Bool](domnode/issamenode(_:).md)
- [func isSupported(String!, version: String!) -> Bool](domnode/issupported(_:version:).md)
- [func lineBoxRects() -> [Any]!](domnode/lineboxrects.md)
  Returns the rectangles that bound each line of text in the node.
- [func lookupNamespaceURI(String!) -> String!](domnode/lookupnamespaceuri(_:).md)
- [func lookupPrefix(String!) -> String!](domnode/lookupprefix(_:).md)
- [func normalize()](domnode/normalize.md)
- [func removeChild(DOMNode!) -> DOMNode!](domnode/removechild(_:).md)
- [func replaceChild(DOMNode!, oldChild: DOMNode!) -> DOMNode!](domnode/replacechild(_:oldchild:).md)

## Relationships

### Inherits From
- [DOMObject](domobject.md)
### Inherited By
- [DOMAttr](domattr.md)
- [DOMCharacterData](domcharacterdata.md)
- [DOMDocument](domdocument.md)
- [DOMDocumentFragment](domdocumentfragment.md)
- [DOMDocumentType](domdocumenttype.md)
- [DOMElement](domelement.md)
- [DOMEntity](domentity.md)
- [DOMEntityReference](domentityreference.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DOMEventTarget](domeventtarget.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/domnode)*