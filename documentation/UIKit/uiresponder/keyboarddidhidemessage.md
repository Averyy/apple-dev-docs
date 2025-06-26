# UIResponder.KeyboardDidHideMessage

**Framework**: UIKit  
**Kind**: struct

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
struct KeyboardDidHideMessage
```

## Topics

### Initializers
- [init(beginFrame: CGRect, endFrame: CGRect, animationDuration: TimeInterval, animationCurve: UIView.AnimationCurve, isLocal: Bool, screen: UIScreen)](uiresponder/keyboarddidhidemessage/init(beginframe:endframe:animationduration:animationcurve:islocal:screen:).md)
### Instance Properties
- [var animationCurve: UIView.AnimationCurve](uiresponder/keyboarddidhidemessage/animationcurve.md)
- [var animationDuration: TimeInterval](uiresponder/keyboarddidhidemessage/animationduration.md)
- [var beginFrame: CGRect](uiresponder/keyboarddidhidemessage/beginframe.md)
- [var endFrame: CGRect](uiresponder/keyboarddidhidemessage/endframe.md)
- [var isLocal: Bool](uiresponder/keyboarddidhidemessage/islocal.md)
- [var screen: UIScreen](uiresponder/keyboarddidhidemessage/screen.md)
### Type Methods
- [static func makeNotification(UIResponder.KeyboardDidHideMessage) -> Notification](uiresponder/keyboarddidhidemessage/makenotification(_:).md)

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/keyboarddidhidemessage)*