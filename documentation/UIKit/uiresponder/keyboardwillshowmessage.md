# UIResponder.KeyboardWillShowMessage

**Framework**: UIKit  
**Kind**: struct

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
struct KeyboardWillShowMessage
```

## Topics

### Initializers
- [init(beginFrame: CGRect, endFrame: CGRect, animationDuration: TimeInterval, animationCurve: UIView.AnimationCurve, isLocal: Bool, screen: UIScreen)](uiresponder/keyboardwillshowmessage/init(beginframe:endframe:animationduration:animationcurve:islocal:screen:).md)
### Instance Properties
- [var animationCurve: UIView.AnimationCurve](uiresponder/keyboardwillshowmessage/animationcurve.md)
- [var animationDuration: TimeInterval](uiresponder/keyboardwillshowmessage/animationduration.md)
- [var beginFrame: CGRect](uiresponder/keyboardwillshowmessage/beginframe.md)
- [var endFrame: CGRect](uiresponder/keyboardwillshowmessage/endframe.md)
- [var isLocal: Bool](uiresponder/keyboardwillshowmessage/islocal.md)
- [var screen: UIScreen](uiresponder/keyboardwillshowmessage/screen.md)
### Type Methods
- [static func makeNotification(UIResponder.KeyboardWillShowMessage) -> Notification](uiresponder/keyboardwillshowmessage/makenotification(_:).md)

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/keyboardwillshowmessage)*