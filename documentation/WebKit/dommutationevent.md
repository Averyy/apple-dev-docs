# DOMMutationEvent

**Framework**: WebKit  
**Kind**: class  
**Role**: Class

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```swift
class DOMMutationEvent
```

```objc
@interface DOMMutationEvent : DOMEvent
```

## Topics

### Instance Properties
- [var attrChange: UInt16](./dommutationevent/attrchange.md)
- [var attrName: String!](./dommutationevent/attrname.md)
- [var newValue: String!](./dommutationevent/newvalue.md)
- [var prevValue: String!](./dommutationevent/prevvalue.md)
- [var relatedNode: DOMNode!](./dommutationevent/relatednode.md)
### Instance Methods
- [func initMutationEvent(String!, canBubble: Bool, cancelable: Bool, relatedNode: DOMNode!, prevValue: String!, newValue: String!, attrName: String!, attrChange: UInt16)](./dommutationevent/initmutationevent%28_,canbubble,cancelable,relatednode,prevvalue,newvalue,attrname,attrchange%29.md)
- [- initMutationEvent::::::::](./dommutationevent/initmutationevent________.md)

## Relationships

### Inherits From
- [DOMEvent](./domevent.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/dommutationevent)*