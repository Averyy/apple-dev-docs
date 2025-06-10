# keyboardFrameEndUserInfoKey

**Framework**: UIKit  
**Kind**: property

A user info key to retrieve the keyboard’s frame at the end of its animation.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let keyboardFrameEndUserInfoKey: String
```

#### Discussion

The value for this key is an [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) object that contains a [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect) for identifying the frame rectangle of the keyboard (in the screen’s coordinate space) after animating the keyboard. The frame rectangle reflects the current orientation of the device.

> ❗ **Important**:  Instead of using this key to track the keyboard’s frame, consider using [`UIKeyboardLayoutGuide`](uikeyboardlayoutguide.md), which allows you to respond dynamically to keyboard movement in your app. For more information, see [`Adjusting your layout with keyboard layout guide`](adjusting-your-layout-with-keyboard-layout-guide.md).

The keyboard’s frame uses the screen’s coordinate space, which is different than the coordinate space of your views. Although they might sometimes match, such as when your app is full screen, they might be different when your app isn’t full screen in Split View, Slide Over, and Stage Manager. This means you need to account for this difference by converting the keyboard’s frame from the screen’s coordinate space to that of your views. The following code example shows how to convert from the screen’s coordinate space to your view’s coordinate space:

The keyboard might overlap only part of your view, so after you convert the frame to your view’s coordinate space, get the intersection of the keyboard’s frame and the view or window it overlaps. Getting the intersection allows you to work with only the portion of the keyboard that overlaps your view. You can use this value to offset your views or perform other necessary updates to your UI. The following code example shows how to offset the bottom of your view the appropriate distance in relation to the keyboard’s frame:

## See Also

- [class let keyboardAnimationCurveUserInfoKey: String](uiresponder/keyboardanimationcurveuserinfokey.md)
  A user info key to retrieve the animation curve that the system uses to animate the keyboard onto or off the screen.
- [class let keyboardAnimationDurationUserInfoKey: String](uiresponder/keyboardanimationdurationuserinfokey.md)
  A user info key to retrieve the duration of the keyboard animation in seconds.
- [class let keyboardDidChangeFrameNotification: NSNotification.Name](uiresponder/keyboarddidchangeframenotification.md)
  A notification that posts immediately after a change in the keyboard’s frame.
- [class let keyboardDidHideNotification: NSNotification.Name](uiresponder/keyboarddidhidenotification.md)
  A notification that posts immediately after dismissing the keyboard.
- [class let keyboardDidShowNotification: NSNotification.Name](uiresponder/keyboarddidshownotification.md)
  A notification that posts immediately after displaying the keyboard.
- [class let keyboardFrameBeginUserInfoKey: String](uiresponder/keyboardframebeginuserinfokey.md)
  A user info key to retrieve the keyboard’s frame at the beginning of its animation.
- [class let keyboardIsLocalUserInfoKey: String](uiresponder/keyboardislocaluserinfokey.md)
  A user info key to retrieve a Boolean value that indicates whether the keyboard belongs to the current app.
- [class let keyboardWillChangeFrameNotification: NSNotification.Name](uiresponder/keyboardwillchangeframenotification.md)
  A notification that posts immediately prior to a change in the keyboard’s frame.
- [class let keyboardWillHideNotification: NSNotification.Name](uiresponder/keyboardwillhidenotification.md)
  A notification that posts immediately prior to dismissing the keyboard.
- [class let keyboardWillShowNotification: NSNotification.Name](uiresponder/keyboardwillshownotification.md)
  A notification that posts immediately prior to displaying the keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/keyboardframeenduserinfokey)*