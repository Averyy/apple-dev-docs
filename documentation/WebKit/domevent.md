# DOMEvent

**Framework**: WebKit  
**Kind**: class

**Availability**:
- macOS 10.4+

## Declaration

```swift
class DOMEvent
```

## Topics

### Instance Properties
- [var bubbles: Bool](domevent/bubbles.md)
- [var cancelBubble: Bool](domevent/cancelbubble.md)
- [var cancelable: Bool](domevent/cancelable.md)
- [var currentTarget: (any DOMEventTarget)!](domevent/currenttarget.md)
- [var eventPhase: UInt16](domevent/eventphase.md)
- [var returnValue: Bool](domevent/returnvalue.md)
- [var srcElement: (any DOMEventTarget)!](domevent/srcelement.md)
- [var target: (any DOMEventTarget)!](domevent/target.md)
- [var timeStamp: DOMTimeStamp](domevent/timestamp.md)
- [var type: String!](domevent/type.md)
### Instance Methods
- [func initEvent(String!, canBubbleArg: Bool, cancelableArg: Bool)](domevent/initevent(_:canbubblearg:cancelablearg:).md)
- [func preventDefault()](domevent/preventdefault.md)
- [func stopPropagation()](domevent/stoppropagation.md)

## Relationships

### Inherits From
- [DOMObject](domobject.md)
### Inherited By
- [DOMMutationEvent](dommutationevent.md)
- [DOMOverflowEvent](domoverflowevent.md)
- [DOMProgressEvent](domprogressevent.md)
- [DOMUIEvent](domuievent.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/domevent)*