# keyboardFrameBeginUserInfoKey

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A user info key to retrieve the keyboard’s frame at the beginning of its animation.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let keyboardFrameBeginUserInfoKey: String
```

```c
extern NSString * const UIKeyboardFrameBeginUserInfoKey;
```

## Discussion

The value for this key is an [`NSValue`](../../Foundation/nsvalue.md) object that contains a [`CGRect`](../../CoreFoundation/cgrect.md) for identifying the frame rectangle of the keyboard (in the screen’s coordinate space) before animating the keyboard. The frame rectangle reflects the current orientation of the device.

The keyboard’s frame uses the screen’s coordinate space, which is different than the coordinate space of your views. Although they might sometimes match, such as when your app is full screen, they might be different when your app isn’t full screen, such as in Split View, Slide Over, and Stage Manager. This means you need to account for this difference by converting the keyboard’s frame from the screen’s coordinate space to that of your views. For an example of how to handle this conversion, see [`keyboardFrameEndUserInfoKey`](./keyboardframeenduserinfokey.md).

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
- [class let keyboardFrameEndUserInfoKey: String](./keyboardframeenduserinfokey.md)
  A user info key to retrieve the keyboard’s frame at the end of its animation.
- [class let keyboardIsLocalUserInfoKey: String](./keyboardislocaluserinfokey.md)
  A user info key to retrieve a Boolean value that indicates whether the keyboard belongs to the current app.
- [class let keyboardWillChangeFrameNotification: NSNotification.Name](./keyboardwillchangeframenotification.md)
  A notification that posts immediately prior to a change in the keyboard’s frame.
- [class let keyboardWillHideNotification: NSNotification.Name](./keyboardwillhidenotification.md)
  A notification that posts immediately prior to dismissing the keyboard.
- [class let keyboardWillShowNotification: NSNotification.Name](./keyboardwillshownotification.md)
  A notification that posts immediately prior to displaying the keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/keyboardframebeginuserinfokey)*