# UIResponder.KeyboardDidShowMessage

**Framework**: UIKit  
**Kind**: struct

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
struct KeyboardDidShowMessage
```

## Topics

### Initializers
- [init(beginFrame: CGRect, endFrame: CGRect, animationDuration: TimeInterval, animationCurve: UIView.AnimationCurve, isLocal: Bool, screen: UIScreen)](uiresponder/keyboarddidshowmessage/init(beginframe:endframe:animationduration:animationcurve:islocal:screen:).md)
### Instance Properties
- [var animationCurve: UIView.AnimationCurve](uiresponder/keyboarddidshowmessage/animationcurve.md)
- [var animationDuration: TimeInterval](uiresponder/keyboarddidshowmessage/animationduration.md)
- [var beginFrame: CGRect](uiresponder/keyboarddidshowmessage/beginframe.md)
- [var endFrame: CGRect](uiresponder/keyboarddidshowmessage/endframe.md)
- [var isLocal: Bool](uiresponder/keyboarddidshowmessage/islocal.md)
- [var screen: UIScreen](uiresponder/keyboarddidshowmessage/screen.md)
### Type Methods
- [static func makeNotification(UIResponder.KeyboardDidShowMessage) -> Notification](uiresponder/keyboarddidshowmessage/makenotification(_:).md)

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [NotificationCenter.Message](../Foundation/NotificationCenter/Message.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/keyboarddidshowmessage)*