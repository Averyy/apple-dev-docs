# UIResponder.KeyboardWillHideMessage

**Framework**: UIKit  
**Kind**: struct

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
struct KeyboardWillHideMessage
```

## Topics

### Initializers
- [init(beginFrame: CGRect, endFrame: CGRect, animationDuration: TimeInterval, animationCurve: UIView.AnimationCurve, isLocal: Bool, screen: UIScreen)](uiresponder/keyboardwillhidemessage/init(beginframe:endframe:animationduration:animationcurve:islocal:screen:).md)
### Instance Properties
- [var animationCurve: UIView.AnimationCurve](uiresponder/keyboardwillhidemessage/animationcurve.md)
- [var animationDuration: TimeInterval](uiresponder/keyboardwillhidemessage/animationduration.md)
- [var beginFrame: CGRect](uiresponder/keyboardwillhidemessage/beginframe.md)
- [var endFrame: CGRect](uiresponder/keyboardwillhidemessage/endframe.md)
- [var isLocal: Bool](uiresponder/keyboardwillhidemessage/islocal.md)
- [var screen: UIScreen](uiresponder/keyboardwillhidemessage/screen.md)
### Type Methods
- [static func makeNotification(UIResponder.KeyboardWillHideMessage) -> Notification](uiresponder/keyboardwillhidemessage/makenotification(_:).md)

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/keyboardwillhidemessage)*