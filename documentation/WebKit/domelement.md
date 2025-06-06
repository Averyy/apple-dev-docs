# DOMElement

**Framework**: Webkit  
**Kind**: class

**Availability**:
- macOS 10.4+

## Declaration

```swift
class DOMElement
```

## Topics

### Instance Properties
- [var childElementCount: UInt32](domelement/childelementcount.md)
- [var className: String!](domelement/classname.md)
- [var clientHeight: Int32](domelement/clientheight.md)
- [var clientLeft: Int32](domelement/clientleft.md)
- [var clientTop: Int32](domelement/clienttop.md)
- [var clientWidth: Int32](domelement/clientwidth.md)
- [var firstElementChild: DOMElement!](domelement/firstelementchild.md)
- [var innerHTML: String!](domelement/innerhtml.md)
- [var innerText: String!](domelement/innertext.md)
- [var lastElementChild: DOMElement!](domelement/lastelementchild.md)
- [var nextElementSibling: DOMElement!](domelement/nextelementsibling.md)
- [var offsetHeight: Int32](domelement/offsetheight.md)
- [var offsetLeft: Int32](domelement/offsetleft.md)
- [var offsetParent: DOMElement!](domelement/offsetparent.md)
- [var offsetTop: Int32](domelement/offsettop.md)
- [var offsetWidth: Int32](domelement/offsetwidth.md)
- [var outerHTML: String!](domelement/outerhtml.md)
- [var previousElementSibling: DOMElement!](domelement/previouselementsibling.md)
- [var scrollHeight: Int32](domelement/scrollheight.md)
- [var scrollLeft: Int32](domelement/scrollleft.md)
- [var scrollTop: Int32](domelement/scrolltop.md)
- [var scrollWidth: Int32](domelement/scrollwidth.md)
- [var style: DOMCSSStyleDeclaration!](domelement/style.md)
- [var tagName: String!](domelement/tagname.md)
### Instance Methods
- [func blur()](domelement/blur.md)
- [func focus()](domelement/focus.md)
- [func getAttribute(String!) -> String!](domelement/getattribute(_:).md)
- [func getAttributeNS(String!, localName: String!) -> String!](domelement/getattributens(_:localname:).md)
- [func getAttributeNode(String!) -> DOMAttr!](domelement/getattributenode(_:).md)
- [func getAttributeNodeNS(String!, localName: String!) -> DOMAttr!](domelement/getattributenodens(_:localname:).md)
- [func getElementsByClassName(String!) -> DOMNodeList!](domelement/getelementsbyclassname(_:).md)
- [func getElementsByTagName(String!) -> DOMNodeList!](domelement/getelementsbytagname(_:).md)
- [func getElementsByTagNameNS(String!, localName: String!) -> DOMNodeList!](domelement/getelementsbytagnamens(_:localname:).md)
- [func hasAttribute(String!) -> Bool](domelement/hasattribute(_:).md)
- [func hasAttributeNS(String!, localName: String!) -> Bool](domelement/hasattributens(_:localname:).md)
- [func image() -> NSImage!](domelement/image.md)
  Returns an image associated with the receiver.
- [func querySelector(String!) -> DOMElement!](domelement/queryselector(_:).md)
- [func querySelectorAll(String!) -> DOMNodeList!](domelement/queryselectorall(_:).md)
- [func removeAttribute(String!)](domelement/removeattribute(_:).md)
- [func removeAttributeNS(String!, localName: String!)](domelement/removeattributens(_:localname:).md)
- [func removeAttributeNode(DOMAttr!) -> DOMAttr!](domelement/removeattributenode(_:).md)
- [func scroll(byLines: Int32)](domelement/scroll(bylines:).md)
- [func scroll(byPages: Int32)](domelement/scroll(bypages:).md)
- [func scroll(intoView: Bool)](domelement/scroll(intoview:).md)
- [func scroll(intoViewIfNeeded: Bool)](domelement/scroll(intoviewifneeded:).md)
- [func setAttribute(String!, value: String!)](domelement/setattribute(_:value:).md)
- [func setAttributeNS(String!, qualifiedName: String!, value: String!)](domelement/setattributens(_:qualifiedname:value:).md)
- [func setAttributeNode(DOMAttr!) -> DOMAttr!](domelement/setattributenode(_:).md)
- [func setAttributeNodeNS(DOMAttr!) -> DOMAttr!](domelement/setattributenodens(_:).md)
- [func webkitRequestFullScreen(UInt16)](domelement/webkitrequestfullscreen(_:).md)

## Relationships

### Inherits From
- [DOMNode](domnode.md)
### Inherited By
- [DOMHTMLElement](domhtmlelement.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/domelement)*