# DOMMouseEvent

**Framework**: WebKit  
**Kind**: class

**Availability**:
- macOS 10.4+

## Declaration

```swift
class DOMMouseEvent
```

## Topics

### Instance Properties
- [var altKey: Bool](dommouseevent/altkey.md)
- [var button: Int16](dommouseevent/button.md)
- [var clientX: Int32](dommouseevent/clientx.md)
- [var clientY: Int32](dommouseevent/clienty.md)
- [var ctrlKey: Bool](dommouseevent/ctrlkey.md)
- [var fromElement: DOMNode!](dommouseevent/fromelement.md)
- [var metaKey: Bool](dommouseevent/metakey.md)
- [var offsetX: Int32](dommouseevent/offsetx.md)
- [var offsetY: Int32](dommouseevent/offsety.md)
- [var relatedTarget: (any DOMEventTarget)!](dommouseevent/relatedtarget.md)
- [var screenX: Int32](dommouseevent/screenx.md)
- [var screenY: Int32](dommouseevent/screeny.md)
- [var shiftKey: Bool](dommouseevent/shiftkey.md)
- [var toElement: DOMNode!](dommouseevent/toelement.md)
- [var x: Int32](dommouseevent/x.md)
- [var y: Int32](dommouseevent/y.md)
### Instance Methods
- [func initMouseEvent(String!, canBubble: Bool, cancelable: Bool, view: DOMAbstractView!, detail: Int32, screenX: Int32, screenY: Int32, clientX: Int32, clientY: Int32, ctrlKey: Bool, altKey: Bool, shiftKey: Bool, metaKey: Bool, button: UInt16, relatedTarget: (any DOMEventTarget)!)](dommouseevent/initmouseevent(_:canbubble:cancelable:view:detail:screenx:screeny:clientx:clienty:ctrlkey:altkey:shiftkey:metakey:button:relatedtarget:).md)

## Relationships

### Inherits From
- [DOMUIEvent](domuievent.md)
### Inherited By
- [DOMWheelEvent](domwheelevent.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/dommouseevent)*