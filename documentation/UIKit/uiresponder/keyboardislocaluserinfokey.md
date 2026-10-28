# keyboardIsLocalUserInfoKey

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A user info key to retrieve a Boolean value that indicates whether the keyboard belongs to the current app.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let keyboardIsLocalUserInfoKey: String
```

```c
extern NSString * const UIKeyboardIsLocalUserInfoKey;
```

## Discussion

The value for this key is an [`NSNumber`](../../Foundation/nsnumber.md) object containing a Boolean value that indicates whether the keyboard belongs to the current app. With Multitasking in iPadOS, the system notifies all visible apps when the keyboard appears and disappears. The value is [`true`](../../Swift/true.md) for the app that caused the keyboard to appear and [`false`](../../Swift/false.md) for the other apps.

## See Also

### Constants
- [class let keyboardAnimationCurveUserInfoKey: String](./keyboardanimationcurveuserinfokey.md)
  A user info key to retrieve the animation curve that the system uses to animate the keyboard onto or off the screen.
- [class let keyboardAnimationDurationUserInfoKey: String](./keyboardanimationdurationuserinfokey.md)
  A user info key to retrieve the duration of the keyboard animation in seconds.
- [class let keyboardDidChangeFrameNotification: NSNotification.Name](./keyboarddidchangeframenotification.md)
  A notification that posts immediately after a change in the keyboard’s frame.
- [class let keyboardDidHideNotification: NSNotification.Name](./keyboarddidhidenotification.md)
  A notification that posts immediately after dismissing the keyboard.
- [class let keyboardDidShowNotification: NSNotification.Name](./keyboarddidshownotification.md)
  A notification that posts immediately after displaying the keyboard.
- [class let keyboardFrameBeginUserInfoKey: String](./keyboardframebeginuserinfokey.md)
  A user info key to retrieve the keyboard’s frame at the beginning of its animation.
- [class let keyboardFrameEndUserInfoKey: String](./keyboardframeenduserinfokey.md)
  A user info key to retrieve the keyboard’s frame at the end of its animation.
- [class let keyboardWillChangeFrameNotification: NSNotification.Name](./keyboardwillchangeframenotification.md)
  A notification that posts immediately prior to a change in the keyboard’s frame.
- [class let keyboardWillHideNotification: NSNotification.Name](./keyboardwillhidenotification.md)
  A notification that posts immediately prior to dismissing the keyboard.
- [class let keyboardWillShowNotification: NSNotification.Name](./keyboardwillshownotification.md)
  A notification that posts immediately prior to displaying the keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/keyboardislocaluserinfokey)*