# canBecomeFirstResponder

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean value indicating whether this object can become the first responder.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var canBecomeFirstResponder: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL canBecomeFirstResponder;
```

#### Return Value

[`true`](../../Swift/true.md) if the responder can become the first responder; otherwise, [`false`](../../Swift/false.md).

#### Discussion

This method returns [`false`](../../Swift/false.md) by default. Subclasses must override this method and return [`true`](../../Swift/true.md) to be able to become first responder.

Don’t call this method on a view that’s not currently in the active view hierarchy. The result is undefined.

## See Also

### Managing the responder chain
- [var next: UIResponder?](./next.md)
  Returns the next responder in the responder chain, or `nil` if there’s no next responder.
- [var isFirstResponder: Bool](./isfirstresponder.md)
  Returns a Boolean value indicating whether this object is the first responder.
- [func becomeFirstResponder() -> Bool](./becomefirstresponder%28%29.md)
  Asks UIKit to make this object the first responder in its window.
- [var canResignFirstResponder: Bool](./canresignfirstresponder.md)
  Returns a Boolean value indicating whether the responder is willing to relinquish first-responder status.
- [func resignFirstResponder() -> Bool](./resignfirstresponder%28%29.md)
  Notifies this object that it has been asked to relinquish its status as first responder in its window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/canbecomefirstresponder)*