# canResignFirstResponder

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean value indicating whether the responder is willing to relinquish first-responder status.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var canResignFirstResponder: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL canResignFirstResponder;
```

#### Return Value

[`true`](../../Swift/true.md) if the responder can resign first-responder status; otherwise, [`false`](../../Swift/false.md).

#### Discussion

This method returns [`true`](../../Swift/true.md) by default. You can override this method in your custom responders and return a different value if needed. For example, a text field containing invalid content might want to return [`false`](../../Swift/false.md) to ensure that the user corrects that content first.

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
- [func resignFirstResponder() -> Bool](./resignfirstresponder%28%29.md)
  Notifies this object that it has been asked to relinquish its status as first responder in its window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/canresignfirstresponder)*