# isFirstResponder

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean value indicating whether this object is the first responder.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isFirstResponder: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isFirstResponder;
```

#### Return Value

[`true`](../../Swift/true.md) if the responder is the first responder; otherwise, [`false`](../../Swift/false.md).

#### Discussion

UIKit dispatches some types of events, such as motion events, to the first responder initially.

## See Also

### Managing the responder chain
- [var next: UIResponder?](./next.md)
  Returns the next responder in the responder chain, or `nil` if there’s no next responder.
- [var canBecomeFirstResponder: Bool](./canbecomefirstresponder.md)
  Returns a Boolean value indicating whether this object can become the first responder.
- [func becomeFirstResponder() -> Bool](./becomefirstresponder%28%29.md)
  Asks UIKit to make this object the first responder in its window.
- [var canResignFirstResponder: Bool](./canresignfirstresponder.md)
  Returns a Boolean value indicating whether the responder is willing to relinquish first-responder status.
- [func resignFirstResponder() -> Bool](./resignfirstresponder%28%29.md)
  Notifies this object that it has been asked to relinquish its status as first responder in its window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/isfirstresponder)*