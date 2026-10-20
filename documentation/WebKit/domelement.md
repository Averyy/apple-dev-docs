# DOMElement

**Framework**: WebKit  
**Kind**: class  
**Role**: Class

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```swift
class DOMElement
```

```objc
@interface DOMElement : DOMNode
```

## Topics

### Instance Properties
- [var childElementCount: UInt32](./domelement/childelementcount.md)
- [var className: String!](./domelement/classname.md)
- [var clientHeight: Int32](./domelement/clientheight.md)
- [var clientLeft: Int32](./domelement/clientleft.md)
- [var clientTop: Int32](./domelement/clienttop.md)
- [var clientWidth: Int32](./domelement/clientwidth.md)
- [var firstElementChild: DOMElement!](./domelement/firstelementchild.md)
- [var innerHTML: String!](./domelement/innerhtml.md)
- [var innerText: String!](./domelement/innertext.md)
- [var lastElementChild: DOMElement!](./domelement/lastelementchild.md)
- [var nextElementSibling: DOMElement!](./domelement/nextelementsibling.md)
- [var offsetHeight: Int32](./domelement/offsetheight.md)
- [var offsetLeft: Int32](./domelement/offsetleft.md)
- [var offsetParent: DOMElement!](./domelement/offsetparent.md)
- [var offsetTop: Int32](./domelement/offsettop.md)
- [var offsetWidth: Int32](./domelement/offsetwidth.md)
- [var outerHTML: String!](./domelement/outerhtml.md)
- [var previousElementSibling: DOMElement!](./domelement/previouselementsibling.md)
- [var scrollHeight: Int32](./domelement/scrollheight.md)
- [var scrollLeft: Int32](./domelement/scrollleft.md)
- [var scrollTop: Int32](./domelement/scrolltop.md)
- [var scrollWidth: Int32](./domelement/scrollwidth.md)
- [var style: DOMCSSStyleDeclaration!](./domelement/style.md)
- [var tagName: String!](./domelement/tagname.md)
### Instance Methods
- [func blur()](./domelement/blur%28%29.md)
- [func focus()](./domelement/focus%28%29.md)
- [func getAttribute(String!) -> String!](./domelement/getattribute%28_%29.md)
- [func getAttributeNS(String!, localName: String!) -> String!](./domelement/getattributens%28_,localname%29.md)
- [func getAttributeNode(String!) -> DOMAttr!](./domelement/getattributenode%28_%29.md)
- [func getAttributeNodeNS(String!, localName: String!) -> DOMAttr!](./domelement/getattributenodens%28_,localname%29.md)
- [func getElementsByClassName(String!) -> DOMNodeList!](./domelement/getelementsbyclassname%28_%29.md)
- [func getElementsByTagName(String!) -> DOMNodeList!](./domelement/getelementsbytagname%28_%29.md)
- [func getElementsByTagNameNS(String!, localName: String!) -> DOMNodeList!](./domelement/getelementsbytagnamens%28_,localname%29.md)
- [func hasAttribute(String!) -> Bool](./domelement/hasattribute%28_%29.md)
- [func hasAttributeNS(String!, localName: String!) -> Bool](./domelement/hasattributens%28_,localname%29.md)
- [func image() -> NSImage!](./domelement/image%28%29.md)
  Returns an image associated with the receiver.
- [func querySelector(String!) -> DOMElement!](./domelement/queryselector%28_%29.md)
- [func querySelectorAll(String!) -> DOMNodeList!](./domelement/queryselectorall%28_%29.md)
- [func removeAttribute(String!)](./domelement/removeattribute%28_%29.md)
- [func removeAttributeNS(String!, localName: String!)](./domelement/removeattributens%28_,localname%29.md)
- [func removeAttributeNode(DOMAttr!) -> DOMAttr!](./domelement/removeattributenode%28_%29.md)
- [func scroll(byLines: Int32)](./domelement/scroll%28bylines%29.md)
- [func scroll(byPages: Int32)](./domelement/scroll%28bypages%29.md)
- [func scroll(intoView: Bool)](./domelement/scroll%28intoview%29.md)
- [func scroll(intoViewIfNeeded: Bool)](./domelement/scroll%28intoviewifneeded%29.md)
- [func setAttribute(String!, value: String!)](./domelement/setattribute%28_,value%29.md)
- [func setAttributeNS(String!, qualifiedName: String!, value: String!)](./domelement/setattributens%28_,qualifiedname,value%29.md)
- [func setAttributeNode(DOMAttr!) -> DOMAttr!](./domelement/setattributenode%28_%29.md)
- [func setAttributeNodeNS(DOMAttr!) -> DOMAttr!](./domelement/setattributenodens%28_%29.md)
- [func webkitRequestFullScreen(UInt16)](./domelement/webkitrequestfullscreen%28_%29.md)

## Relationships

### Inherits From
- [DOMNode](./domnode.md)
### Inherited By
- [DOMHTMLElement](./domhtmlelement.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/domelement)*