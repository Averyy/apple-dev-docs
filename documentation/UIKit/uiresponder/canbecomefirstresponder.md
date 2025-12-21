# canBecomeFirstResponder

**Framework**: UIKit  
**Kind**: property

Returns a Boolean value indicating whether this object can become the first responder.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var canBecomeFirstResponder: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the responder can become the first responder; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method returns [`false`](https://developer.apple.com/documentation/Swift/false) by default. Subclasses must override this method and return [`true`](https://developer.apple.com/documentation/Swift/true) to be able to become first responder.

Don’t call this method on a view that’s not currently in the active view hierarchy. The result is undefined.

## See Also

- [var next: UIResponder?](uiresponder/next.md)
  Returns the next responder in the responder chain, or `nil` if there’s no next responder.
- [var isFirstResponder: Bool](uiresponder/isfirstresponder.md)
  Returns a Boolean value indicating whether this object is the first responder.
- [func becomeFirstResponder() -> Bool](uiresponder/becomefirstresponder.md)
  Asks UIKit to make this object the first responder in its window.
- [var canResignFirstResponder: Bool](uiresponder/canresignfirstresponder.md)
  Returns a Boolean value indicating whether the responder is willing to relinquish first-responder status.
- [func resignFirstResponder() -> Bool](uiresponder/resignfirstresponder.md)
  Notifies this object that it has been asked to relinquish its status as first responder in its window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/canbecomefirstresponder)*