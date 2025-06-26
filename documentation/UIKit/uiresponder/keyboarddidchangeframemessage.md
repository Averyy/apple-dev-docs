# UIResponder.KeyboardDidChangeFrameMessage

**Framework**: UIKit  
**Kind**: struct

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
struct KeyboardDidChangeFrameMessage
```

## Topics

### Initializers
- [init(beginFrame: CGRect, endFrame: CGRect, animationDuration: TimeInterval, animationCurve: UIView.AnimationCurve, isLocal: Bool, screen: UIScreen)](uiresponder/keyboarddidchangeframemessage/init(beginframe:endframe:animationduration:animationcurve:islocal:screen:).md)
### Instance Properties
- [var animationCurve: UIView.AnimationCurve](uiresponder/keyboarddidchangeframemessage/animationcurve.md)
- [var animationDuration: TimeInterval](uiresponder/keyboarddidchangeframemessage/animationduration.md)
- [var beginFrame: CGRect](uiresponder/keyboarddidchangeframemessage/beginframe.md)
- [var endFrame: CGRect](uiresponder/keyboarddidchangeframemessage/endframe.md)
- [var isLocal: Bool](uiresponder/keyboarddidchangeframemessage/islocal.md)
- [var screen: UIScreen](uiresponder/keyboarddidchangeframemessage/screen.md)
### Type Methods
- [static func makeNotification(UIResponder.KeyboardDidChangeFrameMessage) -> Notification](uiresponder/keyboarddidchangeframemessage/makenotification(_:).md)

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/keyboarddidchangeframemessage)*