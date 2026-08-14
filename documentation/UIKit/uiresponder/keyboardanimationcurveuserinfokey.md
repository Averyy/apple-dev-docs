# keyboardAnimationCurveUserInfoKey

**Framework**: UIKit  
**Kind**: property

A user info key to retrieve the animation curve that the system uses to animate the keyboard onto or off the screen.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let keyboardAnimationCurveUserInfoKey: String
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object that contains a [`UIView.AnimationCurve`](uiview/animationcurve.md) constant used to determine how the system animates the keyboard onto or off the screen. You can use this value to match the animation of the keyboard in your own animations.

Before using this value, convert the animation curve constant to [`UIView.AnimationOptions`](uiview/animationoptions.md), which you can pass to one of UIKit’s animation methods, such as [`animate(withDuration:animations:completion:)`](uiview/animate(withduration:animations:completion:).md).

**Swift**:

```swift
// Get the animation curve constant and the duration for your animation.
guard let animationCurve = userInfo[UIResponder.keyboardAnimationCurveUserInfoKey] as? UInt,
      let animationDuration = userInfo[UIResponder.keyboardAnimationDurationUserInfoKey] as? Double else { return }

// Convert the animation curve constant to animation options.
let animationOptions = UIView.AnimationOptions(rawValue: animationCurve << 16)

// Perform your animation.
UIView.animate(withDuration: animationDuration,
               delay: 0,
               options: animationOptions) {
    // Specify what to animate. For example, calling layoutIfNeeded animates a change to
    // the view's constraints.
    self.view.layoutIfNeeded()
} completion: { _ in
    // Use the completion handler to perform anything that needs to happen after the keyboard
    // frame finishes animating, such as scrolling your text view after the animation completes.
}
```

**Objective-C**:

```objc
// Convert the animation curve constant to animation options.
UIViewAnimationOptions options = (UIViewAnimationOptions)[[userInfo objectForKey:UIKeyboardAnimationCurveUserInfoKey]
                          integerValue] << 16;

// Get the duration for your animation.
CGFloat duration = [[userInfo objectForKey:UIKeyboardAnimationDurationUserInfoKey] floatValue];

// Perform your animation.
[UIView animateWithDuration:duration
                      delay:0.0
                    options:options
                 animations:^{
    // Specify what to animate. For example, calling layoutIfNeeded animates a change 
    // to the view's constraints.
    [self.view layoutIfNeeded]; 
}
                 completion:^(BOOL finished) {
    // Use the completion handler to perform anything that needs to happen after the keyboard
    // frame finishes animating, such as scrolling your text view after the animation completes.
}];
```

## See Also

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
- [class let keyboardFrameEndUserInfoKey: String](uiresponder/keyboardframeenduserinfokey.md)
  A user info key to retrieve the keyboard’s frame at the end of its animation.
- [class let keyboardIsLocalUserInfoKey: String](uiresponder/keyboardislocaluserinfokey.md)
  A user info key to retrieve a Boolean value that indicates whether the keyboard belongs to the current app.
- [class let keyboardWillChangeFrameNotification: NSNotification.Name](uiresponder/keyboardwillchangeframenotification.md)
  A notification that posts immediately prior to a change in the keyboard’s frame.
- [class let keyboardWillHideNotification: NSNotification.Name](uiresponder/keyboardwillhidenotification.md)
  A notification that posts immediately prior to dismissing the keyboard.
- [class let keyboardWillShowNotification: NSNotification.Name](uiresponder/keyboardwillshownotification.md)
  A notification that posts immediately prior to displaying the keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/keyboardanimationcurveuserinfokey)*