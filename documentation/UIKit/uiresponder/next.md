# next

**Framework**: UIKit  
**Kind**: property

Returns the next responder in the responder chain, or `nil` if there’s no next responder.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var next: UIResponder? { get }
```

## Mentions

- [Using responders and the responder chain to handle events](using-responders-and-the-responder-chain-to-handle-events.md)

#### Return Value

The next object in the responder chain, or `nil` if this is the last object in the chain.

#### Discussion

The [`UIResponder`](uiresponder.md) class doesn’t store or set the next responder automatically, so this method returns `nil` by default. Subclasses must override this method and return an appropriate next responder. For example, [`UIView`](uiview.md) implements this method and returns the [`UIViewController`](uiviewcontroller.md) object that manages it (if it has one) or its superview (if it doesn’t). [`UIViewController`](uiviewcontroller.md) similarly implements the method and returns its view’s superview. [`UIWindow`](uiwindow.md) returns the application object. The shared [`UIApplication`](uiapplication.md) object normally returns `nil`, but it returns its app delegate if that object is a subclass of [`UIResponder`](uiresponder.md) and hasn’t already been called to handle the event.

## See Also

- [var isFirstResponder: Bool](uiresponder/isfirstresponder.md)
  Returns a Boolean value indicating whether this object is the first responder.
- [var canBecomeFirstResponder: Bool](uiresponder/canbecomefirstresponder.md)
  Returns a Boolean value indicating whether this object can become the first responder.
- [func becomeFirstResponder() -> Bool](uiresponder/becomefirstresponder.md)
  Asks UIKit to make this object the first responder in its window.
- [var canResignFirstResponder: Bool](uiresponder/canresignfirstresponder.md)
  Returns a Boolean value indicating whether the responder is willing to relinquish first-responder status.
- [func resignFirstResponder() -> Bool](uiresponder/resignfirstresponder.md)
  Notifies this object that it has been asked to relinquish its status as first responder in its window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/next)*