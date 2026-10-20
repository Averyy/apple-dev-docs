# DOMDocument

**Framework**: WebKit  
**Kind**: class  
**Role**: Class

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```swift
class DOMDocument
```

```objc
@interface DOMDocument : DOMNode
```

## Topics

### Instance Properties
- [var activeElement: DOMElement!](./domdocument/activeelement.md)
- [var anchors: DOMHTMLCollection!](./domdocument/anchors.md)
- [var applets: DOMHTMLCollection!](./domdocument/applets.md)
- [var body: DOMHTMLElement!](./domdocument/body.md)
- [var characterSet: String!](./domdocument/characterset.md)
- [var charset: String!](./domdocument/charset.md)
- [var cookie: String!](./domdocument/cookie.md)
- [var defaultCharset: String!](./domdocument/defaultcharset.md)
- [var defaultView: DOMAbstractView!](./domdocument/defaultview.md)
- [var doctype: DOMDocumentType!](./domdocument/doctype.md)
- [var documentElement: DOMElement!](./domdocument/documentelement.md)
- [var documentURI: String!](./domdocument/documenturi.md)
- [var domain: String!](./domdocument/domain.md)
- [var forms: DOMHTMLCollection!](./domdocument/forms.md)
- [var images: DOMHTMLCollection!](./domdocument/images.md)
- [var implementation: DOMImplementation!](./domdocument/implementation.md)
- [var inputEncoding: String!](./domdocument/inputencoding.md)
- [var lastModified: String!](./domdocument/lastmodified.md)
- [var links: DOMHTMLCollection!](./domdocument/links.md)
- [var preferredStylesheetSet: String!](./domdocument/preferredstylesheetset.md)
- [var readyState: String!](./domdocument/readystate.md)
- [var referrer: String!](./domdocument/referrer.md)
- [var selectedStylesheetSet: String!](./domdocument/selectedstylesheetset.md)
- [var styleSheets: DOMStyleSheetList!](./domdocument/stylesheets.md)
- [var title: String!](./domdocument/title.md)
- [var url: String!](./domdocument/url.md)
- [var webFrame: WebFrame!](./domdocument/webframe.md)
  The web frame associated with the DOM document.
- [var xmlEncoding: String!](./domdocument/xmlencoding.md)
- [var xmlStandalone: Bool](./domdocument/xmlstandalone.md)
- [var xmlVersion: String!](./domdocument/xmlversion.md)
### Instance Methods
- [func adoptNode(DOMNode!) -> DOMNode!](./domdocument/adoptnode%28_%29.md)
- [func createAttribute(String!) -> DOMAttr!](./domdocument/createattribute%28_%29.md)
- [func createAttributeNS(String!, qualifiedName: String!) -> DOMAttr!](./domdocument/createattributens%28_,qualifiedname%29.md)
- [func createCDATASection(String!) -> DOMCDATASection!](./domdocument/createcdatasection%28_%29.md)
- [func createCSSStyleDeclaration() -> DOMCSSStyleDeclaration!](./domdocument/createcssstyledeclaration%28%29.md)
- [func createComment(String!) -> DOMComment!](./domdocument/createcomment%28_%29.md)
- [func createDocumentFragment() -> DOMDocumentFragment!](./domdocument/createdocumentfragment%28%29.md)
- [func createElement(String!) -> DOMElement!](./domdocument/createelement%28_%29.md)
- [func createElementNS(String!, qualifiedName: String!) -> DOMElement!](./domdocument/createelementns%28_,qualifiedname%29.md)
- [func createEntityReference(String!) -> DOMEntityReference!](./domdocument/createentityreference%28_%29.md)
- [func createEvent(String!) -> DOMEvent!](./domdocument/createevent%28_%29.md)
- [func createExpression(String!, resolver: (any DOMXPathNSResolver)!) -> DOMXPathExpression!](./domdocument/createexpression%28_,resolver%29.md)
- [func createNSResolver(DOMNode!) -> (any DOMXPathNSResolver)!](./domdocument/creatensresolver%28_%29.md)
- [func createNodeIterator(DOMNode!, whatToShow: UInt32, filter: (any DOMNodeFilter)!, expandEntityReferences: Bool) -> DOMNodeIterator!](./domdocument/createnodeiterator%28_,whattoshow,filter,expandentityreferences%29.md)
- [func createProcessingInstruction(String!, data: String!) -> DOMProcessingInstruction!](./domdocument/createprocessinginstruction%28_,data%29.md)
- [func createRange() -> DOMRange!](./domdocument/createrange%28%29.md)
- [func createTextNode(String!) -> DOMText!](./domdocument/createtextnode%28_%29.md)
- [func createTreeWalker(DOMNode!, whatToShow: UInt32, filter: (any DOMNodeFilter)!, expandEntityReferences: Bool) -> DOMTreeWalker!](./domdocument/createtreewalker%28_,whattoshow,filter,expandentityreferences%29.md)
- [func element(fromPoint: Int32, y: Int32) -> DOMElement!](./domdocument/element%28frompoint,y%29.md)
- [func evaluate(String!, contextNode: DOMNode!, resolver: (any DOMXPathNSResolver)!, type: UInt16, in: DOMXPathResult!) -> DOMXPathResult!](./domdocument/evaluate%28_,contextnode,resolver,type,in%29.md)
- [func execCommand(String!) -> Bool](./domdocument/execcommand%28_%29.md)
- [func execCommand(String!, userInterface: Bool) -> Bool](./domdocument/execcommand%28_,userinterface%29.md)
- [func execCommand(String!, userInterface: Bool, value: String!) -> Bool](./domdocument/execcommand%28_,userinterface,value%29.md)
- [func getComputedStyle(DOMElement!, pseudoElement: String!) -> DOMCSSStyleDeclaration!](./domdocument/getcomputedstyle%28_,pseudoelement%29.md)
- [func getElementById(String!) -> DOMElement!](./domdocument/getelementbyid%28_%29.md)
- [func getElementsByClassName(String!) -> DOMNodeList!](./domdocument/getelementsbyclassname%28_%29.md)
- [func getElementsByName(String!) -> DOMNodeList!](./domdocument/getelementsbyname%28_%29.md)
- [func getElementsByTagName(String!) -> DOMNodeList!](./domdocument/getelementsbytagname%28_%29.md)
- [func getElementsByTagNameNS(String!, localName: String!) -> DOMNodeList!](./domdocument/getelementsbytagnamens%28_,localname%29.md)
- [func getMatchedCSSRules(DOMElement!, pseudoElement: String!) -> DOMCSSRuleList!](./domdocument/getmatchedcssrules%28_,pseudoelement%29.md)
- [func getMatchedCSSRules(DOMElement!, pseudoElement: String!, authorOnly: Bool) -> DOMCSSRuleList!](./domdocument/getmatchedcssrules%28_,pseudoelement,authoronly%29.md)
- [func getOverrideStyle(DOMElement!, pseudoElement: String!) -> DOMCSSStyleDeclaration!](./domdocument/getoverridestyle%28_,pseudoelement%29.md)
- [func hasFocus() -> Bool](./domdocument/hasfocus%28%29.md)
- [func `import`(DOMNode!, deep: Bool) -> DOMNode!](./domdocument/import%28_,deep%29.md)
- [func queryCommandEnabled(String!) -> Bool](./domdocument/querycommandenabled%28_%29.md)
- [func queryCommandIndeterm(String!) -> Bool](./domdocument/querycommandindeterm%28_%29.md)
- [func queryCommandState(String!) -> Bool](./domdocument/querycommandstate%28_%29.md)
- [func queryCommandSupported(String!) -> Bool](./domdocument/querycommandsupported%28_%29.md)
- [func queryCommandValue(String!) -> String!](./domdocument/querycommandvalue%28_%29.md)
- [func querySelector(String!) -> DOMElement!](./domdocument/queryselector%28_%29.md)
- [func querySelectorAll(String!) -> DOMNodeList!](./domdocument/queryselectorall%28_%29.md)
- [func url(withAttributeString: String!) -> URL!](./domdocument/url%28withattributestring%29.md)
  Constructs a URL given an attribute string.
- [func webkitCancelFullScreen()](./domdocument/webkitcancelfullscreen%28%29.md)

## Relationships

### Inherits From
- [DOMNode](./domnode.md)
### Inherited By
- [DOMHTMLDocument](./domhtmldocument.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/domdocument)*