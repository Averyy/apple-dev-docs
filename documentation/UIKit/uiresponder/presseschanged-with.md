# pressesChanged(_:with:)

**Framework**: UIKit  
**Kind**: method

Tells this object when a value associated with a press has changed.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func pressesChanged(_ presses: Set<UIPress>, with event: UIPressesEvent?)
```

#### Discussion

UIKit calls this method when an analog value associated with a button or thumbstick changes. For example, it calls this method when the analog force value of a push button changes. Use this method to take any needed actions in response to the change.

The default implementation of this method forwards the message up the responder chain. When creating your own subclasses, call `super` to forward any events that you don’t handle yourself.

## Parameters

- `presses`: A set of   instances containing changed values.
- `event`: The event to which the presses belong.

## See Also

- [func pressesBegan(Set<UIPress>, with: UIPressesEvent?)](uiresponder/pressesbegan(_:with:).md)
  Tells this object when a physical button is first pressed.
- [func pressesEnded(Set<UIPress>, with: UIPressesEvent?)](uiresponder/pressesended(_:with:).md)
  Tells the object when a button is released.
- [func pressesCancelled(Set<UIPress>, with: UIPressesEvent?)](uiresponder/pressescancelled(_:with:).md)
  Tells this object when a system event (such as a low-memory warning) cancels a press event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/presseschanged(_:with:))*