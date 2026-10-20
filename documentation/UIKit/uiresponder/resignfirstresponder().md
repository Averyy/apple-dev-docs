# resignFirstResponder()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Notifies this object that it has been asked to relinquish its status as first responder in its window.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func resignFirstResponder() -> Bool
```

```objc
- (BOOL) resignFirstResponder;
```

#### Discussion

The default implementation returns [`true`](../../Swift/true.md), resigning first responder status. You can override this method in your custom responders to update your object’s state or perform other actions, such as removing the highlight from a selection. You can also return [`false`](../../Swift/false.md), refusing to relinquish first responder status. If you override this method, you must call `super` (the superclass implementation) at some point in your code.

## See Also

### Managing the responder chain
- [var next: UIResponder?](./next.md)
  Returns the next responder in the responder chain, or `nil` if there’s no next responder.
- [var isFirstResponder: Bool](./isfirstresponder.md)
  Returns a Boolean value indicating whether this object is the first responder.
- [var canBecomeFirstResponder: Bool](./canbecomefirstresponder.md)
  Returns a Boolean value indicating whether this object can become the first responder.
- [func becomeFirstResponder() -> Bool](./becomefirstresponder%28%29.md)
  Asks UIKit to make this object the first responder in its window.
- [var canResignFirstResponder: Bool](./canresignfirstresponder.md)
  Returns a Boolean value indicating whether the responder is willing to relinquish first-responder status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/resignfirstresponder())*