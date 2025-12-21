# becomeFirstResponder()

**Framework**: UIKit  
**Kind**: method

Asks UIKit to make this object the first responder in its window.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func becomeFirstResponder() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if this object is now the first responder; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Call this method when you want the object to be the first responder.

Calling this method doesn’t guarantee that the object becomes the first responder. UIKit asks the current first responder to resign as first responder, which it might not do.

If the current first responder resigns as first responder, UIKit checks this object’s [`canBecomeFirstResponder`](uiresponder/canbecomefirstresponder.md) property, which is [`false`](https://developer.apple.com/documentation/Swift/false) by default. If the object succeeds in becoming the first responder, it receives subsequent events that target the first responder, and UIKit attempts to display the object’s input view.

Only call this method on views that are part of the active view hierarchy. To determine whether a view is onscreen, check its [`window`](uiview/window.md) property. If that property contains a valid window, it’s part of an active view hierarchy.

To update your object’s state or perform some action such as highlighting the selection, override this method in your custom responders. If you override this method, call `super` at some point in your implementation.

In iOS 13 or later, the root of the responder chain is the window scene’s key window. In iOS 12 or earlier, the root of the responder chain is the application’s key window.

If your responder is a [`UITextField`](uitextfield.md), a [`UITextView`](uitextview.md), or a text view that implements the [`UIKeyInput`](uikeyinput.md) protocol, expect the software keyboard to appear only if the view’s root window is a key window. Likewise, if a hardware keyboard is attached, only the first responder from the key window receives key events.

## See Also

- [var next: UIResponder?](uiresponder/next.md)
  Returns the next responder in the responder chain, or `nil` if there’s no next responder.
- [var isFirstResponder: Bool](uiresponder/isfirstresponder.md)
  Returns a Boolean value indicating whether this object is the first responder.
- [var canBecomeFirstResponder: Bool](uiresponder/canbecomefirstresponder.md)
  Returns a Boolean value indicating whether this object can become the first responder.
- [var canResignFirstResponder: Bool](uiresponder/canresignfirstresponder.md)
  Returns a Boolean value indicating whether the responder is willing to relinquish first-responder status.
- [func resignFirstResponder() -> Bool](uiresponder/resignfirstresponder.md)
  Notifies this object that it has been asked to relinquish its status as first responder in its window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/becomefirstresponder())*