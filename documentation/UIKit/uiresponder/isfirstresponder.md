# isFirstResponder

**Framework**: UIKit  
**Kind**: property

Returns a Boolean value indicating whether this object is the first responder.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isFirstResponder: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the responder is the first responder; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

UIKit dispatches some types of events, such as motion events, to the first responder initially.

## See Also

- [var next: UIResponder?](uiresponder/next.md)
  Returns the next responder in the responder chain, or `nil` if there’s no next responder.
- [var canBecomeFirstResponder: Bool](uiresponder/canbecomefirstresponder.md)
  Returns a Boolean value indicating whether this object can become the first responder.
- [func becomeFirstResponder() -> Bool](uiresponder/becomefirstresponder.md)
  Asks UIKit to make this object the first responder in its window.
- [var canResignFirstResponder: Bool](uiresponder/canresignfirstresponder.md)
  Returns a Boolean value indicating whether the responder is willing to relinquish first-responder status.
- [func resignFirstResponder() -> Bool](uiresponder/resignfirstresponder.md)
  Notifies this object that it has been asked to relinquish its status as first responder in its window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/isfirstresponder)*