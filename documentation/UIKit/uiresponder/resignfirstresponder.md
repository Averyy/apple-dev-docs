# resignFirstResponder()

**Framework**: UIKit  
**Kind**: method

Notifies this object that it has been asked to relinquish its status as first responder in its window.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func resignFirstResponder() -> Bool
```

#### Discussion

The default implementation returns [`true`](https://developer.apple.com/documentation/Swift/true), resigning first responder status. You can override this method in your custom responders to update your object’s state or perform other actions, such as removing the highlight from a selection. You can also return [`false`](https://developer.apple.com/documentation/Swift/false), refusing to relinquish first responder status. If you override this method, you must call `super` (the superclass implementation) at some point in your code.

## See Also

- [var next: UIResponder?](uiresponder/next.md)
  Returns the next responder in the responder chain, or `nil` if there’s no next responder.
- [var isFirstResponder: Bool](uiresponder/isfirstresponder.md)
  Returns a Boolean value indicating whether this object is the first responder.
- [var canBecomeFirstResponder: Bool](uiresponder/canbecomefirstresponder.md)
  Returns a Boolean value indicating whether this object can become the first responder.
- [func becomeFirstResponder() -> Bool](uiresponder/becomefirstresponder.md)
  Asks UIKit to make this object the first responder in its window.
- [var canResignFirstResponder: Bool](uiresponder/canresignfirstresponder.md)
  Returns a Boolean value indicating whether the responder is willing to relinquish first-responder status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/resignfirstresponder())*