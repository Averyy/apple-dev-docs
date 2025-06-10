# DOMKeyboardEvent

**Framework**: WebKit  
**Kind**: class

**Availability**:
- macOS 10.5+

## Declaration

```swift
class DOMKeyboardEvent
```

## Topics

### Instance Properties
- [var altGraphKey: Bool](domkeyboardevent/altgraphkey.md)
- [var altKey: Bool](domkeyboardevent/altkey.md)
- [var charCode: Int32](domkeyboardevent/charcode.md)
- [var ctrlKey: Bool](domkeyboardevent/ctrlkey.md)
- [var keyCode: Int32](domkeyboardevent/keycode.md)
- [var keyIdentifier: String!](domkeyboardevent/keyidentifier.md)
- [var location: UInt32](domkeyboardevent/location.md)
- [var metaKey: Bool](domkeyboardevent/metakey.md)
- [var shiftKey: Bool](domkeyboardevent/shiftkey.md)
### Instance Methods
- [func getModifierState(String!) -> Bool](domkeyboardevent/getmodifierstate(_:).md)
- [func initKeyboardEvent(String!, canBubble: Bool, cancelable: Bool, view: DOMAbstractView!, keyIdentifier: String!, location: UInt32, ctrlKey: Bool, altKey: Bool, shiftKey: Bool, metaKey: Bool)](domkeyboardevent/initkeyboardevent(_:canbubble:cancelable:view:keyidentifier:location:ctrlkey:altkey:shiftkey:metakey:).md)
- [func initKeyboardEvent(String!, canBubble: Bool, cancelable: Bool, view: DOMAbstractView!, keyIdentifier: String!, location: UInt32, ctrlKey: Bool, altKey: Bool, shiftKey: Bool, metaKey: Bool, altGraphKey: Bool)](domkeyboardevent/initkeyboardevent(_:canbubble:cancelable:view:keyidentifier:location:ctrlkey:altkey:shiftkey:metakey:altgraphkey:).md)

## Relationships

### Inherits From
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/domkeyboardevent)*