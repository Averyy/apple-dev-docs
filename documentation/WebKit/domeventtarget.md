# DOMEventTarget

**Framework**: Webkit  
**Kind**: protocol

**Availability**:
- macOS 10.4+

## Declaration

```swift
protocol DOMEventTarget : NSCopying, NSObjectProtocol
```

## Topics

### Instance Methods
- [func addEventListener(String!, listener: (any DOMEventListener)!, useCapture: Bool)](domeventtarget/addeventlistener(_:listener:usecapture:).md)
- [func dispatchEvent(DOMEvent!) -> Bool](domeventtarget/dispatchevent(_:).md)
- [func removeEventListener(String!, listener: (any DOMEventListener)!, useCapture: Bool)](domeventtarget/removeeventlistener(_:listener:usecapture:).md)

## Relationships

### Inherits From
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [DOMAttr](domattr.md)
- [DOMCDATASection](domcdatasection.md)
- [DOMCharacterData](domcharacterdata.md)
- [DOMComment](domcomment.md)
- [DOMDocument](domdocument.md)
- [DOMDocumentFragment](domdocumentfragment.md)
- [DOMDocumentType](domdocumenttype.md)
- [DOMElement](domelement.md)
- [DOMEntity](domentity.md)
- [DOMEntityReference](domentityreference.md)
- [DOMHTMLAnchorElement](domhtmlanchorelement.md)
- [DOMHTMLAppletElement](domhtmlappletelement.md)
- [DOMHTMLAreaElement](domhtmlareaelement.md)
- [DOMHTMLBRElement](domhtmlbrelement.md)
- [DOMHTMLBaseElement](domhtmlbaseelement.md)
- [DOMHTMLBaseFontElement](domhtmlbasefontelement.md)
- [DOMHTMLBodyElement](domhtmlbodyelement.md)
- [DOMHTMLButtonElement](domhtmlbuttonelement.md)
- [DOMHTMLDListElement](domhtmldlistelement.md)
- [DOMHTMLDirectoryElement](domhtmldirectoryelement.md)
- [DOMHTMLDivElement](domhtmldivelement.md)
- [DOMHTMLDocument](domhtmldocument.md)
- [DOMHTMLElement](domhtmlelement.md)
- [DOMHTMLEmbedElement](domhtmlembedelement.md)
- [DOMHTMLFieldSetElement](domhtmlfieldsetelement.md)
- [DOMHTMLFontElement](domhtmlfontelement.md)
- [DOMHTMLFormElement](domhtmlformelement.md)
- [DOMHTMLFrameElement](domhtmlframeelement.md)
- [DOMHTMLFrameSetElement](domhtmlframesetelement.md)
- [DOMHTMLHRElement](domhtmlhrelement.md)
- [DOMHTMLHeadElement](domhtmlheadelement.md)
- [DOMHTMLHeadingElement](domhtmlheadingelement.md)
- [DOMHTMLHtmlElement](domhtmlhtmlelement.md)
- [DOMHTMLIFrameElement](domhtmliframeelement.md)
- [DOMHTMLImageElement](domhtmlimageelement.md)
- [DOMHTMLInputElement](domhtmlinputelement.md)
- [DOMHTMLLIElement](domhtmllielement.md)
- [DOMHTMLLabelElement](domhtmllabelelement.md)
- [DOMHTMLLegendElement](domhtmllegendelement.md)
- [DOMHTMLLinkElement](domhtmllinkelement.md)
- [DOMHTMLMapElement](domhtmlmapelement.md)
- [DOMHTMLMarqueeElement](domhtmlmarqueeelement.md)
- [DOMHTMLMenuElement](domhtmlmenuelement.md)
- [DOMHTMLMetaElement](domhtmlmetaelement.md)
- [DOMHTMLModElement](domhtmlmodelement.md)
- [DOMHTMLOListElement](domhtmlolistelement.md)
- [DOMHTMLObjectElement](domhtmlobjectelement.md)
- [DOMHTMLOptGroupElement](domhtmloptgroupelement.md)
- [DOMHTMLOptionElement](domhtmloptionelement.md)
- [DOMHTMLParagraphElement](domhtmlparagraphelement.md)
- [DOMHTMLParamElement](domhtmlparamelement.md)
- [DOMHTMLPreElement](domhtmlpreelement.md)
- [DOMHTMLQuoteElement](domhtmlquoteelement.md)
- [DOMHTMLScriptElement](domhtmlscriptelement.md)
- [DOMHTMLSelectElement](domhtmlselectelement.md)
- [DOMHTMLStyleElement](domhtmlstyleelement.md)
- [DOMHTMLTableCaptionElement](domhtmltablecaptionelement.md)
- [DOMHTMLTableCellElement](domhtmltablecellelement.md)
- [DOMHTMLTableColElement](domhtmltablecolelement.md)
- [DOMHTMLTableElement](domhtmltableelement.md)
- [DOMHTMLTableRowElement](domhtmltablerowelement.md)
- [DOMHTMLTableSectionElement](domhtmltablesectionelement.md)
- [DOMHTMLTextAreaElement](domhtmltextareaelement.md)
- [DOMHTMLTitleElement](domhtmltitleelement.md)
- [DOMHTMLUListElement](domhtmlulistelement.md)
- [DOMNode](domnode.md)
- [DOMProcessingInstruction](domprocessinginstruction.md)
- [DOMText](domtext.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/domeventtarget)*