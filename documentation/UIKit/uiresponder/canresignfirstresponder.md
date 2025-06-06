# canResignFirstResponder

**Framework**: UIKit  
**Kind**: property

Returns a Boolean value indicating whether the responder is willing to relinquish first-responder status.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var canResignFirstResponder: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the responder can resign first-responder status; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method returns [`true`](https://developer.apple.com/documentation/swift/true) by default. You can override this method in your custom responders and return a different value if needed. For example, a text field containing invalid content might want to return [`false`](https://developer.apple.com/documentation/swift/false) to ensure that the user corrects that content first.

## See Also

- [var next: UIResponder?](uiresponder/next.md)
  Returns the next responder in the responder chain, or `nil` if there’s no next responder.
- [var isFirstResponder: Bool](uiresponder/isfirstresponder.md)
  Returns a Boolean value indicating whether this object is the first responder.
- [var canBecomeFirstResponder: Bool](uiresponder/canbecomefirstresponder.md)
  Returns a Boolean value indicating whether this object can become the first responder.
- [func becomeFirstResponder() -> Bool](uiresponder/becomefirstresponder.md)
  Asks UIKit to make this object the first responder in its window.
- [func resignFirstResponder() -> Bool](uiresponder/resignfirstresponder.md)
  Notifies this object that it has been asked to relinquish its status as first responder in its window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/canresignfirstresponder)*