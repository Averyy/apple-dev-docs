# pressesEnded(_:with:)

**Framework**: UIKit  
**Kind**: method

Tells the object when a button is released.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func pressesEnded(_ presses: Set<UIPress>, with event: UIPressesEvent?)
```

## Mentions

- [Handling key presses made on a physical keyboard](handling-key-presses-made-on-a-physical-keyboard.md)

#### Discussion

UIKit calls this method when the user stops pressing one or more buttons. Use this method to take any needed actions in response to the end of the press.The default implementation of this method forwards the message up the responder chain. When creating your own subclasses, call `super` to forward any events that you don’t handle yourself.

## Parameters

- `presses`: A set of   instances that represent the buttons that the user is no longer pressing. The phase of each press is set to  .
- `event`: The event to which the presses belong.

## See Also

- [func pressesBegan(Set<UIPress>, with: UIPressesEvent?)](uiresponder/pressesbegan(_:with:).md)
  Tells this object when a physical button is first pressed.
- [func pressesChanged(Set<UIPress>, with: UIPressesEvent?)](uiresponder/presseschanged(_:with:).md)
  Tells this object when a value associated with a press has changed.
- [func pressesCancelled(Set<UIPress>, with: UIPressesEvent?)](uiresponder/pressescancelled(_:with:).md)
  Tells this object when a system event (such as a low-memory warning) cancels a press event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/pressesended(_:with:))*