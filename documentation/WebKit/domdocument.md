# DOMDocument

**Framework**: WebKit  
**Kind**: class

**Availability**:
- macOS 10.4+

## Declaration

```swift
class DOMDocument
```

## Topics

### Instance Properties
- [var activeElement: DOMElement!](domdocument/activeelement.md)
- [var anchors: DOMHTMLCollection!](domdocument/anchors.md)
- [var applets: DOMHTMLCollection!](domdocument/applets.md)
- [var body: DOMHTMLElement!](domdocument/body.md)
- [var characterSet: String!](domdocument/characterset.md)
- [var charset: String!](domdocument/charset.md)
- [var cookie: String!](domdocument/cookie.md)
- [var defaultCharset: String!](domdocument/defaultcharset.md)
- [var defaultView: DOMAbstractView!](domdocument/defaultview.md)
- [var doctype: DOMDocumentType!](domdocument/doctype.md)
- [var documentElement: DOMElement!](domdocument/documentelement.md)
- [var documentURI: String!](domdocument/documenturi.md)
- [var domain: String!](domdocument/domain.md)
- [var forms: DOMHTMLCollection!](domdocument/forms.md)
- [var images: DOMHTMLCollection!](domdocument/images.md)
- [var implementation: DOMImplementation!](domdocument/implementation.md)
- [var inputEncoding: String!](domdocument/inputencoding.md)
- [var lastModified: String!](domdocument/lastmodified.md)
- [var links: DOMHTMLCollection!](domdocument/links.md)
- [var preferredStylesheetSet: String!](domdocument/preferredstylesheetset.md)
- [var readyState: String!](domdocument/readystate.md)
- [var referrer: String!](domdocument/referrer.md)
- [var selectedStylesheetSet: String!](domdocument/selectedstylesheetset.md)
- [var styleSheets: DOMStyleSheetList!](domdocument/stylesheets.md)
- [var title: String!](domdocument/title.md)
- [var url: String!](domdocument/url.md)
- [var webFrame: WebFrame!](domdocument/webframe.md)
  The web frame associated with the DOM document.
- [var xmlEncoding: String!](domdocument/xmlencoding.md)
- [var xmlStandalone: Bool](domdocument/xmlstandalone.md)
- [var xmlVersion: String!](domdocument/xmlversion.md)
### Instance Methods
- [func adoptNode(DOMNode!) -> DOMNode!](domdocument/adoptnode(_:).md)
- [func createAttribute(String!) -> DOMAttr!](domdocument/createattribute(_:).md)
- [func createAttributeNS(String!, qualifiedName: String!) -> DOMAttr!](domdocument/createattributens(_:qualifiedname:).md)
- [func createCDATASection(String!) -> DOMCDATASection!](domdocument/createcdatasection(_:).md)
- [func createCSSStyleDeclaration() -> DOMCSSStyleDeclaration!](domdocument/createcssstyledeclaration.md)
- [func createComment(String!) -> DOMComment!](domdocument/createcomment(_:).md)
- [func createDocumentFragment() -> DOMDocumentFragment!](domdocument/createdocumentfragment.md)
- [func createElement(String!) -> DOMElement!](domdocument/createelement(_:).md)
- [func createElementNS(String!, qualifiedName: String!) -> DOMElement!](domdocument/createelementns(_:qualifiedname:).md)
- [func createEntityReference(String!) -> DOMEntityReference!](domdocument/createentityreference(_:).md)
- [func createEvent(String!) -> DOMEvent!](domdocument/createevent(_:).md)
- [func createExpression(String!, resolver: (any DOMXPathNSResolver)!) -> DOMXPathExpression!](domdocument/createexpression(_:resolver:).md)
- [func createNSResolver(DOMNode!) -> (any DOMXPathNSResolver)!](domdocument/creatensresolver(_:).md)
- [func createNodeIterator(DOMNode!, whatToShow: UInt32, filter: (any DOMNodeFilter)!, expandEntityReferences: Bool) -> DOMNodeIterator!](domdocument/createnodeiterator(_:whattoshow:filter:expandentityreferences:).md)
- [func createProcessingInstruction(String!, data: String!) -> DOMProcessingInstruction!](domdocument/createprocessinginstruction(_:data:).md)
- [func createRange() -> DOMRange!](domdocument/createrange.md)
- [func createTextNode(String!) -> DOMText!](domdocument/createtextnode(_:).md)
- [func createTreeWalker(DOMNode!, whatToShow: UInt32, filter: (any DOMNodeFilter)!, expandEntityReferences: Bool) -> DOMTreeWalker!](domdocument/createtreewalker(_:whattoshow:filter:expandentityreferences:).md)
- [func element(fromPoint: Int32, y: Int32) -> DOMElement!](domdocument/element(frompoint:y:).md)
- [func evaluate(String!, contextNode: DOMNode!, resolver: (any DOMXPathNSResolver)!, type: UInt16, in: DOMXPathResult!) -> DOMXPathResult!](domdocument/evaluate(_:contextnode:resolver:type:in:).md)
- [func execCommand(String!) -> Bool](domdocument/execcommand(_:).md)
- [func execCommand(String!, userInterface: Bool) -> Bool](domdocument/execcommand(_:userinterface:).md)
- [func execCommand(String!, userInterface: Bool, value: String!) -> Bool](domdocument/execcommand(_:userinterface:value:).md)
- [func getComputedStyle(DOMElement!, pseudoElement: String!) -> DOMCSSStyleDeclaration!](domdocument/getcomputedstyle(_:pseudoelement:).md)
- [func getElementById(String!) -> DOMElement!](domdocument/getelementbyid(_:).md)
- [func getElementsByClassName(String!) -> DOMNodeList!](domdocument/getelementsbyclassname(_:).md)
- [func getElementsByName(String!) -> DOMNodeList!](domdocument/getelementsbyname(_:).md)
- [func getElementsByTagName(String!) -> DOMNodeList!](domdocument/getelementsbytagname(_:).md)
- [func getElementsByTagNameNS(String!, localName: String!) -> DOMNodeList!](domdocument/getelementsbytagnamens(_:localname:).md)
- [func getMatchedCSSRules(DOMElement!, pseudoElement: String!) -> DOMCSSRuleList!](domdocument/getmatchedcssrules(_:pseudoelement:).md)
- [func getMatchedCSSRules(DOMElement!, pseudoElement: String!, authorOnly: Bool) -> DOMCSSRuleList!](domdocument/getmatchedcssrules(_:pseudoelement:authoronly:).md)
- [func getOverrideStyle(DOMElement!, pseudoElement: String!) -> DOMCSSStyleDeclaration!](domdocument/getoverridestyle(_:pseudoelement:).md)
- [func hasFocus() -> Bool](domdocument/hasfocus.md)
- [func `import`(DOMNode!, deep: Bool) -> DOMNode!](domdocument/import(_:deep:).md)
- [func queryCommandEnabled(String!) -> Bool](domdocument/querycommandenabled(_:).md)
- [func queryCommandIndeterm(String!) -> Bool](domdocument/querycommandindeterm(_:).md)
- [func queryCommandState(String!) -> Bool](domdocument/querycommandstate(_:).md)
- [func queryCommandSupported(String!) -> Bool](domdocument/querycommandsupported(_:).md)
- [func queryCommandValue(String!) -> String!](domdocument/querycommandvalue(_:).md)
- [func querySelector(String!) -> DOMElement!](domdocument/queryselector(_:).md)
- [func querySelectorAll(String!) -> DOMNodeList!](domdocument/queryselectorall(_:).md)
- [func url(withAttributeString: String!) -> URL!](domdocument/url(withattributestring:).md)
  Constructs a URL given an attribute string.
- [func webkitCancelFullScreen()](domdocument/webkitcancelfullscreen.md)

## Relationships

### Inherits From
- [DOMNode](domnode.md)
### Inherited By
- [DOMHTMLDocument](domhtmldocument.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/domdocument)*